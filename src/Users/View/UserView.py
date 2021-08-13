import mariadb
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QWidget, QLabel
from PyQt5.uic import loadUi
import sys
#sys.path.append('C:\\Users\\DanieleB\\PycharmProjects\\babelib\\src\\homeView.py')
#from src.homeView import HomeView
from src.Users.View.NewUserView import NewUserView
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
        self.loadData()
        self.setup()

    def setup(self):
        self.userButton.clicked.connect(self.newuser)
        self.backButton.clicked.connect(self.back)
        self.schedaButton.clicked.connect(self.gousercard)
        self.deleteButton.clicked.connect(self.delete)
        self.refreshButton.clicked.connect(self.loadData)

    def loadData(self):
        row = 0
        self.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

    def back(self):
        self.close()

    def gousercard(self):
        rowtable = self.userTable.currentRow()

        if rowtable == -1:
            self.showpopup()
        else:
            user = self.users[rowtable]
            self.view = UserCardView(self.widget, user)
            self.view.show()

    def delete(self):
        rowtable = self.userTable.currentRow()
        self.userM.delete(self.users[rowtable].id)
        # self.users[rowTable].remove()
        self.users.remove(self.users[rowtable])
        self.userTable.removeRow(rowtable)
        # self.loadData()

    def showpopup(self):
        self.pop = Popup()
        self.pop.show()

    def newuser(self):
        self.view = NewUserView()
        self.view.show()

class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/PopUp/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)