# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, types, socket, time
import ankiqt
import anki
from anki.sync import SyncClient, HttpSyncServerProxy
from anki.errors import *
from anki import DeckStorage
import ankiqt.forms

# Synchronising a deck with a public server
##########################################################################

class Sync(QThread):

    def __init__(self, parent, user, pwd, interactive, create, onlyMerge):
        QThread.__init__(self)
        self.parent = parent
        self.interactive = interactive
        self.user = user
        self.pwd = pwd
        self.create = create
        self.ok = True
        self.onlyMerge = onlyMerge

    def setStatus(self, msg, timeout=5000):
        self.emit(SIGNAL("setStatus"), msg, timeout)

    def run(self):
        self.syncDeck()

    def error(self, error):
        self.setStatus(self.getErrorMessage(error))
        if self.onlyMerge:
            # new file needs cleaning up
            self.emit(SIGNAL("cleanNewDeck"))
        else:
            self.emit(SIGNAL("syncFinished"))

    def getErrorMessage(self, error):
        if error.data.get('status') == "invalidUserPass":
            msg=_("Please double-check your username/password.")
        elif error.data.get('status') == "oldVersion":
            msg=_("The sync protocol has changed. Please upgrade.")
        elif error.data.get('type') == "noResponse":
            msg=_("Server is down or operation failed.")
        else:
            msg=_("Unknown error: %s") % `error.data`
        return msg

    def connect(self, *args):
        # connect, check auth
        proxy = HttpSyncServerProxy(self.user, self.pwd)
        proxy.connect("ankiqt-" + ankiqt.appVersion)
        return proxy

    def syncDeck(self):
        self.setStatus(_("Connecting.."), 0)
        try:
            proxy = self.connect()
        except SyncError, e:
            return self.error(e)
        # exists on server?
        if not proxy.hasDeck(self.parent.syncName):
            if self.create:
                try:
                    proxy.createDeck(self.parent.syncName)
                except SyncError, e:
                    return self.error(e)
            else:
                self.emit(SIGNAL("noMatchingDeck"), proxy.decks.keys(),
                          not self.onlyMerge)
                self.setStatus("")
                #self.emit(SIGNAL("moveToState"), "initial")
                return
        # reconnect
        try:
            self.deck = DeckStorage.Deck(self.parent.deckPath, rebuild=False,
                                         backup=False, lock=True)
            # need to do anything?
            proxy.deckName = self.parent.syncName
            if self.deck.modified == proxy.modified():
                self.setStatus(_("Sync: nothing to do"))
                self.deck.close()
                self.emit(SIGNAL("syncFinished"))
                return
            # start syncing
            client = SyncClient(self.deck)
            client.setServer(proxy)
            # handle the sync manually so we can give more feedback
            client.localTime = client.modified()
            client.remoteTime = proxy.modified()
            l = self.parent.lastSync; r = proxy._lastSync()
            if l == r:
                self.lastSync = l
            else:
                self.lastSync = 0
            self.setStatus(_("Fetching summary from server.."), 0)
            lsum = client.summary(self.lastSync)
            rsum = proxy.summary(self.lastSync)

            self.setStatus(_("Determining differences.."), 0)
            oldCount = self.deck.cardCount()
            payload = client.genPayload(lsum, rsum)
            ladd = len(payload['added-cards'])
            radd = len(payload['missing-cards'])
            rdel = len(payload['deleted-cards'])
            ldel = max(0, oldCount - self.deck.cardCount())
            stats = {"a": ladd, "b": ldel, "c": radd, "d": rdel}

            self.setStatus(_("Sending payload (local +%(a)d/-%(b)d, "
                             "remote +%(c)d/-%(d)d cards)..") % stats, 0)
            res = proxy.applyPayload(payload)
            self.setStatus(_("Applying reply.."), 0)
            client.applyPayloadReply(res)

            self.setStatus(_("Syncing..done. Local +%(a)d/-%(b)d, "
                             "remote +%(c)d/-%(d)d cards.")
                           % stats)
            # finished. save deck, preserving mod time
            self.deck.lastLoaded = self.deck.modified
            self.deck.s.flush()
            self.deck.s.commit()
            # close and send signal to main thread
            self.deck.close()
            self.emit(SIGNAL("syncFinished"))
        except Exception, e:
            self.deck.close()
            # cheap hack to ensure message is displayed
            time.sleep(1)
            err = `getattr(e, 'data', None) or e`
            self.setStatus(_("Syncing failed: %(a)s") % {
                'a': err})
            self.emit(SIGNAL("syncFinished"))

# Choosing a deck to sync to
##########################################################################

class DeckChooser(QDialog):

    def __init__(self, parent, decks, create):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.decks = decks
        self.dialog = ankiqt.forms.syncdeck.Ui_DeckChooser()
        self.dialog.setupUi(self)
        self.create = create
        if self.create:
            self.dialog.decks.addItem(QListWidgetItem(
                _("Create '%s' on server") % self.parent.syncName))
        self.decks.sort()
        for name in decks:
            name = os.path.splitext(name)[0]
            item = QListWidgetItem(_("Merge with '%s' on server") % name)
            self.dialog.decks.addItem(item)
        self.dialog.decks.setCurrentRow(0)
        # the list widget will swallow the enter key
        s = QShortcut(QKeySequence("Return"), self)
        self.connect(s, SIGNAL("activated()"), self.accept)
        self.name = None

    def getName(self):
        self.exec_()
        return self.name

    def accept(self):
        idx = self.dialog.decks.currentRow()
        if self.create:
            offset = 1
        else:
            offset = 0
        if idx == 0 and self.create:
            self.name = self.parent.syncName
        else:
            self.name = self.decks[self.dialog.decks.currentRow() - offset]
        self.close()

