# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/displayproperties.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DisplayProperties(object):
    def setupUi(self, DisplayProperties):
        DisplayProperties.setObjectName("DisplayProperties")
        DisplayProperties.resize(QtCore.QSize(QtCore.QRect(0,0,794,700).size()).expandedTo(DisplayProperties.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DisplayProperties.sizePolicy().hasHeightForWidth())
        DisplayProperties.setSizePolicy(sizePolicy)
        DisplayProperties.setMinimumSize(QtCore.QSize(0,700))
        DisplayProperties.setWindowIcon(QtGui.QIcon(":/icons/fonts.png"))

        self.vboxlayout = QtGui.QVBoxLayout(DisplayProperties)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(12)
        self.gridlayout.setObjectName("gridlayout")

        self.frame = QtGui.QFrame(DisplayProperties)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(330,16))
        self.frame.setMaximumSize(QtCore.QSize(330,16777215))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.frame)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(7)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout2.addLayout(self.hboxlayout)

        self.modelArea = QtGui.QWidget(self.frame)
        self.modelArea.setObjectName("modelArea")
        self.vboxlayout2.addWidget(self.modelArea)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_3 = QtGui.QLabel(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3,1,0,1,1)

        self.cardList = QtGui.QComboBox(self.frame)
        self.cardList.setObjectName("cardList")
        self.gridlayout1.addWidget(self.cardList,1,1,1,1)
        self.vboxlayout2.addLayout(self.gridlayout1)

        self.groupBox_5 = QtGui.QGroupBox(self.frame)
        self.groupBox_5.setObjectName("groupBox_5")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.vboxlayout3.setMargin(3)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(5)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridlayout2.addWidget(self.label_6,0,0,1,1)

        self.answerColour = QtGui.QPushButton(self.groupBox_5)
        self.answerColour.setAutoDefault(False)
        self.answerColour.setObjectName("answerColour")
        self.gridlayout2.addWidget(self.answerColour,6,1,1,1)

        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridlayout2.addWidget(self.label_10,5,0,1,1)

        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridlayout2.addWidget(self.label_11,6,0,1,1)

        self.label_9 = QtGui.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.gridlayout2.addWidget(self.label_9,4,0,1,1)

        self.answerFont = QtGui.QFontComboBox(self.groupBox_5)
        self.answerFont.setObjectName("answerFont")
        self.gridlayout2.addWidget(self.answerFont,4,1,1,1)

        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridlayout2.addWidget(self.label_4,3,0,1,1)

        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridlayout2.addWidget(self.label_7,1,0,1,1)

        self.questionSize = QtGui.QSpinBox(self.groupBox_5)
        self.questionSize.setMaximum(300)
        self.questionSize.setObjectName("questionSize")
        self.gridlayout2.addWidget(self.questionSize,1,1,1,1)

        self.questionFont = QtGui.QFontComboBox(self.groupBox_5)
        self.questionFont.setObjectName("questionFont")
        self.gridlayout2.addWidget(self.questionFont,0,1,1,1)

        self.questionColour = QtGui.QPushButton(self.groupBox_5)
        self.questionColour.setAutoDefault(False)
        self.questionColour.setObjectName("questionColour")
        self.gridlayout2.addWidget(self.questionColour,2,1,1,1)

        self.answerSize = QtGui.QSpinBox(self.groupBox_5)
        self.answerSize.setMaximum(300)
        self.answerSize.setObjectName("answerSize")
        self.gridlayout2.addWidget(self.answerSize,5,1,1,1)

        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.gridlayout2.addWidget(self.label_8,2,0,1,1)

        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.gridlayout2.addWidget(self.label_12,7,0,1,1)

        self.questionAlign = QtGui.QComboBox(self.groupBox_5)
        self.questionAlign.setObjectName("questionAlign")
        self.gridlayout2.addWidget(self.questionAlign,3,1,1,1)

        self.answerAlign = QtGui.QComboBox(self.groupBox_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerAlign.sizePolicy().hasHeightForWidth())
        self.answerAlign.setSizePolicy(sizePolicy)
        self.answerAlign.setObjectName("answerAlign")
        self.gridlayout2.addWidget(self.answerAlign,7,1,1,1)
        self.vboxlayout3.addLayout(self.gridlayout2)
        self.vboxlayout2.addWidget(self.groupBox_5)

        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout4.setMargin(3)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.fieldList = QtGui.QListWidget(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setMinimumSize(QtCore.QSize(0,60))
        self.fieldList.setObjectName("fieldList")
        self.vboxlayout4.addWidget(self.fieldList)

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.vboxlayout4.addWidget(self.label)

        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setSpacing(5)
        self.gridlayout3.setObjectName("gridlayout3")

        self.useSize = QtGui.QCheckBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useSize.sizePolicy().hasHeightForWidth())
        self.useSize.setSizePolicy(sizePolicy)
        self.useSize.setMinimumSize(QtCore.QSize(0,25))
        self.useSize.setObjectName("useSize")
        self.gridlayout3.addWidget(self.useSize,1,0,1,1)

        self.fontFamily = QtGui.QFontComboBox(self.groupBox)
        self.fontFamily.setMinimumSize(QtCore.QSize(0,25))
        self.fontFamily.setObjectName("fontFamily")
        self.gridlayout3.addWidget(self.fontFamily,0,1,1,1)

        self.useFamily = QtGui.QCheckBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useFamily.sizePolicy().hasHeightForWidth())
        self.useFamily.setSizePolicy(sizePolicy)
        self.useFamily.setMinimumSize(QtCore.QSize(0,25))
        self.useFamily.setObjectName("useFamily")
        self.gridlayout3.addWidget(self.useFamily,0,0,1,1)

        self.fontSize = QtGui.QSpinBox(self.groupBox)
        self.fontSize.setMaximum(300)
        self.fontSize.setMinimum(5)
        self.fontSize.setObjectName("fontSize")
        self.gridlayout3.addWidget(self.fontSize,1,1,1,1)

        self.useColour = QtGui.QCheckBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useColour.sizePolicy().hasHeightForWidth())
        self.useColour.setSizePolicy(sizePolicy)
        self.useColour.setMinimumSize(QtCore.QSize(0,25))
        self.useColour.setObjectName("useColour")
        self.gridlayout3.addWidget(self.useColour,2,0,1,1)

        self.fontColour = QtGui.QPushButton(self.groupBox)
        self.fontColour.setAutoFillBackground(True)
        self.fontColour.setAutoDefault(False)
        self.fontColour.setObjectName("fontColour")
        self.gridlayout3.addWidget(self.fontColour,2,1,1,1)
        self.vboxlayout4.addLayout(self.gridlayout3)

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.vboxlayout4.addWidget(self.label_2)

        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setMargin(0)
        self.gridlayout4.setSpacing(5)
        self.gridlayout4.setObjectName("gridlayout4")

        self.fontSizeEdit = QtGui.QSpinBox(self.groupBox)
        self.fontSizeEdit.setMaximum(300)
        self.fontSizeEdit.setMinimum(5)
        self.fontSizeEdit.setObjectName("fontSizeEdit")
        self.gridlayout4.addWidget(self.fontSizeEdit,1,1,1,1)

        self.useSizeEdit = QtGui.QCheckBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useSizeEdit.sizePolicy().hasHeightForWidth())
        self.useSizeEdit.setSizePolicy(sizePolicy)
        self.useSizeEdit.setMinimumSize(QtCore.QSize(0,25))
        self.useSizeEdit.setObjectName("useSizeEdit")
        self.gridlayout4.addWidget(self.useSizeEdit,1,0,1,1)

        self.fontFamilyEdit = QtGui.QFontComboBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontFamilyEdit.sizePolicy().hasHeightForWidth())
        self.fontFamilyEdit.setSizePolicy(sizePolicy)
        self.fontFamilyEdit.setObjectName("fontFamilyEdit")
        self.gridlayout4.addWidget(self.fontFamilyEdit,0,1,1,1)

        self.useFamilyEdit = QtGui.QCheckBox(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useFamilyEdit.sizePolicy().hasHeightForWidth())
        self.useFamilyEdit.setSizePolicy(sizePolicy)
        self.useFamilyEdit.setMinimumSize(QtCore.QSize(0,25))
        self.useFamilyEdit.setObjectName("useFamilyEdit")
        self.gridlayout4.addWidget(self.useFamilyEdit,0,0,1,1)
        self.vboxlayout4.addLayout(self.gridlayout4)
        self.vboxlayout2.addWidget(self.groupBox)

        self.preview = QtGui.QPushButton(self.frame)
        self.preview.setCheckable(True)
        self.preview.setAutoDefault(False)
        self.preview.setObjectName("preview")
        self.vboxlayout2.addWidget(self.preview)
        self.vboxlayout1.addLayout(self.vboxlayout2)
        self.gridlayout.addWidget(self.frame,0,0,1,1)

        self.previewGroup = QtGui.QGroupBox(DisplayProperties)
        self.previewGroup.setObjectName("previewGroup")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.previewGroup)
        self.vboxlayout5.setMargin(6)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.question = QtGui.QTextEdit(self.previewGroup)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(400,0))
        self.question.setReadOnly(True)
        self.question.setObjectName("question")
        self.vboxlayout5.addWidget(self.question)

        self.answer = QtGui.QTextEdit(self.previewGroup)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setReadOnly(True)
        self.answer.setObjectName("answer")
        self.vboxlayout5.addWidget(self.answer)
        self.gridlayout.addWidget(self.previewGroup,0,1,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.retranslateUi(DisplayProperties)
        QtCore.QObject.connect(self.useFamily,QtCore.SIGNAL("toggled(bool)"),self.fontFamily.setShown)
        QtCore.QObject.connect(self.useSize,QtCore.SIGNAL("toggled(bool)"),self.fontSize.setShown)
        QtCore.QObject.connect(self.useColour,QtCore.SIGNAL("toggled(bool)"),self.fontColour.setShown)
        QtCore.QObject.connect(self.useFamilyEdit,QtCore.SIGNAL("toggled(bool)"),self.fontFamilyEdit.setShown)
        QtCore.QObject.connect(self.useSizeEdit,QtCore.SIGNAL("toggled(bool)"),self.fontSizeEdit.setShown)
        QtCore.QMetaObject.connectSlotsByName(DisplayProperties)
        DisplayProperties.setTabOrder(self.cardList,self.questionFont)
        DisplayProperties.setTabOrder(self.questionFont,self.questionSize)
        DisplayProperties.setTabOrder(self.questionSize,self.questionColour)
        DisplayProperties.setTabOrder(self.questionColour,self.questionAlign)
        DisplayProperties.setTabOrder(self.questionAlign,self.answerFont)
        DisplayProperties.setTabOrder(self.answerFont,self.answerSize)
        DisplayProperties.setTabOrder(self.answerSize,self.answerColour)
        DisplayProperties.setTabOrder(self.answerColour,self.answerAlign)
        DisplayProperties.setTabOrder(self.answerAlign,self.fieldList)
        DisplayProperties.setTabOrder(self.fieldList,self.useFamily)
        DisplayProperties.setTabOrder(self.useFamily,self.fontFamily)
        DisplayProperties.setTabOrder(self.fontFamily,self.useSize)
        DisplayProperties.setTabOrder(self.useSize,self.fontSize)
        DisplayProperties.setTabOrder(self.fontSize,self.useColour)
        DisplayProperties.setTabOrder(self.useColour,self.fontColour)
        DisplayProperties.setTabOrder(self.fontColour,self.useFamilyEdit)
        DisplayProperties.setTabOrder(self.useFamilyEdit,self.fontFamilyEdit)
        DisplayProperties.setTabOrder(self.fontFamilyEdit,self.useSizeEdit)
        DisplayProperties.setTabOrder(self.useSizeEdit,self.fontSizeEdit)
        DisplayProperties.setTabOrder(self.fontSizeEdit,self.preview)
        DisplayProperties.setTabOrder(self.preview,self.question)
        DisplayProperties.setTabOrder(self.question,self.answer)

    def retranslateUi(self, DisplayProperties):
        DisplayProperties.setWindowTitle(_("Fonts and colours"))
        self.label_3.setText(_("Card:"))
        self.groupBox_5.setTitle(_("Card properties"))
        self.label_6.setText(_("Question font"))
        self.label_10.setText(_("Answer size"))
        self.label_11.setText(_("Answer colour"))
        self.label_9.setText(_("Answer font"))
        self.label_4.setText(_("Question alignment"))
        self.label_7.setText(_("Question size"))
        self.label_8.setText(_("Question colour"))
        self.label_12.setText(_("Answer alignment"))
        self.groupBox.setTitle(_("Fields"))
        self.label.setText(_(" <b>When quizzing/adding/editing</b>"))
        self.useSize.setText(_("Use custom size"))
        self.useFamily.setText(_("Use custom font"))
        self.useColour.setText(_("Use custom colour"))
        self.label_2.setText(_(" <b>When adding/editing</b>"))
        self.useSizeEdit.setText(_("Use custom size"))
        self.useFamilyEdit.setText(_("Use custom font"))
        self.preview.setText(_("Show preview"))
        self.previewGroup.setTitle(_("Preview"))

import icons_rc
