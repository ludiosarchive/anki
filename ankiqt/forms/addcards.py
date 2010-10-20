# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addcards.ui'
#

#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddCards(object):
    def setupUi(self, AddCards):
        AddCards.setObjectName("AddCards")
        AddCards.resize(509, 381)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddCards.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AddCards)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setContentsMargins(0, 4, 0, 4)
        self.gridlayout.setHorizontalSpacing(0)
        self.gridlayout.setVerticalSpacing(4)
        self.gridlayout.setObjectName("gridlayout")
        self.modelArea = QtGui.QWidget(AddCards)
        self.modelArea.setObjectName("modelArea")
        self.gridlayout.addWidget(self.modelArea, 0, 0, 1, 1)
        self.line = QtGui.QFrame(AddCards)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.splitter = QtGui.QSplitter(AddCards)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.fieldsArea = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setAutoFillBackground(True)
        self.fieldsArea.setObjectName("fieldsArea")
        self.status = QtGui.QTextBrowser(self.splitter)
        self.status.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.status.setPalette(palette)
        self.status.setAcceptDrops(False)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QtGui.QFrame.NoFrame)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setReadOnly(True)
        self.status.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.status.setOpenLinks(False)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(AddCards)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddCards)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddCards.reject)
        QtCore.QMetaObject.connectSlotsByName(AddCards)

    def retranslateUi(self, AddCards):
        AddCards.setWindowTitle(_("Add Items"))

import icons_rc
