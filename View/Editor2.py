# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/Editor2.ui'
#
# Created: Wed Sep 04 04:50:46 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(865, 778)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Circulation simulator", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/heart_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_newnode = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_newnode.setObjectName(_fromUtf8("lineEdit_newnode"))
        self.horizontalLayout.addWidget(self.lineEdit_newnode)
        self.pushButton_addNode = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addNode.setText(QtGui.QApplication.translate("MainWindow", "Add node", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/accepted_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_addNode.setIcon(icon1)
        self.pushButton_addNode.setObjectName(_fromUtf8("pushButton_addNode"))
        self.horizontalLayout.addWidget(self.pushButton_addNode)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_distribution = QtGui.QComboBox(self.centralwidget)
        self.comboBox_distribution.setObjectName(_fromUtf8("comboBox_distribution"))
        self.horizontalLayout_2.addWidget(self.comboBox_distribution)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Loc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.doubleSpinBox_loc = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_loc.setObjectName(_fromUtf8("doubleSpinBox_loc"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_loc)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.doubleSpinBox_scale = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_scale.setObjectName(_fromUtf8("doubleSpinBox_scale"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_scale)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Smth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_smth = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_smth.setObjectName(_fromUtf8("doubleSpinBox_smth"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_smth)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView_nodes = QtGui.QTableView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_nodes.sizePolicy().hasHeightForWidth())
        self.tableView_nodes.setSizePolicy(sizePolicy)
        self.tableView_nodes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView_nodes.setObjectName(_fromUtf8("tableView_nodes"))
        self.tableView_nodes.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_nodes.horizontalHeader().setDefaultSectionSize(40)
        self.tableView_nodes.horizontalHeader().setMinimumSectionSize(1)
        self.tableView_nodes.verticalHeader().setCascadingSectionResizes(False)
        self.tableView_nodes.verticalHeader().setDefaultSectionSize(30)
        self.tableView_nodes.verticalHeader().setMinimumSectionSize(2)
        self.verticalLayout.addWidget(self.tableView_nodes)
        self.pushButton_removeNode = QtGui.QPushButton(self.centralwidget)
        self.pushButton_removeNode.setText(QtGui.QApplication.translate("MainWindow", "Remove node", None, QtGui.QApplication.UnicodeUTF8))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/cancel_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_removeNode.setIcon(icon2)
        self.pushButton_removeNode.setObjectName(_fromUtf8("pushButton_removeNode"))
        self.verticalLayout.addWidget(self.pushButton_removeNode)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox_nodesForPrecessor = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_nodesForPrecessor.sizePolicy().hasHeightForWidth())
        self.comboBox_nodesForPrecessor.setSizePolicy(sizePolicy)
        self.comboBox_nodesForPrecessor.setObjectName(_fromUtf8("comboBox_nodesForPrecessor"))
        self.horizontalLayout_3.addWidget(self.comboBox_nodesForPrecessor)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.doubleSpinBox_weight = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_weight.setMaximum(1.0)
        self.doubleSpinBox_weight.setSingleStep(0.1)
        self.doubleSpinBox_weight.setProperty("value", 1.0)
        self.doubleSpinBox_weight.setObjectName(_fromUtf8("doubleSpinBox_weight"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_weight)
        self.pushButton_addPrecessor = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addPrecessor.setText(QtGui.QApplication.translate("MainWindow", "Add precessor", None, QtGui.QApplication.UnicodeUTF8))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/arrow_right_green_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_addPrecessor.setIcon(icon3)
        self.pushButton_addPrecessor.setObjectName(_fromUtf8("pushButton_addPrecessor"))
        self.horizontalLayout_3.addWidget(self.pushButton_addPrecessor)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView_edges = QtGui.QTableView(self.centralwidget)
        self.tableView_edges.setObjectName(_fromUtf8("tableView_edges"))
        self.verticalLayout.addWidget(self.tableView_edges)
        self.pushButton_removePred = QtGui.QPushButton(self.centralwidget)
        self.pushButton_removePred.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removePred.setObjectName(_fromUtf8("pushButton_removePred"))
        self.verticalLayout.addWidget(self.pushButton_removePred)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_graph = QtGui.QWidget()
        self.tab_graph.setObjectName(_fromUtf8("tab_graph"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_graph)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mpl_graph = MplWidget(self.tab_graph)
        self.mpl_graph.setObjectName(_fromUtf8("mpl_graph"))
        self.verticalLayout_3.addWidget(self.mpl_graph)
        self.comboBox_graphlayout = QtGui.QComboBox(self.tab_graph)
        self.comboBox_graphlayout.setObjectName(_fromUtf8("comboBox_graphlayout"))
        self.verticalLayout_3.addWidget(self.comboBox_graphlayout)
        self.pushButton_redraw = QtGui.QPushButton(self.tab_graph)
        self.pushButton_redraw.setText(QtGui.QApplication.translate("MainWindow", "Redraw", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_redraw.setObjectName(_fromUtf8("pushButton_redraw"))
        self.verticalLayout_3.addWidget(self.pushButton_redraw)
        self.tabWidget.addTab(self.tab_graph, _fromUtf8(""))
        self.tab_simulation = QtGui.QWidget()
        self.tab_simulation.setObjectName(_fromUtf8("tab_simulation"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_simulation)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mpl_concentration = MplWidget(self.tab_simulation)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_concentration.sizePolicy().hasHeightForWidth())
        self.mpl_concentration.setSizePolicy(sizePolicy)
        self.mpl_concentration.setObjectName(_fromUtf8("mpl_concentration"))
        self.verticalLayout_2.addWidget(self.mpl_concentration)
        self.listView_nodestodraw = QtGui.QListView(self.tab_simulation)
        self.listView_nodestodraw.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_nodestodraw.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listView_nodestodraw.setSelectionRectVisible(True)
        self.listView_nodestodraw.setObjectName(_fromUtf8("listView_nodestodraw"))
        self.verticalLayout_2.addWidget(self.listView_nodestodraw)
        self.pushButton_simulate = QtGui.QPushButton(self.tab_simulation)
        self.pushButton_simulate.setText(QtGui.QApplication.translate("MainWindow", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_simulate.setObjectName(_fromUtf8("pushButton_simulate"))
        self.verticalLayout_2.addWidget(self.pushButton_simulate)
        self.checkBox = QtGui.QCheckBox(self.tab_simulation)
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "simulate ,  some parametrs changed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_simulation, _fromUtf8(""))
        self.tab_profiles = QtGui.QWidget()
        self.tab_profiles.setObjectName(_fromUtf8("tab_profiles"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_profiles)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.mpl_profiles = MplWidget(self.tab_profiles)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_profiles.sizePolicy().hasHeightForWidth())
        self.mpl_profiles.setSizePolicy(sizePolicy)
        self.mpl_profiles.setObjectName(_fromUtf8("mpl_profiles"))
        self.verticalLayout_6.addWidget(self.mpl_profiles)
        self.listView_profilestodraw = QtGui.QListView(self.tab_profiles)
        self.listView_profilestodraw.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_profilestodraw.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listView_profilestodraw.setSelectionRectVisible(True)
        self.listView_profilestodraw.setObjectName(_fromUtf8("listView_profilestodraw"))
        self.verticalLayout_6.addWidget(self.listView_profilestodraw)
        self.tabWidget.addTab(self.tab_profiles, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "aim graph", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "use simulated", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_7.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "input new", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_7.addWidget(self.radioButton_2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.tableView = QtGui.QTableView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 5))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 60))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 4, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "izotrope", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.spinBox_time = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_time.setMaximum(1000)
        self.spinBox_time.setSingleStep(10)
        self.spinBox_time.setProperty("value", 10)
        self.spinBox_time.setObjectName(_fromUtf8("spinBox_time"))
        self.horizontalLayout_6.addWidget(self.spinBox_time)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Time resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.doubleSpinBox_timeres = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_timeres.setMinimum(0.01)
        self.doubleSpinBox_timeres.setProperty("value", 1.0)
        self.doubleSpinBox_timeres.setObjectName(_fromUtf8("doubleSpinBox_timeres"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_timeres)
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setText(QtGui.QApplication.translate("MainWindow", "manual", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_6.addWidget(self.radioButton_4)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/add_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon4)
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("MainWindow", "Create new graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionLoad = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/folder_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon5)
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setToolTip(QtGui.QApplication.translate("MainWindow", "Load graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/floppy_disk_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "Save graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSnap_graph = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/camera_noflash_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSnap_graph.setIcon(icon7)
        self.actionSnap_graph.setText(QtGui.QApplication.translate("MainWindow", "Snap graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnap_graph.setToolTip(QtGui.QApplication.translate("MainWindow", "Save snapshot of the curent visualisation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnap_graph.setObjectName(_fromUtf8("actionSnap_graph"))
        self.actionExport_pics = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/src/box_download_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_pics.setIcon(icon8)
        self.actionExport_pics.setText(QtGui.QApplication.translate("MainWindow", "Export pics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_pics.setObjectName(_fromUtf8("actionExport_pics"))
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSnap_graph)
        self.toolBar.addAction(self.actionExport_pics)
        self.label.setBuddy(self.doubleSpinBox_loc)
        self.label_2.setBuddy(self.doubleSpinBox_scale)
        self.label_3.setBuddy(self.doubleSpinBox_smth)
        self.label_5.setBuddy(self.doubleSpinBox_weight)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_graph), QtGui.QApplication.translate("MainWindow", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simulation), QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profiles), QtGui.QApplication.translate("MainWindow", "Profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Fitting", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
import icons_rc
