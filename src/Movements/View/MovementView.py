from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.uic import loadUi


class MovementView(QDialog):

    def __int__(self):
        super(MovementView, self).__init__()
        uic.loadUi("../designer/Movements/movement.ui", self)
        self.setup()

    def setup(self):
        self.loanButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())