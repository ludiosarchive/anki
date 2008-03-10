# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/changemap.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ChangeMap(object):
    def setupUi(self, ChangeMap):
        ChangeMap.setObjectName("ChangeMap")
        ChangeMap.resize(QtCore.QSize(QtCore.QRect(0,0,391,360).size()).expandedTo(ChangeMap.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ChangeMap)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(ChangeMap)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.fields = QtGui.QListWidget(ChangeMap)
        self.fields.setObjectName("fields")
        self.vboxlayout.addWidget(self.fields)

        self.buttonBox = QtGui.QDialogButtonBox(ChangeMap)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChangeMap)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),ChangeMap.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),ChangeMap.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeMap)

    def retranslateUi(self, ChangeMap):
        ChangeMap.setWindowTitle(_("Change field mapping"))
        self.label.setText(_("<h1>Available fields</h1>Please choose which field you would like to import into. If you select \"Discard field\", all data from this field will be lost."))

