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
    def __init__(self):
        super(UpdateWindow, self).__init__()
        self.setupUi(self)

        self.btnBack.clicked.connect(self.backFn)

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class UninstallWindow(QtGui.QMainWindow, uninstallScreen.Ui_Form):
    #try:
    #    from Package_Management import installedList
    #    self.allPackages = json.load(open('Resource_Files/installedPackageList.json'))
    #except:
    #    self.allPackages = json.load(open('Resource_Files/installedPackageList.json'))

    def __init__(self):
        super(UninstallWindow, self).__init__()
        self.setupUi(self)

        self.btnBack.clicked.connect(self.backFn)

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()


class InstallWindow(QtGui.QMainWindow, installScreen.Ui_Form):
    def __init__(self):
        super(InstallWindow, self).__init__()
        self.setupUi(self)

        self.btnBack.clicked.connect(self.backFn)

    def backFn(self):
        self.close()
        self.window = MainWindow()
        self.window.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
