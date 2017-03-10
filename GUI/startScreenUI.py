from PyQt4 import QtCore, QtGui
import startScreen
import sys

class MainWindow(startScreen.Ui_mainWindow, QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #Quiting the Application
        self.btnExit.clicked.connect(app.quit)
        self.btnExit.setToolTip('Exit Application')
        self.actionExit.triggered.connect(app.quit)
        self.actionExit.setStatusTip('Exit Application')
        self.actionExit.setShortcut('Ctrl+Q')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
