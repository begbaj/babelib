from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from mariadb import Date
from src.Users.controllers.UserManager import UserManager


class NewUserView(QMainWindow):
    def __init__(self):
        super(NewUserView, self).__init__()
        loadUi("../designer/New User View/NewUserView.ui", self)
        # Variabili di Istanza
        self.pop = ''
        # Metodi iniziali
        self.setup()

    def setup(self):
        # Button
        self.returnButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save)

    def save(self):
        pass