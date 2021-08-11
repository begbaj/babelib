import mariadb
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from  loginView import LoginView


## TODO: un view menager per scorrere le varie view senza che rimangano aperte
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = LoginView(widget)
    widget.addWidget(mainwindow)
    widget.show()
    app.exec() #Lancia l'applicazione