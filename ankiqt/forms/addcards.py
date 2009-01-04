# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addcards.ui'
#

#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddCards(object):
    def setupUi(self, AddCards):
        AddCards.setObjectName("AddCards")
        AddCards.resize(509,381)
        self.verticalLayout = QtGui.QVBoxLayout(AddCards)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setContentsMargins(0,4,0,4)
        self.gridlayout.setHorizontalSpacing(0)
        self.gridlayout.setVerticalSpacing(4)
        self.gridlayout.setObjectName("gridlayout")
        self.modelArea = QtGui.QWidget(AddCards)
        self.modelArea.setObjectName("modelArea")
        self.gridlayout.addWidget(self.modelArea,0,0,1,1)
        self.line = QtGui.QFrame(AddCards)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line,1,0,1,1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.splitter = QtGui.QSplitter(AddCards)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.fieldsArea = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setAutoFillBackground(True)
        self.fieldsArea.setObjectName("fieldsArea")
        self.status = QtGui.QTextEdit(self.splitter)
        self.status.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QtGui.QFrame.NoFrame)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(AddCards)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddCards)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddCards.reject)
        QtCore.QMetaObject.connectSlotsByName(AddCards)

    def retranslateUi(self, AddCards):
        AddCards.setWindowTitle(_("Add Items"))
        self.status.setHtml(_("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

import icons_rc
