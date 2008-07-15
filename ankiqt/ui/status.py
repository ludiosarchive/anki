# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import anki
import sys, time

# Status bar
##########################################################################

class StatusView(object):
    "Manage the status bar as we transition through various states."

    def __init__(self, parent):
        self.main = parent
        self.statusbar = parent.mainWin.statusbar
        self.shown = []
        self.hideBorders()
        self.setState("noDeck")

    # State control
    ##########################################################################

    def setState(self, state):
        "Change to STATE, and update the display."
        self.state = state
        if self.state == "initial":
            self.showDeckStatus()
            self.updateProgressGoal()
        elif self.state == "noDeck":
            self.hideDeckStatus()
        elif self.state in ("showQuestion",
                            "deckFinished",
                            "deckEmpty"):
            self.redraw()

    # Setup and teardown
    ##########################################################################

    def vertSep(self):
        spacer = QFrame()
        spacer.setFrameStyle(QFrame.VLine)
        spacer.setFrameShadow(QFrame.Plain)
        return spacer

    def showDeckStatus(self):
        if self.shown:
            return
        progressBarSize = (50, 12)
        # small spacer
        self.initialSpace = QWidget()
        self.addWidget(self.initialSpace, 1)
        # remaining & eta
        self.remText = QLabel()
        self.addWidget(self.remText, 0)
        self.addWidget(self.vertSep(), 0)
        self.etaText = QLabel()
        self.etaText.setToolTip(_(
            "<h1>Estimated time</h1>"
            "This is how long it will take to complete the current mode "
            "at your current pace."))
        self.addWidget(self.etaText, 0)
        # progress
        self.addWidget(self.vertSep(), 0)
        self.progressBar = QProgressBar()
        self.progressBar.setFixedSize(*progressBarSize)
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(False)
        self.addWidget(self.progressBar, 0)
        # retention
        self.addWidget(self.vertSep(), 0)
        self.retentionBar = QProgressBar()
        self.retentionBar.setFixedSize(*progressBarSize)
        self.retentionBar.setMaximum(100)
        self.retentionBar.setTextVisible(False)
        self.addWidget(self.retentionBar, 0)
        # mac
        if sys.platform.startswith("darwin"):
            # we don't want non-coloured, throbbing widgets
            self.plastiqueStyle = QStyleFactory.create("plastique")
            self.progressBar.setStyle(self.plastiqueStyle)
            self.retentionBar.setStyle(self.plastiqueStyle)
        # mode
        self.addWidget(self.vertSep(), 0)
        self.mode = QLabel()
        self.mode.setFrameStyle(QFrame.Box)
        self.mode.setFrameShadow(QFrame.Plain)
        self.mode.setAutoFillBackground(True)
        self.addWidget(self.mode, 0)
        self.redraw()

    def addWidget(self, w, stretch=0, perm=True):
        if perm:
            self.statusbar.addPermanentWidget(w, stretch)
        else:
            self.statusbar.addWidget(w, stretch)
        self.shown.append(w)

    def hideDeckStatus(self):
        for w in self.shown:
            self.statusbar.removeWidget(w)
            w.setParent(None)
        self.shown = []

    def hideBorders(self):
        "Remove the ugly borders QT places on status bar widgets."
        self.statusbar.setStyleSheet("::item { border: 0; }")

    def updateProgressGoal(self):
        return
        stats = self.main.deck.sched.getStats()
        self.totalPending = stats['pending']

    # Updating
    ##########################################################################

    def redraw(self):
        p = QPalette()
        stats = self.main.deck.getStats(self.main.currentCard)
        remStr = _("Remaining: ")
        if self.state == "deckFinished":
            self.mode.setStyleSheet("background: #aaffaa;")
            mode = "finished"
            remStr += "<b>0</b>"
        elif self.state == "deckEmpty":
            self.mode.setStyleSheet("background: #ffaaaa;")
            mode = "empty"
            remStr += "<b>0</b>"
        else:
            if self.main.currentCard and self.main.currentCard.reps == 0:
                mode = "learn"
                self.mode.setStyleSheet("background: #aaaaff;")
            else:
                mode = "review"
                self.mode.setStyleSheet("background: #ffffaa;")
            # remaining string, bolded depending on current card
            if not self.main.currentCard:
                remStr += "%(failed1)s + %(successive1)s + %(new1)s"
            else:
                q = self.main.deck.queueForCard(self.main.currentCard)
                if q == "failed":
                    remStr += "<u>%(failed1)s</u>&nbsp;&nbsp;%(successive1)s&nbsp;&nbsp;%(new1)s"
                elif q == "rev":
                    remStr += "%(failed1)s&nbsp;&nbsp;<u>%(successive1)s</u>&nbsp;&nbsp;%(new1)s"
                else:
                    remStr += "%(failed1)s&nbsp;&nbsp;%(successive1)s&nbsp;&nbsp;<u>%(new1)s</u>"
        stats['failed1'] = '<font color=#990000>%s</font>' % stats['failed']
        stats['successive1'] = '<font color=#000000>%s</font>' % stats['successive']
        stats['new1'] = '<font color=#0000ff>%s</font>' % stats['new']
        self.remText.setText(remStr % stats)
        stats['suspended'] = self.main.deck.suspendedCardCount()
        stats['spaced'] = self.main.deck.spacedCardCount()
        self.remText.setToolTip(_(
            "<h1>Remaining cards</h1>"
            "The number of cards left to answer."
            "<p/>There are <b>%(failed)d</b> failed cards due soon.<br>"
            "There are <b>%(successive)d</b> cards awaiting review.<br>"
            "There are <b>%(new)d</b> new cards.<br>"
            "There are <b>%(spaced)d</b> spaced cards.<br>"
            "There are <b>%(suspended)d</b> suspended cards.") % stats)
        # mode - setup tooltips and i18n
        if mode == "finished":
            mode = _("Finished")
            tip = _(
                "<h1>Finished</h1>"
                "You have finished the deck for now.")
        elif mode == "empty":
            mode = _("Empty")
            tip = _(
                "<h1>Empty deck</h1>"
                "Your deck is empty. Please add some cards.")
        elif mode == "learn":
            mode = _("Learning")
            tip = _(
                "<h1>Learning</h1>"
                "You are currently learning new cards.")
        elif mode == "review":
            mode = _("Reviewing")
            tip = _(
                "<h1>Reviewing</h1>"
                "You are reviewing previously-seen cards.")
        self.mode.setText("&nbsp;<b>" + mode + "</b>&nbsp;")
        self.mode.setToolTip(tip)
        # eta
        self.etaText.setText(_("ETA: <b>%(timeLeft)s</b>") % stats)
        # retention ratio
        p.setColor(QPalette.Base, QColor("black"))
        p.setColor(QPalette.Button, QColor("black"))
        self.setProgressColour(p, stats['gMatureYes%'])
        self.retentionBar.setPalette(p)
        self.retentionBar.setValue(stats['gMatureYes%'])
        stats['avgTime'] = anki.utils.fmtTimeSpan(stats['gAverageTime'], point=2)
        stats['revTime'] = anki.utils.fmtTimeSpan(stats['gReviewTime'], point=2)
        stats['disTime'] = anki.utils.fmtTimeSpan(stats['gDistractedTime'], point=2)
        tip = _("<h1>Retention</h1>The " """
        percentage of material you've remembered over the life of<br>
        the deck. The bar shows your recall rate for cards answered<br>
        correctly after a month or more. Cards less than a month old<br>
        are not considered memorized yet."""
                "<br><br><b>Correct and over a month: %(gMatureYes%)0.1f%% "
                "(%(gMatureYes)d of %(gMatureTotal)d)</b><br>"
                "Correct and under a month: %(gYoungYes%)0.1f%% "
                "(%(gYoungYes)d of %(gYoungTotal)d)<br>"
                "Correct when seen the first time: %(gNewYes%)0.1f%% "
                "(%(gNewYes)d of %(gNewTotal)d)<br>"
                "Total correct: %(gYesTotal%)0.1f%% "
                "(%(gYesTotal)d of %(gTotal)d)<br><br>"
                "Average time per answer: %(avgTime)s<br>"
                "Total distracted time: %(disTime)s<br>"
                "Total review time: %(revTime)s"
                ) % stats
        self.retentionBar.setToolTip(tip)
        # progress
        self.setProgressColour(p, stats['dYesTotal%'])
        self.progressBar.setPalette(p)
        self.progressBar.setValue(stats['dYesTotal%'])
        stats['avgTime'] = anki.utils.fmtTimeSpan(stats['dAverageTime'], point=2)
        stats['revTime'] = anki.utils.fmtTimeSpan(stats['dReviewTime'], point=2)
        stats['disTime'] = anki.utils.fmtTimeSpan(stats['dDistractedTime'], point=2)
        tip = _("<h1>Daily recall</h1>This " """
        bar shows the total percentage of correct answers<br>
        for today. It may be low if you've recently added lots of<br>
        difficult material. Don't worry too much about it, as the<br>
        retention bar on the right is more important."""
                "<p/>Correct and over a month: %(dMatureYes%)0.1f%% "
                "(%(dMatureYes)d of %(dMatureTotal)d)<br>"
                "Correct and under a month: %(dYoungYes%)0.1f%% "
                "(%(dYoungYes)d of %(dYoungTotal)d)<br>"
                "Correct when seen the first time: %(dNewYes%)0.1f%% "
                "(%(dNewYes)d of %(dNewTotal)d)<br>"
                "<b>Total correct: %(dYesTotal%)0.1f%% "
                "(%(dYesTotal)d of %(dTotal)d)</b><br><br>"
                "Average time per answer: %(avgTime)s<br>"
                "Total distracted time: %(disTime)s<br>"
                "Total review time: %(revTime)s") % stats
        self.progressBar.setToolTip(tip)
        return

    def setProgressColour(self, palette, perc):
        if perc == 0:
            palette.setColor(QPalette.Highlight, QColor("black"))
        elif perc < 50:
            palette.setColor(QPalette.Highlight, QColor("#ee0000"))
        elif perc < 65:
            palette.setColor(QPalette.Highlight, QColor("#ee7700"))
        elif perc < 75:
            palette.setColor(QPalette.Highlight, QColor("#eeee00"))
        else:
            palette.setColor(QPalette.Highlight, QColor("#00ee00"))

