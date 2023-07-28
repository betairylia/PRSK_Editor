# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SekaiText(object):
    def setupUi(self, SekaiText):
        SekaiText.setObjectName("Sekai Text")
        SekaiText.resize(1024, 1024)

        font = QtGui.QFont()
        font.setFamily("SimHei")

        self.centralwidget = QtWidgets.QWidget(SekaiText)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.comboBoxStoryType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStoryType.setMinimumSize(QtCore.QSize(130, 30))
        self.comboBoxStoryType.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBoxStoryType.setObjectName("comboBoxStoryType")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.comboBoxStoryType.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxStoryType)

        self.comboBoxStoryTypeSort = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStoryTypeSort.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxStoryTypeSort.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBoxStoryTypeSort.setObjectName("comboBoxStoryTypeSort")
        self.horizontalLayout.addWidget(self.comboBoxStoryTypeSort)
        self.comboBoxStoryTypeSort.setVisible(False)

        self.comboBoxStoryIndex = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStoryIndex.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxStoryIndex.setMaximumSize(QtCore.QSize(680, 30))
        self.comboBoxStoryIndex.setMaxVisibleItems(20)
        self.comboBoxStoryIndex.setObjectName("comboBoxStoryIndex")
        self.horizontalLayout.addWidget(self.comboBoxStoryIndex)

        self.comboBoxStoryChapter = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStoryChapter.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxStoryChapter.setMaximumSize(QtCore.QSize(550, 30))
        self.comboBoxStoryChapter.setMaxVisibleItems(20)
        self.comboBoxStoryChapter.setObjectName("comboBoxStoryChapter")
        self.horizontalLayout.addWidget(self.comboBoxStoryChapter)

        self.pushButtonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRefresh.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.horizontalLayout.addWidget(self.pushButtonRefresh)

        self.label_1e = QtWidgets.QLabel(self.centralwidget)
        self.label_1e.setFixedSize(QtCore.QSize(5, 30))
        self.label_1e.setText("")
        self.label_1e.setObjectName("label_1e")
        self.horizontalLayout.addWidget(self.label_1e)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_3f = QtWidgets.QLabel(self.centralwidget)
        self.label_3f.setFixedSize(QtCore.QSize(5, 30))
        self.label_3f.setText("")
        self.label_3f.setObjectName("label_3f")
        self.horizontalLayout_3.addWidget(self.label_3f)

        self.radioButtonTranslate = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonTranslate.setFixedSize(QtCore.QSize(70, 30))
        self.radioButtonTranslate.setObjectName("radioButtonTranslate")
        self.horizontalLayout_3.addWidget(self.radioButtonTranslate)

        self.radioButtonProofread = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonProofread.setFixedSize(QtCore.QSize(70, 30))
        self.radioButtonProofread.setObjectName("radioButtonProofread")
        self.horizontalLayout_3.addWidget(self.radioButtonProofread)

        self.radioButtonCheck = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonCheck.setFixedSize(QtCore.QSize(70, 30))
        self.radioButtonCheck.setObjectName("radioButtonCheck")
        self.horizontalLayout_3.addWidget(self.radioButtonCheck)

        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout_3.addWidget(self.pushButtonOpen)

        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_3.addWidget(self.pushButtonSave)

        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonClear.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButtonClear)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        self.checkBoxShowDiff = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxShowDiff.setFixedSize(QtCore.QSize(160, 30))
        self.checkBoxShowDiff.setObjectName("checkBoxShowDiff")
        self.horizontalLayout_3.addWidget(self.checkBoxShowDiff)

        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.labelDataSrc = QtWidgets.QLabel(self.centralwidget)
        self.labelDataSrc.setFixedSize(QtCore.QSize(80, 30))
        self.labelDataSrc.setObjectName("labelDataSrc")
        self.horizontalLayout_2.addWidget(self.labelDataSrc)

        self.comboBoxDataSource = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxDataSource.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBoxDataSource.setMaximumSize(QtCore.QSize(230, 30))
        self.comboBoxDataSource.setObjectName("comboBoxDataSource")
        self.horizontalLayout_2.addWidget(self.comboBoxDataSource)

        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout_2.addWidget(self.pushButtonLoad)

        self.checkBoxJapanese = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxJapanese.setFixedSize(QtCore.QSize(110, 30))
        self.checkBoxJapanese.setObjectName("checkBoxJapanese")
        self.horizontalLayout_2.addWidget(self.checkBoxJapanese)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButtonCount = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCount.setFixedSize(QtCore.QSize(100, 30))
        self.pushButtonCount.setObjectName("pushButtonCount")
        self.horizontalLayout_2.addWidget(self.pushButtonCount)

        self.checkBoxAll = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAll.setFixedSize(QtCore.QSize(100, 30))
        self.checkBoxAll.setObjectName("checkBoxAll")
        self.horizontalLayout_2.addWidget(self.checkBoxAll)

        self.label_2e = QtWidgets.QLabel(self.centralwidget)
        self.label_2e.setFixedSize(QtCore.QSize(10, 30))
        self.label_2e.setText("")
        self.label_2e.setObjectName("label_4f")
        self.horizontalLayout_2.addWidget(self.label_2e)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_4f = QtWidgets.QLabel(self.centralwidget)
        self.label_4f.setFixedSize(QtCore.QSize(5, 30))
        self.label_4f.setText("")
        self.label_4f.setObjectName("label_4f")
        self.horizontalLayout_4.addWidget(self.label_4f)

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setFixedSize(QtCore.QSize(50, 30))
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout_4.addWidget(self.labelTitle)

        self.lineEditTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTitle.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEditTitle.setMaximumSize(QtCore.QSize(380, 30))
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.horizontalLayout_4.addWidget(self.lineEditTitle)

        self.pushButtonSpeaker = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSpeaker.setFixedSize(QtCore.QSize(100, 30))
        self.pushButtonSpeaker.setObjectName("pushButtonSpeaker")
        self.horizontalLayout_4.addWidget(self.pushButtonSpeaker)

        self.pushButtonCheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCheck.setFixedSize(QtCore.QSize(60, 30))
        self.pushButtonCheck.setObjectName("pushButtonCheck")
        self.horizontalLayout_4.addWidget(self.pushButtonCheck)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.checkBoxSaveN = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSaveN.setFixedSize(QtCore.QSize(160, 30))
        self.checkBoxSaveN.setObjectName("checkBoxSaveN")
        self.horizontalLayout_4.addWidget(self.checkBoxSaveN)

        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.tableWidgetSrc = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetSrc.setFont(font)
        self.tableWidgetSrc.setMinimumSize(QtCore.QSize(300, 500))
        self.tableWidgetSrc.setMaximumSize(QtCore.QSize(900, 16777215))
        self.tableWidgetSrc.setObjectName("tableWidgetSrc")
        self.tableWidgetSrc.setColumnCount(2)
        self.tableWidgetSrc.setRowCount(0)
        self.tableWidgetSrc.horizontalHeader().hide()
        self.tableWidgetSrc.horizontalHeader().resizeSection(0, 120)
        self.tableWidgetSrc.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # self.tableWidgetSrc.horizontalHeader().resizeSection(2, 60)
        self.tableWidgetSrc.setIconSize(QtCore.QSize(48,48))
        self.gridLayout.addWidget(self.tableWidgetSrc, 2, 0, 1, 1)

        self.tableWidgetDst = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetDst.setFont(font)
        self.tableWidgetDst.setMinimumSize(QtCore.QSize(300, 500))
        self.tableWidgetDst.setObjectName("tableWidgetDst")
        self.tableWidgetDst.setColumnCount(4)
        self.tableWidgetDst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDst.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDst.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDst.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDst.setHorizontalHeaderItem(3, item)
        self.tableWidgetDst.horizontalHeader().resizeSection(0, 50)
        self.tableWidgetDst.horizontalHeader().resizeSection(1, 100)
        self.tableWidgetDst.horizontalHeader().resizeSection(2, 500)
        self.tableWidgetDst.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetDst.horizontalHeader().resizeSection(3, 100)
        self.tableWidgetDst.verticalHeader().hide()
        self.gridLayout.addWidget(self.tableWidgetDst, 2, 1, 1, 1)

        SekaiText.setCentralWidget(self.centralwidget)
        '''
        self.menubar = QtWidgets.QMenuBar(SekaiText)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        SekaiText.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SekaiText)
        self.statusbar.setObjectName("statusbar")
        SekaiText.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(SekaiText)
        self.action.setObjectName("action")
        self.actiondas = QtWidgets.QAction(SekaiText)
        self.actiondas.setObjectName("actiondas")
        self.actionload = QtWidgets.QAction(SekaiText)
        self.actionload.setObjectName("actionload")
        self.actionSave = QtWidgets.QAction(SekaiText)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(SekaiText)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(SekaiText)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(SekaiText)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(SekaiText)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(SekaiText)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(SekaiText)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(SekaiText)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(SekaiText)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFind = QtWidgets.QAction(SekaiText)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next = QtWidgets.QAction(SekaiText)
        self.actionFind_Next.setObjectName("actionFind_Next")
        self.actionFind_Previous = QtWidgets.QAction(SekaiText)
        self.actionFind_Previous.setObjectName("actionFind_Previous")
        self.actionReplace = QtWidgets.QAction(SekaiText)
        self.actionReplace.setObjectName("actionReplace")
        self.actionFont = QtWidgets.QAction(SekaiText)
        self.actionFont.setObjectName("actionFont")
        self.actionAbout = QtWidgets.QAction(SekaiText)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCache = QtWidgets.QAction(SekaiText)
        self.actionCache.setObjectName("actionCache")
        self.actionClear_Cache = QtWidgets.QAction(SekaiText)
        self.actionClear_Cache.setObjectName("actionClear_Cache")
        self.actionData_Path = QtWidgets.QAction(SekaiText)
        self.actionData_Path.setObjectName("actionData_Path")
        self.menu.addAction(self.action)
        self.menu.addAction(self.actiondas)
        self.menu.addAction(self.actionload)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSave_As)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionUndo)
        self.menu_2.addAction(self.actionRedo)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionCut)
        self.menu_2.addAction(self.actionCopy)
        self.menu_2.addAction(self.actionPaste)
        self.menu_2.addAction(self.actionDelete)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionFind)
        self.menu_2.addAction(self.actionFind_Next)
        self.menu_2.addAction(self.actionFind_Previous)
        self.menu_2.addAction(self.actionReplace)
        self.menu_3.addAction(self.actionFont)
        self.menu_4.addAction(self.actionAbout)
        self.menu_5.addAction(self.actionData_Path)
        self.menu_5.addAction(self.actionCache)
        self.menu_5.addAction(self.actionClear_Cache)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        '''
        self.retranslateUi(SekaiText)
        QtCore.QMetaObject.connectSlotsByName(SekaiText)

    def retranslateUi(self, SekaiText):
        _translate = QtCore.QCoreApplication.translate
        SekaiText.setWindowTitle(_translate("SekaiText", "Sekai Text"))
        self.comboBoxStoryType.setItemText(0, _translate("SekaiText", u"主线剧情"))
        self.comboBoxStoryType.setItemText(1, _translate("SekaiText", u"活动剧情"))
        self.comboBoxStoryType.setItemText(2, _translate("SekaiText", u"活动卡面"))
        self.comboBoxStoryType.setItemText(3, _translate("SekaiText", u"特殊卡面"))
        self.comboBoxStoryType.setItemText(4, _translate("SekaiText", u"初始卡面"))
        self.comboBoxStoryType.setItemText(5, _translate("SekaiText", u"初始地图对话"))
        self.comboBoxStoryType.setItemText(6, _translate("SekaiText", u"追加地图对话"))
        self.comboBoxStoryType.setItemText(7, _translate("SekaiText", u"主界面语音"))
        self.comboBoxStoryType.setItemText(8, _translate("SekaiText", u"特殊剧情"))
        self.comboBoxStoryType.setItemText(9, _translate("SekaiText", u"自定义"))
        self.comboBoxStoryType.setCurrentText(_translate("SekaiText", u"活动剧情"))
        self.pushButtonRefresh.setText(_translate("SekaiText", u"更新"))
        self.radioButtonTranslate.setText(_translate("SekaiText", u"翻译"))
        self.radioButtonProofread.setText(_translate("SekaiText", u"校对"))
        self.radioButtonCheck.setText(_translate("SekaiText", u"合意"))
        self.pushButtonOpen.setText(_translate("SekaiText", u"打开"))
        self.pushButtonSave.setText(_translate("SekaiText", u"保存"))
        self.pushButtonClear.setText(_translate("SekaiText", u"清空"))
        self.checkBoxShowDiff.setText(_translate("SekaiText", u"显示修改前内容"))
        self.radioButtonTranslate.setChecked(True)
        # self.pushButtonCheck_2.setText(_translate("SekaiText", u"名词表"))
        self.labelDataSrc.setText(_translate("SekaiText", u"数据来源："))
        self.pushButtonLoad.setText(_translate("SekaiText", u"载入"))
        self.checkBoxJapanese.setText(_translate("SekaiText", u"生成日文"))
        self.pushButtonCount.setText(_translate("SekaiText", u"统计说话人"))
        self.checkBoxAll.setText(_translate("SekaiText", u"全部章节"))
        self.labelTitle.setText(_translate("SekaiText", u"标题："))
        self.pushButtonSpeaker.setText(_translate("SekaiText", u"检查说话人"))
        self.pushButtonCheck.setText(_translate("SekaiText", u"检查"))
        self.checkBoxSaveN.setText(_translate("SekaiText", u"保存换行符\\N"))
        self.checkBoxSaveN.setChecked(True)
        item = self.tableWidgetDst.horizontalHeaderItem(0)
        item.setText(_translate("SekaiText", u"行号"))
        item = self.tableWidgetDst.horizontalHeaderItem(1)
        item.setText(_translate("SekaiText", u"说话人"))
        item = self.tableWidgetDst.horizontalHeaderItem(2)
        item.setText(_translate("SekaiText", u"内容文本"))
        item = self.tableWidgetDst.horizontalHeaderItem(3)
        item.setText(_translate("SekaiText", u"换行"))
        '''
        self.menu.setTitle(_translate("SekaiText", "File"))
        self.menu_2.setTitle(_translate("SekaiText", "Edit"))
        self.menu_3.setTitle(_translate("SekaiText", "View"))
        self.menu_4.setTitle(_translate("SekaiText", "Help"))
        self.menu_5.setTitle(_translate("SekaiText", "Setting"))
        self.action.setText(_translate("SekaiText", "New"))
        self.actiondas.setText(_translate("SekaiText", "New Window"))
        self.actionload.setText(_translate("SekaiText", "Open ..."))
        self.actionSave.setText(_translate("SekaiText", "Save"))
        self.actionSave_As.setText(_translate("SekaiText", "Save as ..."))
        self.actionExit.setText(_translate("SekaiText", "Exit"))
        self.actionUndo.setText(_translate("SekaiText", "Undo"))
        self.actionRedo.setText(_translate("SekaiText", "Redo"))
        self.actionCut.setText(_translate("SekaiText", "Cut"))
        self.actionCopy.setText(_translate("SekaiText", "Copy"))
        self.actionPaste.setText(_translate("SekaiText", "Paste"))
        self.actionDelete.setText(_translate("SekaiText", "Delete"))
        self.actionFind.setText(_translate("SekaiText", "Find"))
        self.actionFind_Next.setText(_translate("SekaiText", "Find Next"))
        self.actionFind_Previous.setText(_translate("SekaiText", "Find \n"
"Previous"))
        self.actionReplace.setText(_translate("SekaiText", "Replace"))
        self.actionFont.setText(_translate("SekaiText", "Font"))
        self.actionAbout.setText(_translate("SekaiText", "About"))
        self.actionCache.setText(_translate("SekaiText", "Cache Path"))
        self.actionClear_Cache.setText(_translate("SekaiText", "Clear Cache"))
        self.actionData_Path.setText(_translate("SekaiText", "Data Path"))
        '''
