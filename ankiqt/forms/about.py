# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(QtCore.QSize(QtCore.QRect(0,0,224,242).size()).expandedTo(About.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)

        self.vboxlayout = QtGui.QVBoxLayout(About)
        self.vboxlayout.setObjectName("vboxlayout")

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

import icons_rc
