# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installScreen.ui'
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
        Form.resize(440, 538)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(300, 140, 121, 98))
        self.verticalLayoutWidget.setObjectName(
            _fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnInstall = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnInstall.setObjectName(_fromUtf8("btnInstall"))
        self.verticalLayout.addWidget(self.btnInstall)
        self.btnBack = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBack.setObjectName(_fromUtf8("btnBack"))
        self.verticalLayout.addWidget(self.btnBack)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 261, 381))
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(20, 10, 401, 80))
        self.horizontalLayoutWidget.setObjectName(
            _fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.packageInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.packageInput.setObjectName(_fromUtf8("packageInput"))
        self.horizontalLayout.addWidget(self.packageInput)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Install Packages", None))
        self.btnInstall.setText(_translate("Form", "Install", None))
        self.btnBack.setText(_translate("Form", "Go Back", None))
        self.label.setText(_translate("Form",
                                      "Please select the packages "
                                      "you want to install:",
                                      None))
        self.label_2.setText(_translate("Form", "Search Packages:", None))
