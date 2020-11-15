# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from MoneyMS import Fluxo
from Comunicacao import Conexao
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 879)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icone_janela/icone_janela.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_top.setStyleSheet("")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.frame_top)
        self.conteudo = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.conteudo.setFont(font)
        self.conteudo.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteudo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cadastro_area = QtWidgets.QFrame(self.conteudo)
        self.cadastro_area.setMaximumSize(QtCore.QSize(450, 550))
        self.cadastro_area.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                         "border-radius: 10px;")
        self.cadastro_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cadastro_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cadastro_area.setObjectName("cadastro_area")
        self.logo = QtWidgets.QFrame(self.cadastro_area)
        self.logo.setGeometry(QtCore.QRect(45, 40, 360, 90))
        self.logo.setMaximumSize(QtCore.QSize(360, 90))
        self.logo.setStyleSheet("background-image: url(:/logo/logo_360x90_-removebg-preview.png);\n"
                                "background-repeat: no-repeat;\n"
                                "background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.lineEdit_cadastro_usuario = QtWidgets.QLineEdit(self.cadastro_area)
        self.lineEdit_cadastro_usuario.setGeometry(QtCore.QRect(85, 220, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_cadastro_usuario.setFont(font)
        self.lineEdit_cadastro_usuario.setStyleSheet("QLineEdit{\n"
                                                     "    color: rgb(0, 0, 0);\n"
                                                     "    border: 2px solid rgb(250,250,250);\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 15px;\n"
                                                     "    background-color: rgb(250, 250, 250);\n"
                                                     "    color: rgb(0, 0, 0);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:hover{\n"
                                                     "    border: 2px solid rgb(16, 5, 136);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:focus{\n"
                                                     "    border: 2px solid rgb(16, 5, 136);\n"
                                                     "    color: rgb(0, 0, 0);\n"
                                                     "}")
        self.lineEdit_cadastro_usuario.setFrame(True)
        self.lineEdit_cadastro_usuario.setObjectName("lineEdit_cadastro_usuario")
        self.lineEdit_cadastro_senha = QtWidgets.QLineEdit(self.cadastro_area)
        self.lineEdit_cadastro_senha.setGeometry(QtCore.QRect(85, 350, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_cadastro_senha.setFont(font)
        self.lineEdit_cadastro_senha.setStyleSheet("QLineEdit{\n"
                                                   "    color: rgb(0, 0, 0);\n"
                                                   "    border: 2px solid rgb(250,250,250);\n"
                                                   "    border-radius: 5px;\n"
                                                   "    padding: 15px;\n"
                                                   "    background-color: rgb(250, 250, 250);\n"
                                                   "    color: rgb(0, 0, 0);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:hover{\n"
                                                   "    border: 2px solid rgb(16, 5, 136);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:focus{\n"
                                                   "    border: 2px solid rgb(16, 5, 136);\n"
                                                   "    color: rgb(0, 0, 0);\n"
                                                   "}")
        self.lineEdit_cadastro_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_cadastro_senha.setObjectName("lineEdit_cadastro_senha")
        self.btn_cadastro_cadastrar = QtWidgets.QPushButton(self.cadastro_area)
        self.btn_cadastro_cadastrar.clicked.connect(self.click_cadastrar)
        self.btn_cadastro_cadastrar.setGeometry(QtCore.QRect(85, 450, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cadastro_cadastrar.setFont(font)
        self.btn_cadastro_cadastrar.setStyleSheet("QPushButton{\n"
                                                  "    background-color: rgb(170, 170, 170);\n"
                                                  "    border: 2px solid rgb(180, 180, 180);\n"
                                                  "    border-radius: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "    background-color: rgb(180, 180, 180);\n"
                                                  "    border: 2px solid rgb(190, 190, 190);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "    \n"
                                                  "    background-color: rgb(16, 5, 136);\n"
                                                  "    border: 2px solid rgb(16, 5, 136);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "}")
        self.btn_cadastro_cadastrar.setObjectName("btn_cadastro_cadastrar")
        self.label_cadastro_usuario = QtWidgets.QLabel(self.cadastro_area)
        self.label_cadastro_usuario.setGeometry(QtCore.QRect(85, 190, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_usuario.setFont(font)
        self.label_cadastro_usuario.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_cadastro_usuario.setObjectName("label_cadastro_usuario")
        self.label_error = QtWidgets.QLabel(self.cadastro_area)
        self.label_error1 = QtWidgets.QLabel(self.cadastro_area)
        self.label_cadastro_senha = QtWidgets.QLabel(self.cadastro_area)
        self.label_cadastro_senha.setGeometry(QtCore.QRect(85, 320, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_senha.setFont(font)
        self.label_cadastro_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_cadastro_senha.setObjectName("label_cadastro_senha")
        self.label_cadastro = QtWidgets.QLabel(self.cadastro_area)
        self.label_cadastro.setGeometry(QtCore.QRect(180, 140, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro.setFont(font)
        self.label_cadastro.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_cadastro.setObjectName("label_cadastro")
        self.horizontalLayout.addWidget(self.cadastro_area)
        self.verticalLayout.addWidget(self.conteudo)
        self.frame_bot = QtWidgets.QFrame(self.centralwidget)
        self.frame_bot.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_bot.setStyleSheet("")
        self.frame_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot.setObjectName("frame_bot")
        self.verticalLayout.addWidget(self.frame_bot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro"))
        self.lineEdit_cadastro_usuario.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.lineEdit_cadastro_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.btn_cadastro_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.label_cadastro_usuario.setText(_translate("MainWindow", "Crie seu nome de usuário"))
        self.label_cadastro_senha.setText(_translate("MainWindow", "Crie sua senha"))
        self.label_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.label_error.setText("Senha Não Pode Estar Vazia")
        self.label_error.setFont(QFont('Arial', 15))
        self.label_error.move(100, 410)
        self.label_error.setStyleSheet("QLabel { color: rgb(60,60,60)}")
        self.label_error1.setText("Login Existente")
        self.label_error1.setFont(QFont('Arial', 15))
        self.label_error1.move(160, 285)
        self.label_error1.setStyleSheet("QLabel { color: rgb(60,60,60)}")



    def click_cadastrar(self):
        checker = Conexao()
        self.label_error.setStyleSheet("QLabel { color: rgb(60,60,60)}")
        self.label_error1.setStyleSheet("QLabel { color: rgb(60,60,60)}")

        if(self.lineEdit_cadastro_senha.text()==""):
            self.label_error.setStyleSheet("QLabel { color: red}")

        elif(checker.verificar_vazio()):
            checker.criar_login(self.lineEdit_cadastro_usuario.text(), self.lineEdit_cadastro_senha.text())
            fluxo = Fluxo()
            fluxo.window_formulario()
            MainWindow.close()

        else:
            frame = pd.read_csv('../Controle/Clientes.csv', encoding='ansi', sep=";")
            if(self.lineEdit_cadastro_usuario.text() in list(frame["Login"])):
                self.label_error1.setStyleSheet("QLabel { color: red}")

            else:
                checker.criar_login(self.lineEdit_cadastro_usuario.text(), self.lineEdit_cadastro_senha.text())
                fluxo = Fluxo()
                fluxo.window_formulario()
                MainWindow.close()


import files_rc
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
