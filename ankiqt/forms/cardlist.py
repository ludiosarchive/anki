# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/cardlist.ui'
#

#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 462)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(4, 0, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hlayout1 = QtGui.QHBoxLayout()
        self.hlayout1.setSpacing(4)
        self.hlayout1.setContentsMargins(0, 0, 0, 4)
        self.hlayout1.setObjectName("hlayout1")
        self.filterEdit = QtGui.QLineEdit(self.centralwidget)
        self.filterEdit.setObjectName("filterEdit")
        self.hlayout1.addWidget(self.filterEdit)
        self.tagList = QtGui.QComboBox(self.centralwidget)
        self.tagList.setObjectName("tagList")
        self.hlayout1.addWidget(self.tagList)
        self.sortBox = QtGui.QComboBox(self.centralwidget)
        self.sortBox.setObjectName("sortBox")
        self.hlayout1.addWidget(self.sortBox)
        self.verticalLayout.addLayout(self.hlayout1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView = QtGui.QTableView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableView.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableView.setFrameShadow(QtGui.QFrame.Plain)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter2 = QtGui.QSplitter(self.frame)
        self.splitter2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter2.setObjectName("splitter2")
        self.fieldsArea = QtGui.QWidget(self.splitter2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setObjectName("fieldsArea")
        self.cardInfoGroup = QtGui.QGroupBox(self.splitter2)
        self.cardInfoGroup.setObjectName("cardInfoGroup")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.cardInfoGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cardLabel = QtGui.QLabel(self.cardInfoGroup)
        self.cardLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cardLabel.setObjectName("cardLabel")
        self.verticalLayout_4.addWidget(self.cardLabel)
        self.verticalLayout_2.addWidget(self.splitter2)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuJump = QtGui.QMenu(self.menubar)
        self.menuJump.setObjectName("menuJump")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.actionDelete = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/editdelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAddTag = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Anki_Add_Tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddTag.setIcon(icon2)
        self.actionAddTag.setObjectName("actionAddTag")
        self.actionDeleteTag = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Anki_Del_Tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteTag.setIcon(icon3)
        self.actionDeleteTag.setObjectName("actionDeleteTag")
        self.actionAddCards = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Anki_Card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddCards.setIcon(icon4)
        self.actionAddCards.setObjectName("actionAddCards")
        self.actionReschedule = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReschedule.setIcon(icon5)
        self.actionReschedule.setObjectName("actionReschedule")
        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setIcon(icon5)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon6)
        self.actionRedo.setObjectName("actionRedo")
        self.actionInvertSelection = QtGui.QAction(MainWindow)
        self.actionInvertSelection.setObjectName("actionInvertSelection")
        self.actionFind = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/document-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon7)
        self.actionFind.setObjectName("actionFind")
        self.actionFact = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/Anki_Fact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFact.setIcon(icon8)
        self.actionFact.setObjectName("actionFact")
        self.actionNextCard = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNextCard.setIcon(icon9)
        self.actionNextCard.setObjectName("actionNextCard")
        self.actionPreviousCard = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreviousCard.setIcon(icon10)
        self.actionPreviousCard.setObjectName("actionPreviousCard")
        self.actionFirstCard = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/go-first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirstCard.setIcon(icon11)
        self.actionFirstCard.setObjectName("actionFirstCard")
        self.actionLastCard = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/go-last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLastCard.setIcon(icon12)
        self.actionLastCard.setObjectName("actionLastCard")
        self.actionReverseOrder = QtGui.QAction(MainWindow)
        self.actionReverseOrder.setCheckable(True)
        self.actionReverseOrder.setObjectName("actionReverseOrder")
        self.actionGuide = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuide.setIcon(icon13)
        self.actionGuide.setObjectName("actionGuide")
        self.actionChangeModel = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/system-software-update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeModel.setIcon(icon14)
        self.actionChangeModel.setObjectName("actionChangeModel")
        self.actionSelectFacts = QtGui.QAction(MainWindow)
        self.actionSelectFacts.setObjectName("actionSelectFacts")
        self.actionFindReplace = QtGui.QAction(MainWindow)
        self.actionFindReplace.setObjectName("actionFindReplace")
        self.actionCram = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/view-pim-calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCram.setIcon(icon15)
        self.actionCram.setObjectName("actionCram")
        self.actionFont = QtGui.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionSelectFacts)
        self.menuEdit.addAction(self.actionInvertSelection)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFindReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionReverseOrder)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFont)
        self.menuActions.addAction(self.actionAddTag)
        self.menuActions.addAction(self.actionDeleteTag)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionAddCards)
        self.menuActions.addAction(self.actionChangeModel)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionCram)
        self.menuActions.addAction(self.actionReschedule)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionDelete)
        self.menuJump.addAction(self.actionFind)
        self.menuJump.addAction(self.actionFact)
        self.menuJump.addSeparator()
        self.menuJump.addAction(self.actionFirstCard)
        self.menuJump.addAction(self.actionPreviousCard)
        self.menuJump.addAction(self.actionNextCard)
        self.menuJump.addAction(self.actionLastCard)
        self.menu_Help.addAction(self.actionGuide)
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuJump.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSelectAll, QtCore.SIGNAL("triggered()"), self.tableView.selectAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_("Browse Items"))
        self.cardInfoGroup.setTitle(_("Current Card"))
        self.menuEdit.setTitle(_("&Edit"))
        self.menuActions.setTitle(_("&Actions"))
        self.menuJump.setTitle(_("&Go"))
        self.menu_Help.setTitle(_("&Help"))
        self.actionDelete.setText(_("Delete"))
        self.actionDelete.setShortcut(_("Ctrl+Del"))
        self.actionAddTag.setText(_("&Add Tag..."))
        self.actionDeleteTag.setText(_("&Delete Tag..."))
        self.actionAddCards.setText(_("&Generate Cards..."))
        self.actionReschedule.setText(_("&Reschedule..."))
        self.actionSelectAll.setText(_("Select &All"))
        self.actionUndo.setText(_("&Undo"))
        self.actionRedo.setText(_("&Redo"))
        self.actionInvertSelection.setText(_("&Invert Selection"))
        self.actionFind.setText(_("&Find"))
        self.actionFind.setShortcut(_("Ctrl+F"))
        self.actionFact.setText(_("F&act"))
        self.actionFact.setShortcut(_("Ctrl+Shift+F"))
        self.actionNextCard.setText(_("&Next Card"))
        self.actionNextCard.setShortcut(_("Ctrl+N"))
        self.actionPreviousCard.setText(_("&Previous Card"))
        self.actionPreviousCard.setShortcut(_("Ctrl+P"))
        self.actionFirstCard.setText(_("F&irst Card"))
        self.actionFirstCard.setShortcut(_("Ctrl+Home"))
        self.actionLastCard.setText(_("&Last Card"))
        self.actionLastCard.setShortcut(_("Ctrl+End"))
        self.actionReverseOrder.setText(_("Reverse &Order"))
        self.actionGuide.setText(_("&Guide..."))
        self.actionChangeModel.setText(_("Change &Model..."))
        self.actionSelectFacts.setText(_("Select &Facts"))
        self.actionFindReplace.setText(_("Find and Re&place..."))
        self.actionCram.setText(_("&Cram..."))
        self.actionFont.setText(_("Font..."))

import icons_rc
