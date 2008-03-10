# Copyright: Damien Elmes <anki@ichi2.net>
# -*- coding: utf-8 -*-
# License: GNU GPL, version 2 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# fixme: sample files read only, need to copy

import os, sys, re, types, gettext, stat, traceback, shutil, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki import DeckStorage
from anki.errors import *
from anki.sound import hasSound, playFromText
from anki.utils import addTags, deleteTags
from anki.deck import FutureItem
import anki.lang
import ankiqt
ui = ankiqt.ui
config = ankiqt.config

class AnkiQt(QMainWindow):
    def __init__(self, app, config, args):
        QMainWindow.__init__(self)
        ankiqt.mw = self
        self.app = app
        self.config = config
        self.deck = None
        self.views = []
        self.macHacks()
        self.setLang()
        self.setupFonts()
        self.setupBackupDir()
        self.setupHooks()
        self.loadUserCustomisations()
        self.mainWin = ankiqt.forms.main.Ui_MainWindow()
        self.mainWin.setupUi(self)
        self.alterShortcuts()
        self.help = ui.help.HelpArea(self.mainWin.helpFrame, self.config, self)
        self.connectMenuActions()
        if sys.platform.startswith("darwin"):
            # window creeps on osx, just resize
            self.resize(*self.config['mainWindowGeometry'][2:4])
        else:
            self.setGeometry(QRect(*self.config['mainWindowGeometry']))
        self.bodyView = ui.view.View(self, self.mainWin.mainText,
                                     self.mainWin.mainTextFrame)
        self.addView(self.bodyView)
        self.statusView = ui.status.StatusView(self)
        self.addView(self.statusView)
        self.setupButtons()
        self.setupAnchors()
        if not self.config['showToolbar']:
            self.removeToolBar(self.mainWin.toolBar)
            self.mainWin.toolBar.hide()
        self.show()
        # load deck
        try:
            self.maybeLoadLastDeck(args)
        finally:
            self.setEnabled(True)
            # the focus is not set while disabled, so fetch card again
            self.moveToState("auto")
        # run after-init hook
        try:
            self.runHook('init')
        except:
            print _("Error running initHook. Broken plugin?")
            print traceback.print_exc()
        # check for updates
        self.setupAutoUpdate()

    # State machine
    ##########################################################################

    def addView(self, view):
        self.views.append(view)

    def updateViews(self, status):
        if self.deck is None and status != "noDeck":
            raise "updateViews() called with no deck. status=%s" % status
        for view in self.views:
            view.setState(status)

    def reset(self):
        if self.deck:
            self.deck.s.flush()
            self.deck.refresh()
            self.deck.updateAllPriorities()
            self.rebuildQueue()

    def rebuildQueue(self):
        # qt on mac is misbehaving
        mac = sys.platform.startswith("darwin")
        if not mac: self.setEnabled(False)
        self.mainWin.mainText.clear()
        self.mainWin.mainText.setHtml("<h1>Building revision queue..</h1>")
        self.app.processEvents()
        self.deck.rebuildQueue()
        if not mac: self.setEnabled(True)
        self.moveToState("initial")

    def moveToState(self, state):
        if state == "initial":
            # reset current card and load again
            self.currentCard = None
            self.lastCard = None
            if self.deck:
                self.mainWin.menu_Lookup.setEnabled(True)
                self.enableDeckMenuItems()
                self.updateRecentFilesMenu()
                self.updateViews(state)
                return self.moveToState("getQuestion")
            else:
                return self.moveToState("noDeck")
        elif state == "auto":
            # load again without resetting current card
            if self.deck:
                return self.moveToState("getQuestion")
            else:
                return self.moveToState("noDeck")
        # save the new & last state
        self.lastState = getattr(self, "state", None)
        self.state = state
        self.updateTitleBar()
        if state == "noDeck":
            self.help.hide()
            self.disableDeckMenuItems()
            self.resetButtons()
        elif state == "getQuestion":
            if self.deck.totalCardCount() == 0:
                return self.moveToState("deckEmpty")
            else:
                if not self.currentCard:
                    self.currentCard = self.deck.getCard()
                if self.currentCard:
                    self.enableCardMenuItems()
                    return self.moveToState("showQuestion")
                else:
                    return self.moveToState("deckFinished")
        elif state == "deckEmpty":
            self.resetButtons()
            self.disableCardMenuItems()
            self.mainWin.menu_Lookup.setEnabled(False)
        elif state == "deckFinished":
            self.deck.s.flush()
            self.resetButtons()
            self.mainWin.menu_Lookup.setEnabled(False)
            self.disableCardMenuItems()
            self.startRefreshTimer()
            self.bodyView.setState(state)
        elif state == "showQuestion":
            if self.deck.mediaDir():
                os.chdir(self.deck.mediaDir())
            self.resetButtons()
            self.showAnswerButton()
            self.updateMarkAction()
            self.runHook('showQuestion')
        elif state == "showAnswer":
            self.resetButtons()
            self.showEaseButtons()
            self.enableCardMenuItems()
        self.updateViews(state)

    def keyPressEvent(self, evt):
        "Show answer on RET or register answer."
        if self.state == "showQuestion":
            if evt.key() in (Qt.Key_Enter,
                             Qt.Key_Return):
                evt.accept()
                return self.moveToState("showAnswer")
        elif self.state == "showAnswer":
            key = unicode(evt.text())
            if key and key >= "0" and key <= "4":
                # user entered a quality setting
                num=int(key)
                evt.accept()
                return self.cardAnswered(num)
        evt.ignore()

    def cardAnswered(self, quality):
        "Reschedule current card and move back to getQuestion state."
        # for undo
        oldFactor = self.currentCard.factor
        successive = self.currentCard.successive
        self.deck.answerCard(self.currentCard, quality)
        self.lastScheduledTime = anki.utils.fmtTimeSpan(
            self.currentCard.due - time.time())
        self.lastQuality = quality
        self.lastCard = self.currentCard
        self.lastCard.oldFactor = oldFactor
        self.lastCard.oldSuccessive = successive
        self.currentCard = None
        if self.config['saveAfterAnswer']:
            num = self.config['saveAfterAnswerNum']
            stats = self.deck.getStats()
            if stats['gTotal'] % num == 0:
                self.saveDeck()
        self.moveToState("getQuestion")

    def startRefreshTimer(self):
        "Update the screen once a minute until next card is displayed."
        if getattr(self, 'refreshTimer', None):
            return
        self.refreshTimer = QTimer(self)
        self.refreshTimer.start(60000)
        self.connect(self.refreshTimer, SIGNAL("timeout()"), self.refreshStatus)
        # start another time to refresh exactly after we've finished
        next = self.deck.earliestTime()
        if next:
            delay = next - time.time()
            delay = (delay+1)*1000
            if delay > 86400:
                return
            if delay < 0:
                sys.stderr.write("earliest time returned negative value\n")
                return
            t = QTimer(self)
            t.setSingleShot(True)
            self.connect(t, SIGNAL("timeout()"), self.refreshStatus)
            t.start((delay+1)*1000)

    def refreshStatus(self):
        "If triggered when the deck is finished, reset state."
        if self.state == "deckFinished":
            self.moveToState("initial")
        if self.state != "deckFinished":
            self.refreshTimer.stop()
            self.refreshTimer = None

    # Buttons
    ##########################################################################

    def setupButtons(self):
        self.outerButtonBox = QHBoxLayout(self.mainWin.buttonWidget)
        self.outerButtonBox.setMargin(3)
        self.outerButtonBox.setSpacing(0)
        self.innerButtonWidget = None

    def resetButtons(self):
        # this round-about process is trying to work around a bug in qt
        if self.lastState == self.state:
            return
        if self.innerButtonWidget:
            self.outerButtonBox.removeWidget(self.innerButtonWidget)
            self.innerButtonWidget.setParent(None)
        self.innerButtonWidget = QWidget()
        self.outerButtonBox.addWidget(self.innerButtonWidget)
        self.buttonBox = QVBoxLayout(self.innerButtonWidget)
        self.buttonBox.setSpacing(3)
        self.buttonBox.setMargin(3)
        if self.config['easeButtonHeight'] == "tall":
            self.easeButtonHeight = 50
        else:
            if sys.platform.startswith("darwin"):
                self.easeButtonHeight = 35
            else:
                self.easeButtonHeight = 25

    def showAnswerButton(self):
        if self.lastState == self.state:
            return
        button = QPushButton(_("Show answer"))
        button.setFixedHeight(self.easeButtonHeight)
        self.buttonBox.addWidget(button)
        button.setFocus()
        button.setDefault(True)
        self.connect(button, SIGNAL("clicked()"),
                     lambda: self.moveToState("showAnswer"))

    def getSpacer(self, hpolicy=QSizePolicy.Preferred):
        return QSpacerItem(20, 20,
                           hpolicy,
                           QSizePolicy.Preferred)

    def showEaseButtons(self):
        # if the state hasn't changed, do nothing
        if self.lastState == self.state:
            return
        # gather next intervals
        nextInts = {}
        for i in range(5):
            s=self.deck.nextIntervalStr(self.currentCard, i)
            nextInts["ease%d" % i] = s
        text = (
            (_("Completely forgot"), ""),
            (_("Made a mistake"), ""),
            (_("Difficult"),
             _("Next in <b>%(ease2)s</b>")),
            (_("About right"),
             _("Next in <b>%(ease3)s</b>")),
            (_("Easy"),
             _("Next in <b>%(ease4)s</b>")))
        # button grid
        grid = QGridLayout()
        grid.setSpacing(3)
        if self.config['easeButtonStyle'] == 'standard':
            button3 = self.showStandardEaseButtons(grid, nextInts, text)
        else:
            button3 = self.showCompactEaseButtons(grid, nextInts)
        self.buttonBox.addLayout(grid)
        button3.setFocus()

    def showStandardEaseButtons(self, grid, nextInts, text):
        # show 'how well?' message
        hbox = QHBoxLayout()
        hbox.addItem(self.getSpacer(QSizePolicy.Expanding))
        label = QLabel(self.withInterfaceFont(
            _("<b>How well did you remember?</b>")))
        hbox.addWidget(label)
        hbox.addItem(self.getSpacer(QSizePolicy.Expanding))
        self.buttonBox.addLayout(hbox)
        # populate buttons
        button3 = None
        for i in range(5):
            button = QPushButton(str(i))
            button.setFixedWidth(100)
            button.setFixedHeight(self.easeButtonHeight)
            if i == 3:
                button3 = button
            grid.addItem(self.getSpacer(QSizePolicy.Expanding), i, 0)
            grid.addWidget(button, i, 1)
            grid.addItem(self.getSpacer(), i, 2)
            grid.addWidget(QLabel(self.withInterfaceFont(text[i][0])), i, 3)
            grid.addItem(self.getSpacer(), i, 4)
            grid.addWidget(QLabel(self.withInterfaceFont(
                text[i][1] % nextInts)), i, 5)
            grid.addItem(self.getSpacer(QSizePolicy.Expanding), i, 6)
            self.connect(button, SIGNAL("clicked()"),
                         lambda i=i: self.cardAnswered(i))
        return button3

    def showCompactEaseButtons(self, grid, nextInts):
        text = (
            (_("<b>%(ease0)s</b>")),
            (_("<b>%(ease1)s</b>")),
            (_("<b>%(ease2)s</b>")),
            (_("<b>%(ease3)s</b>")),
            (_("<b>%(ease4)s</b>")))
        button3 = None
        for i in range(5):
            button = QPushButton(str(i))
            button.setFixedHeight(self.easeButtonHeight)
            #button.setFixedWidth(70)
            if i == 3:
                button3 = button
            grid.addWidget(button, 0, (i*2)+1)
            label = QLabel(self.withInterfaceFont(text[i] % nextInts))
            label.setAlignment(Qt.AlignHCenter)
            grid.addWidget(label, 1, (i*2)+1)
            self.connect(button, SIGNAL("clicked()"),
                lambda i=i: self.cardAnswered(i))
        return button3

    def withInterfaceFont(self, text):
        family = self.config["interfaceFontFamily"]
        size = self.config["interfaceFontSize"]
        colour = self.config["interfaceColour"]
        css = ('.interface {font-family: "%s"; font-size: %spx; color: %s}\n' %
               (family, size, colour))
        css = "<style>\n" + css + "</style>\n"
        text = css + '<span class="interface">' + text + "</span>"
        return text

    # Hooks
    ##########################################################################

    def setupHooks(self):
        self.hooks = {}

    def addHook(self, hookName, func):
        if not self.hooks.get(hookName, None):
            self.hooks[hookName] = []
        if func not in self.hooks[hookName]:
            self.hooks[hookName].append(func)

    def removeHook(self, hookName, func):
        hook = self.hooks.get(hookName, [])
        if func in hook:
            hook.remove(func)

    def runHook(self, hookName, *args):
        hook = self.hooks.get(hookName, None)
        if hook:
            for func in hook:
                func(*args)

    # Deck loading & saving: backend
    ##########################################################################

    def setupBackupDir(self):
        anki.deck.backupDir = os.path.join(
            self.config.configPath, "backups")

    def loadDeck(self, deckPath, sync=True):
        "Load a deck and update the user interface. Maybe sync."
        # return None if error should be reported
        # return 0 to fail with no error
        # return True on success
        if not self.saveAndClose():
            return 0
        if not os.path.exists(deckPath):
            return
        try:
            self.deck = DeckStorage.Deck(deckPath, rebuild=False)
        except (IOError, ImportError):
            return
        except DeckWrongFormatError, e:
            self.importOldDeck(deckPath)
            if not self.deck:
                return
        except DeckAccessError, e:
            if e.data.get('type') == 'inuse':
                ui.utils.showWarning(_("Unable to load the same deck twice."))
                return 0
            return
        self.updateRecentFiles(self.deck.path)
        if sync and self.config['syncOnLoad']:
            self.syncDeck(False)
        else:
            self.rebuildQueue()
        return True

    def importOldDeck(self, deckPath):
        from anki.importing.anki03 import Anki03Importer
        # back up the old file
        newPath = re.sub("\.anki$", ".anki-v3", deckPath)
        while os.path.exists(newPath):
            newPath += "-1"
        os.rename(deckPath, newPath)
        try:
            self.deck = DeckStorage.Deck(deckPath)
            imp = Anki03Importer(self.deck, newPath)
            imp.doImport()
        except DeckWrongFormatError, e:
            ui.utils.showWarning(_(
                "An error occurred while upgrading:\n%s") % `e.data`)
            return
        self.rebuildQueue()

    def maybeLoadLastDeck(self, args):
        "Open the last deck if possible."
        # try a command line argument if available
        try:
            if args:
                f = unicode(args[0], sys.getfilesystemencoding())
                return self.loadDeck(f)
        except:
            sys.stderr.write("Error loading last deck.\n")
            traceback.print_exc()
            self.deck = None
            return self.moveToState("initial")
        # try recent deck paths
        for path in self.config['recentDeckPaths']:
            try:
                r = self.loadDeck(path)
                if r == 0:
                    # in use
                    continue
                return r
            except:
                sys.stderr.write("Error loading last deck.\n")
                traceback.print_exc()
                self.deck = None
                return self.moveToState("initial")
        return self.moveToState("initial")

    def getDefaultDir(self, save=False):
        "Try and get default dir from most recently opened file."
        defaultDir = ""
        if self.config['recentDeckPaths']:
            latest = self.config['recentDeckPaths'][0]
            defaultDir = os.path.dirname(latest)
        else:
            if save:
                defaultDir = unicode(os.path.expanduser("~/"),
                                     sys.getfilesystemencoding())
            else:
                samples = self.getSamplesDir()
                if samples:
                    return samples
        return defaultDir

    def getSamplesDir(self):
        path = "/usr/share/doc/anki/examples"
        if not os.path.exists(path):
            return ""
        return path

    def openMacSamplesDir(self, path):
        # some versions of macosx don't allow the open dialog to point inside
        # a .App file, it seems - so we copy the files onto the desktop.
        newDir = os.path.expanduser("~/Documents/Anki 0.3 Sample Decks")
        import shutil
        if os.path.exists(newDir):
            files = os.listdir(path)
            for file in files:
                loc = os.path.join(path, file)
                if not os.path.exists(os.path.join(newDir, file)):
                    shutil.copy2(loc, newDir)
            return newDir
        shutil.copytree(path, newDir)
        return newDir

    def updateRecentFiles(self, path):
        "Add the current deck to the list of recent files."
        path = os.path.normpath(path)
        if path in self.config['recentDeckPaths']:
            self.config['recentDeckPaths'].remove(path)
        self.config['recentDeckPaths'].insert(0, path)
        del self.config['recentDeckPaths'][4:]
        self.config.save()
        self.updateRecentFilesMenu()

    def updateRecentFilesMenu(self):
        if not self.config['recentDeckPaths']:
            self.mainWin.menuOpenRecent.setEnabled(False)
            return
        self.mainWin.menuOpenRecent.setEnabled(True)
        self.mainWin.menuOpenRecent.clear()
        n = 1
        for file in self.config['recentDeckPaths']:
            a = QAction(self)
            a.setShortcut(_("Alt+%d" % n))
            a.setText(os.path.basename(file))
            self.connect(a, SIGNAL("triggered()"),
                         lambda n=n: self.loadRecent(n-1))
            self.mainWin.menuOpenRecent.addAction(a)
            n += 1

    def loadRecent(self, n):
        self.loadDeck(self.config['recentDeckPaths'][n])

    # New files, loading & saving
    ##########################################################################

    def saveAndClose(self, exit=False):
        "(Auto)save and close. Prompt if necessary. True if okay to proceed."
        if self.deck is not None:
            # sync (saving automatically)
            if self.config['syncOnClose']:
                self.syncDeck(False, reload=False)
                while self.deckPath:
                    self.app.processEvents()
                    time.sleep(0.1)
                return True
            # save
            if self.deck.modifiedSinceSave():
                if self.config['saveOnClose'] or self.config['syncOnClose']:
                    self.saveDeck()
                else:
                    res = ui.unsaved.ask(self)
                    if res == ui.unsaved.save:
                        self.saveDeck()
                    elif res == ui.unsaved.cancel:
                        return False
                    elif res == ui.unsaved.discard:
                        pass
            # close
            self.deck.rollback()
            self.deck = None
        if not exit:
            self.moveToState("noDeck")
        return True

    def onNew(self):
        if not self.saveAndClose(): return
        self.deck = DeckStorage.Deck()
        m = ui.modelchooser.AddModel(self, online=True).getModel()
        if m:
            if m != "online":
                self.deck.addModel(m)
                self.saveDeck()
                self.moveToState("initial")
                return
            # ensure all changes come to us
            self.deck.syncName = None
            self.deck.modified = 0
            self.deck.lastLoaded = self.deck.modified
            self.deck.s.flush()
            self.deck.s.commit()
            self.syncDeck(onlyMerge=True)
            return
        self.deck = None
        self.moveToState("initial")

    def onOpen(self, samples=False):
        key = _("Deck files (*.anki)")
        if samples: defaultDir = self.getSamplesDir()
        else: defaultDir = self.getDefaultDir()
        file = QFileDialog.getOpenFileName(self, _("Open deck"),
                                           defaultDir, key)
        file = unicode(file)
        if not file:
            return False
        if samples:
            # we need to copy into a writeable location
            new = DeckStorage.newDeckPath()
            shutil.copyfile(file, new)
            file = new
        ret = self.loadDeck(file)
        if not ret:
            if ret is None:
                ui.utils.showWarning(_("Unable to load file."))
            self.deck = None
            return False
        else:
            self.updateRecentFiles(file)
            return True

    def onOpenSamples(self):
        self.onOpen(samples=True)

    def onSave(self):
        if self.deck.modifiedSinceSave():
            self.saveDeck()
        else:
            self.setStatus(_("Deck is not modified."))

            self.updateTitleBar()

    def onSaveAs(self):
        "Prompt for a file name, then save."
        title = _("Save deck")
        dir = os.path.dirname(self.deck.path)
        file = QFileDialog.getSaveFileName(self, title,
                                           dir,
                                           _("Deck files (*.anki)"),
                                           None,
                                           QFileDialog.DontConfirmOverwrite)
        file = unicode(file)
        if not file:
            return
        if not file.lower().endswith(".anki"):
            file += ".anki"
        if os.path.exists(file):
            # check for existence after extension
            if not ui.utils.askUser(
                "This file exists. Are you sure you want to overwrite it?"):
                return
        self.deck = self.deck.saveAs(file)
        self.updateTitleBar()
        self.moveToState("initial")

    def saveDeck(self):
        self.setStatus(_("Saving.."))
        self.deck.save()
        self.updateRecentFiles(self.deck.path)
        self.updateTitleBar()
        self.setStatus(_("Saving..done"))

    # Opening and closing the app
    ##########################################################################

    def prepareForExit(self):
        "Save config and window geometry."
        g = self.geometry()
        self.help.hide()
        self.config['mainWindowGeometry'] = (g.left(),
                                             g.top(),
                                             self.width(),
                                             self.height())
        # save config and kill main window
        try:
            self.config.save()
        except (IOError, OSError), e:
            ui.utils.showWarning(_("Anki was unable to save your "
                                   "configuration file:\n%s" % e))

    def closeEvent(self, event):
        "User hit the X button, etc."
        if not self.saveAndClose(exit=True):
            event.ignore()
        else:
            self.prepareForExit()
            event.accept()
            self.app.quit()

    # Anchor clicks
    ##########################################################################

    def onWelcomeAnchor(self, str):
        if str == "new":
            self.onNew()
        elif str == "sample":
            self.onOpenSamples()
        elif str == "open":
            self.onOpen()

    def setupAnchors(self):
        self.anchorPrefixes = {
            'welcome': self.onWelcomeAnchor,
            }
        self.connect(self.mainWin.mainText,
                     SIGNAL("anchorClicked(QUrl)"),
                     self.anchorClicked)

    def anchorClicked(self, url):
        # prevent the link being handled
        self.mainWin.mainText.setSource(QUrl(""))
        addr = unicode(url.toString())
        fields = addr.split(":")
        if len(fields) > 1 and fields[0] in self.anchorPrefixes:
            self.anchorPrefixes[fields[0]](*fields[1:])
        else:
            # open in browser
            QDesktopServices.openUrl(QUrl(url))

    # Tools - looking up words in the dictionary
    ##########################################################################

    def initLookup(self):
        if not getattr(self, "lookup", None):
            self.lookup = ui.lookup.Lookup(self)

    def onLookupExpression(self):
        self.initLookup()
        try:
            self.lookup.alc(self.currentCard.fact['Expression'])
        except KeyError:
            self.setStatus(_("No expression in current card."))

    def onLookupMeaning(self):
        self.initLookup()
        try:
            self.lookup.alc(self.currentCard.fact['Meaning'])
        except KeyError:
            self.setStatus(_("No meaning in current card."))

    def onLookupEdictSelection(self):
        self.initLookup()
        self.lookup.selection(self.lookup.edict)

    def onLookupEdictKanjiSelection(self):
        self.initLookup()
        self.lookup.selection(self.lookup.edictKanji)

    def onLookupAlcSelection(self):
        self.initLookup()
        self.lookup.selection(self.lookup.alc)

    # Tools - statistics
    ##########################################################################

    def onKanjiStats(self):
        rep = anki.stats.KanjiStats(self.deck).report()
        rep += _("<a href=py:miss>Missing Kanji</a><br>")
        self.help.showText(rep, py={"miss": self.onMissingStats})

    def onMissingStats(self):
        ks = anki.stats.KanjiStats(self.deck)
        ks.genKanjiSets()
        self.help.showText(ks.missingReport())

    def onDeckStats(self):
        txt = anki.stats.DeckStats(self.deck).report()
        self.help.showText(txt)

    def onCardStats(self):
        self.addHook("showQuestion", self.onCardStats)
        self.addHook("helpChanged", self.removeCardStatsHook)
        txt = ""
        if self.currentCard:
            txt += _("<h1>Current card</h1>")
            txt += anki.stats.CardStats(self.deck, self.currentCard).report()
        if self.lastCard and self.lastCard != self.currentCard:
            txt += _("<h1>Last card</h1>")
            txt += anki.stats.CardStats(self.deck, self.lastCard).report()
        if not txt:
            txt = _("No current card or last card.")
        self.help.showText(txt, key="cardStats")

    def removeCardStatsHook(self):
        "Remove the update hook if the help menu was changed."
        if self.help.currentKey != "cardStats":
            self.removeHook("showQuestion", self.onCardStats)

    def onShowGraph(self):
        self.setStatus(_("Loading graphs (may take time).."))
        self.app.processEvents()
        import anki.graphs
        if anki.graphs.graphsAvailable():
            try:
                ui.dialogs.get("Graphs", self, self.deck)
            except (ImportError, ValueError):
                if sys.platform.startswith("win32"):
                    ui.utils.showInfo(
                        _("To display graphs, Anki needs a .dll file which\n"
                          "you don't have. Please install:\n") +
                        "http://www.dll-files.com/dllindex/dll-files.shtml?msvcp71")
                else:
                    ui.utils.showInfo(_(
                        "Your version of Matplotlib is broken.\n"
                        "Please see http://repose.ath.cx/tracker/anki/issue102"))
        else:
            ui.utils.showInfo(_("Please install python-matplotlib to access graphs."))

    def onKanjiOccur(self):
        self.setStatus(_("Generating report (may take time).."))
        self.app.processEvents()
        import tempfile
        (fd, name) = tempfile.mkstemp(suffix=".html")
        f = os.fdopen(fd, 'w')
        ko = anki.stats.KanjiOccurStats(self.deck)
        ko.reportFile(f)
        f.close()
        if sys.platform == "win32":
            url = "file:///"
        else:
            url = "file://"
        url += os.path.abspath(name)
        QDesktopServices.openUrl(QUrl(url))

    # Marking, suspending and undoing
    ##########################################################################

    def onMark(self, toggled):
        if self.currentCard.hasTag("Marked"):
            self.currentCard.tags = deleteTags("Marked", self.currentCard.tags)
        else:
            self.currentCard.tags = addTags("Marked", self.currentCard.tags)
        self.currentCard.setModified()
        self.deck.setModified()

    def onSuspend(self):
        self.currentCard.tags = addTags("Suspended", self.currentCard.tags)
        self.deck.updatePriority(self.currentCard)
        self.currentCard.setModified()
        self.deck.setModified()
        self.lastScheduledTime = None
        self.moveToState("initial")

    def onUndoAnswer(self):
        # quick and dirty undo for now
        self.lastCard.interval = self.lastCard.lastInterval
        self.lastCard.due = self.lastCard.lastDue
        self.lastCard.successive = self.lastCard.oldSuccessive
        self.lastCard.reps -= 1
        self.lastCard.factor = self.lastCard.oldFactor
        self.deck.s.flush()
        self.reset()

    # Other menu operations
    ##########################################################################

    def onAddCard(self):
        ui.dialogs.get("AddCards", self)

    def onEditDeck(self):
        ui.dialogs.get("CardList", self)

    def onDeckProperties(self):
        self.deckProperties = ui.deckproperties.DeckProperties(self)

    def onModelProperties(self):
        if self.currentCard:
            model = self.currentCard.fact.model
        else:
            model = self.deck.currentModel
        ui.modelproperties.ModelProperties(self, model)

    def onDisplayProperties(self):
        ui.dialogs.get("DisplayProperties", self)

    def onPrefs(self):
        ui.preferences.Preferences(self, self.config)

    def onReportBug(self):
        QDesktopServices.openUrl(QUrl(ankiqt.appIssueTracker))

    def onForum(self):
        QDesktopServices.openUrl(QUrl(ankiqt.appForum))

    def onAbout(self):
        ui.about.show(self)

    # Importing & exporting
    ##########################################################################

    def onImport(self):
        if self.deck is None:
            self.onNew()
        if self.deck is not None:
            ui.importing.ImportDialog(self)

    def onExport(self):
        ui.exporting.ExportDialog(self)

    # Language handling
    ##########################################################################

    def setLang(self):
        "Set the user interface language."
        languageDir="/usr/share/locale"
        self.languageTrans = gettext.translation('ankiqt', languageDir,
                                            languages=[self.config["interfaceLang"]],
                                            fallback=True)
        self.installTranslation()
        if getattr(self, 'mainWin', None):
            self.mainWin.retranslateUi(self)
            self.alterShortcuts()
        anki.lang.setLang(self.config["interfaceLang"])
        self.updateTitleBar()

    def getTranslation(self, text):
        return self.languageTrans.ugettext(text)

    def installTranslation(self):
        import __builtin__
        __builtin__.__dict__['_'] = self.getTranslation

    # Syncing
    ##########################################################################

    def syncDeck(self, interactive=True, create=False, onlyMerge=False, reload=True):
        "Synchronise a deck with the server."
        # vet input
        u=self.config['syncUsername']
        p=self.config['syncPassword']
        if not u or not p:
            msg = _("Not syncing, username or password unset.")
            if interactive:
                ui.utils.showWarning(msg)
            return
        if self.deck is None and self.deckPath is None:
            # qt on linux incorrectly accepts shortcuts for disabled actions
            return
        if self.deck:
            # save first, so we can rollback on failure
            self.deck.save()
            self.deck.close()
            self.deckPath = self.deck.path
            self.syncName = self.deck.syncName or self.deck.name()
            self.lastSync = self.deck.lastSync
            self.deck = None
            self.loadAfterSync = reload
        # bug triggered by preferences dialog - underlying c++ widgets are not
        # garbage collected until the middle of the child thread
        import gc; gc.collect()
        self.mainWin.mainText.clear()
        self.syncThread = ui.sync.Sync(self, u, p, interactive, create, onlyMerge)
        self.connect(self.syncThread, SIGNAL("setStatus"), self.setSyncStatus)
        self.connect(self.syncThread, SIGNAL("showWarning"), ui.utils.showWarning)
        self.connect(self.syncThread, SIGNAL("moveToState"), self.moveToState)
        self.connect(self.syncThread, SIGNAL("noMatchingDeck"), self.selectSyncDeck)
        self.connect(self.syncThread, SIGNAL("cleanNewDeck"), self.cleanNewDeck)
        self.connect(self.syncThread, SIGNAL("syncFinished"), self.syncFinished)
        self.syncThread.start()
        self.setEnabled(False)
        while not self.syncThread.isFinished():
            self.app.processEvents()
            self.syncThread.wait(100)
        # the priorities on the server are different (no phone, etc)
        self.setEnabled(True)
        return self.syncThread.ok

    def syncFinished(self):
        "Reopen after sync finished."
        if self.loadAfterSync:
            self.loadDeck(self.deckPath, sync=False)
            self.deck.syncName = self.syncName
            self.deck.s.flush()
            self.deck.s.commit()
        else:
            self.moveToState("noDeck")
        self.deckPath = None

    def selectSyncDeck(self, decks, create=True):
        name = ui.sync.DeckChooser(self, decks, create).getName()
        if name:
            if name == self.syncName:
                self.syncDeck(create=True)
            else:
                self.syncName = name
                self.syncDeck()
        else:
            if not create:
                # called via 'new' - close
                self.cleanNewDeck()
            else:
                self.syncFinished()

    def cleanNewDeck(self):
        "Unload a new deck if an initial sync failed."
        self.deck = None
        self.moveToState("initial")

    def setSyncStatus(self, text, *args):
        self.setStatus(text, *args)
        self.mainWin.mainText.append("<font size=+6>" + text + "</font>")

    # Menu, title bar & status
    ##########################################################################

    deckRelatedMenuItems = (
        "Save",
        "Close",
        "Addcards",
        "Editdeck",
        "Syncdeck",
        "DisplayProperties",
        "DeckProperties",
        "ModelProperties",
        "Export",
        "MarkCard",
        "Graphs",
        "Dstats",
        "Kstats",
        "Cstats",
        )

    deckRelatedMenus = (
        "Tools",
        )

    def connectMenuActions(self):
        self.connect(self.mainWin.actionNew, SIGNAL("triggered()"), self.onNew)
        self.connect(self.mainWin.actionOpen, SIGNAL("triggered()"), self.onOpen)
        self.connect(self.mainWin.actionOpenSamples, SIGNAL("triggered()"), self.onOpenSamples)
        self.connect(self.mainWin.actionSave, SIGNAL("triggered()"), self.onSave)
        self.connect(self.mainWin.actionSaveAs, SIGNAL("triggered()"), self.onSaveAs)
        self.connect(self.mainWin.actionClose, SIGNAL("triggered()"), self.saveAndClose)
        self.connect(self.mainWin.actionExit, SIGNAL("triggered()"), self, SLOT("close()"))
        self.connect(self.mainWin.actionSyncdeck, SIGNAL("triggered()"), self.syncDeck)
        self.connect(self.mainWin.actionDeckProperties, SIGNAL("triggered()"), self.onDeckProperties)
        self.connect(self.mainWin.actionDisplayProperties, SIGNAL("triggered()"),self.onDisplayProperties)
        self.connect(self.mainWin.actionAddcards, SIGNAL("triggered()"), self.onAddCard)
        self.connect(self.mainWin.actionEditdeck, SIGNAL("triggered()"), self.onEditDeck)
        self.connect(self.mainWin.actionPreferences, SIGNAL("triggered()"), self.onPrefs)
        self.connect(self.mainWin.actionLookup_es, SIGNAL("triggered()"), self.onLookupEdictSelection)
        self.connect(self.mainWin.actionLookup_esk, SIGNAL("triggered()"), self.onLookupEdictKanjiSelection)
        self.connect(self.mainWin.actionLookup_expr, SIGNAL("triggered()"), self.onLookupExpression)
        self.connect(self.mainWin.actionLookup_mean, SIGNAL("triggered()"), self.onLookupMeaning)
        self.connect(self.mainWin.actionLookup_as, SIGNAL("triggered()"), self.onLookupAlcSelection)
        self.connect(self.mainWin.actionDstats, SIGNAL("triggered()"), self.onDeckStats)
        self.connect(self.mainWin.actionKstats, SIGNAL("triggered()"), self.onKanjiStats)
        self.connect(self.mainWin.actionCstats, SIGNAL("triggered()"), self.onCardStats)
        self.connect(self.mainWin.actionGraphs, SIGNAL("triggered()"), self.onShowGraph)
        self.connect(self.mainWin.actionAbout, SIGNAL("triggered()"), self.onAbout)
        self.connect(self.mainWin.actionReportbug, SIGNAL("triggered()"), self.onReportBug)
        self.connect(self.mainWin.actionForum, SIGNAL("triggered()"), self.onForum)
        self.connect(self.mainWin.actionStarthere, SIGNAL("triggered()"), self.onStartHere)
        self.connect(self.mainWin.actionImport, SIGNAL("triggered()"), self.onImport)
        self.connect(self.mainWin.actionExport, SIGNAL("triggered()"), self.onExport)
        self.connect(self.mainWin.actionMarkCard, SIGNAL("toggled(bool)"), self.onMark)
        self.connect(self.mainWin.actionSuspendCard, SIGNAL("triggered()"), self.onSuspend)
        self.connect(self.mainWin.actionModelProperties, SIGNAL("triggered()"), self.onModelProperties)
        self.connect(self.mainWin.actionRepeatQuestionAudio, SIGNAL("triggered()"), self.onRepeatQuestion)
        self.connect(self.mainWin.actionRepeatAnswerAudio, SIGNAL("triggered()"), self.onRepeatAnswer)
        self.connect(self.mainWin.actionRepeatAudio, SIGNAL("triggered()"), self.onRepeatAudio)
        self.connect(self.mainWin.actionUndoAnswer, SIGNAL("triggered()"), self.onUndoAnswer)

    def enableDeckMenuItems(self, enabled=True):
        "setEnabled deck-related items."
        for item in self.deckRelatedMenus:
            getattr(self.mainWin, "menu" + item).setEnabled(enabled)
        for item in self.deckRelatedMenuItems:
            getattr(self.mainWin, "action" + item).setEnabled(enabled)

    def disableDeckMenuItems(self):
        "Disable deck-related items."
        self.enableDeckMenuItems(enabled=False)

    def updateTitleBar(self):
        "Display the current deck and card count in the titlebar."
        title=ankiqt.appName + " " + ankiqt.appVersion
        if self.deck != None:
            deckpath = self.deck.name()
            if self.deck.modifiedSinceSave():
                deckpath += "*"
            title = _("%(path)s (%(facts)d facts, %(cards)d cards)"
                      " - %(title)s") % {
                # FIXME: safe to assume filesystem is utf-8?
                "path": deckpath,
                "title": title,
                "cards": self.deck.totalCardCount(),
                "facts": self.deck.totalFactCount(),
                }
        self.setWindowTitle(title)

    def setStatus(self, text, timeout=3000):
        self.mainWin.statusbar.showMessage(text, timeout)

    def onStartHere(self):
        QDesktopServices.openUrl(QUrl(ankiqt.appHelpSite))

    def alterShortcuts(self):
        if sys.platform.startswith("darwin"):
            self.mainWin.actionAddcards.setShortcut(_("Ctrl+D"))

    def updateMarkAction(self):
        self.mainWin.actionMarkCard.blockSignals(True)
        if self.currentCard.hasTag("Marked"):
            self.mainWin.actionMarkCard.setChecked(True)
        else:
            self.mainWin.actionMarkCard.setChecked(False)
        self.mainWin.actionMarkCard.blockSignals(False)

    def disableCardMenuItems(self):
        if not self.lastCard:
            self.mainWin.actionUndoAnswer.setEnabled(False)
        self.mainWin.actionMarkCard.setEnabled(False)
        self.mainWin.actionSuspendCard.setEnabled(False)
        self.mainWin.actionRepeatQuestionAudio.setEnabled(False)
        self.mainWin.actionRepeatAnswerAudio.setEnabled(False)
        self.mainWin.actionRepeatAudio.setEnabled(False)

    def enableCardMenuItems(self):
        self.mainWin.actionUndoAnswer.setEnabled(not not self.lastCard)
        self.mainWin.actionMarkCard.setEnabled(True)
        self.mainWin.actionSuspendCard.setEnabled(True)
        self.mainWin.actionRepeatQuestionAudio.setEnabled(
            hasSound(self.currentCard.question))
        self.mainWin.actionRepeatAnswerAudio.setEnabled(
            hasSound(self.currentCard.answer) and self.state != "getQuestion")
        self.mainWin.actionRepeatAudio.setEnabled(
            self.mainWin.actionRepeatQuestionAudio.isEnabled() or
            self.mainWin.actionRepeatAnswerAudio.isEnabled())

    # Auto update
    ##########################################################################

    def setupAutoUpdate(self):
        return  # do not lookup latest upstream version in Debian packaged anki
        self.autoUpdate = ui.update.LatestVersionFinder(self)
        self.connect(self.autoUpdate, SIGNAL("newVerAvail"), self.newVerAvail)
        self.autoUpdate.start()

    def newVerAvail(self, version):
        ui.update.askAndUpdate(self, version)

    # User customisations
    ##########################################################################

    def loadUserCustomisations(self):
        # look for config file
        dir = self.config.configPath
        file = os.path.join(dir, "custom.py")
        plugdir = os.path.join(dir, "plugins")
        sys.path.insert(0, dir)
        if os.path.exists(file):
            try:
                import custom
            except:
                print "Error in custom.py"
                print traceback.print_exc()
        sys.path.insert(0, plugdir)
        import glob
        plugins = [f.replace(".py", "") for f in os.listdir(plugdir) \
                   if f.endswith(".py")]
        plugins.sort()
        for plugin in plugins:
            try:
                __import__(plugin)
            except:
                print "Error in %s.py" % plugin
                print traceback.print_exc()

    # Mac support
    ##########################################################################

    def macHacks(self):
        if sys.platform.startswith("darwin"):
            self.setUnifiedTitleAndToolBarOnMac(True)
            qt_mac_set_menubar_icons(False)

    # Font localisation
    ##########################################################################

    def setupFonts(self):
        for (s, p) in anki.fonts.substitutions():
            QFont.insertSubstitution(s, p)

    # Sounds
    ##########################################################################

    def onRepeatQuestion(self):
        playFromText(self.currentCard.question)

    def onRepeatAnswer(self):
        playFromText(self.currentCard.answer)

    def onRepeatAudio(self):
        if self.state == "showQuestion":
            playFromText(self.currentCard.question)
        else:
            if hasSound(self.currentCard.answer):
                playFromText(self.currentCard.answer)
            else:
                playFromText(self.currentCard.question)
