# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addmodel.ui'
#

#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddModel(object):
    def setupUi(self, AddModel):
        AddModel.setObjectName("AddModel")
        AddModel.resize(285,269)
        self.vboxlayout = QtGui.QVBoxLayout(AddModel)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtGui.QLabel(AddModel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(AddModel)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.models = QtGui.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.models.setFont(font)
        self.models.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.models.setTabKeyNavigation(True)
        self.models.setObjectName("models")
        self.vboxlayout1.addWidget(self.models)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddModel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddModel)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),AddModel.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddModel.reject)
        QtCore.QMetaObject.connectSlotsByName(AddModel)

    def retranslateUi(self, AddModel):
        AddModel.setWindowTitle(_("Anki"))
        self.label.setText(_("<h1>Please choose a template</h1>"))

