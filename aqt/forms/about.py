# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about.ui'
#
# Created: Thu Jul 18 18:08:51 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(410, 664)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        self.vboxlayout = QtGui.QVBoxLayout(About)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label = QtWebKit.QWebView(About)
        self.label.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), About.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_("About Anki"))

from PyQt4 import QtWebKit
import icons_rc
