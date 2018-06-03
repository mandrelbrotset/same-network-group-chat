from socket import *
import threading
import random
import pickle
import queue
from PyQt5.QtCore import QThread, QTimer

class Server(QThread):
    def __init__(self, host, port, clientField, debugField):
        super(Server, self).__init__(parent = None)
        self.connections = []
        self.messageQueue = queue.Queue()
        self.host = host
        self.port = port
        self.clientField = clientField
        self.debugField = debugField

        # create a socket
        self.serversock = socket(AF_INET, SOCK_STREAM)
        self.serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # create a qtimer to call the sendMsgs method every .5 second
        self.timer = QTimer()
        self.timer.timeout.connect(self.sendMsgs)
        self.timer.start(500)

        #self.timer1 = QTimer()
        #self.timer1.timeout.connect(self.updateClients)
        #self.timer1.start(500)

        # start server on specified host and port
        try:
            self.port = int(self.port)
            self.serversock.bind((self.host, self.port))
        except Exception as e:
            print(e)
            # if error occurs try another port number
            self.port = int(self.port) + random.randint(1, 1000)
            self.serversock.bind((self.host, self.port))

        self.serversock.listen(5)

        debugMsg = "Server running on {} at port {}".format(self.host, self.port) 
        self.debugField.addItem(debugMsg)
        print(debugMsg)

    def run(self):
        while True:
            self.clientsock, self.addr = self.serversock.accept()

            if self.clientsock:
                self.data = self.clientsock.recv(1024)
                self.nickname = pickle.loads(self.data)
                self.clientField.addItem(self.nickname)
                self.connections.append((self.nickname, self.clientsock, self.addr))
                threading.Thread(target=self.receiveMsg, args=(self.clientsock, self.addr), daemon=True).start()
    
    def receiveMsg(self, sock, addr):
        length = len(self.connections)
        debugMsg = "{} is connected with {} on port {} ".format(self.connections[length-1][0], self.connections[length-1][2][0], self.connections[length-1][2][1])
        self.debugField.addItem(debugMsg)

        while True:
            try:
                self.data = sock.recv(1024)
            except:
                self.data = None

            if self.data:
                self.data = pickle.loads(self.data)
                
                # set the nickname and message
                self.messageQueue.put(self.data)

    def sendMsgs(self):
        while(not self.messageQueue.empty()):
            if not self.messageQueue.empty():
                self.message = self.messageQueue.get()
                self.message = pickle.dumps(self.message)
                if self.message:
                    for i in self.connections:
                        try:
                            i[1].send(self.message)
                        except:
                            debugMsg = "[ERROR] Sending message to " + str(i[0])
                            print(debugMsg)
                            self.debugField.addItem(debugMsg)

    """def updateClients(self):
        count = self.clientField.count()
        for j in self.connections:
            print(j[0])
            for i in range(count):
                print(i.text())
                if i.text() != j[0]:
                    self.clientField.addItem(j[0])
    """

    #def stop(self):
    #    for i in self.connections:
    #        