import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import client_gui, clientSetup
from networking import client
import threading
import random

class main(QtWidgets.QMainWindow, client_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.setupWidget = QtWidgets.QWidget(self)
        self.config = clientSetup.Ui_Form()
        self.config.setupUi(self.setupWidget)
        self.show()

        # hide the widget on start because another widget 
        #   which receives configuration details is being shown
        self.centralwidget.setHidden(True)

        # set default values for hostname and port number
        self.hostname = "127.0.0.1"
        self.port = 8080
        self.nickname = "User " + str(random.randint(1, 1000))      # use a randomly generated nickname as the default nickname

        # connect the slot method "self.start" to its signals
        self.config.hostnameField.returnPressed.connect(self.start)     # call start method if user enters return in hostname field
        self.config.portNoField.returnPressed.connect(self.start)       # call start method if user enters return in port number field
        self.config.nicknameField.returnPressed.connect(self.start)     # call start method if user enters return in nickname field
        self.config.connectButton.clicked.connect(self.start)           # call start method if user clicks connect button

    def start(self):
        # check for user input to determine whether to use default values or not
        if self.config.hostnameField.text() != "":
            # if user enters a hostname, set the hostname to what the user entered
            self.hostname = self.config.hostnameField.text()
        if self.config.portNoField.text() != "":
            # if user enters a port number, set the port number to what the user entered
            self.port = self.config.portNoField.text()
        if self.config.nicknameField.text() != "":
            # if user enters a nickname, set the nickname to what the user entered
            self.nickname = self.config.nicknameField.text()

        self.setWindowTitle(self.nickname + "'s chat")      # change the title of the window
        self.receivedMessages.append("Your nickname is " + self.nickname)       # show the users nickname

        print("Nickname ----:", self.nickname)      # print nickname
        print("Hostname: ---:", self.hostname)      # print hostname
        print("Port number -:", self.port)          # print port number

        # create an instance of Client
        self.client = client.Client(self.hostname, self.port, self.sendBtn, self.nickname, self.messageEdit, self.receivedMessages)
        self.client.start()     # call method inherited from QThread to thread run method in client

        # hide the widget after user has pressed enter or clicked connect
        self.setupWidget.setHidden(True)
        # show the main group chat widget
        self.centralwidget.setVisible(True)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()         # create an instance of main
    sys.exit(app.exec())        # stops the script on exiting the gui
