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


    def __init__(self):
        super(UserView, self).__init__()
        loadUi("../designer/User view/UserView.ui", self)
        users = self.userM.list()

        row = 0
        self.userTable.setRowCount(len(users))
        for user in users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

        #users = self.userM.list()
        #for row in users:
        #self.userTable.setColumnWidth(0,10)

        self.setUp()

    #def loadData(self):







    def setUp(self):
        pass
        #self.backButton.clicked.connect(self.back)

    #def back(self):
        #self.cams = HomeView()
        #self.cams.show()
        #self.close()

