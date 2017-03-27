from PyQt4 import QtCore, QtGui
import sys
import json
#sys.path.insert(0,'./GUI')

#Importing GUIs
from GUI import startScreen, uninstallScreen, updateScreen, installScreen
#from Scraping import genreList, packageList

class MainWindow(startScreen.Ui_mainWindow, QtGui.QMainWindow):
    def radioCheck(self):
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

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #Quiting the Application
        self.btnExit.clicked.connect(app.quit)
        self.btnExit.setToolTip('Exit Application')
        self.actionExit.triggered.connect(app.quit)
        self.actionExit.setStatusTip('Exit Application')
        self.actionExit.setShortcut('Ctrl+Q')

        #Binding button to radio button result
        self.btnNext.clicked.connect(self.radioCheck)


class UpdateWindow(QtGui.QMainWindow, updateScreen.Ui_Form):
    outdatedPackages = json.load(open('Resource_Files/outdatedPackageList.json'))
    selectedList = list()

    def __init__(self):
        super(UpdateWindow, self).__init__()
        self.setupUi(self)

        self.btnBack.clicked.connect(self.backFn)
        self.btnUpdateAll.clicked.connect(self.updateAllFn)
        self.btnUpdate.clicked.connect(self.updateFn)

        global outdatedPackages
        for i in self.outdatedPackages:
            self.item = QtGui.QListWidgetItem(i)
            self.listWidget.addItem(self.item)

    def updateFn(self):
        items = self.listWidget.selectedItems()
        global selectedList
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        import os
        for i in self.selectedList:
            os.system('pip install ' + i + ' -U')
            self.outdatedPackages.remove(i)
        print 'Selected Packages Updated'
        json.dump(self.outdatedPackages, open('Resource_Files/outdatedPackageList.json', 'w'))
        self.close()
        self.update = UpdateWindow()
        self.update.show()

    def updateAllFn(self):
        import os
        for i in self.outdatedPackages:
            os.system('pip install ' + i + ' -U')
        print 'All Packages Updated.'
        json.dump([], open('Resource_Files/outdatedPackageList.json', 'w'))
        self.close()
        self.update = UpdateWindow()
        self.update.show()

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class UninstallWindow(QtGui.QMainWindow, uninstallScreen.Ui_Form):
    allPackages = json.load(open('Resource_Files/installedPackageList.json'))
    selectedList = list()

    def __init__(self):
        super(UninstallWindow, self).__init__()
        self.setupUi(self)

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
        global selectedList
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        print self.selectedList
        import os
        self.uninstall.show()

        for i in self.selectedList:
            os.system('pip uninstall ' + i + ' -y')
            self.allPackages.remove(i)
        print 'Selected Packages Uninstalled'
        json.dump(self.allPackages, open('Resource_Files/installedPackageList.json', 'w'))
        self.close()
        self.uninstall = UninstallWindow()
        self.uninstall.show()

    def uninstallAllFn(self):
        import os
        os.system('pip freeze > requirements.txt ')
        os.system('pip uninstall -r requirements.txt')
        print 'All Packages Uninstalled.'
        json.dump([], open('Resource_Files/installedPackageList.json', 'w'))
        self.close()
        self.uninstall = UninstallWindow()
        self.uninstall.show()

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class InstallWindow(QtGui.QMainWindow, installScreen.Ui_Form):
    packages = json.load(open('Resource_Files/packageList.json'))
    matchedList = list()
    selectedList = list()
    searchStr = str()

    def __init__(self):
        super(InstallWindow, self).__init__()
        self.setupUi(self)

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
        items = self.listWidget.selectedItems()
        global selectedList
        for i in items:
            k = str(i.text())
            if k not in self.selectedList:
                self.selectedList.append(k)
        import os
        for i in self.selectedList:
            os.system('pip install ' + i)
        print 'Selected Packages Installed'
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
