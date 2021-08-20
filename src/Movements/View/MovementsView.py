from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.uic import loadUi
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager


class MovementsView(QMainWindow):

    def __init__(self, widget):
        super(MovementsView, self).__init__()
        loadUi("../designer/movement.ui", self)
        self.widget = widget

