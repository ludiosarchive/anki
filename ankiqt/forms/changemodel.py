# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/changemodel.ui'
#

#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(294, 331)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.oldModelLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldModelLabel.sizePolicy().hasHeightForWidth())
        self.oldModelLabel.setSizePolicy(sizePolicy)
        self.oldModelLabel.setMargin(4)
        self.oldModelLabel.setObjectName("oldModelLabel")
        self.gridLayout.addWidget(self.oldModelLabel, 0, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.modelChooserWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelChooserWidget.sizePolicy().hasHeightForWidth())
        self.modelChooserWidget.setSizePolicy(sizePolicy)
        self.modelChooserWidget.setObjectName("modelChooserWidget")
        self.gridLayout.addWidget(self.modelChooserWidget, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.templateMap = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templateMap.sizePolicy().hasHeightForWidth())
        self.templateMap.setSizePolicy(sizePolicy)
        self.templateMap.setObjectName("templateMap")
        self.verticalLayout.addWidget(self.templateMap)
        self.fieldMap = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldMap.sizePolicy().hasHeightForWidth())
        self.fieldMap.setSizePolicy(sizePolicy)
        self.fieldMap.setObjectName("fieldMap")
        self.verticalLayout.addWidget(self.fieldMap)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Change Model"))
        self.label_6.setText(_("<b>Old Model</b>:"))
        self.label.setText(_("<b>New Model</b>:"))
        self.templateMap.setTitle(_("Templates"))
        self.fieldMap.setTitle(_("Fields"))

