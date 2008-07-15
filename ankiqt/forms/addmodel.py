# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addmodel.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddModel(object):
    def setupUi(self, AddModel):
        AddModel.setObjectName("AddModel")
        AddModel.resize(QtCore.QSize(QtCore.QRect(0,0,388,363).size()).expandedTo(AddModel.minimumSizeHint()))

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

        self.createTemplate = QtGui.QRadioButton(self.groupBox)
        self.createTemplate.setChecked(True)
        self.createTemplate.setObjectName("createTemplate")
        self.vboxlayout1.addWidget(self.createTemplate)

        self.models = QtGui.QListWidget(self.groupBox)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.models.setFont(font)
        self.models.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.models.setTabKeyNavigation(True)
        self.models.setObjectName("models")
        self.vboxlayout1.addWidget(self.models)

        self.createBasic = QtGui.QRadioButton(self.groupBox)
        self.createBasic.setObjectName("createBasic")
        self.vboxlayout1.addWidget(self.createBasic)

        self.loadOnline = QtGui.QRadioButton(self.groupBox)
        self.loadOnline.setObjectName("loadOnline")
        self.vboxlayout1.addWidget(self.loadOnline)
        self.vboxlayout.addWidget(self.groupBox)

        self.buttonBox = QtGui.QDialogButtonBox(AddModel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddModel)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),AddModel.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddModel.reject)
        QtCore.QObject.connect(self.createTemplate,QtCore.SIGNAL("toggled(bool)"),self.models.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AddModel)

    def retranslateUi(self, AddModel):
        AddModel.setWindowTitle(_("Anki"))
        self.label.setText(_("<h1>What would you like to study?</h1>"))
        self.createTemplate.setText(_("A pre-made quiz style."))
        self.createBasic.setText(_("A simple front-to-back quiz style."))
        self.loadOnline.setText(_("An existing online deck."))

