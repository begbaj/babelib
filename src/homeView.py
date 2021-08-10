from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi


class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
