# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 804)
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
        self.login_area = QtWidgets.QFrame(self.conteudo)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(45, 40, 360, 90))
        self.logo.setMaximumSize(QtCore.QSize(360, 90))
        self.logo.setStyleSheet("background-image: url(:/logo/logo_360x90_-removebg-preview.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.usuario_lineEdit = QtWidgets.QLineEdit(self.login_area)
        self.usuario_lineEdit.setGeometry(QtCore.QRect(85, 200, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.usuario_lineEdit.setFont(font)
        self.usuario_lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.usuario_lineEdit.setFrame(True)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.senha_lineEdit = QtWidgets.QLineEdit(self.login_area)
        self.senha_lineEdit.setGeometry(QtCore.QRect(85, 280, 280, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.senha_lineEdit.setFont(font)
        self.senha_lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.senha_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_lineEdit.setObjectName("senha_lineEdit")
        self.btn_login = QtWidgets.QPushButton(self.login_area)
        self.btn_login.setGeometry(QtCore.QRect(85, 400, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton{\n"
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
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.login_area)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.usuario_lineEdit.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.senha_lineEdit.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.btn_login.setText(_translate("MainWindow", "Conectar"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
