from PyQt4 import QtCore, QtGui
import sys
import json

#Importing GUIs
from GUI import startScreen, uninstallScreen, updateScreen, installScreen
#from Scraping import genreList, packageList

Yes = QtGui.QMessageBox.Yes
def msgBox(x):
    msg = QtGui.QMessageBox()
    msg.setWindowTitle("Status Window")
    msg.setIcon(QtGui.QMessageBox.Information)

    if x == 1:
        msg.setText("Selected Packages have been installed.")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
    if x ==2:
        msg.setText('Selected Packages have been upgraded.')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
    if x == 3:
        msg.setText('Are you sure you wanna uninstall?')
        msg.setIcon(QtGui.QMessageBox.Question)
        msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if x == 4:
        msg.setText('Uninstall Aborted.')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
    if x == 5:
        msg.setText('Selected Packages have been uninstalled.')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
    if x ==6:
        msg.setText('Lists Refreshed.')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
    if x == 7:
        msg.setText('Are you sure you wanna exit?')
        msg.setIcon(QtGui.QMessageBox.Question)
        msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    return msg.exec_()

version = 0 #0 is for py2 and 1 is for py3
fileVersion = ''

class MainWindow(startScreen.Ui_mainWindow, QtGui.QMainWindow):
    ver = ''
    def pythonVersion(self):
        global version
        global fileVersion
        if self.radioPy2.isChecked():
            version = 'pip'
            fileVersion = 'List'
        if self.radioPy3.isChecked():
            version = 'pip3'
            fileVersion = 'List3'

    def radioCheck(self):
        self.pythonVersion() #Checking the version of python being used
        #Checking the radio button status
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
        print "Refreshing Online Package List..."
        from Scraping import pypiList
        print "\nRefreshing Installed Package List..."
        from Package_Management import installedList
        print "\nRefreshing Outdated Package List..."
        from Package_Management import outdatedList
        msgBox(6)
        self.close()
        self.window = MainWindow()
        self.window.show()

    def endApp(self):
        global Yes
        if msgBox(7) == Yes:
            app.quit()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Resource_Files/googledev.png'))
        #Quiting the Application
        self.btnExit.clicked.connect(self.endApp)
        self.btnExit.setToolTip('Exit Application')
        self.actionExit.triggered.connect(self.endApp)
        self.actionExit.setStatusTip('Exit Application')
        self.actionExit.setShortcut('Ctrl+Q')

        self.actionRefresh.triggered.connect(self.refreshLists)
        self.actionRefresh.setToolTip('Refresh Package Lists')
        self.actionRefresh.setShortcut('Ctrl+R')

        #Binding button to radio button result
        self.btnNext.clicked.connect(self.radioCheck)


class UpdateWindow(QtGui.QMainWindow, updateScreen.Ui_Form):
    global fileVersion
    global version
    ver = ''
    def __init__(self):
        super(UpdateWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Resource_Files/googledev.png'))
        self.outdatedPackages = json.load(open('Resource_Files/outdatedPackage' + fileVersion+ '.json'))
        self.selectedList = list()

        self.btnBack.clicked.connect(self.backFn)
        self.btnUpdateAll.clicked.connect(self.updateAllFn)
        self.btnUpdate.clicked.connect(self.updateFn)

        global outdatedPackages
        if len(self.outdatedPackages):
            for i in self.outdatedPackages:
                self.item = QtGui.QListWidgetItem(i)
                self.listWidget.addItem(self.item)
        else:
            self.item = QtGui.QListWidgetItem('=== No Outdated Packges ===')
            self.listWidget.addItem(self.item)

    def updateFn(self):
        items = self.listWidget.selectedItems()
        global selectedList
        global version
        if version == 0:
            ver = 'pip'
        elif version == 1:
            ver = 'pip3'
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        import os
        for i in self.selectedList:
            os.system(version + ' install ' + i + ' -U')
            self.outdatedPackages.remove(i)
        print 'Selected Packages Updated'
        json.dump(self.outdatedPackages, open('Resource_Files/outdatedPackage' + fileVersion + '.json', 'w'))
        msgBox(2)
        self.close()
        self.update = UpdateWindow()
        self.update.show()

    def updateAllFn(self):
        import os
        global version
        if version == 0:
            ver = 'pip'
        elif version == 1:
            ver = 'pip3'
        for i in self.outdatedPackages:
            os.system(version + ' install ' + i + ' -U')
        print 'All Packages Updated.'
        json.dump([], open('Resource_Files/outdatedPackage' + fileVersion + '.json', 'w'))
        msgBox(2)
        self.close()
        self.update = UpdateWindow()
        self.update.show()

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class UninstallWindow(QtGui.QMainWindow, uninstallScreen.Ui_Form):
    selectedList = list()
    ver = ''
    global fileVersion
    global version
    def __init__(self):
        super(UninstallWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Resource_Files/googledev.png'))
        self.allPackages = json.load(open('Resource_Files/installedPackage' + fileVersion + '.json'))

        self.btnBack.clicked.connect(self.backFn)
        self.btnUninstallAll.clicked.connect(self.uninstallAllFn)
        self.btnUninstall.clicked.connect(self.uninstallFn)

        # global allPackages
        for i in self.allPackages:
            self.item = QtGui.QListWidgetItem(i)
            self.listWidget.addItem(self.item)

    def uninstallFn(self):
        # global allPackages
        items = self.listWidget.selectedItems()
        #global selectedList
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        #print self.selectedList
        global Yes
        global version
        if version == 0:
            ver = 'pip'
        elif version == 1:
            ver = 'pip3'
        if msgBox(3) == Yes:
            import os
            for i in self.selectedList:
                os.system(version + ' uninstall ' + i + ' -y')
                if i in self.allPackages:
                    self.allPackages.remove(i)
            print 'Selected Packages Uninstalled'
            self.selectedList = list()
            json.dump(self.allPackages, open('Resource_Files/installedPackage' + fileVersion + '.json', 'w'))
            msgBox(5)
        else:
            msgBox(4)
        self.close()
        self.uninstall = UninstallWindow()
        self.uninstall.show()

    def uninstallAllFn(self):
        global Yes
        global version
        if version == 0:
            ver = 'pip'
        elif version == 1:
            ver = 'pip3'
        if msgBox(3) == Yes:
            import os
            os.system(version + ' freeze > requirements.txt ')
            os.system(version + ' uninstall -r requirements.txt')
            print 'All Packages Uninstalled.'
            json.dump([], open('Resource_Files/installedPackage' + fileVersion + '.json', 'w'))
            msgBox(5)
        else:
            msgBox(4)
        self.close()
        self.uninstall = UninstallWindow()
        self.uninstall.show()

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class InstallWindow(QtGui.QMainWindow, installScreen.Ui_Form):
    ver = ''
    global fileVersion
    def __init__(self):
        super(InstallWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Resource_Files/googledev.png'))
        self.offlinePackages = json.load(open('Resource_Files/installedPackage' + fileVersion + '.json'))
        self.packages = json.load(open('Resource_Files/package' + fileVersion + '.json'))
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
            self.item = QtGui.QListWidgetItem(i)
            self.listWidget.addItem(self.item)

    def installFn(self):
        global version
        if version == 0:
            ver = 'pip'
        elif version == 1:
            ver = 'pip3'
        items = self.listWidget.selectedItems()
        global selectedList
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        import os
        for i in self.selectedList:
            os.system(version + ' install ' + i)
            if i not in self.offlinePackages:
                self.offlinePackages.append(i)
        print 'Selected Packages Installed'
        json.dump(sorted(self.offlinePackages), open('Resource_Files/installedPackage' + fileVersion + '.json', 'w'))
        msgBox(1)
        self.close()
        self.install = InstallWindow()
        self.install.show()
    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
