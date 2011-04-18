# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/activetags.ui'
#

#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(341, 348)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.activeCheck = QtGui.QCheckBox(Dialog)
        self.activeCheck.setObjectName("activeCheck")
        self.verticalLayout.addWidget(self.activeCheck)
        self.activeList = QtGui.QListWidget(Dialog)
        self.activeList.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.activeList.sizePolicy().hasHeightForWidth())
        self.activeList.setSizePolicy(sizePolicy)
        self.activeList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.activeList.setObjectName("activeList")
        self.verticalLayout.addWidget(self.activeList)
        self.inactiveCheck = QtGui.QCheckBox(Dialog)
        self.inactiveCheck.setObjectName("inactiveCheck")
        self.verticalLayout.addWidget(self.inactiveCheck)
        self.inactiveList = QtGui.QListWidget(Dialog)
        self.inactiveList.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.inactiveList.sizePolicy().hasHeightForWidth())
        self.inactiveList.setSizePolicy(sizePolicy)
        self.inactiveList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.inactiveList.setObjectName("inactiveList")
        self.verticalLayout.addWidget(self.inactiveList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.newButton = QtGui.QRadioButton(self.groupBox)
        self.newButton.setObjectName("newButton")
        self.verticalLayout_3.addWidget(self.newButton)
        self.revButton = QtGui.QRadioButton(self.groupBox)
        self.revButton.setObjectName("revButton")
        self.verticalLayout_3.addWidget(self.revButton)
        self.bothButton = QtGui.QRadioButton(self.groupBox)
        self.bothButton.setObjectName("bothButton")
        self.verticalLayout_3.addWidget(self.bothButton)
        self.horizontalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.activeCheck, QtCore.SIGNAL("toggled(bool)"), self.activeList.setEnabled)
        QtCore.QObject.connect(self.inactiveCheck, QtCore.SIGNAL("toggled(bool)"), self.inactiveList.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Selective Study"))
        self.activeCheck.setText(_("Show only cards with any of these tags:"))
        self.inactiveCheck.setText(_("Hide cards with any of these tags:"))
        self.groupBox.setTitle(_("Change settings for:"))
        self.newButton.setText(_("New Cards"))
        self.revButton.setText(_("Reviews"))
        self.bothButton.setText(_("Both"))

