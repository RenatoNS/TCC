from PyQt5 import QtCore, QtGui, QtWidgets
from Fluxo import Fluxo
from Comunicacao import Conexao


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1217, 881)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 700))
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
        self.formulario_area = QtWidgets.QFrame(self.conteudo)
        self.formulario_area.setEnabled(True)
        self.formulario_area.setMaximumSize(QtCore.QSize(1100, 900))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.formulario_area.setFont(font)
        self.formulario_area.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px;")
        self.formulario_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.formulario_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formulario_area.setObjectName("formulario_area")
        self.logo = QtWidgets.QFrame(self.formulario_area)
        self.logo.setGeometry(QtCore.QRect(405, 10, 360, 90))
        self.logo.setMaximumSize(QtCore.QSize(360, 90))
        self.logo.setStyleSheet("background-image: url(:/logo/logo_360x90_-removebg-preview.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.btn_formulario_cadastrar = QtWidgets.QPushButton(self.formulario_area)
        self.btn_formulario_cadastrar.clicked.connect(self.click_cadastrar)
        self.btn_formulario_cadastrar.setGeometry(QtCore.QRect(400, 730, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_formulario_cadastrar.setFont(font)
        self.btn_formulario_cadastrar.setStyleSheet("QPushButton{\n"
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
        self.btn_formulario_cadastrar.setObjectName("btn_formulario_cadastrar")
        self.Q1_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q1_comboBox.setGeometry(QtCore.QRect(15, 210, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q1_comboBox.setFont(font)
        self.Q1_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q1_comboBox.setObjectName("Q1_comboBox")
        self.Q1_comboBox.addItem("")
        self.Q1_comboBox.addItem("")
        self.Q1_comboBox.addItem("")
        self.Q1_comboBox.addItem("")
        self.Q2_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q2_comboBox.setGeometry(QtCore.QRect(20, 340, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q2_comboBox.setFont(font)
        self.Q2_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q2_comboBox.setObjectName("Q2_comboBox")
        self.Q2_comboBox.addItem("")
        self.Q2_comboBox.addItem("")
        self.Q2_comboBox.addItem("")
        self.Q2_comboBox.addItem("")
        self.Q3_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q3_comboBox.setGeometry(QtCore.QRect(20, 470, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q3_comboBox.setFont(font)
        self.Q3_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q3_comboBox.setObjectName("Q3_comboBox")
        self.Q3_comboBox.addItem("")
        self.Q3_comboBox.addItem("")
        self.Q3_comboBox.addItem("")
        self.Q3_comboBox.addItem("")
        self.Q4_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q4_comboBox.setGeometry(QtCore.QRect(20, 600, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q4_comboBox.setFont(font)
        self.Q4_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q4_comboBox.setObjectName("Q4_comboBox")
        self.Q4_comboBox.addItem("")
        self.Q4_comboBox.addItem("")
        self.Q4_comboBox.addItem("")
        self.Q4_comboBox.addItem("")
        self.Q5_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q5_comboBox.setGeometry(QtCore.QRect(400, 210, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q5_comboBox.setFont(font)
        self.Q5_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q5_comboBox.setObjectName("Q5_comboBox")
        self.Q5_comboBox.addItem("")
        self.Q5_comboBox.addItem("")
        self.Q5_comboBox.addItem("")
        self.Q5_comboBox.addItem("")
        self.Q6_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q6_comboBox.setGeometry(QtCore.QRect(400, 340, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q6_comboBox.setFont(font)
        self.Q6_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q6_comboBox.setObjectName("Q6_comboBox")
        self.Q6_comboBox.addItem("")
        self.Q6_comboBox.addItem("")
        self.Q6_comboBox.addItem("")
        self.Q6_comboBox.addItem("")
        self.Q7_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q7_comboBox.setGeometry(QtCore.QRect(400, 470, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q7_comboBox.setFont(font)
        self.Q7_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q7_comboBox.setObjectName("Q7_comboBox")
        self.Q7_comboBox.addItem("")
        self.Q7_comboBox.addItem("")
        self.Q7_comboBox.addItem("")
        self.Q7_comboBox.addItem("")
        self.Q8_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q8_comboBox.setGeometry(QtCore.QRect(400, 600, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q8_comboBox.setFont(font)
        self.Q8_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q8_comboBox.setObjectName("Q8_comboBox")
        self.Q8_comboBox.addItem("")
        self.Q8_comboBox.addItem("")
        self.Q8_comboBox.addItem("")
        self.Q8_comboBox.addItem("")
        self.Q9_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q9_comboBox.setGeometry(QtCore.QRect(820, 210, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q9_comboBox.setFont(font)
        self.Q9_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q9_comboBox.setObjectName("Q9_comboBox")
        self.Q9_comboBox.addItem("")
        self.Q9_comboBox.addItem("")
        self.Q9_comboBox.addItem("")
        self.Q9_comboBox.addItem("")
        self.Q10_comboBox = QtWidgets.QComboBox(self.formulario_area)
        self.Q10_comboBox.setGeometry(QtCore.QRect(820, 340, 260, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Q10_comboBox.setFont(font)
        self.Q10_comboBox.setStyleSheet("QComboBox{\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(250,250,250);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(250, 250, 250);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(16, 5, 136);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Q10_comboBox.setObjectName("Q10_comboBox")
        self.Q10_comboBox.addItem("")
        self.Q10_comboBox.addItem("")
        self.Q10_comboBox.addItem("")
        self.Q10_comboBox.addItem("")
        self.Questao_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_1_label.setGeometry(QtCore.QRect(20, 180, 230, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_1_label.setFont(font)
        self.Questao_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_1_label.setObjectName("Questao_1_label")
        self.Questao_2_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_2_1_label.setGeometry(QtCore.QRect(20, 290, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_2_1_label.setFont(font)
        self.Questao_2_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_2_1_label.setObjectName("Questao_2_1_label")
        self.Questao_3_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_3_label.setGeometry(QtCore.QRect(20, 440, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_3_label.setFont(font)
        self.Questao_3_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_3_label.setObjectName("Questao_3_label")
        self.Questao_4_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_4_1_label.setGeometry(QtCore.QRect(20, 550, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_4_1_label.setFont(font)
        self.Questao_4_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_4_1_label.setObjectName("Questao_4_1_label")
        self.Questao_5_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_5_1_label.setGeometry(QtCore.QRect(400, 160, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_5_1_label.setFont(font)
        self.Questao_5_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_5_1_label.setObjectName("Questao_5_1_label")
        self.Questao_6_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_6_1_label.setGeometry(QtCore.QRect(400, 290, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_6_1_label.setFont(font)
        self.Questao_6_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_6_1_label.setObjectName("Questao_6_1_label")
        self.Questao_7_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_7_label.setGeometry(QtCore.QRect(400, 440, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_7_label.setFont(font)
        self.Questao_7_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_7_label.setObjectName("Questao_7_label")
        self.Questao_8_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_8_1_label.setGeometry(QtCore.QRect(400, 550, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_8_1_label.setFont(font)
        self.Questao_8_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_8_1_label.setObjectName("Questao_8_1_label")
        self.Questao_9_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_9_1_label.setGeometry(QtCore.QRect(820, 160, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_9_1_label.setFont(font)
        self.Questao_9_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_9_1_label.setObjectName("Questao_9_1_label")
        self.Questao_10_1_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_10_1_label.setGeometry(QtCore.QRect(820, 290, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_10_1_label.setFont(font)
        self.Questao_10_1_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_10_1_label.setObjectName("Questao_10_1_label")
        self.Questao_2_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_2_2_label.setGeometry(QtCore.QRect(20, 310, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_2_2_label.setFont(font)
        self.Questao_2_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_2_2_label.setObjectName("Questao_2_2_label")
        self.Questao_4_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_4_2_label.setGeometry(QtCore.QRect(20, 570, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_4_2_label.setFont(font)
        self.Questao_4_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_4_2_label.setObjectName("Questao_4_2_label")
        self.Questao_5_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_5_2_label.setGeometry(QtCore.QRect(400, 180, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_5_2_label.setFont(font)
        self.Questao_5_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_5_2_label.setObjectName("Questao_5_2_label")
        self.Questao_6_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_6_2_label.setGeometry(QtCore.QRect(400, 310, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_6_2_label.setFont(font)
        self.Questao_6_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_6_2_label.setObjectName("Questao_6_2_label")
        self.Questao_8_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_8_2_label.setGeometry(QtCore.QRect(400, 570, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_8_2_label.setFont(font)
        self.Questao_8_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_8_2_label.setObjectName("Questao_8_2_label")
        self.Questao_9_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_9_2_label.setGeometry(QtCore.QRect(820, 180, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_9_2_label.setFont(font)
        self.Questao_9_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_9_2_label.setObjectName("Questao_9_2_label")
        self.Questao_10_2_label = QtWidgets.QLabel(self.formulario_area)
        self.Questao_10_2_label.setGeometry(QtCore.QRect(820, 310, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Questao_10_2_label.setFont(font)
        self.Questao_10_2_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Questao_10_2_label.setObjectName("Questao_10_2_label")
        self.horizontalLayout.addWidget(self.formulario_area)
        self.verticalLayout.addWidget(self.conteudo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1217, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Formulário"))
        self.btn_formulario_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.Q1_comboBox.setItemText(0, _translate("MainWindow", "Abaixo de 25 anos"))
        self.Q1_comboBox.setItemText(1, _translate("MainWindow", "25 até 40 anos"))
        self.Q1_comboBox.setItemText(2, _translate("MainWindow", "41 até 55 anos"))
        self.Q1_comboBox.setItemText(3, _translate("MainWindow", "Acima de 56 anos"))
        self.Q2_comboBox.setItemText(0, _translate("MainWindow", "Até 25%"))
        self.Q2_comboBox.setItemText(1, _translate("MainWindow", "Entre 26% e 50%"))
        self.Q2_comboBox.setItemText(2, _translate("MainWindow", "Entre 51% e 75%"))
        self.Q2_comboBox.setItemText(3, _translate("MainWindow", "Mais de 76%"))
        self.Q3_comboBox.setItemText(0, _translate("MainWindow", "Aposentadoria"))
        self.Q3_comboBox.setItemText(1, _translate("MainWindow", "Proteção do capital"))
        self.Q3_comboBox.setItemText(2, _translate("MainWindow", "Compra de um bem"))
        self.Q3_comboBox.setItemText(3, _translate("MainWindow", "Crescimento significativo do patrimônio"))
        self.Q4_comboBox.setItemText(0, _translate("MainWindow", "Extremamente desanimado"))
        self.Q4_comboBox.setItemText(1, _translate("MainWindow", "Moderadamente desanimado"))
        self.Q4_comboBox.setItemText(2, _translate("MainWindow", "Levemente desanimado"))
        self.Q4_comboBox.setItemText(3, _translate("MainWindow", "Normal"))
        self.Q5_comboBox.setItemText(0, _translate("MainWindow", "Não possuo"))
        self.Q5_comboBox.setItemText(1, _translate("MainWindow", "Renda fixa"))
        self.Q5_comboBox.setItemText(2, _translate("MainWindow", "Renda fixa e ações de longo prazo"))
        self.Q5_comboBox.setItemText(3, _translate("MainWindow", "Outras além das anteriores"))
        self.Q6_comboBox.setItemText(0, _translate("MainWindow", "Não"))
        self.Q6_comboBox.setItemText(1, _translate("MainWindow", "Pouco"))
        self.Q6_comboBox.setItemText(2, _translate("MainWindow", "Médio"))
        self.Q6_comboBox.setItemText(3, _translate("MainWindow", "Bastante"))
        self.Q7_comboBox.setItemText(0, _translate("MainWindow", "Ensino fundamental ou inferior"))
        self.Q7_comboBox.setItemText(1, _translate("MainWindow", "Ensino médio"))
        self.Q7_comboBox.setItemText(2, _translate("MainWindow", "Ensino superior"))
        self.Q7_comboBox.setItemText(3, _translate("MainWindow", "Maior que ensino superior"))
        self.Q8_comboBox.setItemText(0, _translate("MainWindow", "Pouquíssima"))
        self.Q8_comboBox.setItemText(1, _translate("MainWindow", "Pouca"))
        self.Q8_comboBox.setItemText(2, _translate("MainWindow", "Média"))
        self.Q8_comboBox.setItemText(3, _translate("MainWindow", "Alta"))
        self.Q9_comboBox.setItemText(0, _translate("MainWindow", "Não. Pretendo diminuir"))
        self.Q9_comboBox.setItemText(1, _translate("MainWindow", "Não. Pretendo manter as que tenho"))
        self.Q9_comboBox.setItemText(2, _translate("MainWindow", "Sim. Pretendo aumentar"))
        self.Q9_comboBox.setItemText(3, _translate("MainWindow", "Sim. Pretendo ter um grande aumento"))
        self.Q10_comboBox.setItemText(0, _translate("MainWindow", "Menos de 1 ano"))
        self.Q10_comboBox.setItemText(1, _translate("MainWindow", "De 1 até 2 anos"))
        self.Q10_comboBox.setItemText(2, _translate("MainWindow", "De 2 até 3 anos"))
        self.Q10_comboBox.setItemText(3, _translate("MainWindow", "Mais de 3 anos"))
        self.Questao_1_label.setText(_translate("MainWindow", "Qual sua faixa etária?"))
        self.Questao_2_1_label.setText(_translate("MainWindow", "Qual percentual do seu patrimônio está"))
        self.Questao_3_label.setText(_translate("MainWindow", "Qual o objetivo dos seus investimentos?"))
        self.Questao_4_1_label.setText(_translate("MainWindow", "Como você se sentiria caso verificasse perdas"))
        self.Questao_5_1_label.setText(_translate("MainWindow", "Quais são as aplicações financeiras"))
        self.Questao_6_1_label.setText(_translate("MainWindow", "Possui algum conhecimento sobre"))
        self.Questao_7_label.setText(_translate("MainWindow", "Qual sua escolaridade?"))
        self.Questao_8_1_label.setText(_translate("MainWindow", "Você costuma operar financeiramente"))
        self.Questao_9_1_label.setText(_translate("MainWindow", "Você espera precisar de renda extra"))
        self.Questao_10_1_label.setText(_translate("MainWindow", "Qual o tempo disponível que você"))
        self.Questao_2_2_label.setText(_translate("MainWindow", "investido? (Carros, casas, ações, etc)"))
        self.Questao_4_2_label.setText(_translate("MainWindow", "em seus investimentos?"))
        self.Questao_5_2_label.setText(_translate("MainWindow", "em que você tem experiência?"))
        self.Questao_6_2_label.setText(_translate("MainWindow", "o mercado financeiro?"))
        self.Questao_8_2_label.setText(_translate("MainWindow", "com que frequência?"))
        self.Questao_9_2_label.setText(_translate("MainWindow", "no futuro?"))
        self.Questao_10_2_label.setText(_translate("MainWindow", "tem para manter seu dinheiro aplicado?"))

    def click_cadastrar(self):
        perfil = [self.Q1_comboBox.currentIndex(),
             self.Q2_comboBox.currentIndex(),
             self.Q3_comboBox.currentIndex(),
             self.Q4_comboBox.currentIndex(),
             self.Q5_comboBox.currentIndex(),
             self.Q6_comboBox.currentIndex(),
             self.Q7_comboBox.currentIndex(),
             self.Q8_comboBox.currentIndex(),
             self.Q9_comboBox.currentIndex(),
             self.Q10_comboBox.currentIndex()]

        respostas = [self.Q1_comboBox.currentText(),
             self.Q2_comboBox.currentText(),
             self.Q3_comboBox.currentText(),
             self.Q4_comboBox.currentText(),
             self.Q5_comboBox.currentText(),
             self.Q6_comboBox.currentText(),
             self.Q7_comboBox.currentText(),
             self.Q8_comboBox.currentText(),
             self.Q9_comboBox.currentText(),
             self.Q10_comboBox.currentText()]

        checker = Conexao()
        if (checker.verificar_vazio()):
                checker.criar_primeira_conta(respostas,perfil)
                fluxo = Fluxo()
                fluxo.window_login()
                MainWindow.close()

        else:
                checker.criar_conta(respostas,perfil)
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
