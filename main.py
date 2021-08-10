'''import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap'''

import sys, pyodbc
from PyQt5.uic       import *
from PyQt5           import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

class telaEntrada(QDialog):
    #Carrega tela
    def __init__(self):
        super(telaEntrada, self).__init__()
        loadUi("telaInicial.ui", self)
        self.btnEntrar.clicked.connect(self.logar)
        self.btnCad.clicked.connect(self.cadastrar)

    #Função para carregar a tela
    def logar(self):
        login = telaLogin()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    #Função para carregar a tela
    def cadastrar(self):
        cadastre = telaCadastro()
        widget.addWidget(cadastre)
        widget.setCurrentIndex(widget.currentIndex()+1)

#Completa
class telaCadastro(QDialog):
    #Chama a tela
    def __init__(self):
        super(telaCadastro, self).__init__()
        loadUi("cadastro.ui", self)
        self.btnCad.clicked.connect(self.cadastroFunc)
        self.btnVolta.clicked.connect(self.voltaFunc)

    #Cadastra no banco de dados
    def cadastroFunc(self):    
        nome = self.txtNomeUser.text()
        senha = self.txtSenha.text()
        if len(nome) > 0 or len(senha) > 0:
            string_conexao = pyodbc.connect('Driver={SQL Server Native Client 11.0}; Server=localhost; Database=Projeto; UID=sa; PWD=dba')
            cursor = string_conexao.cursor()
            cursor.execute('INSERT INTO usuarios(nome, senha) VALUES(?, ?)', nome, senha)
            string_conexao.commit()
            string_conexao.close()
        else:
            self.lblErro.setText("Preencha todos os campos!")
    
    #Botão voltar
    def voltaFunc(self):
        volta = telaEntrada()
        widget.addWidget(volta)
        widget.setCurrentIndex(widget.currentIndex()+1)            

#Completa
class telaLogin(QDialog):
    #Chama a tela
    def __init__(self):
        super(telaLogin, self).__init__()
        loadUi("login.ui", self)
        self.txtSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnLogin.clicked.connect(self.logar)
        self.btnVolta.clicked.connect(self.voltaFunc)
    
    #Verificação para logar
    def logar(self):
        user = self.txtLogin.text()
        senha = self.txtSenha.text()
        if len(user) > 0 or len(senha) > 0:
            string_conexao = pyodbc.connect('Driver={SQL Server Native Client 11.0}; Server=localhost; Database=Projeto; UID=sa; PWD=dba')
            cursor = string_conexao.cursor()
            try:
                cursor.execute("SELECT senha FROM usuarios WHERE nome ='{}'".format(user))
                senha_temp = cursor.fetchall()
                senha_temp = senha_temp[0][0]
                string_conexao.close()
                if senha == senha_temp:
                    entrar = telaFinal()
                    widget.addWidget(entrar)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.lblErro.setText('Senha incorreta.')  
            except:
                self.lblErro.setText('Erro ao validar o login.')
        else:
            self.lblErro.setText("Preencha todos os campos!")

    #Botão voltar
    def voltaFunc(self):
        volta = telaEntrada()
        widget.addWidget(volta)
        widget.setCurrentIndex(widget.currentIndex()+1)   

#Completa
class telaFinal(QDialog):
    #Chama a tela
    def __init__(self):
        super(telaFinal, self).__init__()
        loadUi("telaFinal.ui", self)
        self.btnVolta.clicked.connect(self.home)
        self.btnExcluir.clicked.connect(self.excluirFunc)

        #Exibe lista dos usuários cadastrados
        #self.tbl.setColumnWidth(0, 30)
        #self.tbl.setColumnWidth(1, 125)
        #self.tbl.setColumnWidth(2, 75)
        #self.tbl.setColumnWidth(3, 50)
        #self.tbl.setHorizontalHeaderLabels(['Id', 'Nome', 'Senha', 'Eoq'])
        self.carregar()

    #Conectar ao banco e listar cadastros
    def carregar(self):
        string_conexao = pyodbc.connect('Driver={SQL Server Native Client 11.0}; Server=localhost; Database=Projeto; UID=sa; PWD=dba')
        cursor = string_conexao.cursor()
        #cursor.execute("SELECT * FROM usuarios WHERE status != 2")
        cursor.execute("SELECT * FROM usuarios") 
        dados_lidos = cursor.fetchall()
        self.tbl.setRowCount(len(dados_lidos))
        self.tbl.setColumnCount(4)

        for i in range(0, len(dados_lidos)):
            for j in range(0, 4):
                self.tbl.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        string_conexao.close()

    #Botão voltar
    def home(self):
        volta = telaEntrada()
        widget.addWidget(volta)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    #Botão excluir
    def excluirFunc(self):
        apaga = excluir()
        widget.addWidget(apaga)
        widget.setCurrentIndex(widget.currentIndex()+1)   

#Completa
class excluir(QDialog):
    #Chama a tela
    def __init__(self):
        super(excluir, self).__init__()
        loadUi("excluir.ui", self)
        self.btnExcluir.clicked.connect(self.excluir)
        self.btnVolta.clicked.connect(self.voltaFunc)
    
    #Botão excluir
    def excluir(self):
        id = self.txtId.text()
        if len(id) > 0:
            id = int(id)
            string_conexao = pyodbc.connect('Driver={SQL Server Native Client 11.0}; Server=localhost; Database=Projeto; UID=sa; PWD=dba')
            cursor = string_conexao.cursor()    
            try:
                cursor.execute("SELECT status FROM usuarios WHERE codigo ='{}'".format(id))
                status_temp = cursor.fetchall()
                status_temp = int(status_temp[0][0])
                if status_temp != 2:
                    cursor.execute("UPDATE usuarios SET status ='{}' WHERE codigo ='{}'".format('2',id))
                    string_conexao.commit()
                    self.lblErro.setText('Usuário foi desativado.')
                else:
                    self.lblErro.setText('Este usuário já foi desativado.')
            except:
                self.lblErro.setText('Não há nenhum usuário com este código.')
            string_conexao.close()
        else:
            self.lblErro.setText("Preencha todos os campos!")

    #Botão voltar
    def voltaFunc(self):
        volta = telaEntrada()
        widget.addWidget(volta)
        widget.setCurrentIndex(widget.currentIndex()+1)

#main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = telaEntrada()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(461)
    widget.setFixedWidth(461)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")