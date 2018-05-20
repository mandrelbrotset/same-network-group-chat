# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/debug.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 80)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(1, 1, 346, 75))
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def addDebugMsg(self, msg):
        self.listWidget.addItem(msg)

