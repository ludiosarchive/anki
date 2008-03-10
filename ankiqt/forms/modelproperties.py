# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/modelproperties.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ModelProperties(object):
    def setupUi(self, ModelProperties):
        ModelProperties.setObjectName("ModelProperties")
        ModelProperties.setWindowModality(QtCore.Qt.ApplicationModal)
        ModelProperties.resize(QtCore.QSize(QtCore.QRect(0,0,568,533).size()).expandedTo(ModelProperties.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ModelProperties)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(ModelProperties)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.vboxlayout1.addWidget(self.label_7)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,2,0,1,1)

        self.name = QtGui.QLineEdit(self.tab)
        self.name.setObjectName("name")
        self.gridlayout.addWidget(self.name,0,1,1,1)

        self.description = QtGui.QTextEdit(self.tab)
        self.description.setTabChangesFocus(True)
        self.description.setObjectName("description")
        self.gridlayout.addWidget(self.description,2,1,1,1)

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,4,0,1,1)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setSpacing(0)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.vboxlayout2.addWidget(self.label_6)

        self.decorators = QtGui.QLineEdit(self.tab)
        self.decorators.setObjectName("decorators")
        self.vboxlayout2.addWidget(self.decorators)
        self.gridlayout.addLayout(self.vboxlayout2,4,1,1,1)

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.tags = QtGui.QLineEdit(self.tab)
        self.tags.setObjectName("tags")
        self.gridlayout.addWidget(self.tags,1,1,1,1)

        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,3,0,1,1)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridlayout1.addWidget(self.label_16,0,0,1,1)

        self.initialSpacing = QtGui.QLineEdit(self.tab)
        self.initialSpacing.setObjectName("initialSpacing")
        self.gridlayout1.addWidget(self.initialSpacing,0,2,1,1)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem,0,1,1,1)

        self.label_24 = QtGui.QLabel(self.tab)
        self.label_24.setObjectName("label_24")
        self.gridlayout1.addWidget(self.label_24,1,0,1,1)

        self.spacing = QtGui.QLineEdit(self.tab)
        self.spacing.setObjectName("spacing")
        self.gridlayout1.addWidget(self.spacing,1,2,1,1)
        self.gridlayout.addLayout(self.gridlayout1,3,1,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.vboxlayout3.addWidget(self.label_8)

        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.vboxlayout3.addWidget(self.label_10)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.fieldList = QtGui.QListWidget(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setMinimumSize(QtCore.QSize(0,60))
        self.fieldList.setObjectName("fieldList")
        self.hboxlayout.addWidget(self.fieldList)

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.fieldAdd = QtGui.QPushButton(self.tab_2)
        self.fieldAdd.setAutoDefault(False)
        self.fieldAdd.setObjectName("fieldAdd")
        self.vboxlayout4.addWidget(self.fieldAdd)

        self.fieldDelete = QtGui.QPushButton(self.tab_2)
        self.fieldDelete.setAutoDefault(False)
        self.fieldDelete.setObjectName("fieldDelete")
        self.vboxlayout4.addWidget(self.fieldDelete)
        self.hboxlayout.addLayout(self.vboxlayout4)
        self.vboxlayout3.addLayout(self.hboxlayout)

        self.fieldEditBox = QtGui.QGroupBox(self.tab_2)
        self.fieldEditBox.setObjectName("fieldEditBox")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.fieldEditBox)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setMargin(9)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label_18 = QtGui.QLabel(self.fieldEditBox)
        self.label_18.setObjectName("label_18")
        self.gridlayout2.addWidget(self.label_18,2,0,1,1)

        self.fieldName = QtGui.QLineEdit(self.fieldEditBox)
        self.fieldName.setObjectName("fieldName")
        self.gridlayout2.addWidget(self.fieldName,0,1,1,1)

        self.fieldUnique = QtGui.QCheckBox(self.fieldEditBox)
        self.fieldUnique.setObjectName("fieldUnique")
        self.gridlayout2.addWidget(self.fieldUnique,2,1,1,1)

        self.label_20 = QtGui.QLabel(self.fieldEditBox)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.gridlayout2.addWidget(self.label_20,0,0,1,1)

        self.label_19 = QtGui.QLabel(self.fieldEditBox)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.gridlayout2.addWidget(self.label_19,1,0,1,1)

        self.label_17 = QtGui.QLabel(self.fieldEditBox)
        self.label_17.setObjectName("label_17")
        self.gridlayout2.addWidget(self.label_17,3,0,1,1)

        self.fieldRequired = QtGui.QCheckBox(self.fieldEditBox)
        self.fieldRequired.setObjectName("fieldRequired")
        self.gridlayout2.addWidget(self.fieldRequired,3,1,1,1)

        self.label_22 = QtGui.QLabel(self.fieldEditBox)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.gridlayout2.addWidget(self.label_22,5,0,1,1)

        self.fieldDescription = QtGui.QTextEdit(self.fieldEditBox)
        self.fieldDescription.setTabChangesFocus(True)
        self.fieldDescription.setObjectName("fieldDescription")
        self.gridlayout2.addWidget(self.fieldDescription,1,1,1,1)

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setSpacing(0)
        self.vboxlayout6.setMargin(0)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.label_25 = QtGui.QLabel(self.fieldEditBox)
        self.label_25.setObjectName("label_25")
        self.vboxlayout6.addWidget(self.label_25)

        self.fieldFeatures = QtGui.QLineEdit(self.fieldEditBox)
        self.fieldFeatures.setObjectName("fieldFeatures")
        self.vboxlayout6.addWidget(self.fieldFeatures)
        self.gridlayout2.addLayout(self.vboxlayout6,5,1,1,1)

        self.label_21 = QtGui.QLabel(self.fieldEditBox)
        self.label_21.setObjectName("label_21")
        self.gridlayout2.addWidget(self.label_21,4,0,1,1)

        self.numeric = QtGui.QCheckBox(self.fieldEditBox)
        self.numeric.setObjectName("numeric")
        self.gridlayout2.addWidget(self.numeric,4,1,1,1)
        self.vboxlayout5.addLayout(self.gridlayout2)
        self.vboxlayout3.addWidget(self.fieldEditBox)
        self.tabWidget.addTab(self.tab_2,"")

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.vboxlayout7 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setMargin(9)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.label_9 = QtGui.QLabel(self.tab_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.vboxlayout7.addWidget(self.label_9)

        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.vboxlayout7.addWidget(self.label_11)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.cardList = QtGui.QListWidget(self.tab_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardList.sizePolicy().hasHeightForWidth())
        self.cardList.setSizePolicy(sizePolicy)
        self.cardList.setMinimumSize(QtCore.QSize(0,60))
        self.cardList.setObjectName("cardList")
        self.hboxlayout1.addWidget(self.cardList)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setMargin(0)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.cardAdd = QtGui.QPushButton(self.tab_3)
        self.cardAdd.setObjectName("cardAdd")
        self.vboxlayout8.addWidget(self.cardAdd)

        self.cardToggle = QtGui.QPushButton(self.tab_3)
        self.cardToggle.setObjectName("cardToggle")
        self.vboxlayout8.addWidget(self.cardToggle)

        self.cardDelete = QtGui.QPushButton(self.tab_3)
        self.cardDelete.setObjectName("cardDelete")
        self.vboxlayout8.addWidget(self.cardDelete)
        self.hboxlayout1.addLayout(self.vboxlayout8)
        self.vboxlayout7.addLayout(self.hboxlayout1)

        self.cardEditBox = QtGui.QGroupBox(self.tab_3)
        self.cardEditBox.setObjectName("cardEditBox")

        self.vboxlayout9 = QtGui.QVBoxLayout(self.cardEditBox)
        self.vboxlayout9.setSpacing(6)
        self.vboxlayout9.setMargin(9)
        self.vboxlayout9.setObjectName("vboxlayout9")

        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.cardDescription = QtGui.QTextEdit(self.cardEditBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardDescription.sizePolicy().hasHeightForWidth())
        self.cardDescription.setSizePolicy(sizePolicy)
        self.cardDescription.setMaximumSize(QtCore.QSize(16777215,60))
        self.cardDescription.setTabChangesFocus(True)
        self.cardDescription.setObjectName("cardDescription")
        self.gridlayout3.addWidget(self.cardDescription,1,1,1,1)

        self.label_13 = QtGui.QLabel(self.cardEditBox)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.gridlayout3.addWidget(self.label_13,1,0,1,1)

        self.label_23 = QtGui.QLabel(self.cardEditBox)
        self.label_23.setObjectName("label_23")
        self.gridlayout3.addWidget(self.label_23,4,0,1,1)

        self.questionInAnswer = QtGui.QCheckBox(self.cardEditBox)
        self.questionInAnswer.setObjectName("questionInAnswer")
        self.gridlayout3.addWidget(self.questionInAnswer,4,1,1,1)

        self.cardAnswer = QtGui.QTextEdit(self.cardEditBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardAnswer.sizePolicy().hasHeightForWidth())
        self.cardAnswer.setSizePolicy(sizePolicy)
        self.cardAnswer.setMaximumSize(QtCore.QSize(16777215,60))
        self.cardAnswer.setTabChangesFocus(True)
        self.cardAnswer.setAcceptRichText(False)
        self.cardAnswer.setObjectName("cardAnswer")
        self.gridlayout3.addWidget(self.cardAnswer,3,1,1,1)

        self.label_15 = QtGui.QLabel(self.cardEditBox)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.gridlayout3.addWidget(self.label_15,3,0,1,1)

        self.cardName = QtGui.QLineEdit(self.cardEditBox)
        self.cardName.setObjectName("cardName")
        self.gridlayout3.addWidget(self.cardName,0,1,1,1)

        self.cardQuestion = QtGui.QTextEdit(self.cardEditBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardQuestion.sizePolicy().hasHeightForWidth())
        self.cardQuestion.setSizePolicy(sizePolicy)
        self.cardQuestion.setMaximumSize(QtCore.QSize(16777215,60))
        self.cardQuestion.setTabChangesFocus(True)
        self.cardQuestion.setObjectName("cardQuestion")
        self.gridlayout3.addWidget(self.cardQuestion,2,1,1,1)

        self.label_14 = QtGui.QLabel(self.cardEditBox)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.gridlayout3.addWidget(self.label_14,2,0,1,1)

        self.label_12 = QtGui.QLabel(self.cardEditBox)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.gridlayout3.addWidget(self.label_12,0,0,1,1)
        self.vboxlayout9.addLayout(self.gridlayout3)
        self.vboxlayout7.addWidget(self.cardEditBox)
        self.tabWidget.addTab(self.tab_3,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.buttonBox = QtGui.QDialogButtonBox(ModelProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ModelProperties)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),ModelProperties.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),ModelProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(ModelProperties)
        ModelProperties.setTabOrder(self.tabWidget,self.name)
        ModelProperties.setTabOrder(self.name,self.tags)
        ModelProperties.setTabOrder(self.tags,self.description)
        ModelProperties.setTabOrder(self.description,self.initialSpacing)
        ModelProperties.setTabOrder(self.initialSpacing,self.spacing)
        ModelProperties.setTabOrder(self.spacing,self.decorators)
        ModelProperties.setTabOrder(self.decorators,self.fieldList)
        ModelProperties.setTabOrder(self.fieldList,self.fieldAdd)
        ModelProperties.setTabOrder(self.fieldAdd,self.fieldDelete)
        ModelProperties.setTabOrder(self.fieldDelete,self.fieldName)
        ModelProperties.setTabOrder(self.fieldName,self.fieldDescription)
        ModelProperties.setTabOrder(self.fieldDescription,self.fieldUnique)
        ModelProperties.setTabOrder(self.fieldUnique,self.fieldRequired)
        ModelProperties.setTabOrder(self.fieldRequired,self.numeric)
        ModelProperties.setTabOrder(self.numeric,self.fieldFeatures)
        ModelProperties.setTabOrder(self.fieldFeatures,self.cardList)
        ModelProperties.setTabOrder(self.cardList,self.cardAdd)
        ModelProperties.setTabOrder(self.cardAdd,self.cardToggle)
        ModelProperties.setTabOrder(self.cardToggle,self.cardDelete)
        ModelProperties.setTabOrder(self.cardDelete,self.cardName)
        ModelProperties.setTabOrder(self.cardName,self.cardDescription)
        ModelProperties.setTabOrder(self.cardDescription,self.cardQuestion)
        ModelProperties.setTabOrder(self.cardQuestion,self.cardAnswer)
        ModelProperties.setTabOrder(self.cardAnswer,self.questionInAnswer)
        ModelProperties.setTabOrder(self.questionInAnswer,self.buttonBox)

    def retranslateUi(self, ModelProperties):
        ModelProperties.setWindowTitle(_("Model Properties"))
        self.label_7.setText(_("<h1>Model properties</h1>"))
        self.label.setText(_("<b>Name</b>:"))
        self.label_2.setText(_("<b>Description</b>:"))
        self.label_4.setText(_("<b>Features</b>:"))
        self.label_6.setText(_("Special features used by the model."))
        self.label_3.setText(_("<b>Tags</b>:"))
        self.label_5.setText(_("<b>Card spacing</b>"))
        self.label_16.setText(_("Initial delay in seconds for each card"))
        self.label_24.setText(_("Percentage of minimum interval"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Model properties"))
        self.label_8.setText(_("<h1>Fields</h1>"))
        self.label_10.setText(_("A flashcard is made from a number of fields, like \"meaning\", \"notes\", etc."))
        self.fieldAdd.setText(_("&Add"))
        self.fieldDelete.setText(_("&Delete"))
        self.fieldEditBox.setTitle(_("Field properties"))
        self.label_18.setText(_("<b>Unique?"))
        self.fieldUnique.setText(_("Prevent me from entering the same thing in this field twice"))
        self.label_20.setText(_("<b>Name</b>"))
        self.label_19.setText(_("<b>Description</b>"))
        self.label_17.setText(_("<b>Required?</b>"))
        self.fieldRequired.setText(_("Prevent new cards from being added if this field is blank"))
        self.label_22.setText(_("<b>Features</b>"))
        self.label_25.setText(_("Special features used by the field."))
        self.label_21.setText(_("<b>Numeric?</b>"))
        self.numeric.setText(_("Sort this field using numeric order instead of string order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Fields"))
        self.label_9.setText(_("<h1>Card models</h1>"))
        self.label_11.setText(_("One or more cards are generated for each piece of information you enter into Anki. Here you can control how many cards are generated, and what they look like. Spacing is the amount of time before showing a different card for the same piece of information."))
        self.cardAdd.setText(_("&Add"))
        self.cardDelete.setText(_("&Delete"))
        self.cardEditBox.setTitle(_("Edit card"))
        self.label_13.setText(_("<b>Description</b>"))
        self.label_23.setText(_("<b>Question hiding</b>"))
        self.questionInAnswer.setText(_("Hide the question when showing answer"))
        self.label_15.setText(_("<b>Answer format</b>"))
        self.label_14.setText(_("<b>Question format</b>"))
        self.label_12.setText(_("<b>Name/tag</b>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("Cards"))

