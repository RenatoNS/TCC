# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valor_investimento.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Fluxo import Fluxo


class Ui_MainWindow_valor_investimento(object):
    def setupUi(self, MainWindow_valor_investimento):
        MainWindow_valor_investimento.setObjectName("MainWindow_valor_investimento")
        MainWindow_valor_investimento.resize(1104, 879)
        MainWindow_valor_investimento.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icone_janela/icone_janela.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_valor_investimento.setWindowIcon(icon)
        MainWindow_valor_investimento.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget_valor_investimento = QtWidgets.QWidget(MainWindow_valor_investimento)
        self.centralwidget_valor_investimento.setObjectName("centralwidget_valor_investimento")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget_valor_investimento)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top_valorinvestimento = QtWidgets.QFrame(self.centralwidget_valor_investimento)
        self.frame_top_valorinvestimento.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_top_valorinvestimento.setStyleSheet("")
        self.frame_top_valorinvestimento.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_valorinvestimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_valorinvestimento.setObjectName("frame_top_valorinvestimento")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top_valorinvestimento)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.frame_top_valorinvestimento)
        self.conteudo_valor_investimento = QtWidgets.QFrame(self.centralwidget_valor_investimento)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.conteudo_valor_investimento.setFont(font)
        self.conteudo_valor_investimento.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.conteudo_valor_investimento.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteudo_valor_investimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo_valor_investimento.setObjectName("conteudo_valor_investimento")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteudo_valor_investimento)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valor_investimento_area = QtWidgets.QFrame(self.conteudo_valor_investimento)
        self.valor_investimento_area.setMaximumSize(QtCore.QSize(450, 550))
        self.valor_investimento_area.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px;")
        self.valor_investimento_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.valor_investimento_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.valor_investimento_area.setObjectName("valor_investimento_area")
        self.logo = QtWidgets.QFrame(self.valor_investimento_area)
        self.logo.setGeometry(QtCore.QRect(45, 40, 360, 90))
        self.logo.setMaximumSize(QtCore.QSize(360, 90))
        self.logo.setStyleSheet("background-image: url(:/logo/logo_360x90_-removebg-preview.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.lineEdit_valor_investimento_valor = QtWidgets.QLineEdit(self.valor_investimento_area)
        self.lineEdit_valor_investimento_valor.setGeometry(QtCore.QRect(85, 210, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_valor_investimento_valor.setFont(font)
        self.lineEdit_valor_investimento_valor.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_valor_investimento_valor.setFrame(True)
        self.lineEdit_valor_investimento_valor.setObjectName("lineEdit_valor_investimento_valor")
        self.btn_valor_investimento_ok = QtWidgets.QPushButton(self.valor_investimento_area)
        self.btn_valor_investimento_ok.clicked.connect(self.pesquisar)
        self.btn_valor_investimento_ok.setGeometry(QtCore.QRect(85, 450, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_valor_investimento_ok.setFont(font)
        self.btn_valor_investimento_ok.setStyleSheet("QPushButton{\n"
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
        self.btn_valor_investimento_ok.setObjectName("btn_valor_investimento_ok")
        self.label_valor_investimento_valor = QtWidgets.QLabel(self.valor_investimento_area)
        self.label_valor_investimento_valor.setGeometry(QtCore.QRect(94, 180, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_valor_investimento_valor.setFont(font)
        self.label_valor_investimento_valor.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_valor_investimento_valor.setObjectName("label_valor_investimento_valor")
        self.label_valor_investimento_tempo1 = QtWidgets.QLabel(self.valor_investimento_area)
        self.label_valor_investimento_tempo1.setGeometry(QtCore.QRect(99, 300, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_valor_investimento_tempo1.setFont(font)
        self.label_valor_investimento_tempo1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_valor_investimento_tempo1.setObjectName("label_valor_investimento_tempo1")
        self.label_valor_investimento_tempo2 = QtWidgets.QLabel(self.valor_investimento_area)
        self.label_valor_investimento_tempo2.setGeometry(QtCore.QRect(99, 320, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_valor_investimento_tempo2.setFont(font)
        self.label_valor_investimento_tempo2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_valor_investimento_tempo2.setObjectName("label_valor_investimento_tempo2")
        self.lineEdit_valor_investimento_valor_2 = QtWidgets.QLineEdit(self.valor_investimento_area)
        self.lineEdit_valor_investimento_valor_2.setGeometry(QtCore.QRect(85, 350, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_valor_investimento_valor_2.setFont(font)
        self.lineEdit_valor_investimento_valor_2.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_valor_investimento_valor_2.setFrame(True)
        self.lineEdit_valor_investimento_valor_2.setObjectName("lineEdit_valor_investimento_valor_2")
        self.radioButton = QtWidgets.QRadioButton(self.valor_investimento_area)
        self.radioButton.setGeometry(QtCore.QRect(90, 420, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.valor_investimento_area)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 420, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.valor_investimento_area)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 420, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.valor_investimento_area)
        self.verticalLayout.addWidget(self.conteudo_valor_investimento)
        self.frame_bot_valor_investimento = QtWidgets.QFrame(self.centralwidget_valor_investimento)
        self.frame_bot_valor_investimento.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_bot_valor_investimento.setStyleSheet("")
        self.frame_bot_valor_investimento.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bot_valor_investimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot_valor_investimento.setObjectName("frame_bot_valor_investimento")
        self.verticalLayout.addWidget(self.frame_bot_valor_investimento)
        MainWindow_valor_investimento.setCentralWidget(self.centralwidget_valor_investimento)
        self.menubar = QtWidgets.QMenuBar(MainWindow_valor_investimento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_valor_investimento.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow_valor_investimento)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_valor_investimento)

    def retranslateUi(self, MainWindow_valor_investimento):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_valor_investimento.setWindowTitle(_translate("MainWindow_valor_investimento", "Investimento"))
        self.lineEdit_valor_investimento_valor.setPlaceholderText(_translate("MainWindow_valor_investimento", "Valor investido"))
        self.btn_valor_investimento_ok.setText(_translate("MainWindow_valor_investimento", "Ok"))
        self.label_valor_investimento_valor.setText(_translate("MainWindow_valor_investimento", "Qual será o valor investido hoje?"))
        self.label_valor_investimento_tempo1.setText(_translate("MainWindow_valor_investimento", "Por quanto tempo esse valor"))
        self.label_valor_investimento_tempo2.setText(_translate("MainWindow_valor_investimento", "poderá ficar aplicado?"))
        self.lineEdit_valor_investimento_valor_2.setPlaceholderText(_translate("MainWindow_valor_investimento", "Tempo da aplicação"))
        self.radioButton.setText(_translate("MainWindow_valor_investimento", "Dias"))
        self.radioButton_2.setText(_translate("MainWindow_valor_investimento", "Meses"))
        self.radioButton_3.setText(_translate("MainWindow_valor_investimento", "Anos"))

    def pesquisar(self):
        pass

import files_rc
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow_valor_investimento = QtWidgets.QMainWindow()
ui = Ui_MainWindow_valor_investimento()
ui.setupUi(MainWindow_valor_investimento)
MainWindow_valor_investimento.show()
app.exec_()
