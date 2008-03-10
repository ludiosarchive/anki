# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(QtCore.QSize(QtCore.QRect(0,0,475,500).size()).expandedTo(Preferences.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Preferences)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.hboxlayout = QtGui.QHBoxLayout(self.tab_1)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label = QtGui.QLabel(self.tab_1)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)

        self.interfaceLang = QtGui.QComboBox(self.tab_1)
        self.interfaceLang.setMinimumSize(QtCore.QSize(300,0))
        self.interfaceLang.setObjectName("interfaceLang")
        self.vboxlayout1.addWidget(self.interfaceLang)

        self.label_2 = QtGui.QLabel(self.tab_1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.interfaceSize = QtGui.QSpinBox(self.tab_1)
        self.interfaceSize.setMaximum(300)
        self.interfaceSize.setObjectName("interfaceSize")
        self.gridlayout.addWidget(self.interfaceSize,0,2,1,1)

        self.label_9 = QtGui.QLabel(self.tab_1)
        self.label_9.setObjectName("label_9")
        self.gridlayout.addWidget(self.label_9,1,0,1,1)

        self.interfaceFamily = QtGui.QFontComboBox(self.tab_1)
        self.interfaceFamily.setMaximumSize(QtCore.QSize(170,16777215))
        self.interfaceFamily.setObjectName("interfaceFamily")
        self.gridlayout.addWidget(self.interfaceFamily,0,1,1,1)

        self.lastCardFamily = QtGui.QFontComboBox(self.tab_1)
        self.lastCardFamily.setMaximumSize(QtCore.QSize(170,16777215))
        self.lastCardFamily.setObjectName("lastCardFamily")
        self.gridlayout.addWidget(self.lastCardFamily,1,1,1,1)

        self.label_8 = QtGui.QLabel(self.tab_1)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,0,0,1,1)

        self.lastCardSize = QtGui.QSpinBox(self.tab_1)
        self.lastCardSize.setMaximum(300)
        self.lastCardSize.setObjectName("lastCardSize")
        self.gridlayout.addWidget(self.lastCardSize,1,2,1,1)

        self.label_10 = QtGui.QLabel(self.tab_1)
        self.label_10.setObjectName("label_10")
        self.gridlayout.addWidget(self.label_10,2,0,1,1)

        self.editFamily = QtGui.QFontComboBox(self.tab_1)
        self.editFamily.setMaximumSize(QtCore.QSize(170,16777215))
        self.editFamily.setObjectName("editFamily")
        self.gridlayout.addWidget(self.editFamily,2,1,1,1)

        self.editSize = QtGui.QSpinBox(self.tab_1)
        self.editSize.setMinimum(6)
        self.editSize.setMaximum(20)
        self.editSize.setObjectName("editSize")
        self.gridlayout.addWidget(self.editSize,2,2,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.label_3 = QtGui.QLabel(self.tab_1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.vboxlayout1.addWidget(self.label_3)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.interfaceColour = QtGui.QPushButton(self.tab_1)
        self.interfaceColour.setObjectName("interfaceColour")
        self.gridlayout1.addWidget(self.interfaceColour,0,1,1,1)

        self.label_13 = QtGui.QLabel(self.tab_1)
        self.label_13.setObjectName("label_13")
        self.gridlayout1.addWidget(self.label_13,0,0,1,1)

        self.lastCardColour = QtGui.QPushButton(self.tab_1)
        self.lastCardColour.setObjectName("lastCardColour")
        self.gridlayout1.addWidget(self.lastCardColour,1,1,1,1)

        self.label_14 = QtGui.QLabel(self.tab_1)
        self.label_14.setObjectName("label_14")
        self.gridlayout1.addWidget(self.label_14,1,0,1,1)

        self.label_15 = QtGui.QLabel(self.tab_1)
        self.label_15.setObjectName("label_15")
        self.gridlayout1.addWidget(self.label_15,2,0,1,1)

        self.backgroundColour = QtGui.QPushButton(self.tab_1)
        self.backgroundColour.setObjectName("backgroundColour")
        self.gridlayout1.addWidget(self.backgroundColour,2,1,1,1)
        self.vboxlayout1.addLayout(self.gridlayout1)
        self.hboxlayout.addLayout(self.vboxlayout1)
        self.tabWidget.addTab(self.tab_1,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setSpacing(12)
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.vboxlayout3.addWidget(self.label_4)

        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.saveAfterEvery = QtGui.QCheckBox(self.tab_2)
        self.saveAfterEvery.setChecked(True)
        self.saveAfterEvery.setObjectName("saveAfterEvery")
        self.gridlayout2.addWidget(self.saveAfterEvery,1,0,1,1)

        self.saveAfterEveryNum = QtGui.QSpinBox(self.tab_2)
        self.saveAfterEveryNum.setObjectName("saveAfterEveryNum")
        self.gridlayout2.addWidget(self.saveAfterEveryNum,1,1,1,1)

        self.saveWhenClosing = QtGui.QCheckBox(self.tab_2)
        self.saveWhenClosing.setChecked(True)
        self.saveWhenClosing.setObjectName("saveWhenClosing")
        self.gridlayout2.addWidget(self.saveWhenClosing,0,0,1,1)

        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout2.addWidget(self.label_5,1,2,1,1)

        self.saveAfterAdding = QtGui.QCheckBox(self.tab_2)
        self.saveAfterAdding.setChecked(True)
        self.saveAfterAdding.setObjectName("saveAfterAdding")
        self.gridlayout2.addWidget(self.saveAfterAdding,2,0,1,1)

        self.saveAfterAddingNum = QtGui.QSpinBox(self.tab_2)
        self.saveAfterAddingNum.setObjectName("saveAfterAddingNum")
        self.gridlayout2.addWidget(self.saveAfterAddingNum,2,1,1,1)

        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridlayout2.addWidget(self.label_7,2,2,1,1)
        self.vboxlayout3.addLayout(self.gridlayout2)

        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setWordWrap(True)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName("label_16")
        self.vboxlayout3.addWidget(self.label_16)

        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.gridlayout3.addWidget(self.label_18,1,0,1,1)

        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridlayout3.addWidget(self.label_17,0,0,1,1)

        self.syncUser = QtGui.QLineEdit(self.tab_2)
        self.syncUser.setObjectName("syncUser")
        self.gridlayout3.addWidget(self.syncUser,0,1,1,1)

        self.syncOnClose = QtGui.QCheckBox(self.tab_2)
        self.syncOnClose.setChecked(True)
        self.syncOnClose.setObjectName("syncOnClose")
        self.gridlayout3.addWidget(self.syncOnClose,3,0,1,1)

        self.syncPass = QtGui.QLineEdit(self.tab_2)
        self.syncPass.setEchoMode(QtGui.QLineEdit.Password)
        self.syncPass.setObjectName("syncPass")
        self.gridlayout3.addWidget(self.syncPass,1,1,1,1)

        self.syncOnOpen = QtGui.QCheckBox(self.tab_2)
        self.syncOnOpen.setChecked(True)
        self.syncOnOpen.setObjectName("syncOnOpen")
        self.gridlayout3.addWidget(self.syncOnOpen,2,0,1,1)
        self.vboxlayout3.addLayout(self.gridlayout3)
        self.hboxlayout1.addLayout(self.vboxlayout3)
        self.vboxlayout2.addLayout(self.hboxlayout1)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2,"")

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setObjectName("gridlayout4")

        self.showToolbar = QtGui.QCheckBox(self.tab_3)
        self.showToolbar.setObjectName("showToolbar")
        self.gridlayout4.addWidget(self.showToolbar,1,0,1,1)

        self.compactEaseButtons = QtGui.QCheckBox(self.tab_3)
        self.compactEaseButtons.setObjectName("compactEaseButtons")
        self.gridlayout4.addWidget(self.compactEaseButtons,2,0,1,1)

        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridlayout4.addWidget(self.label_6,0,0,1,1)

        self.tallButtons = QtGui.QCheckBox(self.tab_3)
        self.tallButtons.setObjectName("tallButtons")
        self.gridlayout4.addWidget(self.tallButtons,3,0,1,1)
        self.vboxlayout4.addLayout(self.gridlayout4)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Preferences.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Preferences.reject)
        QtCore.QObject.connect(self.saveAfterEvery,QtCore.SIGNAL("toggled(bool)"),self.saveAfterEveryNum.setEnabled)
        QtCore.QObject.connect(self.saveAfterAdding,QtCore.SIGNAL("toggled(bool)"),self.saveAfterAddingNum.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.tabWidget,self.interfaceLang)
        Preferences.setTabOrder(self.interfaceLang,self.interfaceFamily)
        Preferences.setTabOrder(self.interfaceFamily,self.interfaceSize)
        Preferences.setTabOrder(self.interfaceSize,self.lastCardFamily)
        Preferences.setTabOrder(self.lastCardFamily,self.lastCardSize)
        Preferences.setTabOrder(self.lastCardSize,self.editFamily)
        Preferences.setTabOrder(self.editFamily,self.editSize)
        Preferences.setTabOrder(self.editSize,self.interfaceColour)
        Preferences.setTabOrder(self.interfaceColour,self.lastCardColour)
        Preferences.setTabOrder(self.lastCardColour,self.backgroundColour)
        Preferences.setTabOrder(self.backgroundColour,self.saveWhenClosing)
        Preferences.setTabOrder(self.saveWhenClosing,self.saveAfterEvery)
        Preferences.setTabOrder(self.saveAfterEvery,self.saveAfterEveryNum)
        Preferences.setTabOrder(self.saveAfterEveryNum,self.saveAfterAdding)
        Preferences.setTabOrder(self.saveAfterAdding,self.saveAfterAddingNum)
        Preferences.setTabOrder(self.saveAfterAddingNum,self.syncUser)
        Preferences.setTabOrder(self.syncUser,self.syncPass)
        Preferences.setTabOrder(self.syncPass,self.syncOnOpen)
        Preferences.setTabOrder(self.syncOnOpen,self.syncOnClose)
        Preferences.setTabOrder(self.syncOnClose,self.buttonBox)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_("Preferences"))
        self.label.setText(_("<h1>Interface language</h1>The language for the user interface: dialogs, menus, etc."))
        self.label_2.setText(_("<h1>Standard fonts</h1>See \'display properties\' for deck specific font preferences."))
        self.label_9.setText(_("Last card"))
        self.label_8.setText(_("Interface"))
        self.label_10.setText(_("Card editor"))
        self.label_3.setText(_("<h1>Standard colours</h1>These colours are used for all decks."))
        self.label_13.setText(_("Interface colour"))
        self.label_14.setText(_("Last card colour"))
        self.label_15.setText(_("Background colour"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _("Language, Fonts and Colours"))
        self.label_4.setText(_("<h1>Autosaving</h1>Anki can save your progress automatically."))
        self.saveAfterEvery.setText(_("Save after answering"))
        self.saveWhenClosing.setText(_("Save when closing"))
        self.label_5.setText(_("cards"))
        self.saveAfterAdding.setText(_("Save after adding"))
        self.label_7.setText(_("facts"))
        self.label_16.setText(_("<h1>Synchronisation</h1>Synchronisation enables you to access your deck from the web and your mobile phone. You can <a href=\"http://anki.ichi2.net/\">create a free account</a>."))
        self.label_18.setText(_("Password"))
        self.label_17.setText(_("Username"))
        self.syncOnClose.setText(_("Sync on close"))
        self.syncOnOpen.setText(_("Sync on open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Autosave and Synchronisation"))
        self.showToolbar.setText(_("Show toolbar on startup"))
        self.compactEaseButtons.setText(_("Use compact answer button style"))
        self.label_6.setText(_("<h1>Advanced settings</h1>"))
        self.tallButtons.setText(_("Tall buttons (for touchscreen)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("Advanced Settings"))

