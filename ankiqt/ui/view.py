# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import anki, anki.utils
from anki.sound import playFromText, stripSounds
from anki.latex import renderLatex
from anki.utils import stripHTML
import types, time
from ankiqt import ui

# Views - define the way a user is prompted for questions, etc
##########################################################################

class View(object):
    "Handle the main window update as we transition through various states."

    def __init__(self, parent, body, frame=None):
        self.main = parent
        self.body = body
        self.frame = frame

    # State control
    ##########################################################################

    def setState(self, state):
        "Change to STATE, and update the display."
        self.oldState = getattr(self, 'state', None)
        self.state = state
        if self.state == "initial":
            self.shownLearnHelp = False
            self.shownReviewHelp = False
            self.shownFinalHelp = False
            return
        elif self.state == "noDeck":
            self.clearWindow()
            self.drawNoDeckMessage()
            self.flush()
            return
        self.redisplay()

    def redisplay(self):
        "Idempotently display the current state (prompt for question, etc)"
        if self.state == "noDeck":
            return
        self.clearWindow()
        self.setBackgroundColour()
        self.maybeHelp()
        if self.main.deck.totalCardCount():
            self.addStyles()
            if self.main.lastCard:
                self.drawTopSection()
            else:
                self.buffer += "<br>"
        if self.state == "showQuestion":
            self.drawQuestion()
        elif self.state == "showAnswer":
            if not self.main.currentCard.cardModel.questionInAnswer:
                self.drawQuestion(nosound=True)
            self.drawAnswer()
        elif self.state == "deckEmpty":
            self.drawDeckEmptyMessage()
        elif self.state == "deckFinished":
            self.drawDeckFinishedMessage()
        self.flush()

    def addStyles(self):
        # card styles
        self.buffer += "<style>\n"
        if self.main.currentCard:
            self.buffer += self.main.currentCard.css()
        # last card
        for base in ("lastCard", "interface"):
            family = self.main.config[base + "FontFamily"]
            size = self.main.config[base + "FontSize"]
            color = ("; color: " + self.main.config[base + "Colour"])
            self.buffer += ('.%s {font-family: "%s"; font-size: %spx%s}\n' %
                            (base, family, size, color))
        # standard margins
        self.buffer += "</style>"

    def clearWindow(self):
        self.body.setHtml("")
        self.buffer = ""

    # Font properties & output
    ##########################################################################

    def flush(self):
        "Write the current HTML buffer to the screen."
        self.body.setHtml(self.buffer)

    def write(self, text):
        if type(text) != types.UnicodeType:
            text = unicode(text, "utf-8")
        self.buffer += text

    def setBackgroundColour(self):
        p = QPalette()
        p.setColor(QPalette.Base, QColor(self.main.config['backgroundColour']))
        self.body.setPalette(p)
        if self.frame:
            p.setColor(QPalette.Background, QColor(self.main.config['backgroundColour']))
            self.frame.setPalette(p)

    # Question and answer
    ##########################################################################

    def drawQuestion(self, nosound=False):
        "Show the question."
        q = self.main.currentCard.htmlQuestion
        q = renderLatex(self.main.deck, q)
        self.write(stripSounds(q))
        if self.state != self.oldState and not nosound:
            playFromText(q)

    def drawAnswer(self):
        "Show the answer."
        a = self.main.currentCard.htmlAnswer
        a = renderLatex(self.main.deck, a)
        self.write(stripSounds(a))
        if self.state != self.oldState:
            playFromText(a)

    # Top section
    ##########################################################################

    def drawTopSection(self):
        "Show previous card, next scheduled time, and stats."
        self.buffer += "<center>"
        self.drawLastCard()
        self.buffer += "</center>"

    def drawLastCard(self):
        "Show the last card if not the current one, and next time."
        if self.main.lastCard and (
            self.state == "deckFinished" or
            self.main.lastCard != self.main.currentCard):
            q = self.main.lastCard.question.replace("<br>", "  ")
            q = stripHTML(q)
            if len(q) > 50:
                q = q[:50] + "..."
            a = self.main.lastCard.answer.replace("<br>", "  ")
            a = stripHTML(a)
            if len(a) > 50:
                a = a[:50] + "..."
            s = "%s<br>%s" % (q, a)
            self.write('<span class="lastCard">%s</span><br>' % s)
            if self.main.lastQuality > 1:
                msg = _("Well done! This card will appear again in "
                        "<b>%(next)s</b>.") % \
                        {"next":self.main.lastScheduledTime}
            else:
                msg = _("This card will appear again in "
                        "<b>%(next)s</b>.") % \
                        {"next":self.main.lastScheduledTime}
            self.write('<span class="interface">' + msg + "</span><br>")

    # Help
    ##########################################################################

    def maybeHelp(self):
        return
        stats = self.main.deck.sched.getStats()
        if not stats['pending']:
            self.main.help.hide()
        elif (self.main.currentCard and
            self.main.currentCard.nextTime > time.time()):
            if not self.shownFinalHelp:
                self.shownFinalHelp = True
                self.main.help.showHideableKey("finalReview")
        elif stats['learnMode']:
            if not self.shownLearnHelp:
                if stats['pending'] != 0:
                    self.shownLearnHelp = True
                    self.main.help.showHideableKey("learn")
        else:
            if not self.shownReviewHelp:
                self.shownReviewHelp = True
                self.main.help.showHideableKey("review")

    # Welcome/empty/finished deck messages
    ##########################################################################

    def drawNoDeckMessage(self):
        self.write(_("""<h1>Welcome to Anki!</h1>
<p>
<table width=90%>
<tr>
<td>
Anki is a tool which will help you remember things as quickly and easily as
possible. Anki works by asking you questions. After answering a question,
Anki will ask how well you remembered. If you made a mistake or had difficulty
remembering, Anki will show you the question again after a short amount of
time. If you answered the question easily, Anki will wait for a number of days
before asking you again. Each time you successfully remember something, the
time before you see it again will get bigger.
</td>
</tr>
</table>

<p>
<table>

<tr>
<td width=50>
<a href="welcome:sample"><img src=":/icons/anki.png"></a>
</td>
<td valign=middle><h2><a href="welcome:sample">Open a sample deck</a></h2></td>
</tr>

<tr>
<td>
<a href="welcome:open"><img src=":/icons/fileopen.png"></a>
</td>
<td valign=middle><h2><a href="welcome:open">Open an existing deck</a></h2></td>
</tr>

<tr>
<td>
<a href="welcome:new"><img src=":/icons/filenew.png"></a>
</td>
<td valign=middle>
<h2><a href="welcome:new">Create a new deck</a></h2></td>
</tr>
</table>
<p>
<table width=90%>
<tr>
<td>
<h2>Adding material</h2>
There are three ways to add material to Anki: typing it in yourself, using a
pre-made Anki deck, or importing word lists that you find on the internet.
<p>

For language learning, it's a good idea to add material yourself, from sources
like a textbook or a TV show. By adding words that you see or hear in context,
you also learn how they are used. While it may be tempting to use a big,
pre-made vocabulary list to save time, learning words and grammar in context
will ensure you can use them naturally.
<p>

So if you're learning a language, consider adding material you want to learn
into Anki by yourself. Initially the time required to type in material may
seem daunting, but it's a small amount of time compared to the time you'll
save by not forgetting.
</td>
</tr>
</table>
"""))

    def drawDeckEmptyMessage(self):
        "Tell the user the deck is empty."
        self.write(_("""
<h1>Empty deck</h1>The current deck has no cards in it. Please select 'Add
card' from the Edit menu."""))

    def drawDeckFinishedMessage(self):
        "Tell the user the deck is finished."
        next = self.main.deck.earliestTimeStr()
        suspended = self.main.deck.suspendedCardCount()
        waiting = self.main.deck.spacedCardCount()
        self.clearWindow()
        self.write(_("""
<h1>Congratulations!</h1>You have finished the deck for now.<br>
The next question will be shown in <b>%(next)s</b>.<p>
There are %(waiting)d
<a href="http://ichi2.net/anki/wiki/FrequentlyAskedQuestions#head-ef653836eaddb2b9c1af6b8fa56bcea458a04c20">spaced</a> cards.<br>
There are %(suspended)d suspended cards.<p>
Spaced cards are cards that won't be shown for a while, because you have seen<br>
a related card recently. Suspended cards are cards removed from the learning<br>
process - they won't be shown until you unsuspend them.""") % {
    "next": next,
    "suspended": suspended,
    "waiting": waiting,
    })
