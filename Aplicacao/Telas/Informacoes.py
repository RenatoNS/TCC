# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Informacoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Tela_base(object):
    def setupUi(self, MainWindow_Tela_base):
        MainWindow_Tela_base.setObjectName("MainWindow_Tela_base")
        MainWindow_Tela_base.resize(1072, 834)
        MainWindow_Tela_base.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow_Tela_base.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget_Tela_base = QtWidgets.QWidget(MainWindow_Tela_base)
        self.centralwidget_Tela_base.setObjectName("centralwidget_Tela_base")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget_Tela_base)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conteudo_Tela_base = QtWidgets.QFrame(self.centralwidget_Tela_base)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.conteudo_Tela_base.setFont(font)
        self.conteudo_Tela_base.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.conteudo_Tela_base.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteudo_Tela_base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo_Tela_base.setObjectName("conteudo_Tela_base")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteudo_Tela_base)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Tela_Base = QtWidgets.QFrame(self.conteudo_Tela_base)
        self.Tela_Base.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Tela_Base.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px;")
        self.Tela_Base.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Tela_Base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Tela_Base.setObjectName("Tela_Base")
        self.label = QtWidgets.QLabel(self.Tela_Base)
        self.label.setGeometry(QtCore.QRect(30, 20, 591, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Tela_Base)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.Tela_Base)
        self.tabWidget.setGeometry(QtCore.QRect(40, 160, 921, 631))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab1)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, -10, 921, 641))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: white;\n"
"padding-left: 20px; padding-right: 40px; padding-top: 40 px; padding-bottom: 20px;\n"
"font-size: 40pt")
        self.textBrowser_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab1, "")
        self.horizontalLayout.addWidget(self.Tela_Base)
        self.verticalLayout.addWidget(self.conteudo_Tela_base)
        MainWindow_Tela_base.setCentralWidget(self.centralwidget_Tela_base)

        self.retranslateUi(MainWindow_Tela_base)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Tela_base)

    def retranslateUi(self, MainWindow_Tela_base):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Tela_base.setWindowTitle(_translate("MainWindow_Tela_base", "Tela_base"))
        self.label.setText(_translate("MainWindow_Tela_base", "Mais Informações"))
        self.label_2.setText(_translate("MainWindow_Tela_base", "O Que Saber?"))
        self.textBrowser_3.setHtml(_translate("MainWindow_Tela_base", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:40pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; vertical-align:super;\">Insira o Texto</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow_Tela_base", "Bibliografia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Tela_base = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Tela_base()
    ui.setupUi(MainWindow_Tela_base)
    MainWindow_Tela_base.show()
    sys.exit(app.exec_())
