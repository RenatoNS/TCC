import pandas as pd
import numpy as np
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)

    def setupUi(self, MainWindow1):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 600)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 367, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout.addWidget(self.comboBox_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.comboBox_7 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.verticalLayout.addWidget(self.comboBox_7)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.comboBox_8 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.verticalLayout.addWidget(self.comboBox_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.comboBox_9 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.verticalLayout.addWidget(self.comboBox_9)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox_10 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.verticalLayout.addWidget(self.comboBox_10)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 490, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Qual sua faixa etária?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Abaixo de 25 anos"))
        self.comboBox.setItemText(1, _translate("MainWindow", "25 até 40 anos"))
        self.comboBox.setItemText(2, _translate("MainWindow", "41 até 55 anos"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Acima de 56 anos"))
        self.label_2.setText(
            _translate("MainWindow", "Qual Percentual do seu patrimônio está investido?(Carros, casa, ações, etc)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Até 25% "))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Entre 26% e 50%"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Entre 51% e 75%"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Mais de 76% "))
        self.label_3.setText(_translate("MainWindow", "Qual o objetivo dos seus investimentos?"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Aposentadoria  "))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Proteção do capital"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Compra de um bem"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Crescimento significativo do patrimônio"))
        self.label_4.setText(
            _translate("MainWindow", "Como você se sentiria caso verificasse perdas em seus investimentos?"))
        self.comboBox_5.setItemText(0, _translate("MainWindow",
                                                  "Extremamente desanimado. Não quero passar nunca por essa situação"))
        self.comboBox_5.setItemText(1, _translate("MainWindow",
                                                  "Moderadamente desanimado. Posso passar por essa situação, mas não gostaria"))
        self.comboBox_5.setItemText(2, _translate("MainWindow",
                                                  "Levemente desanimado. Entendo que a perda faz parte do processo de investimento"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Normal. Tudo bem passar por isso"))
        self.label_6.setText(
            _translate("MainWindow", "Quais são as aplicações financeiras em que você tem experiência?"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Não Possuo"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Renda Fixa"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Renda Fixa e Ações de Longo Prazo"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Outras além das anteriores"))
        self.label_8.setText(_translate("MainWindow", "Possui algum conhecimento sobre o mercado financeiro?"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Não"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Pouco"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Médio"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Bastante"))
        self.label_10.setText(_translate("MainWindow", "Qual sua escoladidade?"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Ensino fundamental ou inferior"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Ensino Médio "))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Ensino Superior"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Maior que Ensino Superior"))
        self.label_9.setText(_translate("MainWindow", "Você costuma operar financeiramente com que frequência?"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Pouquíssima"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Pouco"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Média"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Alta"))
        self.label_7.setText(_translate("MainWindow", "Você espera precisar de renda extra no futuro?"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Não. Pretendo diminuir"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Não. Pretendo ter as mesmas que tenho hoje"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Sim. Pretendo aumentar "))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "Sim. Pretendo ter um grande aumento"))
        self.label_5.setText(
            _translate("MainWindow", "Qual o tempo disponível que você tem para manter seu dinheiro aplicado? "))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Menos de 1 ano"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "De 1 até 2 anos"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "De 2 até 3 anos"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Mais de 3 anos "))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButton.clicked.connect(self.clicked)

    def clicked(self):
        opiniao = [self.comboBox.currentIndex(),
                   self.comboBox_2.currentIndex(),
                   self.comboBox_3.currentIndex(),
                   self.comboBox_4.currentIndex(),
                   self.comboBox_5.currentIndex(),
                   self.comboBox_6.currentIndex(),
                   self.comboBox_7.currentIndex(),
                   self.comboBox_8.currentIndex(),
                   self.comboBox_9.currentIndex(),
                   self.comboBox_10.currentIndex()]

        y = np.array([self.comboBox.currentText(),
                      self.comboBox_2.currentText(),
                      self.comboBox_3.currentText(),
                      self.comboBox_4.currentText(),
                      self.comboBox_5.currentText(),
                      self.comboBox_6.currentText(),
                      self.comboBox_7.currentText(),
                      self.comboBox_8.currentText(),
                      self.comboBox_9.currentText(),
                      self.comboBox_10.currentText()
                      ])
        df = pd.DataFrame(y)
        opiniao.sort()
        if (opiniao[4] == 0):
            perfil = "Conservador"
        elif (opiniao[4] == 1):
            perfil = "Conservador"
        elif (opiniao[4] == 2):
            perfil = "Moderado"
        else:
            perfil = "Agressivo"
        print(perfil)
        MainWindow.close()


app = QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow3()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
