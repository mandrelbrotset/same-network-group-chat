import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import client_gui
import client
import clientSetup
import threading
import random

class main(QtWidgets.QMainWindow, client_gui.Ui_MainWindow, clientSetup.Ui_Form):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.setupWidget = QtWidgets.QWidget(self.MainWindow)
        self.setupUi2(self.setupWidget)
        self.centralwidget.setHidden(True)
        self.show()

        # set default values for hostname and port number
        self.hostname = "127.0.0.1"
        self.port = 8080
        self.nickname = "User " + str(random.randint(1, 1000))

        self.hostnameField.returnPressed.connect(self.start)
        self.portNoField.returnPressed.connect(self.start)
        self.nicknameField.returnPressed.connect(self.start)
        self.connectButton.clicked.connect(self.start)

    def start(self):
        if self.hostnameField.text() != "":
            self.hostname = self.hostnameField.text()
        if self.portNoField.text() != "":
            self.port = self.portNoField.text()
        if self.nicknameField.text() != "":
            self.nickname = self.nicknameField.text()



        print("created object")
        self.client = client.Client(self.hostname, self.port, self.sendBtn, self.nickname, self.messageEdit, self.receivedMessages)
        self.client.start()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()
    # mainWindow.start()
    sys.exit(app.exec())
