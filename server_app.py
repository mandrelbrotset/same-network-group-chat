# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import serverSetup, serverMainWindow, debugMsgWidget, clientListWidget
from networking import server

class main(QtWidgets.QMainWindow, serverMainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

        #create instances of the forms
        self.userInput = serverSetup.Ui_Form()
        self.client = clientListWidget.Ui_Form()
        self.debug = debugMsgWidget.Ui_Form()

        # create widgets
        self.inputWidget = QtWidgets.QWidget(self)          # widget to show input for host and port number
        self.clientwidget = QtWidgets.QWidget(self)         # widget to show the clients and debug messages
        self.debugWidget = QtWidgets.QWidget(self)

        # put the widgets in the correct position
        self.clientwidget.setGeometry(0, 0, 348, 200)
        self.debugWidget.setGeometry(0, 180, 348, 100)

        # add the forms to a widget
        self.userInput.setupUi(self.inputWidget)
        self.client.setupUi(self.clientwidget)
        self.debug.setupUi(self.debugWidget)

        # show input widget and hide the widget
        self.inputWidget.setVisible(True)
        self.clientwidget.setHidden(True)
        self.debugWidget.setHidden(True)

        # if start or stop server button is pressed
        self.start_stop_server.clicked.connect(self.start_stop)
        # also start server on pressing return in the port number field
        self.userInput.portNoField.returnPressed.connect(self.start_stop)

        self.show()

        # set default hostname and port number
        self.hostname = "127.0.0.1"
        self.port = 8080

    def start_stop(self):
        # if a port number is entered use that otherwise use the default port number
        if self.userInput.portNoField.text() != "":
            self.port = self.userInput.portNoField.text()

        if self.start_stop_server.text() == "Start Server":
            self.start_stop_server.setText("Stop Server")
            self.clientwidget.setVisible(True)
            self.debugWidget.setVisible(True)
            self.inputWidget.setHidden(True)

            self.server = server.Server(self.hostname, self.port, self.client.listWidget, self.debug.listWidget)
            self.server.start()
        else:
            #self.server.stop()
            self.inputWidget.setVisible(True)
            self.debugWidget.setHidden(True)
            self.clientwidget.setHidden(True)
            self.start_stop_server.setText("Start Server")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()
    mainWindow.show()
    sys.exit(app.exec())
