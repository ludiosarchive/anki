# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/exporting.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName("ExportDialog")
        ExportDialog.resize(QtCore.QSize(QtCore.QRect(0,0,295,154).size()).expandedTo(ExportDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ExportDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(ExportDialog)
        self.label.setMinimumSize(QtCore.QSize(100,0))
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.format = QtGui.QComboBox(ExportDialog)
        self.format.setObjectName("format")
        self.gridlayout.addWidget(self.format,0,1,1,1)

        self.label_2 = QtGui.QLabel(ExportDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.includeScheduling = QtGui.QCheckBox(ExportDialog)
        self.includeScheduling.setObjectName("includeScheduling")
        self.vboxlayout1.addWidget(self.includeScheduling)

        self.includeTags = QtGui.QCheckBox(ExportDialog)
        self.includeTags.setObjectName("includeTags")
        self.vboxlayout1.addWidget(self.includeTags)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(_("Export"))
        self.label.setText(_("<b>Export format</b>:"))
        self.label_2.setText(_("<b>Limit to tags</b>:"))
        self.includeScheduling.setText(_("Include scheduling information"))
        self.includeTags.setText(_("Include tags"))

