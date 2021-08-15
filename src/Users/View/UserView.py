import mariadb
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QWidget, QLabel
from PyQt5.uic import loadUi
import sys
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
        self.load_data()
        self.setup()

        self.nameField.textChanged.connect(lambda: self.search())
        self.surnameField.textChanged.connect(lambda: self.search())

        #self.nameField.setStyleSheet(open("../designer/style/davtheme.qss", "r").read())
        #self.nameField.setStyleSheet('background-color: orange')

        #TODO sto effettuando test con il qss
    def style(self):
        self.schedaButton.setStyleSheet(open("../designer/style/buttonTheame.txt", "r").read())
        self.userButton.setStyleSheet(open("../designer/style/buttonTheame.txt", "r").read())
        self.backButton.setStyleSheet(open("../designer/style/buttonTheame.txt", "r").read())

    def setup(self):
        self.userButton.clicked.connect(self.__go_new_user)
        self.backButton.clicked.connect(self.close)
        self.schedaButton.clicked.connect(self.__go_user_card)
        self.deleteButton.clicked.connect(self.delete)
        self.refreshButton.clicked.connect(self.load_data)
        self.searchButton.clicked.connect(self.search)
        self.style()

    def load_data(self):
        row = 0
        self.users = self.userM.list()
        self.load_table(self.users)
        '''
        self.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1
        '''

    def search(self):
        # Reload all the Users
        if (self.nameField.text() == '') and (self.surnameField.text() == ''):
            self.load_data()
        # Search User by name
        elif (self.nameField.text() != '') and (self.surnameField.text() == ''):
            self.load_data_research(self.userM.findName(self.nameField.text()))
        # Search User by surname
        elif (self.nameField.text() == '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findSurname(self.surnameField.text()))
        # Search User by both
        elif (self.nameField.text() != '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findNameSurname(self.nameField.text(), self.surnameField.text()))

    def load_data_research(self, users):
        self.users = users
        self.load_table(self.users)
        '''row = 0
        sel
        f.userTable.setRowCount(len(self.users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1
        '''
    def __go_user_card(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            user = self.users[rowtable]
            self.view = UserCardView(self.widget, user, self.load_data)
            self.view.show()

    def delete(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            self.pop = DeletePopup()
            self.pop.show()
            self.userM.delete(self.users[rowtable].id)
            self.users.remove(self.users[rowtable])
            self.userTable.removeRow(rowtable)

    def load_table(self, users):
        row = 0
        self.userTable.setRowCount(len(users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

    def show_popup(self):
        self.pop = Popup()
        self.pop.show()

    def __go_new_user(self):
        user = None
        self.view = UserCardView(self.widget, user, self.load_data)
        self.view.show()


class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/PopUp/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)
        self.okButton.clicked.connect(self.close)


class DeletePopup(QDialog):
    def __init__(self):
        super(DeletePopup, self).__init__()
        loadUi("../designer/Delete PopUp/deletepopup.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        # self.confirmButton.clicked.connect(self.delete)