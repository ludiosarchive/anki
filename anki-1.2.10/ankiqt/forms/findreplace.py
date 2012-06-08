# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/findreplace.ui'
#

#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 159)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.find = QtGui.QLineEdit(Dialog)
        self.find.setObjectName("find")
        self.gridLayout.addWidget(self.find, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.replace = QtGui.QLineEdit(Dialog)
        self.replace.setObjectName("replace")
        self.gridLayout.addWidget(self.replace, 2, 1, 1, 1)
        self.re = QtGui.QCheckBox(Dialog)
        self.re.setObjectName("re")
        self.gridLayout.addWidget(self.re, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.field = QtGui.QComboBox(Dialog)
        self.field.setObjectName("field")
        self.gridLayout.addWidget(self.field, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.find, self.field)
        Dialog.setTabOrder(self.field, self.replace)
        Dialog.setTabOrder(self.replace, self.re)
        Dialog.setTabOrder(self.re, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Find and Replace"))
        self.label.setText(_("<b>Find</b>:"))
        self.label_2.setText(_("<b>Replace With</b>:"))
        self.re.setText(_("Treat input as regular expression"))
        self.label_3.setText(_("<b>In</b>:"))

