from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class madeWindow(QMainWindow):
    def __init__(self):
        super(madeWindow, self).__init__()

        # inicialização normal da janela.
        uic.loadUi("Aula Designer - Multiplas Telas\madeWindow.ui", self)

        # atribuindo função ao botão
        self.findChild(QPushButton, 'backButton').clicked.connect(self.parseBack)

    # função do botão.
    def parseBack(self):
        # Aqui escondemos a janela atual para que ela não continue aberta.
        self.hide()

        # Aqui atribuimos a janela a uma variavel que referencia a janela atual.
        # A janela NOVA deve continuar referenciando a janela ANTIGA, caso contrário ela se fecha imediatamente após abrir.
        # Você pode testar removendo o 'self.' daqui e o de baixo.
        self.v = mainWindow()
        # ficando: 
        # v = mainWindow()

        # Aqui mostramos a janela.
        self.v.show()
        # Ficando: 
        # v.show()
            
class congratsWindow(QMainWindow):
    def __init__(self):
        super(congratsWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\congratsWindow.ui", self)
        self.findChild(QPushButton, 'backButton').clicked.connect(self.parseBack)
    
    def parseBack(self):
        self.hide()
        self.v = mainWindow()
        self.v.show()

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("Aula Designer - Multiplas Telas\mainWindow.ui", self)
        
        self.findChild(QPushButton, 'button_one').clicked.connect(self.parseOne)
        self.findChild(QPushButton, 'button_two').clicked.connect(self.parseTwo)
        self.show()

    def parseOne(self):
        self.hide()
        self.v = madeWindow()
        self.v.show()

    def parseTwo(self):
        self.hide()
        self.v = congratsWindow()
        self.v.show()

app = QApplication(sys.argv)
UIWindow = mainWindow()
app.exec_()