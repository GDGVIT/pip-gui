import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('New Window')
		self.setGeometry(20, 20, 400, 500)

		btn = QPushButton('Button Name', self)
		btn.setToolTip('Hint for Button Action')
		btn.move(20,20)
		btn.clicked.connect(self.on_click)

		self.show()

	def on_click(self):
		print('Button was clicked')

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
