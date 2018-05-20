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
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(1, 278, 418, 34))
        self.connectButton.setObjectName("connectButton")
        self.InfoLabel = QtWidgets.QLabel(Form)
        self.InfoLabel.setGeometry(QtCore.QRect(90, 20, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setObjectName("InfoLabel")
        self.lblNickname = QtWidgets.QLabel(Form)
        self.lblNickname.setGeometry(QtCore.QRect(40, 89, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNickname.setFont(font)
        self.lblNickname.setObjectName("lblNickname")
        self.lblPortNo = QtWidgets.QLabel(Form)
        self.lblPortNo.setGeometry(QtCore.QRect(40, 145, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPortNo.setFont(font)
        self.lblPortNo.setObjectName("lblPortNo")
        self.nicknameField = QtWidgets.QLineEdit(Form)
        self.nicknameField.setGeometry(QtCore.QRect(180, 89, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nicknameField.setFont(font)
        self.nicknameField.setObjectName("nicknameField")
        self.portNoField = QtWidgets.QLineEdit(Form)
        self.portNoField.setGeometry(QtCore.QRect(180, 145, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portNoField.setFont(font)
        self.portNoField.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.portNoField.setObjectName("portNoField")
        self.hostnameField = QtWidgets.QLineEdit(Form)
        self.hostnameField.setGeometry(QtCore.QRect(180, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hostnameField.setFont(font)
        self.hostnameField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.hostnameField.setObjectName("hostnameField")
        self.lblHostname = QtWidgets.QLabel(Form)
        self.lblHostname.setGeometry(QtCore.QRect(40, 200, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblHostname.setFont(font)
        self.lblHostname.setObjectName("lblHostname")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.connectButton.setText(_translate("Form", "Connect to Server"))
        self.InfoLabel.setText(_translate("Form", "Leave fields empty for default values"))
        self.lblNickname.setText(_translate("Form", "Chat nickname"))
        self.lblPortNo.setText(_translate("Form", "Port number"))
        self.lblHostname.setText(_translate("Form", "Hostname"))

