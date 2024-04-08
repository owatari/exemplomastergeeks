from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox, QRadioButton, QCheckBox, QComboBox, QTableView, QSpinBox
from PyQt5 import QtWidgets
from PyQt5 import uic
from database import db
import sys

class UI(QMainWindow):
        def __init__(self):
            super(UI, self).__init__()
            uic.loadUi("Aula Designer/ui.ui", self)
            
            self.findChild(QPushButton, 'confirm').clicked.connect(self.parseInfo)
            self.findChild(QPushButton, 'search').clicked.connect(self.searchPass)
            self.findChild(QPushButton, 'delete_2').clicked.connect(self.deletePass)
            self.findChild(QLineEdit, 'lineEdit').textChanged.connect(self.onChange)
            
            self.show()
        
        def parseInfo(self):
            if len(self.findChild(QLineEdit, 'nome').text()) <= 3:
                return self.showMsg('Por favor preencha o nome')

            if len(self.findChild(QLineEdit, 'cpf').text()) < 11:
                return self.showMsg('Por favor preencha o CPF')

            if self.findChild(QRadioButton, 'corredor').isChecked():
                db.session.add(db.Flight(nome = self.findChild(QLineEdit, 'nome').text(), cpf = self.findChild(QLineEdit, 'cpf').text(), assento = 'corredor', destino = self.findChild(QComboBox, 'destino').currentText(), executivo = self.findChild(QCheckBox, 'executivo').isChecked()))
            elif self.findChild(QRadioButton, 'janela').isChecked():
                db.session.add(db.Flight(nome = self.findChild(QLineEdit, 'nome').text(), cpf = self.findChild(QLineEdit, 'cpf').text(), assento = 'janela', destino = self.findChild(QComboBox, 'destino').currentText(), executivo = self.findChild(QCheckBox, 'executivo').isChecked()))
            else:
                 return self.showMsg('Por favor escolha seu assento.')   
            db.session.commit()         
            self.showMsg('Passageiro registrado com sucesso.', 'Aviso') 
            self.clearAll()
        
        def showMsg(self, texto, title='Erro'):
            msg = QMessageBox()
            msg.setWindowTitle(title)
            msg.setText(texto)
            msg.exec_()
        
        def clearAll(self):
            self.findChild(QLineEdit, 'nome').setText('')
            self.findChild(QLineEdit, 'cpf').setText('')
            self.findChild(QCheckBox, 'executivo').setChecked(False)

        def searchPass(self):
            data = db.session.query(db.Flight).all()

            # O query nada mais é do que transformar nossa database em uma lista.
            # data = [{id, nome, cpf, assento, destino, executivo}, {id, nome, cpf, assento, destino, executivo}, {id, nome, cpf, assento, destino, executivo}]

            self.tableWidget.setRowCount(len(data))
            for i in range (len(data)):
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(data[i].id)))
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(data[i].nome))

        def deletePass(self):
            valor = self.findChild(QLineEdit, 'lineEdit').text()
            qry = db.session.get(db.Flight, valor)
            if not qry:
                self.showMsg('Por favor insira um ID válido.')
                return
            db.session.delete(qry)
            db.session.commit()
            self.showMsg('Passageiro deletado com sucesso.', 'Aviso')
            
        def onChange(self):
            valor = self.findChild(QLineEdit, 'lineEdit').text()
            qry = db.session.get(db.Flight, valor)
            if not qry:
                self.showMsg('Por favor insira um ID válido.')
                return
            self.findChild(QLabel, 'label_8').setText(f'Você tem certeza que gostaria de deletar o passageiro: {qry.nome}?')
            self.findChild(QLabel, 'label_8').setWordWrap(True)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()