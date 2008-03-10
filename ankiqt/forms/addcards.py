# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addcards.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddCards(object):
    def setupUi(self, AddCards):
        AddCards.setObjectName("AddCards")
        AddCards.resize(QtCore.QSize(QtCore.QRect(0,0,921,553).size()).expandedTo(AddCards.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(AddCards)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(3)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(6)
        self.vboxlayout.setSpacing(3)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(3)
        self.gridlayout.setSpacing(3)
        self.gridlayout.setObjectName("gridlayout")

        self.modelArea = QtGui.QWidget(AddCards)
        self.modelArea.setObjectName("modelArea")
        self.gridlayout.addWidget(self.modelArea,0,0,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.fieldsArea = QtGui.QGroupBox(AddCards)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setObjectName("fieldsArea")
        self.vboxlayout.addWidget(self.fieldsArea)

        self.statusGroup = QtGui.QGroupBox(AddCards)
        self.statusGroup.setObjectName("statusGroup")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.statusGroup)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.status = QtGui.QTextEdit(self.statusGroup)
        self.status.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMaximumSize(QtCore.QSize(16777215,50))
        self.status.setFrameShape(QtGui.QFrame.NoFrame)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setObjectName("status")
        self.vboxlayout1.addWidget(self.status)
        self.vboxlayout.addWidget(self.statusGroup)

        self.buttonBox = QtGui.QDialogButtonBox(AddCards)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.helpFrame = QtGui.QFrame(AddCards)
        self.helpFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.helpFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.helpFrame.setObjectName("helpFrame")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.helpFrame)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.line = QtGui.QFrame(self.helpFrame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout1.addWidget(self.line)

        self.innerHelpFrame = QtGui.QFrame(self.helpFrame)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
        self.innerHelpFrame.setPalette(palette)
        self.innerHelpFrame.setAutoFillBackground(True)
        self.innerHelpFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.innerHelpFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.innerHelpFrame.setObjectName("innerHelpFrame")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.innerHelpFrame)
        self.hboxlayout2.setMargin(9)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.help = QtGui.QTextBrowser(self.innerHelpFrame)
        self.help.setEnabled(True)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMinimumSize(QtCore.QSize(200,0))
        self.help.setMaximumSize(QtCore.QSize(300,16777215))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,250,230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(207,207,207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.help.setPalette(palette)
        self.help.setFrameShape(QtGui.QFrame.NoFrame)
        self.help.setFrameShadow(QtGui.QFrame.Sunken)
        self.help.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.help.setObjectName("help")
        self.hboxlayout2.addWidget(self.help)
        self.hboxlayout1.addWidget(self.innerHelpFrame)
        self.hboxlayout.addWidget(self.helpFrame)

        self.retranslateUi(AddCards)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddCards.reject)
        QtCore.QMetaObject.connectSlotsByName(AddCards)

    def retranslateUi(self, AddCards):
        AddCards.setWindowTitle(_("Anki - Add Cards"))
        self.fieldsArea.setTitle(_("Fields"))
        self.statusGroup.setTitle(_("Status"))

import icons_rc
