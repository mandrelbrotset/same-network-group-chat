import socket
import time
import threading
import pickle
import sys
from PyQt5.QtCore import QThread

class Client(QThread):
    def __init__(self, host, port, sendBtn, nickname, messageEdit, receivedMessage):
        super(Client, self).__init__(parent = None)
        self.receivedMessage = receivedMessage
        self.nickname = nickname
        self.running = True
        self.port = port
        self.host = host
        self.messageEdit = messageEdit
        sendBtn.clicked.connect(self.send)
        self.messageEdit.returnPressed.connect(self.send)

        self.clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.clientsoc.connect((self.host, self.port))
            self.clientsoc.send(pickle.dumps(self.nickname))
            self.receivedMessage.append("Connected to server")
        except:
            print("Could not connect to server")
            sys.exit()
        self.message = ""

    def run(self):
        while True:
            self.receive()

    def receive(self):
        while True:
            print("waiting to receive ")
            try:
                self.data = self.clientsoc.recv(1024)
            except:
                # To Do make pop up to show error
                print("Error receiving")
            self.data = pickle.loads(self.data)
            if self.data:                
                print(str(self.data[0] + ": " +self.data[1]))
                # do not show the message if you're the sender
                if self.data[0] != self.nickname:
                    #self.emit(QtCore.SIGNAL("MESSAGES", self.message))
                    self.receivedMessage.append(str(self.data[0] + ": " +self.data[1]))
                    


    def send(self):
        self.message = self.messageEdit.text()
        self.receivedMessage.append("You: " + self.message)
        self.messageEdit.setText("")
        self.data = (self.nickname, self.message)
        self.data = pickle.dumps(self.data)

        try:
            self.clientsoc.send(self.data)
        except:
            print("Error sending message")

        #if self.message == "quit":
        #    self.receivedMessage.append("Closed connection")
        #    self.stop()

    def stop(self):
        self.running = False
        self.clientsoc.close()