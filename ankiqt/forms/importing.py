# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/importing.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        ImportDialog.setObjectName("ImportDialog")
        ImportDialog.resize(QtCore.QSize(QtCore.QRect(0,0,477,484).size()).expandedTo(ImportDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ImportDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(ImportDialog)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.file = QtGui.QPushButton(self.groupBox)
        self.file.setDefault(True)
        self.file.setObjectName("file")
        self.gridlayout.addWidget(self.file,1,1,1,1)

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.type = QtGui.QComboBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        self.type.setObjectName("type")
        self.gridlayout.addWidget(self.type,0,1,1,1)

        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,2,0,1,1)

        self.tags = QtGui.QLineEdit(self.groupBox)
        self.tags.setObjectName("tags")
        self.gridlayout.addWidget(self.tags,2,1,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.tagDuplicates = QtGui.QCheckBox(self.groupBox)
        self.tagDuplicates.setObjectName("tagDuplicates")
        self.vboxlayout1.addWidget(self.tagDuplicates)

        self.modelArea = QtGui.QWidget(self.groupBox)
        self.modelArea.setObjectName("modelArea")
        self.vboxlayout1.addWidget(self.modelArea)
        self.vboxlayout.addWidget(self.groupBox)

        self.mappingGroup = QtGui.QGroupBox(ImportDialog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingGroup.sizePolicy().hasHeightForWidth())
        self.mappingGroup.setSizePolicy(sizePolicy)
        self.mappingGroup.setObjectName("mappingGroup")

        self.hboxlayout = QtGui.QHBoxLayout(self.mappingGroup)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.importButton = QtGui.QPushButton(self.mappingGroup)
        self.importButton.setObjectName("importButton")
        self.gridlayout1.addWidget(self.importButton,0,2,1,1)

        self.mappingArea = QtGui.QFrame(self.mappingGroup)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingArea.sizePolicy().hasHeightForWidth())
        self.mappingArea.setSizePolicy(sizePolicy)
        self.mappingArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mappingArea.setFrameShadow(QtGui.QFrame.Raised)
        self.mappingArea.setObjectName("mappingArea")
        self.gridlayout1.addWidget(self.mappingArea,0,0,1,1)
        self.hboxlayout.addLayout(self.gridlayout1)
        self.vboxlayout.addWidget(self.mappingGroup)

        self.groupBox_2 = QtGui.QGroupBox(ImportDialog)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.status = QtGui.QTextEdit(self.groupBox_2)
        self.status.setReadOnly(True)
        self.status.setObjectName("status")
        self.vboxlayout2.addWidget(self.status)
        self.vboxlayout.addWidget(self.groupBox_2)

        self.buttonBox = QtGui.QDialogButtonBox(ImportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ImportDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),ImportDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),ImportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportDialog)
        ImportDialog.setTabOrder(self.type,self.file)
        ImportDialog.setTabOrder(self.file,self.tags)
        ImportDialog.setTabOrder(self.tags,self.tagDuplicates)
        ImportDialog.setTabOrder(self.tagDuplicates,self.importButton)
        ImportDialog.setTabOrder(self.importButton,self.status)
        ImportDialog.setTabOrder(self.status,self.buttonBox)

    def retranslateUi(self, ImportDialog):
        ImportDialog.setWindowTitle(_("Import"))
        self.groupBox.setTitle(_("Import options"))
        self.label_2.setText(_("<b>File to import</b>:"))
        self.file.setText(_("Choose &file..."))
        self.label.setText(_("<b>Type of file</b>:"))
        self.label_4.setText(_("Tags to append:"))
        self.tagDuplicates.setText(_("Tag facts with duplicate fields instead of deleting"))
        self.mappingGroup.setTitle(_("Field mapping"))
        self.importButton.setText(_("&Import"))
        self.groupBox_2.setTitle(_("Status"))

