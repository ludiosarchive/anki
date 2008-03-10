# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 2 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib, urllib2, os, sys, time
import anki, anki.utils, anki.lang, anki.stats
import ankiqt

baseUrl = "http://anki.ichi2.net/update/"

# when requesting latest version number, gather their version, deck size and
# average retention ratio for future development
# FIXME: add ability to disable in prefs, warn about anonymous sent info
class LatestVersionFinder(QThread):

    def __init__(self, main):
        QThread.__init__(self)
        self.main = main
        self.config = main.config
        # calculate stats before we start a new thread
        if self.main.deck != None:
            deckSize = self.main.deck.totalCardCount()
            stats = anki.stats.globalStats(self.main.deck.s)
            deckRecall = "%0.2f" % (
                (stats.matureEase3 + stats.matureEase4) /
                float(stats.matureEase0 +
                      stats.matureEase1 +
                      stats.matureEase2 +
                      stats.matureEase3 +
                      stats.matureEase4 + 0.000001) * 100)
            pending = "(%d, %d)" % (self.main.deck.oldCardCount(),
                                    self.main.deck.newCardCount())
            ct = self.main.deck.created
            if ct:
                ol = anki.lang.getLang()
                anki.lang.setLang("en")
                age = anki.utils.fmtTimeSpan(abs(
                    time.time() - ct))
                anki.lang.setLang(ol)
            else:
                age = ""
            plat=sys.platform
            pver=sys.version
        else:
            deckSize = "nodeck"
            deckRecall = ""
            pending = ""
            age = ""
            plat=""
            pver=""
        d = {"ver": ankiqt.appVersion,
             "size": deckSize,
             "rec": deckRecall,
             "pend": pending,
             "age": age,
             "pver": pver,
             "plat": plat,}
        self.stats = d

    def run(self):
        if not self.config['checkForUpdates']:
            return
        d = self.stats
        d = urllib.urlencode(d)
        try:
            f = urllib2.urlopen(baseUrl + "getQtVersion", d)
        except urllib2.URLError:
            return
        resp = f.read()
        if not resp:
            return
        if resp > ankiqt.appVersion:
            self.emit(SIGNAL("newVerAvail"), resp)

class Updater(QThread):

    filename = "anki-update.exe"
    # FIXME: get when checking version number
    chunkSize = 428027
    percChange = 5

    def __init__(self):
        QThread.__init__(self)

    def setStatus(self, msg, timeout=0):
        self.emit(SIGNAL("statusChanged"), msg, timeout)

    def run(self):
        try:
            f = urllib2.urlopen(baseUrl + "getQt")
        except urllib2.URLError:
            self.setStatus(_("Unable to reach server"))
            return
        try:
            newfile = open(self.filename, "wb")
        except:
            self.setStatus(_("Unable to open file"))
            return
        perc = 0
        while 1:
            self.setStatus(
                _("Downloading anki updater - %d%% complete.") % perc)
            resp = f.read(self.chunkSize)
            if not resp:
                break
            newfile.write(resp)
            perc += self.percChange
            if perc > 100:
                perc = 99
        newfile.close()
        self.setStatus(_("Updating.."))
        os.system(self.filename)
        self.setStatus(_("Update complete. Please restart Anki."))
        os.unlink(self.filename)

def askAndUpdate(parent, version=None):
    if not version:
        baseStr = _("<h1>Update Anki manually</h1>"
                    "Usually there is no need to do this. "
                    "You will be notified automatically "
                    "when a new version of Anki is available. ")
    else:
        baseStr = _("""<h1>Anki updated</h1>A new version of Anki is
        available.<br/>""")
    if sys.platform == "win32":
        # automated installer available
        ret = QMessageBox.question(
            parent, "Anki", baseStr +
            _("Would you like to download it now?"),
            QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            parent.autoUpdate = Updater()
            parent.connect(parent.autoUpdate,
                           SIGNAL("statusChanged"),
                           parent.setStatus)
            parent.autoUpdate.start()
    else:
        # manual
        ret = QMessageBox.question(
            parent, "Anki", baseStr +
            "Would you like to visit the website now?",
            QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            QDesktopServices.openUrl(QUrl(ankiqt.appWebsite))
