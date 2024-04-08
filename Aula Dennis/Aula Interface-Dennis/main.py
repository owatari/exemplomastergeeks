from PyQt5 import QtWidgets
import ui

class Tela (ui.Ui_MainWindow):
    def __init__(self,MainWindow) -> None:
        self.setupUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0) # Exemplo de como mudar de página
        # self.pushButton.clicked.connect(lambda : self.Botao1()) Exemplo de clique de botão

        self.apresentar_dados()
    def Botao1(self):
        nome = self.lineEdit.text()
        idade = self.lineEdit_2.text()
        comida = self.lineEdit_3.text() 
        print(nome, idade, comida)


    def apresentar_dados(self):
        ## Exemplo de como apresentar dados
        data = ((1, "Joao", "32406655", "joao@exemplo.com"),
            (2, "Maria", "32409865", "maria@exemplo.com"))
        
        self.tableWidget.setRowCount(len(data))
        for i,row in enumerate(data):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(row[3]))


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    tela = Tela(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())

