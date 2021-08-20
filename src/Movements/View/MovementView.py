from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi


class MovementView(QMainWindow):

    def __int__(self):
        super(MovementView, self).__init__()
        uic.loadUi("../designer/Items/ShowItemView.ui", self)
        self.setup()

    def setup(self):
        self.loanButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())