from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi

from src.Items.View.InventoryView import InventoryView
from src.Users.View.UserView import UserView


class LoanView(QDialog):

    def __init__(self, widget):
        super(LoanView, self).__init__()
        loadUi("../designer/Movements/LoanView.ui", self)
        self.widget = widget
        # self.widget = QtWidgets.QStackedWidget()
        # self.widget.addWidget(self)
        # self.widget.show()
        self.setup()

    def setup(self):
        self.selectuserButton.clicked.connect(lambda: self.select_user())
        self.selectuserButton.setDisabled(False)
        self.selectdocButton.clicked.connect(lambda: self.select_item())
        self.selectdocButton.setDisabled(False)
        self.style()

    def style(self):
        pass

    def select_user(self):
        view = UserView(self.widget)
        # self.widget.addWidget(view)
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        view.show()
        view.selectButton.show()
        view.schedaButton.hide()
        view.backButton.hide()
        pass

    def select_item(self):
        self.itemview = InventoryView(self.widget, self)
        self.itemview.show()
        pass
