import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
#sys.path.append('C:\\Users\\DanieleB\\PycharmProjects\\babelib\\src\\homeView.py')
#from src.homeView import HomeView
from src.Users.controllers.UserManager import UserManager


class UserView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget):
        super(UserView, self).__init__()
        loadUi("../designer/User view/UserView.ui", self)
        self.users = self.userM.list()
        self.loadData()
        self.widget = widget


        #users = self.userM.list()
        #for row in users:
        #self.userTable.setColumnWidth(0,10)

        self.setUp()

    def loadData(self):
        row = 0
        self.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

    def setUp(self):
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)


