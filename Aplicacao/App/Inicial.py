from PyQt5 import QtCore, QtGui, QtWidgets
from Fluxo import Fluxo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 831)
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
        self.inicial_area = QtWidgets.QFrame(self.conteudo)
        self.inicial_area.setMaximumSize(QtCore.QSize(450, 550))
        self.inicial_area.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px;")
        self.inicial_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inicial_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inicial_area.setObjectName("inicial_area")
        self.inicial_logo = QtWidgets.QFrame(self.inicial_area)
        self.inicial_logo.setGeometry(QtCore.QRect(45, 40, 360, 90))
        self.inicial_logo.setMaximumSize(QtCore.QSize(360, 90))
        self.inicial_logo.setStyleSheet("background-image: url(:/logo/logo_360x90_-removebg-preview.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.inicial_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inicial_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inicial_logo.setObjectName("inicial_logo")
        self.label_inicial_bemVindo = QtWidgets.QLabel(self.inicial_area)
        self.label_inicial_bemVindo.setGeometry(QtCore.QRect(40, 220, 370, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_inicial_bemVindo.setFont(font)
        self.label_inicial_bemVindo.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_inicial_bemVindo.setObjectName("label_inicial_bemVindo")
        self.btn_inicial_sim = QtWidgets.QPushButton(self.inicial_area)
        self.btn_inicial_sim.setGeometry(QtCore.QRect(50, 340, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_inicial_sim.setFont(font)
        self.btn_inicial_sim.setStyleSheet("QPushButton{\n"
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
        self.btn_inicial_sim.setObjectName("btn_inicial_sim")
        self.btn_inicial_sim.clicked.connect(self.click_sim)
        self.btn_inicial_nao = QtWidgets.QPushButton(self.inicial_area)
        self.btn_inicial_nao.setGeometry(QtCore.QRect(280, 340, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_inicial_nao.setFont(font)
        self.btn_inicial_nao.setStyleSheet("QPushButton{\n"
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
        self.btn_inicial_nao.setObjectName("btn_inicial_nao")
        self.btn_inicial_nao.clicked.connect(self.click_nao)
        self.horizontalLayout.addWidget(self.inicial_area)
        self.verticalLayout.addWidget(self.conteudo)
        self.inicial_frame_bot = QtWidgets.QFrame(self.centralwidget)
        self.inicial_frame_bot.setMaximumSize(QtCore.QSize(16777215, 35))
        self.inicial_frame_bot.setStyleSheet("")
        self.inicial_frame_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inicial_frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inicial_frame_bot.setObjectName("inicial_frame_bot")
        self.verticalLayout.addWidget(self.inicial_frame_bot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicial"))
        self.label_inicial_bemVindo.setText(_translate("MainWindow", "Bem-vindo(a) a Money MS, você já possui cadastro? "))
        self.btn_inicial_sim.setText(_translate("MainWindow", "Sim"))
        self.btn_inicial_nao.setText(_translate("MainWindow", "Não"))

    def click_nao(self):
        fluxo = Fluxo()
        fluxo.window_cadastro()
        MainWindow.close()

    def click_sim(self):
        fluxo = Fluxo()
        fluxo.window_login()
        MainWindow.close()

import files_rc
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
