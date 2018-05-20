import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import gui
import client3
import threading

class main(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.getNickname()

    def start(self):
        self.client = client3.Client(self.hostname, self.port, self.sendBtn, self.nickname, self.messageEdit, self.receivedMessages)
        self.client.start()
        #threading.Thread(target=self.client.receive, daemon=True).start()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()
    mainWindow.start()
    sys.exit(app.exec())
