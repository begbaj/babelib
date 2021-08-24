from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from src.Items.Controllers.ItemManager import ItemManager
from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager
from src.Utils.UI import Popup


class LoanView(QDialog):

    userM = UserManager()
    itemM = ItemManager()


    def __init__(self, widget):
        super(LoanView, self).__init__()
        loadUi("../designer/Movements/LoanView.ui", self)
        self.widget = widget
        self.users = self.userM.list()
        self.items = self.itemM.get_items('', 0)
        self.user = ''
        # self.setModal(True)
        # self.widget = QtWidgets.QStackedWidget()
        # self.widget.addWidget(self)
        # self.widget.show()
        self.setup()
        #self.movementM = MovementManager()
        #self.movementM.findAll("tu", 1)


    def setup(self):
        self.selectuserButton.clicked.connect(lambda: self.select_user())
        self.selectuserButton.setDisabled(False)
        self.selectdocButton.clicked.connect(lambda: self.select_item())
        self.selectdocButton.setDisabled(False)
        self.newuserButton.clicked.connect(lambda: self.new_user())
        self.userField.setReadOnly(True)
        self.fiscalcodeField.setReadOnly(True)
        self.cellField.setReadOnly(True)
        self.style()
        self.load_user_table(self.users)
        self.load_item_table(self.items)

    def style(self):
        self.userTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())
        self.itemTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())
        self.nameField.textChanged.connect(lambda: self.search_user())
        self.surnameField.textChanged.connect(lambda: self.search_user())
        self.itemField.textChanged.connect(lambda: self.search_item())

    def select_user(self):
        if self.userTable.currentRow() == -1:
            self.pop = Popup("Selezionare un utente")
            self.pop.show()
        else:
            row = self.userTable.currentRow()
            self.user = self.users[row]
            self.userField.setText(self.user.name + " " + self.user.surname)
            self.fiscalcodeField.setText(self.user.fiscal_code)
            self.cellField.setText(self.user.first_cellphone)

    def select_item(self):
        if self.itemTable.currentRow() == -1:
            self.pop = Popup("Selezionare un Documento")
            self.pop.show()
        else:
            row = self.itemTable.currentRow()
            item = self.items[row]
            self.isbnField.setText(item.isbn)
            self.titleField.setText(item.title)

    def new_user(self):
        self.view = UserCardView(self.widget, None, self.load_user_table)
        self.view.show()

# region Table

    def load_user_table(self, users):
        if users is not None:
            self.users = users
            row = 0
            self.userTable.setRowCount(len(self.users))
            for user in users:
                self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
                self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
                self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.fiscal_code))
                row = row + 1

    def load_item_table(self, items):
        self.items = items
        row = 0
        self.itemTable.setRowCount(len(self.items))
        for item in self.items:
            self.itemTable.setItem(row, 0, QtWidgets.QTableWidgetItem(item.title))
            self.itemTable.setItem(row, 1, QtWidgets.QTableWidgetItem(item.author))
            self.itemTable.setItem(row, 2, QtWidgets.QTableWidgetItem(item.isbn))
            row = row + 1

# endregion

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

# endregion
