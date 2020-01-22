#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# Importing GUIs
try:
    from pipgui.GUI import startScreen, progressScreen, uninstallScreen, \
        updateScreen, installScreen
except BaseException:
    from GUI import startScreen, progressScreen, uninstallScreen, \
        updateScreen, installScreen

# from Scraping import genreList, packageList

__version__ = "1.1"

VERSION = 0
FILEVERSION = ''
Yes = QtWidgets.QMessageBox.Yes


class ProgressWindow(QtWidgets.QMainWindow, progressScreen.Ui_Form):
    
    """This class is for showing the progress of all the events happening in the interface"""
    
    def __init__(self):

        super(ProgressWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('Resource_Files/googledev.png'))
        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)
        self.process.started.connect(
            lambda: self.btnContinue.setEnabled(False))
        self.process.finished.connect(
            lambda: self.btnContinue.setEnabled(True))
        self.process.finished.connect(self.onFinished)
        self.btnContinue.clicked.connect(self.continueFn)

    def continueFn(self):
        
        msgBox(self.msgInt)
        self.close()
        if self.msgInt == 1:
            self.install = InstallWindow()
            self.install.show()
        if self.msgInt == 2:
            self.update = UpdateWindow()
            self.update.show()
        if self.msgInt == 5:
            self.uninstall = UninstallWindow()
            self.uninstall.show()
        if self.msgInt == 6:
            self.window = MainWindow()
            self.window.show()

    def setLabelText(self, text):
        
        self.labelProgress.setText(text)

    def dataReady(self):
        
        str_data = str(self.process.readAll(), 'utf-8')
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str_data)
        self.textEdit.ensureCursorVisible()
        
    def onStart(self,ver,processList):
        
        self.progressBar.setRange(0,0)
        self.process.start(ver,processList)
        
    def onFinished(self):
        
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)

    def callProgram(self, ver, processList, x):
        
        self.msgInt = x
        if x == 1:
            self.onStart(ver,processList)
        if x == 2:
            tempList = list()
            tempList.append(processList[0])
            for i in processList[1:]:
                tempList.append(i)
                tempList.append('-U')
            self.onStart(ver,tempList)
        if x == 5:
            tempList = list()
            tempList.append(processList[0])
            for i in processList[1:]:
                tempList.append(i)
                tempList.append('-y')
            self.onStart(ver,tempList)
            
        if x == 6:
            self.onStart(ver,processList)



def msgBox(x):
    
    """Function for defining various status message for actions"""
    
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Status Window")
    msg.setIcon(QtWidgets.QMessageBox.Information)

    if x == 1:
        msg.setText("Selected Packages have been installed.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 2:
        msg.setText('Selected Packages have been upgraded.')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 3:
        msg.setText('Are you sure you wanna uninstall?')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if x == 4:
        msg.setText('Uninstall Aborted.')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 5:
        msg.setText('Selected Packages have been uninstalled.')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 6:
        msg.setText('Lists Refreshed.')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 7:
        msg.setText('Are you sure you wanna exit?')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    return msg.exec_()





class MainWindow(startScreen.Ui_mainWindow, QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('Resource_Files/googledev.png'))
        # Check for python version
        if sys.version_info.major == 3:
            self.radioPy3.setChecked(True)
        elif sys.version_info.major == 2:
            self.radioPy2.setChecked(True)
        # Quiting the Application
        self.btnExit.clicked.connect(self.endApp)
        self.btnExit.setToolTip('Exit Application')
        self.actionExit.triggered.connect(self.endApp)
        self.actionExit.setStatusTip('Exit Application')
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionRefresh.triggered.connect(self.refreshLists)
        self.actionRefresh.setToolTip('Refresh Package Lists')
        self.actionRefresh.setShortcut('Ctrl+R')
        # Binding button to radio button result
        self.btnNext.clicked.connect(self.radioCheck)
    
    def pythonVersion(self):
        
        global VERSION
        global FILEVERSION
        if self.radioPy2.isChecked():
            VERSION = 'pip'
            FILEVERSION = 'List'
        if self.radioPy3.isChecked():
            VERSION = 'pip3'
            FILEVERSION = 'List3'

    def radioCheck(self):
        
        self.pythonVersion()  # Checking the version of python being used
        # Checking the radio button status
        if self.radioInstall.isChecked():
            self.close()
            self.install = InstallWindow()
            self.install.show()
        elif self.radioUpdate.isChecked():
            self.close()
            self.update = UpdateWindow()
            self.update.show()
        elif self.radioUninstall.isChecked():
            self.close()
            self.uninstall = UninstallWindow()
            self.uninstall.show()

    def refreshLists(self):
        
        self.progWindow = ProgressWindow()
        self.progWindow.setLabelText('Refreshing package list in progress…')
        self.close()
        self.progWindow.show()
        try:
            self.progWindow.callProgram('python',['refreshLists.py'], 6)
        except:
            self.progWindow.callProgram('python3',['refreshLists.py'], 6)
        
     
    def endApp(self):
        global Yes
        if msgBox(7) == Yes:
            app.quit()

    


class UpdateWindow(QtWidgets.QMainWindow, updateScreen.Ui_Form):
    
    """ This is a class for updation window. The updation window will show all the details 
    of updation of pip packages """
    
    global FILEVERSION
    global VERSION
    global outdatedPackages

    ver = ''

    def __init__(self):
        
        super(UpdateWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('Resource_Files/googledev.png'))
        self.outdatedPackages = json.load(open(
            'Resource_Files/outdatedPackage' + FILEVERSION + '.json'))
        self.selectedList = list()
        self.btnBack.clicked.connect(self.backFn)
        self.btnUpdateAll.clicked.connect(self.updateAllFn)
        self.btnUpdate.clicked.connect(self.updateFn)
        if len(self.outdatedPackages):
            for i in self.outdatedPackages:
                self.item = QtWidgets.QListWidgetItem(i)
                self.listWidget.addItem(self.item)
        else:
            self.item = QtWidgets.QListWidgetItem(
                '=== No Outdated Packges ===')
            self.listWidget.addItem(self.item)
            self.btnUpdate.setEnabled(False)
            self.btnUpdateAll.setEnabled(False)

    def updateFn(self):
        
        items = self.listWidget.selectedItems()
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        self.progWindow = ProgressWindow()
        self.progWindow.setLabelText('Updation in progress…')
        self.close()
        self.progWindow.show()
        for i in self.selectedList:
            self.outdatedPackages.remove(i)
        self.progWindow.callProgram(VERSION,
                                    ['install'] + self.selectedList, 2)
        
        # print 'Selected Packages Updated'
        with open('Resource_Files/outdatedPackage' + FILEVERSION + '.json', 'w') as file:
            json.dump(self.outdatedPackages, file)

    def updateAllFn(self):
        
        self.progWindow = ProgressWindow()
        self.progWindow.setLabelText('Updation in progress…')
        self.close()
        self.progWindow.show()
        self.progWindow.callProgram(VERSION,
                                    ['install'] + self.outdatedPackages, 2)
        # print 'All Packages Updated.'
        with open('Resource_Files/outdatedPackage' + FILEVERSION + '.json', 'w') as file:
            json.dump([], file)

    def backFn(self):
        
        self.close()
        self.window = MainWindow()
        self.window.show()


class UninstallWindow(QtWidgets.QMainWindow, uninstallScreen.Ui_Form):
    
    """ This is a class for uninstall window. The uninstall window will show all the details 
    of updation of pip packages """
    
    selectedList = list()
    ver = ''
    global FILEVERSION
    global VERSION
    global Yes

    def __init__(self):
        
        super(UninstallWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('Resource_Files/googledev.png'))
        self.allPackages = json.load(open(
            'Resource_Files/installedPackage' + FILEVERSION + '.json'))
        self.btnBack.clicked.connect(self.backFn)
        self.btnUninstallAll.clicked.connect(self.uninstallAllFn)
        self.btnUninstall.clicked.connect(self.uninstallFn)
        # global allPackages
        for i in self.allPackages:
            self.item = QtWidgets.QListWidgetItem(i)
            self.listWidget.addItem(self.item)

    def uninstallFn(self):
        
        items = self.listWidget.selectedItems()
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        if msgBox(3) == Yes:
            self.progWindow = ProgressWindow()
            self.progWindow.setLabelText('Uninstallation in progress…')
            self.close()
            self.progWindow.show()
            for i in self.selectedList:
                if i in self.allPackages:
                    self.allPackages.remove(i)
            self.progWindow.callProgram(VERSION,
                                        ['uninstall'] + self.selectedList,
                                        5)
            
            # print 'Selected Packages Uninstalled'
            self.selectedList = list()
            with open('Resource_Files/installedPackage' + FILEVERSION + '.json', 'w') as file:
                json.dump(self.allPackages, file)

        else:
            msgBox(4)

    def uninstallAllFn(self):
        
        if msgBox(3) == Yes:
            self.progWindow = ProgressWindow()
            self.progWindow.setLabelText('Uninstallation in progress…')
            self.close()
            self.progWindow.show()
            self.progWindow.callProgram(VERSION,
                                        ['uninstall'] + self.allPackages, 5)
            # print 'All Packages Uninstalled.'
            with open('Resource_Files/installedPackage' + FILEVERSION + '.json', 'w') as file:
                json.dump([], file)
            msgBox(5)
        else:
            msgBox(4)

    def backFn(self):
        
        self.close()
        self.window = MainWindow()
        self.window.show()


class InstallWindow(QtWidgets.QMainWindow, installScreen.Ui_Form):
    
    """ This is a class for installation window. The installation window will show all the details 
    of installation of pip packages """
    
    global FILEVERSION
    global VERSION

    ver = ''

    def __init__(self):
        
        super(InstallWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('Resource_Files/googledev.png'))
        self.offlinePackages = json.load(open(
            'Resource_Files/installedPackage' + FILEVERSION + '.json'))
        self.packages = json.load(
            open('Resource_Files/package' + FILEVERSION + '.json'))
        self.matchedList = list()
        self.selectedList = list()
        self.searchStr = str()

        self.btnBack.clicked.connect(self.backFn)
        self.btnInstall.clicked.connect(self.installFn)
        self.packageInput.textChanged.connect(self.textChange)

    def textChange(self, i):
        
        self.matchedList = list()
        self.searchStr = i
        self.listWidget.clear()
        for i in self.packages:
            if self.searchStr in i:
                self.matchedList.append(i)
        for i in self.matchedList:
            self.item = QtWidgets.QListWidgetItem(i)
            self.listWidget.addItem(self.item)

    def installFn(self):
        
        self.progWindow = ProgressWindow()
        self.progWindow.setLabelText('Installation in progress…')
        items = self.listWidget.selectedItems()
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        self.progWindow.show()
        for i in self.selectedList:
            if i not in self.offlinePackages:
                self.offlinePackages.append(i)  
        self.progWindow.callProgram(VERSION,
                                    ['install'] + self.selectedList, 1)
        # print 'Selected Packages Installed'
        with open('Resource_Files/installedPackage' + FILEVERSION + '.json', 'w') as file:
            json.dump(sorted(self.offlinePackages), file)
        self.close()

    def backFn(self):
        
        self.close()
        self.window = MainWindow()
        self.window.show()


def main():
    
    """ Function for starting of application"""
    
    global app
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
