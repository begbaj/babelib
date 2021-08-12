import mariadb
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QWidget, QLabel
from PyQt5.uic import loadUi
import sys
#sys.path.append('C:\\Users\\DanieleB\\PycharmProjects\\babelib\\src\\homeView.py')
#from src.homeView import HomeView
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager


class UserView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget):
        super(UserView, self).__init__()
        loadUi("../designer/User view/UserView.ui", self)
        self.users = self.userM.list()
        self.widget = widget

        self.loadData()
        self.setup()

    def loadData(self):
        row = 0
        self.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

    def setup(self):
        self.backButton.clicked.connect(self.back)
        self.schedaButton.clicked.connect(self.gousercard)

    def back(self):
        self.close()

    def gousercard(self):
        row = self.userTable.currentRow()
        if row == -1:
            self.showpopup()
        else:
            user = self.users[row]
            self.view = UserCardView(self.widget, user)
            self.view.show()

    def showpopup(self):
        self.pop = Popup()
        self.pop.show()


class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/PopUp/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)