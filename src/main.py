import mariadb
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from loginView import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = LoginView()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(600)
    widget.setFixedHeight(600)
    widget.show()
    app.exec() #Lancia l'applicazione