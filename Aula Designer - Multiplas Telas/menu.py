from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class menuWindow(QMainWindow):
    def __init__(self):
        super(menuWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\menuWindow.ui", self)

        self.findChild(QPushButton, 'pedroButton').clicked.connect(self.goPedro)
        self.findChild(QPushButton, 'mariaButton').clicked.connect(self.goMaria)

        self.show()

class menuWindow(QMainWindow):
    def __init__(self):
        super(menuWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\menuWindow.ui", self)

        self.findChild(QPushButton, 'pedroButton').clicked.connect(self.goPedro)
        self.findChild(QPushButton, 'mariaButton').clicked.connect(self.goMaria)

        self.show()
    
    def goPedro(self):
        self.hide()
        self.v = pedroWindow()
        self.v.show()

    def goMaria(self):
        self.hide()
        self.v = mariaWindow()
        self.v.show()

class pedroWindow(QMainWindow):
    def __init__(self):
        super(pedroWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\pedroWindow.ui", self)

        self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
    
    def goBack(self):
        self.hide()
        self.v = menuWindow()
        self.v.show()
        
class mariaWindow(QMainWindow):
    def __init__(self):
        super(mariaWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\mariaWindow.ui", self)

        self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
    
    def goBack(self):
        self.hide()
        self.v = menuWindow()
        self.v.show()



app = QApplication(sys.argv)
UIWindow = menuWindow()
app.exec_()