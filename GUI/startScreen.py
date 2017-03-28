# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(352, 289)
        mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Resource_Files/googledev.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 251, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioInstall = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioInstall.setObjectName(_fromUtf8("radioInstall"))
        self.verticalLayout.addWidget(self.radioInstall)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.radioUpdate = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioUpdate.setObjectName(_fromUtf8("radioUpdate"))
        self.verticalLayout.addWidget(self.radioUpdate)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.radioUninstall = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioUninstall.setObjectName(_fromUtf8("radioUninstall"))
        self.verticalLayout.addWidget(self.radioUninstall)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 160, 188, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnNext = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.horizontalLayout.addWidget(self.btnNext)
        self.btnExit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout.addWidget(self.btnExit)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPIP_GUI = QtGui.QAction(mainWindow)
        self.actionPIP_GUI.setObjectName(_fromUtf8("actionPIP_GUI"))
        self.actionRefresh = QtGui.QAction(mainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "PIP GUI", None))
        self.label.setText(_translate("mainWindow", "What do you wanna do?", None))
        self.radioInstall.setText(_translate("mainWindow", "Install new packages", None))
        self.radioUpdate.setText(_translate("mainWindow", "Update existing packages", None))
        self.radioUninstall.setText(_translate("mainWindow", "Uninstall existing packages", None))
        self.btnNext.setText(_translate("mainWindow", "Next", None))
        self.btnExit.setText(_translate("mainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.actionExit.setText(_translate("mainWindow", "Exit", None))
        self.actionPIP_GUI.setText(_translate("mainWindow", "PIP GUI", None))
        self.actionRefresh.setText(_translate("mainWindow", "Refresh Lists", None))

