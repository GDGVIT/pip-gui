import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle('Some Title')
		self.setGeometry(500, 10, 1000, 480)
		self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
