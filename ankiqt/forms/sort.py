# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/sort.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Sort(object):
    def setupUi(self, Sort):
        Sort.setObjectName("Sort")
        Sort.resize(QtCore.QSize(QtCore.QRect(0,0,425,358).size()).expandedTo(Sort.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Sort)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(20)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(Sort)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.fields = QtGui.QListWidget(Sort)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.fields.setFont(font)
        self.fields.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.fields.setTabKeyNavigation(True)
        self.fields.setObjectName("fields")
        self.vboxlayout.addWidget(self.fields)

        self.buttonBox = QtGui.QDialogButtonBox(Sort)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(Sort)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Sort.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Sort.reject)
        QtCore.QMetaObject.connectSlotsByName(Sort)

    def retranslateUi(self, Sort):
        Sort.setWindowTitle(_("Anki"))
        self.label.setText(_("Please choose a field to sort by."))

