from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from src.Items.Controllers.ItemManager import ItemManager
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager


class LoanView(QDialog):

    userM = UserManager()
    itemM = ItemManager()

    def __init__(self, widget):
        super(LoanView, self).__init__()
        loadUi("../designer/Movements/LoanView.ui", self)
        self.widget = widget
        self.setModal(True)
        # self.widget = QtWidgets.QStackedWidget()
        # self.widget.addWidget(self)
        # self.widget.show()
        self.setup()

    def setup(self):
        self.selectuserButton.clicked.connect(lambda: self.select_user())
        self.selectuserButton.setDisabled(False)

        self.selectdocButton.clicked.connect(lambda: self.select_item())
        self.selectdocButton.setDisabled(False)

        self.newuserButton.clicked.connect(lambda: self.new_user())
        self.style()
        self.load_user_table(self.userM.list())
        self.load_item_table(self.itemM.get_items('', 0))

    def style(self):
        self.userTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())
        self.itemTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())
        self.nameField.textChanged.connect(lambda: self.search_user())
        self.surnameField.textChanged.connect(lambda: self.search_user())
        self.itemField.textChanged.connect(lambda: self.search_item())

    def select_user(self):
        '''
        view = UserView(self.widget)
        # self.widget.addWidget(view)
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        view.show()
        view.selectButton.show()
        view.schedaButton.hide()
        view.backButton.hide()
        pass
        '''

    def select_item(self):
        pass

    def search(self):
        pass

    def new_user(self):
        self.view = UserCardView(self.widget, None)
        self.view.show()

    def load_user_table(self, users):
        row = 0
        self.userTable.setRowCount(len(users))
        for user in users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.fiscal_code))
            row = row + 1

    def load_item_table(self, items):
        row = 0
        self.itemTable.setRowCount(len(items))
        for item in items:
            self.itemTable.setItem(row, 0, QtWidgets.QTableWidgetItem(item.title))
            self.itemTable.setItem(row, 1, QtWidgets.QTableWidgetItem(item.author))
            self.itemTable.setItem(row, 2, QtWidgets.QTableWidgetItem(item.isbn))
            row = row + 1

# region Search

    def search_user(self):
        if (self.nameField.text() == '') and (self.surnameField.text() == ''):
            self.load_user_table(self.userM.list())
        elif (self.nameField.text() != '') and (self.surnameField.text() == ''):
            self.load_user_table(self.userM.findName(self.nameField.text()))
        elif (self.nameField.text() == '') and (self.surnameField.text() != ''):
            self.load_user_table(self.userM.findSurname(self.surnameField.text()))
        elif (self.nameField.text() != '') and (self.surnameField.text() != ''):
            self.load_user_table(self.userM.findNameSurname(self.nameField.text(), self.surnameField.text()))

    def search_item(self):
        self.load_item_table(self.itemM.get_items(self.itemField.text(), 1))
        pass

# endregion
