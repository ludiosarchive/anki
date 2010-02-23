# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/reschedule.ui'
#

#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(255, 158)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.asNew = QtGui.QRadioButton(Dialog)
        self.asNew.setChecked(True)
        self.asNew.setObjectName("asNew")
        self.verticalLayout_2.addWidget(self.asNew)
        self.inRange = QtGui.QRadioButton(Dialog)
        self.inRange.setObjectName("inRange")
        self.verticalLayout_2.addWidget(self.inRange)
        self.rangebox = QtGui.QWidget(Dialog)
        self.rangebox.setEnabled(False)
        self.rangebox.setObjectName("rangebox")
        self.verticalLayout = QtGui.QVBoxLayout(self.rangebox)
        self.verticalLayout.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.rangebox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.rangebox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.rangebox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.rangebox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.rangeMin = QtGui.QDoubleSpinBox(self.rangebox)
        self.rangeMin.setMaximum(99999.0)
        self.rangeMin.setObjectName("rangeMin")
        self.gridLayout.addWidget(self.rangeMin, 0, 1, 1, 1)
        self.rangeMax = QtGui.QDoubleSpinBox(self.rangebox)
        self.rangeMax.setMaximum(99999.0)
        self.rangeMax.setObjectName("rangeMax")
        self.gridLayout.addWidget(self.rangeMax, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.rangebox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.inRange, QtCore.SIGNAL("toggled(bool)"), self.rangebox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.asNew, self.inRange)
        Dialog.setTabOrder(self.inRange, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Reschedule"))
        self.asNew.setText(_("Reschedule as new cards"))
        self.inRange.setText(_("Reschedule with initial interval in range:"))
        self.label.setText(_("Min"))
        self.label_3.setText(_("days"))
        self.label_2.setText(_("Max"))
        self.label_4.setText(_("days"))

