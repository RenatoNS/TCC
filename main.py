import wx
import wx.xrc
import pandas as pd
import numpy as np
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QLineEdit, QSlider, QMainWindow, QApplication, QPushButton, QVBoxLayout
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtCore import Qt
import Perfil

z = -1

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
        canvas = Canvas(self, width=8, height=4)
        canvas.move(200, 0)

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
        self.s1.move(20,300)
        self.s2 = QSlider(Qt.Horizontal, self)
        self.s2.move(20,200)
        self.s3 = QSlider(Qt.Horizontal, self)
        self.s3.move(20,100)
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
        pass

    def clickPadrao(self):
        pass

    def clickOfertas(self):
        pass

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot(20,50,30)

    def plot(self,RF,TD,AC):
        x = np.array([RF, TD, AC])
        labels = ["Renda Fixa", "Tesouro Direto", "Ações"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)

class LeftPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(50, 50))

        self.figure = Figure()

        labels = 'Renda Fixa', 'Tesouro Direto', 'Renda Variável'
        sizes = [15, 35, 50]
        explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
        self.canvas = FigureCanvas(self, -1, self.figure)


class RightPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.m_button4 = wx.Button(self, -1, "button")


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None)

        splitter = wx.SplitterWindow(self)
        left = LeftPanel(splitter)
        right = RightPanel(splitter)
        splitter.SplitHorizontally(left, right)


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(496, 658), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"Qual sua faixa etária?", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        bSizer1.Add(self.m_staticText12, 0, wx.ALL, 5)

        m_comboBox11Choices = [u"Abaixo de 25 anos", u"25 até 40 anos", u"41 até 55 anos", u"Acima de 56 anos"]
        self.m_comboBox11 = wx.ComboBox(self, wx.ID_ANY, u"Abaixo de 25 anos", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox11Choices, 0)
        self.m_comboBox11.SetSelection(0)
        bSizer1.Add(self.m_comboBox11, 0, wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY,
                                            u"Qual Percentual do seu patrimônio está investido?(Carros, casa, ações, etc)",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        bSizer1.Add(self.m_staticText13, 0, wx.ALL, 5)

        m_comboBox12Choices = [u"Até 25% ", u"Entre 26% e 50%", u"Entre 51% e 75%", u"Mais de 76% "]
        self.m_comboBox12 = wx.ComboBox(self, wx.ID_ANY, u"Até 25% ", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox12Choices, 0)
        self.m_comboBox12.SetSelection(0)
        bSizer1.Add(self.m_comboBox12, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"Qual o objetivo dos seus investimentos?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        bSizer1.Add(self.m_staticText14, 0, wx.ALL, 5)

        m_comboBox13Choices = [u"Aposentadoria  ", u"Proteção do capital   ", u"Compra de um bem  ",
                               u"Crescimento significativo do patrimônio "]
        self.m_comboBox13 = wx.ComboBox(self, wx.ID_ANY, u"Aposentadoria  ", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox13Choices, 0)
        self.m_comboBox13.SetSelection(0)
        bSizer1.Add(self.m_comboBox13, 0, wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY,
                                            u"Como você se sentiria caso verificasse perdas em seus investimentos?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        bSizer1.Add(self.m_staticText15, 0, wx.ALL, 5)

        m_comboBox14Choices = [u"Extremamente desanimado. Não quero passar nunca por essa situação",
                               u"Moderadamente desanimado. Posso passar por essa situação, mas não gostaria",
                               u"Levemente desanimado. Entendo que a perda faz parte do processo de investimento",
                               u"Normal. Tudo bem passar por isso"]
        self.m_comboBox14 = wx.ComboBox(self, wx.ID_ANY,
                                        u"Extremamente desanimado. Não quero passar nunca por essa situação",
                                        wx.DefaultPosition, wx.DefaultSize, m_comboBox14Choices, 0)
        self.m_comboBox14.SetSelection(0)
        bSizer1.Add(self.m_comboBox14, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY,
                                            u"Quais são as aplicações financeiras em que você tem experiência?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        bSizer1.Add(self.m_staticText16, 0, wx.ALL, 5)

        m_comboBox15Choices = [u"Não Possuo", u"Renda Fixa", u"Renda Fixa e Ações de Longo Prazo",
                               u"Outras além das anteriores"]
        self.m_comboBox15 = wx.ComboBox(self, wx.ID_ANY, u"Não Possuo", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox15Choices, 0)
        self.m_comboBox15.SetSelection(0)
        bSizer1.Add(self.m_comboBox15, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Possui algum conhecimento sobre o mercado financeiro?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        bSizer1.Add(self.m_staticText17, 0, wx.ALL, 5)

        m_comboBox16Choices = [u"Não", u"Pouco", u"Médio", u"Bastante"]
        self.m_comboBox16 = wx.ComboBox(self, wx.ID_ANY, u"Não", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox16Choices, 0)
        self.m_comboBox16.SetSelection(0)
        bSizer1.Add(self.m_comboBox16, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"Qual sua escoladidade?", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)

        bSizer1.Add(self.m_staticText18, 0, wx.ALL, 5)

        m_comboBox17Choices = [u"Ensino fundamental ou inferior", u"Ensino Médio ", u"Ensino Superior",
                               u"Maior que Ensino Superior"]
        self.m_comboBox17 = wx.ComboBox(self, wx.ID_ANY, u"Ensino fundamental ou inferior", wx.DefaultPosition,
                                        wx.DefaultSize, m_comboBox17Choices, 0)
        self.m_comboBox17.SetSelection(0)
        bSizer1.Add(self.m_comboBox17, 0, wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"Você costuma operar financeiramente com que frequência?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)

        bSizer1.Add(self.m_staticText19, 0, wx.ALL, 5)

        m_comboBox18Choices = [u"Pouquíssima", u"Pouca", u"Média", u"Alta"]
        self.m_comboBox18 = wx.ComboBox(self, wx.ID_ANY, u"Pouquíssima", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox18Choices, 0)
        self.m_comboBox18.SetSelection(0)
        bSizer1.Add(self.m_comboBox18, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"Você pretende ter aumento de despesas no futuro?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)

        bSizer1.Add(self.m_staticText20, 0, wx.ALL, 5)

        m_comboBox19Choices = [u"Não. Pretendo diminuir", u"Não. Pretendo ter as mesmas que tenho hoje",
                               u"Sim. Pretendo aumentar ", u"Sim. Pretendo ter um grande aumento"]
        self.m_comboBox19 = wx.ComboBox(self, wx.ID_ANY, u"Não. Pretendo diminuir", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox19Choices, 0)
        self.m_comboBox19.SetSelection(0)
        bSizer1.Add(self.m_comboBox19, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY,
                                            u"Por quanto tempo você deseja manter seu dinheiro aplicado?",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        bSizer1.Add(self.m_staticText21, 0, wx.ALL, 5)

        m_comboBox20Choices = [u"Menos de 1 ano", u"De 1 até 2 anos", u"De 2 até 3 anos", u"Mais de 3 anos"]
        self.m_comboBox20 = wx.ComboBox(self, wx.ID_ANY, u"Menos de 1 ano", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox20Choices, 0)
        self.m_comboBox20.SetSelection(0)
        bSizer1.Add(self.m_comboBox20, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Cadastrar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.save)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def save(self, event):
        opiniao = [self.m_comboBox11.GetSelection(),
             self.m_comboBox12.GetSelection(),
             self.m_comboBox13.GetSelection(),
             self.m_comboBox14.GetSelection(),
             self.m_comboBox15.GetSelection(),
             self.m_comboBox16.GetSelection(),
             self.m_comboBox17.GetSelection(),
             self.m_comboBox18.GetSelection(),
             self.m_comboBox19.GetSelection(),
             self.m_comboBox20.GetSelection()]
        y = np.array([self.m_comboBox11.GetValue(),
                      self.m_comboBox12.GetValue(),
                      self.m_comboBox13.GetValue(),
                      self.m_comboBox14.GetValue(),
                      self.m_comboBox15.GetValue(),
                      self.m_comboBox16.GetValue(),
                      self.m_comboBox17.GetValue(),
                      self.m_comboBox18.GetValue(),
                      self.m_comboBox19.GetValue(),
                      self.m_comboBox20.GetValue()
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
        frame.Close()
        event.Skip()

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
if (z==-1):
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
