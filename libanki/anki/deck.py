# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

"""\
The Deck
====================
"""
__docformat__ = 'restructuredtext'

try:
    from pysqlite2 import dbapi2 as sqlite
except ImportError:
    try:
        from sqlite3 import dbapi2 as sqlite
    except:
        raise "Please install pysqlite2 or python2.5"
sqlite.enable_shared_cache(True)

import tempfile, time, os, random, sys, re, stat, shutil, types
from heapq import heapify, heappush, heappop

from anki.db import *
from anki.lang import _
from anki.errors import DeckAccessError, DeckWrongFormatError
from anki.stdmodels import BasicModel
from anki.utils import parseTags, tidyHTML
from anki.history import CardHistoryEntry
from anki.models import Model
from anki.stats import dailyStats, globalStats
from anki.models import CardModel

# ensure all the metadata in other files is loaded before proceeding
import anki.models, anki.facts, anki.cards, anki.stats, anki.history

PRIORITY_HIGH = 4
PRIORITY_MED = 3
PRIORITY_NORM = 2
PRIORITY_LOW = 1
PRIORITY_NONE = 0

MATURE_THRESHOLD = 21

# need interval > 0 to ensure relative delay is ordered properly
NEW_INTERVAL = 0.001

NewCardOrder = {
    0: _("Show new cards in random order"),
    1: _("Show new cards in order they were added"),
    }

# parts of the code assume we only have one deck
decksTable = Table(
    'decks', metadata,
    Column('id', Integer, primary_key=True),
    Column('created', Float, nullable=False, default=time.time),
    Column('modified', Float, nullable=False, default=time.time),
    Column('description', UnicodeText, nullable=False, default=u""),
    Column('version', Integer, nullable=False, default=3),
    Column('currentModelId', Integer, ForeignKey("models.id")),
    # syncing
    Column('syncName', UnicodeText),
    Column('lastSync', Float, nullable=False, default=0),
    # scheduling
    ##############
    # initial intervals
    Column('hardIntervalMin', Float, nullable=False, default=0.333),
    Column('hardIntervalMax', Float, nullable=False, default=0.5),
    Column('midIntervalMin', Float, nullable=False, default=3.0),
    Column('midIntervalMax', Float, nullable=False, default=5.0),
    Column('easyIntervalMin', Float, nullable=False, default=7.0),
    Column('easyIntervalMax', Float, nullable=False, default=9.0),
    # delays on failure
    Column('delay0', Integer, nullable=False, default=600),
    Column('delay1', Integer, nullable=False, default=1200),
    Column('delay2', Integer, nullable=False, default=28800),
    # collapsing future cards
    Column('collapseTime', Float, nullable=False, default=18000),
    # priorities & postponing
    Column('highPriority', UnicodeText, nullable=False, default=u""),
    Column('medPriority', UnicodeText, nullable=False, default=u""),
    Column('lowPriority', UnicodeText, nullable=False, default=u""),
    Column('suspended', UnicodeText, nullable=False, default=u"Suspended"),
    # 0 is random, 1 is by input date
    Column('newCardOrder', Integer, nullable=False, default=0),
    # not currently used
    Column('newCardSpacing', Integer, nullable=False, default=0),
    # limit the number of failed cards in play
    Column('failedCardMax', Integer, nullable=False, default=20))

class Deck(object):
    "Top-level object. Manages facts, cards and scheduling information."

    factorFour = 1.3
    initialFactor = 2.5
    maxScheduleTime = 1825

    def __init__(self, path=None):
        "Create a new deck."
        # a limit of 1 deck in the table
        self.id = 1
        # db session factory and instance
        self.Session = None
        self.s = None

    def _initVars(self):
        self.lastTags = u""
        self.lastLoaded = time.time()
        self._countsDirty = True

    def modifiedSinceSave(self):
        return self.modified > self.lastLoaded

    # Asking & answering
    ##########################################################################

    def getCard(self, orm=True):
        ids = self.getCardIds()
        if ids:
            return self.cardFromId(ids[0], orm)

    def getCards(self, limit=1, orm=True):
        ids = self.getCardIds(limit)
        return [self.cardFromId(x, orm) for x in ids]

    def getCardIds(self, limit=1):
        """Return up to LIMIT number of pending card IDs.
Caller is responsible for checking cards are not spaced if
limit is above 1."""
        now = time.time()
        ids = []
        # failed card due?
        ids += self.s.column0("select id from failedCardsNow limit %d" % limit)
        rem = limit - len(ids)
        if rem > 0:
            # failed card queue too big?
            if self.failedCount >= self.failedCardMax:
                ids += self.s.column0(
                    "select id from failedCardsSoon limit %d" % rem)
        rem = limit - len(ids)
        if rem > 0:
            # card due for review?
            ids += self.s.column0("select id from revCards limit %d" % rem)
        rem = limit - len(ids)
        if rem > 0:
            # new card
            if self.newCardOrder == 0:
                ids += self.s.column0(
                    "select id from acqCardsRandom limit %d" % rem)
            else:
                ids += self.s.column0(
                    "select id from acqCardsOrdered limit %d" % rem)
        if not ids:
            if self.collapseTime:
                # final review
                ids += self.s.column0(
                    "select id from failedCardsSoon limit %d" % rem)
        return ids

    def cardFromId(self, id, orm=False):
        if orm:
            card = self.s.query(anki.cards.Card).get(id)
            card.genFuzz()
            card.startTimer()
        else:
            card = anki.cards.Card()
            card.fromDB(self.s, id)
            card.genFuzz()
        return card

    def answerCard(self, card, ease):
        now = time.time()
        oldState = self.cardState(card)
        lastDelay = max(0, (time.time() - card.due) / 86400.0)
        # update card details
        card.lastInterval = card.interval
        card.interval = self.nextInterval(card, ease)
        card.lastDue = card.due
        card.due = self.nextDue(card, ease, oldState)
        card.isDue = 0
        card.lastFactor = card.factor
        self.updateFactor(card, ease)
        # spacing - first, we get the times of all other cards with the same
        # fact
        (minSpacing, spaceFactor) = self.s.first("""
select models.initialSpacing, models.spacing from
facts, models where facts.modelId = models.id and facts.id = :id""", id=card.factId)
        minOfOtherCards = self.s.scalar("""
select min(interval) from cards
where factId = :fid and id != :id""", fid=card.factId, id=card.id) or 0
        if minOfOtherCards:
            space = min(minOfOtherCards, card.interval)
        else:
            space = 0
        space = space * spaceFactor * 86400.0
        space = max(minSpacing, space)
        space += time.time()
        self.s.statement("""
update cards set
spaceUntil = :space,
combinedDue = max(:space, due),
modified = :now,
isDue = 0
where id != :id and factId = :factId""",
                         id=card.id, space=space, now=now, factId=card.factId)
        card.spaceUntil = 0
        # card stats
        anki.cards.Card.updateStats(card, ease, oldState)
        card.toDB(self.s)
        # global/daily stats
        anki.stats.updateAllStats(self.s, self._globalStats, self._dailyStats,
                                  card, ease, oldState)
        # review history
        entry = CardHistoryEntry(card, ease, lastDelay)
        entry.writeSQL(self.s)
        self.modified = now
        # update isDue for failed cards
        self.markExpiredCardsDue()
        # invalidate counts
        self._countsDirty = True

    # Queue/cache management
    ##########################################################################

    def rebuildTypes(self, where=""):
        "Rebuild the type cache. Done on upgrade or priority change."
        self.s.statement("""
update cards
set type = (case
when successive = 0 and reps != 0 and priority != 0
then 0 -- failed
when priority = 4 or successive != 0 and reps != 0 and priority > 1
then 1 -- review
else 2 -- new
end)""" + where)

    def markExpiredCardsDue(self):
        "Mark expired cards due, and update their relativeDelay."
        self.s.statement("""update cards
set isDue = 1, relativeDelay = interval / (strftime("%s", "now") - due + 1)
where isDue = 0 and priority in (1,2,3,4) and combinedDue < :now""",
                         now=time.time())

    def updateRelativeDelays(self):
        "Update relative delays for expired cards."
        self.s.statement("""update cards
set relativeDelay = interval / (strftime("%s", "now") - due + 1)
where isDue = 1""")

    def rebuildQueue(self):
        "Update relative delays based on current time."
        self.updateRelativeDelays()
        self.markExpiredCardsDue()
        # cache global/daily stats
        self._globalStats = globalStats(self.s)
        self._dailyStats = dailyStats(self.s)
        # invalid card count
        self._countsDirty = True

    # Interval management
    ##########################################################################

    def nextInterval(self, card, ease):
        "Return the next interval for CARD given EASE."
        delay = self._adjustedDelay(card, ease)
        # if interval is less than mid interval, use presets
        if (card.interval + delay) < self.midIntervalMin:
            if ease < 2:
                interval = NEW_INTERVAL
            elif ease == 2:
                interval = random.uniform(self.hardIntervalMin,
                                          self.hardIntervalMax)
            elif ease == 3:
                interval = random.uniform(self.midIntervalMin,
                                          self.midIntervalMax)
            elif ease == 4:
                interval = random.uniform(self.easyIntervalMin,
                                          self.easyIntervalMax)
            interval += delay
        else:
            # otherwise, multiply the old interval by a factor
            if ease == 0:
                factor = 0
            elif ease == 1:
                factor = 1 / card.factor / 2.0
            elif ease == 2:
                factor = 1.2
            elif ease == 3:
                factor = card.factor
            elif ease == 4:
                factor = card.factor * self.factorFour
            interval = (card.interval + delay) * factor * card.fuzz
        if self.maxScheduleTime:
            interval = min(interval, self.maxScheduleTime)
        return interval

    def nextDue(self, card, ease, oldState):
        "Return time when CARD will expire given EASE."
        if ease == 0:
            due =  self.delay0
        elif ease == 1 and oldState != 'mature':
            due =  self.delay1
        elif ease == 1:
            due =  self.delay2
        else:
            due =  card.interval * 86400.0
        return due + time.time()

    def updateFactor(self, card, ease):
        "Update CARD's factor based on EASE."
        card.lastFactor = card.factor
        if self.cardIsBeingLearnt(card) and ease in [0, 1, 2]:
            # only penalize failures after success when starting
            if card.successive and ease != 2:
                card.factor -= 0.20
        elif ease in [0, 1]:
            card.factor -= 0.20
        elif ease == 2:
            card.factor -= 0.15
        elif ease == 4:
            card.factor += 0.10
        card.factor = max(1.3, card.factor)

    def _adjustedDelay(self, card, ease):
        "Return an adjusted delay value for CARD based on EASE."
        if self.cardIsNew(card):
            return 0
        return max(0, (time.time() - card.due) / 86400.0)

    def resetCards(self, ids):
        "Reset progress on cards in IDS."
        strids = ",".join([str(id) for id in ids])
        self.s.statement("""
update cards set interval = :new, lastInterval = 0, lastDue = 0,
factor = 2.5, reps = 0, successive = 0, averageTime = 0, reviewTime = 0,
youngEase0 = 0, youngEase1 = 0, youngEase2 = 0, youngEase3 = 0,
youngEase4 = 0, matureEase0 = 0, matureEase1 = 0, matureEase2 = 0,
matureEase3 = 0,matureEase4 = 0, yesCount = 0, noCount = 0,
spaceUntil = 0, relativeDelay = 0, isDue = 0, type = 2,
combinedDue = created, modified = :now, due = created
where id in (%s)""" % strids, now=time.time(), new=NEW_INTERVAL)
        self.flushMod()

    # Times
    ##########################################################################

    def nextDueMsg(self):
        next = self.earliestTime()
        if next:
            if next - time.time() > 86400:
                msg = (_("The next card will be shown in <b>%s</b>") %
                       self.earliestTimeStr())
            else:
                msg = (_("At the same time tomorrow, there will be "
                         "<b>%d</b> cards waiting") %
                       self.cardsDueBy(time.time() + 86400))
        else:
            msg = _("The deck is empty. Please add some cards.")
        return msg

    def earliestTime(self):
        """Return the time of the earliest card.
        This may be in the past if the deck is not finished.
        If the deck has no (enabled) cards, return None."""
        return self.s.scalar("""
select combinedDue from cards where priority != 0
order by combinedDue limit 1""")

    def earliestTimeStr(self, next=None):
        """Return the relative time to the earliest card as a string."""
        if next == None:
            next = self.earliestTime()
        if not next:
            return _("unknown")
        diff = next - time.time()
        return anki.utils.fmtTimeSpan(diff)

    def cardsDueBy(self, time):
        "Number of cards due at TIME."
        return self.s.scalar("""
select count(id) from cards where combinedDue < :time
and priority != 0""", time=time)

    def nextIntervalStr(self, card, ease):
        "Return the next interval for CARD given EASE as a string."
        delay = self._adjustedDelay(card, ease)
        if card.due > time.time() and ease < 2:
            # the card is not yet due, and we are in the final drill
            return _("a short time")
        if ease < 2:
            interval = self.nextDue(card, ease, self.cardState(card)) - time.time()
        elif (card.interval+delay) < self.midIntervalMin:
            if ease == 4:
                interval = [self.easyIntervalMin, self.easyIntervalMax]
            elif ease == 3:
                interval = [self.midIntervalMin, self.midIntervalMax]
            else:
                interval = [self.hardIntervalMin, self.hardIntervalMax]
            interval[0] = (interval[0] + delay) * 86400.0
            interval[1] = (interval[1] + delay) * 86400.0
            if interval[0] != interval[1]:
                return anki.utils.fmtTimeSpanPair(*interval)
            interval = interval[0]
        else:
            interval = self.nextInterval(card, ease) * 86400.0
        return anki.utils.fmtTimeSpan(interval)

    def deckFinishedMsg(self):
        return _('''
<h1>Congratulations!</h1>You have finished the deck for now.<br><br>
%(next)s
<br><br>
There are %(waiting)d
<a href="http://ichi2.net/anki/wiki/Key_Terms_and_Concepts#head-59a81e35b6afb23930005e943068945214d194b3">
spaced</a> cards.<br>
There are %(suspended)d
<a href="http://ichi2.net/anki/wiki/Key_Terms_and_Concepts#head-37d2db274e6caa23aef55e29655a6b806901774b">
suspended</a> cards.''') % {
    "next": self.nextDueMsg(),
    "suspended": self.suspendedCardCount(),
    "waiting": self.spacedCardCount()
    }

    # Priorities
    ##########################################################################

    def updateAllPriorities(self, extraExcludes=[]):
        "Update all card priorities if changed."
        now = time.time()
        newPriorities = []
        tagsList = self.tagsList()
        tagCache = self.genTagCache()
        for e in extraExcludes:
            tagCache['suspended'][e] = 1
        for (cardId, tags, oldPriority) in tagsList:
            newPriority = self.priorityFromTagString(tags, tagCache)
            if newPriority != oldPriority:
                newPriorities.append({"id": cardId, "pri": newPriority})
        # update db
        self.s.execute(text(
            "update cards set priority = :pri where cards.id = :id"),
            newPriorities)
        self.rebuildTypes()
        self.s.execute("update cards set isDue = 0 where priority = 0")

    def updatePriority(self, card):
        "Update priority on a single card."
        tagCache = self.genTagCache()
        tags = (card.tags + "," + card.fact.tags + "," +
                card.fact.model.tags + "," + card.cardModel.name)
        p = self.priorityFromTagString(tags, tagCache)
        if p != card.priority:
            card.priority = p
            if p == 0:
                card.isDue = 0
            self.s.flush()
            self.rebuildTypes(" where id = %d" % card.id)

    def priorityFromTagString(self, tagString, tagCache):
        tags = parseTags(tagString.lower())
        for tag in tags:
            if tag in tagCache['suspended']:
                return PRIORITY_NONE
        for tag in tags:
            if tag in tagCache['high']:
                return PRIORITY_HIGH
        for tag in tags:
            if tag in tagCache['med']:
                return PRIORITY_MED
        for tag in tags:
            if tag in tagCache['low']:
                return PRIORITY_LOW
        return PRIORITY_NORM

    def genTagCache(self):
        "Cache tags for quick lookup. Return dict."
        d = {}
        t = parseTags(self.suspended.lower())
        d['suspended'] = dict([(k, 1) for k in t])
        t = parseTags(self.highPriority.lower())
        d['high'] = dict([(k, 1) for k in t])
        t = parseTags(self.medPriority.lower())
        d['med'] = dict([(k, 1) for k in t])
        t = parseTags(self.lowPriority.lower())
        d['low'] = dict([(k, 1) for k in t])
        return d

    # Card/fact counts
    ##########################################################################

    def cardCount(self):
        return self.s.scalar(
            "select count(id) from cards")

    def factCount(self):
        return self.s.scalar(
            "select count(id) from facts")

    def suspendedCardCount(self):
        return self.s.scalar(
            "select count(id) from cards where priority = 0")

    def seenCardCount(self):
        return self.s.scalar(
            "select count(id) from cards where reps != 0")

    def newCardCount(self):
        return self.s.scalar(
            "select count(id) from cards where reps = 0")

    def updateCounts(self):
        "Update failed/rev/new counts if cache is dirty."
        if self._countsDirty:
            self._failedCount = self.s.scalar("""
select count(id) from failedCardsSoon""")
            self._failedDueNowCount = self.s.scalar("""
select count(id) from failedCardsNow""")
            self._reviewCount = self.s.scalar(
                "select count(isDue) from cards where isDue = 1 and type = 1")
            self._newCount = self.s.scalar(
                "select count(isDue) from cards where isDue = 1 and type = 2")
            self._countsDirty = False

    def _getFailedCount(self):
        self.updateCounts()
        return self._failedCount
    failedCount = property(_getFailedCount)

    def _getFailedDueNowCount(self):
        self.updateCounts()
        return self._failedDueNowCount
    failedDueNowCount = property(_getFailedDueNowCount)

    def _getReviewCount(self):
        self.updateCounts()
        return self._reviewCount
    reviewCount = property(_getReviewCount)

    def _getNewCount(self):
        self.updateCounts()
        return self._newCount
    newCount = property(_getNewCount)

    def spacedCardCount(self):
        return self.s.scalar("""
select count(cards.id) from cards where
priority != 0 and due < :now and spaceUntil > :now""",
                             now=time.time())

    def isEmpty(self):
        return self.cardCount() == 0

    def matureCardCount(self):
        return self.s.scalar(
            "select count(id) from cards where interval >= :t ",
            t=MATURE_THRESHOLD)

    def youngCardCount(self):
        return self.s.scalar(
            "select count(id) from cards where interval < :t "
            "and reps != 0", t=MATURE_THRESHOLD)

    # Card predicates
    ##########################################################################

    def cardState(self, card):
        if self.cardIsNew(card):
            return "new"
        elif card.interval > MATURE_THRESHOLD:
            return "mature"
        return "young"

    def cardIsNew(self, card):
        "True if a card has never been seen before."
        return card.reps == 0

    def cardIsBeingLearnt(self, card):
        "True if card should use present intervals."
        return card.interval < self.easyIntervalMin

    def cardIsYoung(self, card):
        "True if card is not new and not mature."
        return (not self.cardIsNew(card) and
                not self.cardIsMature(card))

    def cardIsMature(self, card):
        return card.interval >= MATURE_THRESHOLD

    # Stats
    ##########################################################################

    def getStats(self):
        "Return some commonly needed stats."
        stats = anki.stats.getStats(self.s, self._globalStats, self._dailyStats)
        # add scheduling related stats
        stats['new'] = self.newCount
        stats['failed'] = self.failedCount
        stats['successive'] = self.reviewCount
        #stats['old'] = stats['failed'] + stats['successive']
        if stats['dAverageTime']:
            stats['timeLeft'] = anki.utils.fmtTimeSpan(
                stats['dAverageTime'] * (stats['successive'] or stats['new']),
                pad=0, point=1)
        else:
            stats['timeLeft'] = _("Unknown")
        return stats

    def queueForCard(self, card):
        "Return the queue the current card is in."
        if self.cardIsNew(card):
            if card.priority == 4:
                return "rev"
            else:
                return "new"
        elif card.successive == 0:
            return "failed"
        elif card.reps:
            return "rev"
        else:
            sys.stderr.write("couldn't determine queue for %s" %
                             `card.__dict__`)

    # Facts
    ##########################################################################

    def newFact(self):
        "Return a new fact with the current model."
        return anki.facts.Fact(self.currentModel)

    def addFact(self, fact):
        "Add a fact to the deck. Return list of new cards."
        if not fact.model:
            fact.model = self.currentModel
        # the session may have been cleared, so refresh model
        fact.model = self.s.query(Model).get(fact.model.id)
        # validate
        fact.assertValid()
        fact.assertUnique(self.s)
        # and associated cards
        n = 0
        cards = []
        self.s.save(fact)
        self.flushMod()
        for cardModel in fact.model.cardModels:
            if cardModel.active:
                card = anki.cards.Card(fact, cardModel)
                self.flushMod()
                self.updatePriority(card)
                cards.append(card)
        # keep track of last used tags for convenience
        self.lastTags = fact.tags
        self.setModified()
        return cards

    def addMissingCards(self, fact):
        for cardModel in fact.model.cardModels:
            if cardModel.active:
                if self.s.scalar("""
select count(id) from cards
where factId = :fid and cardModelId = :cmid""",
                                 fid=fact.id, cmid=cardModel.id) == 0:
                    card = anki.cards.Card(fact, cardModel)
                    self.flushMod()
                    self.updatePriority(card)
                    # not added to queue
        self.setModified()

    def factIsInvalid(self, fact):
        "True if existing fact is invalid. Returns the error."
        try:
            fact.assertValid()
            fact.assertUnique(self.s)
        except FactInvalidError, e:
            return e

    def factUseCount(self, factId):
        "Return number of cards referencing a given fact id."
        return self.s.scalar("select count(id) from cards where factId = :id",
                             id=factId)

    def deleteFact(self, factId):
        "Delete a fact. Removes any associated cards. Don't flush."
        self.s.flush()
        # remove any remaining cards
        self.s.statement("insert into cardsDeleted select id, :time "
                         "from cards where factId = :factId",
                         time=time.time(), factId=factId)
        self.s.statement("delete from cards where factId = :id", id=factId)
        # and then the fact
        self.s.statement("delete from facts where id = :id", id=factId)
        self.s.statement("delete from fields where factId = :id", id=factId)
        self.s.statement("insert into factsDeleted values (:id, :time)",
                         id=factId, time=time.time())
        self.setModified()

    def deleteFacts(self, ids):
        "Bulk delete facts by ID. Assume any cards have already been removed."
        if not ids:
            return
        self.s.flush()
        now = time.time()
        strids = ",".join([str(id) for id in ids])
        self.s.statement("delete from facts where id in (%s)" % strids)
        self.s.statement("delete from fields where factId in (%s)" % strids)
        data = [{'id': id, 'time': now} for id in ids]
        self.s.statements("insert into factsDeleted values (:id, :time)", data)
        self.setModified()

    def deleteDanglingFacts(self):
        "Delete any facts without cards. Return deleted ids."
        ids = self.s.column0("""
select facts.id from facts
where facts.id not in (select factId from cards)""")
        self.deleteFacts(ids)
        return ids

    # Cards
    ##########################################################################

    #def getCardById(self, id):
    #    return self.s.query(anki.cards.Card).get(id)

    def deleteCard(self, id):
        "Delete a card given its id. Delete any unused facts. Don't flush."
        self.s.flush()
        factId = self.s.scalar("select factId from cards where id=:id", id=id)
        self.s.statement("delete from cards where id = :id", id=id)
        self.s.statement("insert into cardsDeleted values (:id, :time)",
                         id=id, time=time.time())
        if factId and not self.factUseCount(factId):
            self.deleteFact(factId)
        self.setModified()

    def deleteCards(self, ids):
        "Bulk delete cards by ID."
        if not ids:
            return
        self.s.flush()
        now = time.time()
        strids = ",".join([str(id) for id in ids])
        # grab fact ids
        factIds = self.s.column0("select factId from cards where id in (%s)"
                                 % strids)
        # drop from cards
        self.s.statement("delete from cards where id in (%s)" % strids)
        # note deleted
        data = [{'id': id, 'time': now} for id in ids]
        self.s.statements("insert into cardsDeleted values (:id, :time)", data)
        # remove any dangling facts
        self.deleteDanglingFacts()
        self.setModified()

    # Models
    ##########################################################################

    def addModel(self, model):
        if model not in self.models:
            self.models.append(model)
        self.currentModel = model
        self.flushMod()

    def deleteModel(self, model):
        "Delete MODEL, and delete any referencing cards/facts. Maybe flush."
        if self.s.scalar("select count(id) from models where id=:id",
                         id=model.id):
            # delete facts/cards
            self.currentModel
            self.deleteCards(self.s.column0("""
select cards.id from cards, facts where
facts.modelId = :id and
facts.id = cards.factId""", id=model.id))
            # then the model
            self.models.remove(model)
            self.s.delete(model)
            self.s.flush()
            if self.currentModel == model:
                self.currentModel = self.models[0]
            self.s.statement("insert into modelsDeleted values (:id, :time)",
                             id=model.id, time=time.time())
            self.flushMod()
            self.refresh()
            self.setModified()

    def modelUseCount(self, model):
        "Return number of facts using model."
        return self.s.scalar("select count(facts.modelId) from facts "
                             "where facts.modelId = :id",
                             id=model.id)

    def deleteEmptyModels(self):
        for model in self.models:
            if not self.modelUseCount(model):
                self.deleteModel(model)

    def modelsGroupedByName(self):
        "Return hash of name -> [id, cardModelIds, fieldIds]"
        l = self.s.all("select name, id from models order by created")
        models = {}
        for m in l:
            cms = self.s.column0("""
select id from cardModels where modelId = :id order by ordinal""", id=m[1])
            fms = self.s.column0("""
select id from fieldModels where modelId = :id order by ordinal""", id=m[1])
            if m[0] in models:
                models[m[0]].append((m[1], cms, fms))
            else:
                models[m[0]] = [(m[1], cms, fms)]
        return models

    def canMergeModels(self):
        models = self.modelsGroupedByName()
        toProcess = []
        msg = ""
        for (name, ids) in models.items():
            if len(ids) > 1:
                cms = len(ids[0][1])
                fms = len(ids[0][2])
                for id in ids[1:]:
                    if len(id[1]) != cms:
                        msg = (_(
                            "Model '%s' has wrong card model count") % name)
                        break
                    if len(id[2]) != fms:
                        msg = (_(
                            "Model '%s' has wrong field model count") % name)
                        break
                toProcess.append((name, ids))
        if msg:
            return ("no", msg)
        return ("ok", toProcess)

    def mergeModels(self, toProcess):
        for (name, ids) in toProcess:
            (id1, cms1, fms1) = ids[0]
            for (id2, cms2, fms2) in ids[1:]:
                self.mergeModel((id1, cms1, fms1),
                                (id2, cms2, fms2))

    def mergeModel(self, m1, m2):
        "Given two model ids, merge m2 into m1."
        (id1, cms1, fms1) = m1
        (id2, cms2, fms2) = m2
        self.s.flush()
        # cards
        for n in range(len(cms1)):
            self.s.statement("""
update cards set
modified = strftime("%s", "now"),
cardModelId = :new where cardModelId = :old""",
                             new=cms1[n], old=cms2[n])
        # facts
        self.s.statement("""
update facts set
modified = strftime("%s", "now"),
modelId = :new where modelId = :old""",
                         new=id1, old=id2)
        # fields
        for n in range(len(fms1)):
            self.s.statement("""
update fields set
fieldModelId = :new where fieldModelId = :old""",
                             new=fms1[n], old=fms2[n])
        # delete m2
        model = [m for m in self.models if m.id == id2][0]
        self.deleteModel(model)
        self.refresh()

    # Fields
    ##########################################################################

    def allFields(self):
        "Return a list of all possible fields across all models."
        return self.s.column0("select distinct name from fieldmodels")

    def deleteFieldModel(self, model, field):
        self.s.statement("delete from fields where fieldModelId = :id",
                         id=field.id)
        self.s.statement("update facts set modified = :t where modelId = :id",
                         id=model.id, t=time.time())
        model.fieldModels.remove(field)
        # update q/a formats
        for cm in model.cardModels:
            cm.qformat = cm.qformat.replace("%%(%s)s" % field.name, "")
            cm.aformat = cm.aformat.replace("%%(%s)s" % field.name, "")
        model.setModified()
        self.flushMod()

    def addFieldModel(self, model, field):
        "Add FIELD to MODEL and update cards."
        model.addFieldModel(field)
        # commit field to disk
        self.s.flush()
        self.s.statement("""
insert into fields (factId, fieldModelId, ordinal, value)
select facts.id, :fmid, :ordinal, "" from facts
where facts.modelId = :mid""", fmid=field.id, mid=model.id, ordinal=field.ordinal)
        # ensure facts are marked updated
        self.s.statement("""
update facts set modified = :t where modelId = :mid"""
                         , t=time.time(), mid=model.id)
        model.setModified()
        self.flushMod()

    def renameFieldModel(self, model, field, newName):
        "Change FIELD's name in MODEL and update FIELD in all facts."
        for cm in model.cardModels:
            cm.qformat = cm.qformat.replace(
                "%%(%s)s" % field.name, "%%(%s)s" % newName)
            cm.aformat = cm.aformat.replace(
                "%%(%s)s" % field.name, "%%(%s)s" % newName)
        field.name = newName
        model.setModified()
        self.flushMod()

    def fieldModelUseCount(self, fieldModel):
        "Return the number of cards using fieldModel."
        return self.s.scalar("""
select count(id) from fields where
fieldModelId = :id and value != ""
""", id=fieldModel.id)

    def rebuildFieldOrdinals(self, modelId, ids):
        """Update field ordinal for all fields given field model IDS.
Caller must update model modtime."""
        self.s.flush()
        strids = ",".join([str(id) for id in ids])
        self.s.statement("""
update fields
set ordinal = (select ordinal from fieldModels where id = fieldModelId)
where fields.fieldModelId in (%s)""" % strids)
        # dirty associated facts
        self.s.statement("""
update facts
set modified = strftime("%s", "now")
where modelId = :id""", id=modelId)
        self.flushMod()

    # Card models
    ##########################################################################

    def cardModelUseCount(self, cardModel):
        "Return the number of cards using cardModel."
        return self.s.scalar("""
select count(id) from cards where
cardModelId = :id""", id=cardModel.id)

    def deleteCardModel(self, model, cardModel):
        "Delete all cards that use CARDMODEL from the deck."
        cards = self.s.column0("select id from cards where cardModelId = :id",
                               id=cardModel.id)
        for id in cards:
            self.deleteCard(id)
        model.cardModels.remove(cardModel)
        model.setModified()
        self.flushMod()

    def updateCardsFromModel(self, cardModel):
        "Update all card question/answer when model changes."
        ids = self.s.all("""
select cards.id, cards.factId from cards, facts, cardmodels
where
cards.factId = facts.id and
facts.modelId = cardModels.modelId and
cards.cardModelId = :id""", id=cardModel.id)
        if not ids:
            return
        pend = [{'q': cardModel.renderQASQL('q', fid),
                 'a': cardModel.renderQASQL('a', fid),
                 'id': cid}
                for (cid, fid) in ids]
        self.s.execute("""
update cards
set
question = :q,
answer = :a,
modified = %f
where id = :id""" % time.time(), pend)

    def rebuildCardOrdinals(self, ids):
        "Update all card models in IDS. Caller must update model modtime."
        self.s.flush()
        strids = ",".join([str(id) for id in ids])
        self.s.statement("""
update cards set
ordinal = (select ordinal from cardModels where id = cardModelId),
modified = :now
where cardModelId in (%s)""" % strids, now=time.time())
        self.flushMod()

    # Tags
    ##########################################################################

    def tagsList(self):
        "Return a list of (cardId, allTags, priority)"
        return self.s.all("""
select cards.id, cards.tags || "," || facts.tags || "," || models.tags || "," ||
cardModels.name, cards.priority from cards, facts, models, cardModels where
cards.factId == facts.id and facts.modelId == models.id
and cards.cardModelId = cardModels.id""")

    def allTags(self):
        "Return a hash listing tags in model, fact and cards."
        return list(set(parseTags(",".join([x[1] for x in self.tagsList()]))))

    def cardTags(self, ids):
        return self.s.all("""
select id, tags from cards
where id in (%s)""" % ",".join([str(id) for id in ids]))

    def factTags(self, ids):
        return self.s.all("""
select id, tags from facts
where id in (%s)""" % ",".join([str(id) for id in ids]))

    def addCardTags(self, ids, tags, idfunc=None, table="cards"):
        if not idfunc:
            idfunc=self.cardTags
        tlist = idfunc(ids)
        newTags = parseTags(tags)
        now = time.time()
        pending = []
        for (id, tags) in tlist:
            oldTags = parseTags(tags)
            tmpTags = list(set(oldTags + newTags))
            if tmpTags != oldTags:
                pending.append(
                    {'id': id, 'now': now, 'tags': ", ".join(tmpTags)})
        self.s.statements("""
update %s set
tags = :tags,
modified = :now
where id = :id""" % table, pending)
        self.flushMod()

    def addFactTags(self, ids, tags):
        self.addCardTags(ids, tags, idfunc=self.factTags, table="facts")

    def deleteCardTags(self, ids, tags, idfunc=None, table="cards"):
        if not idfunc:
            idfunc=self.cardTags
        tlist = idfunc(ids)
        newTags = parseTags(tags)
        now = time.time()
        pending = []
        for (id, tags) in tlist:
            oldTags = parseTags(tags)
            tmpTags = oldTags[:]
            for tag in newTags:
                try:
                    tmpTags.remove(tag)
                except ValueError:
                    pass
            if tmpTags != oldTags:
                pending.append(
                    {'id': id, 'now': now, 'tags': ", ".join(tmpTags)})
        self.s.statements("""
update %s set
tags = :tags,
modified = :now
where id = :id""" % table, pending)
        self.flushMod()

    def deleteFactTags(self, ids, tags):
        self.deleteCardTags(ids, tags, idfunc=self.factTags, table="facts")

    # File-related
    ##########################################################################

    def name(self):
        n = os.path.splitext(os.path.basename(self.path))[0]
        n = re.sub("[^-A-Za-z0-9_+<>[]() ]", "", n)
        return n

    # Media
    ##########################################################################

    def mediaDir(self, create=False):
        "Return the media directory if exists. None if couldn't create."
        if not self.path:
            return None
        dir = re.sub("(?i)\.(anki)$", ".media", self.path)
        if not os.path.exists(dir) and create:
            try:
                os.mkdir(dir)
            except OSError:
                # permission denied
                return None
        if not os.path.exists(dir):
            return None
        return dir

    def _fileSize(self, file):
        st = os.stat(file)
        return st[stat.ST_SIZE]

    def addMedia(self, path):
        """Add PATH to the media directory.
Rename for uniqueness if not the same. Return the new name."""
        file = os.path.basename(path)
        dir = self.mediaDir()
        location = os.path.join(dir, file)
        location = location.replace('"', "")
        if os.path.exists(location):
            if self._fileSize(location) != self._fileSize(path):
                (location, exists) = self.uniquifyMediaLocation(
                    dir, location, self._fileSize(path))
                if not exists:
                    shutil.copy2(path, location)
        else:
            shutil.copy2(path, location)
        return os.path.basename(location)

    def renameMediaDir(self, oldPath):
        "Copy oldPath to our current media dir. "
        assert os.path.exists(oldPath)
        newPath = self.mediaDir(create=True)
        # copytree doesn't want the dir to exist
        os.rmdir(newPath)
        shutil.copytree(oldPath, newPath)

    def uniquifyMediaLocation(self, dir, location, fileSize):
        n = 0
        while 1:
            new = re.sub("^(.*)\.(.*?)$", "\\1_%d.\\2" % n, location)
            if not os.path.exists(new):
                return (new, True)
            if self._fileSize(new) == fileSize:
                return (new, False)
            n += 1

    # DB helpers
    ##########################################################################

    def save(self):
        "Commit any pending changes to disk."
        if self.lastLoaded == self.modified:
            return
        self.lastLoaded = self.modified
        self.s.commit()

    def close(self):
        self.s.rollback()
        self.s.clear()
        self.engine.dispose()

    def rollback(self):
        "Roll back the current transaction and reset session state."
        self.s.rollback()
        self.s.clear()
        self.refresh()

    def refresh(self):
        "Flush, invalidate all objects from cache and reload."
        self.s.flush()
        self.s.clear()
        self.s.update(self)
        self.s.refresh(self)

    def openSession(self):
        "Open a new session. Assumes old session is already closed."
        self.s = SessionHelper(self.Session(), lock=self.needLock)
        self.refresh()

    def closeSession(self):
        "Close the current session, saving any changes. Do nothing if no session."
        if self.s:
            self.save()
            try:
                self.s.expunge(self)
            except:
                import sys
                sys.stderr.write("ERROR expunging deck..\n")
            self.s.close()
            self.s = None

    def setModified(self, newTime=None):
        self.modified = newTime or time.time()

    def flushMod(self):
        "Mark modified and flush to DB."
        self.setModified()
        self.s.flush()

    def saveAs(self, newPath):
        oldMediaDir = self.mediaDir()
        # flush old deck
        self.s.flush()
        # remove new deck if it exists
        try:
            os.unlink(newPath)
        except OSError:
            pass
        # create new deck
        newDeck = DeckStorage.Deck(newPath)
        # attach current db to new
        s = newDeck.s.statement
        s("pragma read_uncommitted = 1")
        s("attach database :path as old", path=self.path)
        # copy all data
        s("delete from decks")
        s("delete from stats")
        s("insert into decks select * from old.decks")
        s("insert into fieldModels select * from old.fieldModels")
        s("insert into modelsDeleted select * from old.modelsDeleted")
        s("insert into cardModels select * from old.cardModels")
        s("insert into facts select * from old.facts")
        s("insert into fields select * from old.fields")
        s("insert into cards select * from old.cards")
        s("insert into factsDeleted select * from old.factsDeleted")
        s("insert into reviewHistory select * from old.reviewHistory")
        s("insert into cardsDeleted select * from old.cardsDeleted")
        s("insert into models select * from old.models")
        s("insert into stats select * from old.stats")
        # detach old db and commit
        s("detach database old")
        newDeck.s.commit()
        # close ourself, rebuild queue
        self.s.close()
        newDeck.refresh()
        newDeck.rebuildQueue()
        # move media
        if oldMediaDir:
            newDeck.renameMediaDir(oldMediaDir)
        # and return the new deck object
        return newDeck

    # DB maintenance
    ##########################################################################

    def fixIntegrity(self):
        "Responsibility of caller to call rebuildQueue()"
        if self.s.scalar("pragma integrity_check") != "ok":
            return _("Database file damaged. Restore from backup.")
        problems = []
        # does the user have a model?
        if not self.s.scalar("select count(id) from models"):
            self.addModel(stdmodels.byName("Basic"))
            problems.append(_("Deck was missing a model"))
        # is currentModel pointing to a valid model?
        if not self.s.all("""
select decks.id from decks, models where
decks.currentModelId = models.id"""):
            self.currentModelId = self.models[0].id
            problems.append(_("The current model didn't exist"))
        # facts missing a field?
        ids = self.s.column0("""
select distinct facts.id from facts, fieldModels where
facts.modelId = fieldModels.modelId and fieldModels.id not in
(select fieldModelId from fields where factId = facts.id)""")
        if ids:
            self.deleteFacts(ids)
            problems.append(_("Deleted %d facts with missing fields") %
                            len(ids))
        # cards missing a fact?
        ids = self.s.column0("""
select id from cards where factId not in (select id from facts)""")
        if ids:
            self.deleteCards(ids)
            problems.append(_("Deleted %d cards with missing fact") %
                            len(ids))
        # cards missing a card model?
        ids = self.s.column0("""
select id from cards where cardModelId not in
(select id from cardModels)""")
        if ids:
            self.deleteCards(ids)
            problems.append(_("Deleted %d cards with no card model" %
                              len(ids)))
        # facts missing a card?
        ids = self.deleteDanglingFacts()
        if ids:
            problems.append(_("Deleted %d facts with no cards" %
                              len(ids)))
        # dangling fields?
        ids = self.s.column0("""
select id from fields where factId not in (select id from facts)""")
        if ids:
            self.s.statement(
                "delete from fields where id in (%s)",
                ",".join([str(id) for id in ids]))
            problems.append(_("Deleted %d dangling fields") % len(ids))
        self.s.flush()
        # fix problems with cards being scheduled when not due
        self.s.statement("update cards set isDue = 0")
        # fix problems with conflicts on merge
        self.s.statement("update fields set id = random()")
        # fix any priorities
        self.updateAllPriorities()
        # fix problems with stripping html
        fields = self.s.all("select id, value from fields")
        newFields = []
        for (id, value) in fields:
            newFields.append({'id': id, 'value': tidyHTML(value)})
        self.s.statements(
            "update fields set value=:value where id=:id",
            newFields)
        # regenerate question/answer cache
        cms = self.s.query(CardModel).all()
        for cm in cms:
            self.updateCardsFromModel(cm)
            self.s.expunge(cm)
        # mark everything changed to force sync
        self.s.flush()
        self.s.statement("update cards set modified = :t", t=time.time())
        self.s.statement("update facts set modified = :t", t=time.time())
        self.s.statement("update models set modified = :t", t=time.time())
        # update deck and save
        self.flushMod()
        self.save()
        self.refresh()
        self.rebuildQueue()
        if problems:
            return "\n".join(problems)
        return "ok"

    def optimize(self):
        oldSize = os.stat(self.path)[stat.ST_SIZE]
        self.s.statement("vacuum")
        self.s.statement("analyze")
        newSize = os.stat(self.path)[stat.ST_SIZE]
        return oldSize - newSize

##########################################################################

mapper(Deck, decksTable, properties={
    'currentModel': relation(anki.models.Model, primaryjoin=
                             decksTable.c.currentModelId ==
                             anki.models.modelsTable.c.id),
    'models': relation(anki.models.Model, post_update=True,
                       primaryjoin=
                       decksTable.c.id ==
                       anki.models.modelsTable.c.deckId),
    })

# Deck storage
##########################################################################

class DeckStorage(object):

    backupDir = os.path.expanduser("~/.anki/backups")
    numBackups = 100
    newDeckDir = "~"

    def newDeckPath():
        # create ~/mydeck(N).anki
        n = 2
        path = os.path.expanduser(
            os.path.join(DeckStorage.newDeckDir, "mydeck.anki"))
        while os.path.exists(path):
            path = os.path.expanduser(
                os.path.join(DeckStorage.newDeckDir, "mydeck%d.anki") % n)
            n += 1
        return path
    newDeckPath = staticmethod(newDeckPath)

    def Deck(path=None, rebuild=True, backup=True, lock=True):
        "Create a new deck or attach to an existing one."
        # generate a temp name if necessary
        if path is None:
            path = DeckStorage.newDeckPath()
        create = True
        if path != -1:
            if isinstance(path, types.UnicodeType):
                path = path.encode(sys.getfilesystemencoding())
            path = os.path.abspath(path)
            #print "using path", path
            if os.path.exists(path):
                # attach
                if not os.access(path, os.R_OK | os.W_OK):
                    raise DeckAccessError(_("Can't read/write deck"))
                create = False
        # attach and sync/fetch deck - first, to unicode
        if not isinstance(path, types.UnicodeType):
            path = unicode(path, sys.getfilesystemencoding())
        # sqlite needs utf8
        (engine, session) = DeckStorage._attach(path.encode("utf-8"), create)
        s = session()
        try:
            if create:
                deck = DeckStorage._init(s)
            else:
                deck = s.query(Deck).get(1)
            # attach db vars
            deck.path = path
            deck.engine = engine
            deck.Session = session
            deck.needLock = lock
            deck.s = SessionHelper(s, lock=lock)
            if create:
                # new-style file format
                deck.s.execute("pragma legacy_file_format = off")
                deck.s.execute("vacuum")
                # add views/indices
                DeckStorage._addViews(deck)
                DeckStorage._addIndices(deck)
                deck.s.statement("analyze")
            else:
                if backup:
                    DeckStorage.backup(deck.modified, path)
                deck = DeckStorage._upgradeDeck(deck, path)
        except OperationalError, e:
            if (str(e.orig).startswith("database table is locked") or
                str(e.orig).startswith("database is locked")):
                raise DeckAccessError(_("File is in use by another process"),
                                      type="inuse")
            else:
                raise e
        # rebuild?
        if rebuild:
            deck.rebuildQueue()
        deck._initVars()
        deck.s.commit()
        return deck
    Deck = staticmethod(Deck)

    def _attach(path, create):
        "Attach to a file, initializing DB"
        if path == -1:
            path = "sqlite:///:memory:"
        else:
            path = "sqlite:///" + path
        engine = create_engine(path,
                               strategy='threadlocal',
                               connect_args={'timeout': 0})
        session = sessionmaker(bind=engine,
                               autoflush=False,
                               transactional=False)
        try:
            metadata.create_all(engine)
        except DBAPIError, e:
            engine.dispose()
            if create:
                raise DeckAccessError(_("Can't read/write deck"))
            else:
                raise DeckWrongFormatError("Deck is not in the right format")
        return (engine, session)
    _attach = staticmethod(_attach)

    def _init(s):
        "Add a new deck to the database. Return saved deck."
        deck = Deck()
        s.save(deck)
        s.flush()
        return deck
    _init = staticmethod(_init)

    def _addIndices(deck):
        "Add indices to the DB."
        # card queues
        deck.s.statement("""
create index if not exists ix_cards_markExpired on cards
(isDue, priority desc, combinedDue desc)""")
        deck.s.statement("""
create index if not exists ix_cards_failedIsDue on cards
(type, isDue, combinedDue)""")
        deck.s.statement("""
create index if not exists ix_cards_failedOrder on cards
(type, isDue, due)""")
        deck.s.statement("""
create index if not exists ix_cards_revisionOrder on cards
(type, isDue, priority desc, relativeDelay)""")
        deck.s.statement("""
create index if not exists ix_cards_newRandomOrder on cards
(priority desc, factId, ordinal)""")
        deck.s.statement("""
create index if not exists ix_cards_newOrderedOrder on cards
(priority desc, due)""")
        # card spacing
        deck.s.statement("""
create index if not exists ix_cards_factId on cards (factId)""")
        # stats
        deck.s.statement("""
create index if not exists ix_stats_typeDay on stats (type, day)""""")
        # fields
        deck.s.statement("""
create index if not exists ix_fields_factId on fields (factId)""")
        deck.s.statement("""
create index if not exists ix_fields_fieldModelId on fields (fieldModelId)""")
        deck.s.statement("""
create index if not exists ix_fields_value on fields (value)""")
        # deletion tracking
        deck.s.statement("""
create index if not exists ix_cardsDeleted_cardId on cardsDeleted (cardId)""")
        deck.s.statement("""
create index if not exists ix_modelsDeleted_modelId on modelsDeleted (modelId)""")
        deck.s.statement("""
create index if not exists ix_factsDeleted_factId on factsDeleted (factId)""")
    _addIndices = staticmethod(_addIndices)

    def _addViews(deck):
        "Add latest version of SQL views to DB."
        s = deck.s
        # old tables
        s.statement("drop view if exists failedCards")
        s.statement("drop view if exists acqCards")
        s.statement("drop view if exists futureCards")
        s.statement("drop view if exists typedCards")
        s.statement("drop view if exists failedCards")
        s.statement("drop view if exists failedCardsNow")
        s.statement("""
create view failedCardsNow as
select * from cards
where type = 0 and isDue = 1
and combinedDue <= (strftime("%s", "now") + 1)
order by combinedDue
""")
        s.statement("drop view if exists failedCardsSoon")
        s.statement("""
create view failedCardsSoon as
select * from cards
where type = 0 and priority != 0
and combinedDue <=
(select max(delay0, delay1)+strftime("%s", "now")+1
from decks)
order by modified
""")
        s.statement("drop view if exists revCards")
        s.statement("""
create view revCards as
select * from cards where
type = 1 and isDue = 1
order by type, isDue, priority desc, relativeDelay""")
        s.statement("drop view if exists acqCardsRandom")
        s.statement("""
create view acqCardsRandom as
select * from cards
where type = 2 and isDue = 1
order by priority desc, factId, ordinal""")
        s.statement("drop view if exists acqCardsOrdered")
        s.statement("""
create view acqCardsOrdered as
select * from cards
where type = 2 and isDue = 1
order by priority desc, due""")
    _addViews = staticmethod(_addViews)

    def _upgradeDeck(deck, path):
        "Upgrade deck to the latest version."
        deck.path = path
        if deck.version == 0:
            # new columns
            try:
                deck.s.statement("""
    alter table cards add column spaceUntil float not null default 0""")
                deck.s.statement("""
    alter table cards add column relativeDelay float not null default 0.0""")
                deck.s.statement("""
    alter table cards add column isDue boolean not null default 0""")
                deck.s.statement("""
    alter table cards add column type integer not null default 0""")
                deck.s.statement("""
    alter table cards add column combinedDue float not null default 0""")
                # update cards.spaceUntil based on old facts
                deck.s.statement("""
    update cards
    set spaceUntil = (select (case
    when cards.id = facts.lastCardId
    then 0
    else facts.spaceUntil
    end) from cards as c, facts
    where c.factId = facts.id
    and cards.id = c.id)""")
                deck.s.statement("""
    update cards
    set combinedDue = max(due, spaceUntil)
    """)
            except:
                print "failed to upgrade"
            # rebuild with new file format
            deck.s.execute("pragma legacy_file_format = off")
            deck.s.execute("vacuum")
            # bump version
            deck.version = 1
            deck.s.commit()
            # add views/indices
            DeckStorage._addViews(deck)
            DeckStorage._addIndices(deck)
            # rebuild type and delay cache
            deck.rebuildTypes()
            deck.rebuildQueue()
            deck.s.commit()
            # optimize indices
            deck.s.statement("analyze")
        if deck.version == 1:
            # fix indexes and views
            deck.s.statement("drop index ix_cards_newRandomOrder")
            deck.s.statement("drop index ix_cards_newOrderedOrder")
            DeckStorage._addViews(deck)
            DeckStorage._addIndices(deck)
            deck.rebuildTypes()
            # optimize indices
            deck.s.statement("analyze")
            deck.version = 2
            deck.s.commit()
        if deck.version == 2:
            # compensate for bug in 0.9.7 by rebuilding isDue and priorities
            deck.s.statement("update cards set isDue = 0")
            deck.updateAllPriorities()
            # compensate for bug in early 0.9.x where fieldId was not unique
            deck.s.statement("update fields set id = random()")
            deck.version = 3
            deck.s.commit()
        if deck.version == 3:
            # remove conflicting and unused indexes
            deck.s.statement("drop index if exists ix_cards_isDueCombined")
            deck.s.statement("drop index if exists ix_facts_lastCardId")
            deck.s.statement("drop index if exists ix_cards_successive")
            deck.s.statement("drop index if exists ix_cards_priority")
            deck.s.statement("drop index if exists ix_cards_reps")
            deck.s.statement("drop index if exists ix_cards_due")
            deck.s.statement("drop index if exists ix_stats_type")
            deck.s.statement("drop index if exists ix_stats_day")
            deck.s.statement("drop index if exists ix_factsDeleted_cardId")
            deck.s.statement("drop index if exists ix_modelsDeleted_cardId")
            DeckStorage._addIndices(deck)
            deck.s.statement("analyze")
            deck.version = 4
            deck.s.commit()
        return deck
    _upgradeDeck = staticmethod(_upgradeDeck)

    def backup(modified, path):
        # need a non-unicode path
        path = path.encode(sys.getfilesystemencoding())
        backupDir = DeckStorage.backupDir.encode(sys.getfilesystemencoding())
        numBackups = DeckStorage.numBackups
        def backupName(path, num):
            path = os.path.abspath(path)
            path = path.replace("\\", "!")
            path = path.replace("/", "!")
            path = path.replace(":", "")
            path = os.path.join(backupDir, path)
            path = re.sub("\.anki$", ".backup-%d.anki" % num, path)
            return path
        if not os.path.exists(backupDir):
            os.makedirs(backupDir)
        # if the mod time is identical, don't make a new backup
        firstBack = backupName(path, 0)
        if os.path.exists(firstBack):
            s1 = int(modified)
            s2 = int(os.stat(firstBack)[stat.ST_MTIME])
            if s1 == s2:
                return
        # remove the oldest backup if it exists
        oldest = backupName(path, numBackups)
        if os.path.exists(oldest):
            os.chmod(oldest, 0666)
            os.unlink(oldest)
        # move all the other backups up one
        for n in range(numBackups - 1, -1, -1):
            name = backupName(path, n)
            if os.path.exists(name):
                newname = backupName(path, n+1)
                if os.path.exists(newname):
                    os.chmod(newname, 0666)
                    os.unlink(newname)
                os.rename(name, newname)
        # save the current path
        newpath = backupName(path, 0)
        if os.path.exists(newpath):
            os.chmod(newpath, 0666)
            os.unlink(newpath)
        shutil.copy2(path, newpath)
        # set mtimes to be identical
        os.utime(newpath, (modified, modified))
    backup = staticmethod(backup)
