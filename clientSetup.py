# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/clientSetup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 315)
        Form.setMinimumSize(QtCore.QSize(420, 315))
        Form.setMaximumSize(QtCore.QSize(420, 315))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1, 278, 418, 34))
        self.pushButton.setObjectName("pushButton")
        self.InfoLabel = QtWidgets.QLabel(Form)
        self.InfoLabel.setGeometry(QtCore.QRect(90, 40, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setObjectName("InfoLabel")
        self.lblNickname = QtWidgets.QLabel(Form)
        self.lblNickname.setGeometry(QtCore.QRect(40, 99, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNickname.setFont(font)
        self.lblNickname.setObjectName("lblNickname")
        self.lblPortNo = QtWidgets.QLabel(Form)
        self.lblPortNo.setGeometry(QtCore.QRect(40, 155, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPortNo.setFont(font)
        self.lblPortNo.setObjectName("lblPortNo")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 99, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 155, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Connect to Server"))
        self.InfoLabel.setText(_translate("Form", "Leave fields empty for default values"))
        self.lblNickname.setText(_translate("Form", "Chat nickname"))
        self.lblPortNo.setText(_translate("Form", "Port number"))

