# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/syncdeck.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeckChooser(object):
    def setupUi(self, DeckChooser):
        DeckChooser.setObjectName("DeckChooser")
        DeckChooser.resize(QtCore.QSize(QtCore.QRect(0,0,484,320).size()).expandedTo(DeckChooser.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(DeckChooser)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(DeckChooser)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.decks = QtGui.QListWidget(DeckChooser)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.decks.setFont(font)
        self.decks.setObjectName("decks")
        self.vboxlayout.addWidget(self.decks)

        self.buttonBox = QtGui.QDialogButtonBox(DeckChooser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DeckChooser)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),DeckChooser.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),DeckChooser.reject)
        QtCore.QMetaObject.connectSlotsByName(DeckChooser)

    def retranslateUi(self, DeckChooser):
        DeckChooser.setWindowTitle(_("Anki"))
        self.label.setText(_("<h1>Where should we synchronize to?</h1>"))

