# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(QtCore.QSize(QtCore.QRect(0,0,252,185).size()).expandedTo(About.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(About)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(12)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_3 = QtGui.QLabel(About)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.hboxlayout.addWidget(self.label_3)

        self.label_2 = QtGui.QLabel(About)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/anki.png"))
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.label = QtGui.QLabel(About)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.buttonBox = QtGui.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),About.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_("About Anki"))
        self.label_3.setText(_("<h1>Anki</h1>"))
        self.label.setText(_("<span>Anki is a spaced repetition flashcard program designed to maximise your memory potential.<p/>It\'s free and licensed under the GPL.<p/><a href=\"http://ichi2.net/anki/\">Visit website</a></span>"))

import icons_rc
