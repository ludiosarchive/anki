# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/infodialog.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(QtCore.QSize(QtCore.QRect(0,0,409,284).size()).expandedTo(InfoDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(InfoDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.textEdit = QtGui.QTextEdit(InfoDialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.vboxlayout.addWidget(self.textEdit)

        self.buttonBox = QtGui.QDialogButtonBox(InfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(InfoDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),InfoDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),InfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(_("Dialog"))

