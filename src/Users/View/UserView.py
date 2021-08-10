import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
#sys.path.append('C:\\Users\\DanieleB\\PycharmProjects\\babelib\\src\\homeView.py')
#from src.homeView import HomeView



class UserView(QMainWindow):
    def __init__(self):
        super(UserView, self).__init__()
        loadUi("../designer/User view/UserView.ui", self)



        self.setUp()

    def setUp(self):
        pass
        #self.backButton.clicked.connect(self.back)

    #def back(self):
        #self.cams = HomeView()
        #self.cams.show()
        #self.close()

