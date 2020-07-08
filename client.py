from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui

import sys
import socket
import random


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

        print(message)
        self.signal.emit(message)


class Client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        self.chatWidget.setHidden(True)
        self.chat_widget = client_ui.Ui_Form()
        self.chat_widget.setupUi(self.chatWidget)
        self.chat_widget.pushButton.clicked.connect(self.send_message)

        self.connect_widget = connect_ui.Ui_Form()
        self.connect_widget.setupUi(self.connectWidget)
        self.connect_widget.pushButton.clicked.connect(self.btn_connect_clicked)

        self.mainWindow.setGeometry(QtCore.QRect(1080, 20,350, 500))
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def btn_connect_clicked(self):
        host = self.connect_widget.hostTextEdit.toPlainText()
        port = self.connect_widget.portTextEdit.toPlainText()
        nickname = self.connect_widget.nameTextEdit.toPlainText()

        if len(host) == 0:
            host = "localhost"
        
        if len(port) == 0:
            port = 5555
        else:
            try:
                port = int(port)
            except Exception as e:
                error = "Invalid port number \n'{}'".format(str(e))
                print("[INFO]", error)
                self.show_error("Port Number Error", error)
        
        if len(nickname) < 1:
            nickname = socket.gethostname()

        nickname = nickname + "_" + str(random.randint(1, port))

        if self.connect(host, port, nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)

            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")


    def show_message(self, message):
        self.chat_widget.textBrowser.append(message)
        

    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error_message = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error_message)
            self.connect_widget.hostTextEdit.clear()
            self.connect_widget.portTextEdit.clear()
            
            return False
        

    def send_message(self):
        message = self.chat_widget.textEdit.toPlainText()
        self.chat_widget.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_widget.textEdit.clear()


    def show_error(self, error_type, message):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(message)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())