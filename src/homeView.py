import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from Users.View.UserView import UserView


class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
        self.setUp()


    def setUp(self):
        self.userButton.clicked.connect(self.gotoUser)


    def gotoUser(self):
        self.cams = UserView()
        self.cams.show()
        self.close()

