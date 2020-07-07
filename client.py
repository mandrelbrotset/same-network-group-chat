from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui
import sys

class Client(object):
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()

        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        self.chatWidget.setHidden(True)
        self.host = ""

        self.connect_widget = connect_ui.Ui_Form()
        self.connect_widget.setupUi(self.connectWidget)
        self.connect_widget.pushButton.clicked.connect(self.btn_connect_event)

        self.mainWindow.setGeometry(QtCore.QRect(1080, 20,350, 500))
        self.mainWindow.show()
        
    def btn_connect_event(self):
        self.host = self.connect_widget.hostTextEdit.toPlainText()
        print(self.host)

        if len(self.host) > 0:
            self.client_widget = client_ui.Ui_Form()
            self.client_widget.setupUi(self.chatWidget)
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())