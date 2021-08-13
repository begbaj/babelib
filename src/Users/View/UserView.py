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
        self.pop = ''
        self.load_data()
        self.setup()

    def setup(self):
        self.userButton.clicked.connect(self.__go_new_user)
        self.backButton.clicked.connect(self.back)
        self.schedaButton.clicked.connect(self.__go_user_card)
        self.deleteButton.clicked.connect(self.delete)
        self.refreshButton.clicked.connect(self.load_data)

    def load_data(self):
        row = 0
        self.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

    def back(self):
        self.close()

    def __go_user_card(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            user = self.users[rowtable]
            self.view = UserCardView(self.widget, user, self.load_data)
            self.view.show()

    def delete(self):
        rowtable = self.userTable.currentRow()
        self.userM.delete(self.users[rowtable].id)
        # self.users[rowTable].remove()
        self.users.remove(self.users[rowtable])
        self.userTable.removeRow(rowtable)
        # self.loadData()

    def show_popup(self):
        self.pop = Popup()
        self.pop.show()

    def __go_new_user(self):
        user = None
        self.view = UserCardView(self.widget, user, self.load_data)
        self.view.show()

class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/PopUp/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)