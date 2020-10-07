import pandas as pd
import numpy as np
import sys
from PyQt5.QtWidgets import QLineEdit, QSlider, QMainWindow, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Investimentos"
        top = 500
        left = 500
        width = 900
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.MyUI()

    def MyUI(self):
        button = QPushButton("Pesquisar Ofertas", self)
        button.move(20, 450)
        button2 = QPushButton("Atualizar", self)
        button2.move(20, 350)
        self.button3 = QPushButton("Retornar ao Padrão", self)
        self.button3.move(120, 350)
        self.le1 = QLineEdit(self)
        self.le1.move(20, 50)
        self.le1.setText("30")
        self.le2 = QLineEdit(self)
        self.le2.move(20, 150)
        self.le2.setText("40")
        self.le3 = QLineEdit(self)
        self.le3.move(20, 250)
        self.le3.setText("30")
        self.s1 = QSlider(Qt.Horizontal, self)
        self.s1.move(20, 300)
        self.s2 = QSlider(Qt.Horizontal, self)
        self.s2.move(20, 200)
        self.s3 = QSlider(Qt.Horizontal, self)
        self.s3.move(20, 100)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)
        self.s2.setMinimum(0)
        self.s2.setMaximum(100)
        self.s3.setMinimum(0)
        self.s3.setMaximum(100)
        self.s1.valueChanged.connect(self.v_change1)
        self.s2.valueChanged.connect(self.v_change2)
        self.s3.valueChanged.connect(self.v_change3)
        self.button3.clicked.connect(self.clickAtualizar)

    def v_change1(self):
        my_value = str(self.s1.value())
        self.le3.setText(my_value)

    def v_change2(self):
        my_value = str(self.s2.value())
        self.le2.setText(my_value)

    def v_change3(self):
        my_value = str(self.s3.value())
        self.le1.setText(my_value)

    def clickAtualizar(self):
        main()
        pass

    def clickPadrao(self):
        pass

    def clickOfertas(self):
        pass


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
