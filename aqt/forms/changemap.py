# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/changemap.ui'
#
# Created: Sat Dec 22 09:16:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChangeMap(object):
    def setupUi(self, ChangeMap):
        ChangeMap.setObjectName(_fromUtf8("ChangeMap"))
        ChangeMap.resize(391, 360)
        self.vboxlayout = QtGui.QVBoxLayout(ChangeMap)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label = QtGui.QLabel(ChangeMap)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout.addWidget(self.label)
        self.fields = QtGui.QListWidget(ChangeMap)
        self.fields.setObjectName(_fromUtf8("fields"))
        self.vboxlayout.addWidget(self.fields)
        self.buttonBox = QtGui.QDialogButtonBox(ChangeMap)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChangeMap)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChangeMap.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChangeMap.reject)
        QtCore.QObject.connect(self.fields, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), ChangeMap.accept)
        QtCore.QMetaObject.connectSlotsByName(ChangeMap)

    def retranslateUi(self, ChangeMap):
        ChangeMap.setWindowTitle(_("Import"))
        self.label.setText(_("Target field:"))

