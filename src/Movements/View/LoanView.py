import os
from datetime import datetime, date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget
from PyQt5.uic import loadUi
from src.Items.Controllers.ItemManager import ItemManager
from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Reports.ReportManager import ReportManager
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager
from src.Utils.UI import Popup
from src.Items.Models.ItemEnumerators import *


class LoanView(QDialog):

    userM = UserManager()
    itemM = ItemManager()
    movementM = MovementManager()


    def __init__(self, widget, callback, flag):
        super(LoanView, self).__init__()

        '''
        
        0:Consultazione
        1:Prestito
        2:Rientro
        
        '''

        loadUi("../designer/Movements/LoanView.ui", self)
        self.widget = widget
        self.users = self.userM.list()
        self.items = self.movementM.get_items_available()
        self.user = ''
        self.movement = Movement()

        self.callback = callback


        self.flag = flag

        # self.setModal(True)
        # self.widget = QtWidgets.QStackedWidget()
        # self.widget.addWidget(self)
        # self.widget.show()
        self.setup()
        #self.movementM = MovementManager()
        #self.movementM.findAll("tu", 1)

        if self.flag == 0:
            self.loantypeBox.hide()
            self.expirationEdit.hide()
            self.label_9.hide()
            self.label_10.hide()
            #self.frame_13.setGeometry(931,210)

    def setup(self):
        self.selectuserButton.clicked.connect(lambda: self.select_user())
        self.selectuserButton.setDisabled(False)
        self.selectdocButton.clicked.connect(lambda: self.select_item())
        self.selectdocButton.setDisabled(False)
        self.newuserButton.clicked.connect(lambda: self.new_user())
        self.confirmButton.clicked.connect(lambda: self.save()) #salvataggio del movimento
        self.userField.setReadOnly(True)
        self.fiscalcodeField.setReadOnly(True)
        self.cellField.setReadOnly(True)
        self.style()
        self.load_user_table()
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

            # assegno l'id dello user al movimento
            self.movement.user_id = self.user.id

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

            #assegno l'id dell'item al movimento
            self.movement.item_id = item.id

            self.isbnField.setText(item.isbn)
            self.titleField.setText(item.title)

    def new_user(self):
        self.view = UserCardView(self.widget, None, self.load_user_table)
        self.view.show()

# region Table

    def load_user_table(self):
        self.users = self.userM.list()
        if self.users is not None:
            row = 0
            self.userTable.setRowCount(len(self.users))
            for user in self.users:
                self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
                self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
                self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.fiscal_code))
                row = row + 1
            self.userTable.setEditTriggers(QTableWidget.NoEditTriggers)

    def load_item_table(self, items):
        self.items = items
        row = 0
        self.itemTable.setRowCount(len(self.items))
        for item in self.items:
            self.itemTable.setItem(row, 0, QtWidgets.QTableWidgetItem(item.title))
            self.itemTable.setItem(row, 1, QtWidgets.QTableWidgetItem(item.author))
            self.itemTable.setItem(row, 2, QtWidgets.QTableWidgetItem(item.isbn))
            row = row + 1
        self.itemTable.setEditTriggers(QTableWidget.NoEditTriggers)


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

# region Save_and_back

    def save(self):
        row = self.itemTable.currentRow()
        if self.movement.user_id is None or self.movement.item_id is None:
            self.pop = Popup("Selezionare sia un Utente sia un Documento")
            self.pop.show()

        else:
            if self.flag == 1:
                self.movement.mov_type = 1
            else:
                self.movement.mov_type = 0
            self.movement.timestamp = date.today()
            self.movementM.add(self.movement)

            self.movement = self.movementM.find(self.movementM.get_last_movement_id())

            newpath = os.path.expanduser("~/Desktop/Moduli Prestito")
            if not os.path.exists(newpath):
                os.makedirs(newpath)

            self.reportM = ReportManager(self.movement, newpath)
            self.reportM.set_report()
            self.back()

        self.items[row].availability = AvailabilityEnum.in_prestito
        self.itemM.edit_item(self.items[row])

    def back(self):
        self.callback()
        self.close()

# endregion
