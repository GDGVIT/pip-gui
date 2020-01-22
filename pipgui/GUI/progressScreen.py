# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig,
                                                _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(582, 317)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(10, 10, 561, 261))
        self.verticalLayoutWidget.setObjectName(
            _fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelProgress = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelProgress.setFont(font)
        self.labelProgress.setObjectName(_fromUtf8("labelProgress"))
        self.verticalLayout.addWidget(self.labelProgress)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setRange(0,1)
        self.progressBar.setGeometry(QtCore.QRect(30, 30, 1050, 35))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.btnContinue = QtWidgets.QPushButton(Form)
        self.btnContinue.setGeometry(QtCore.QRect(450, 280, 90, 28))
        self.btnContinue.setObjectName(_fromUtf8("btnContinue"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Progress Window", None))
        self.labelProgress.setText(
            _translate("Form", "Filler Text..", None))
        self.btnContinue.setText(_translate("Form", "Continue", None))
        

