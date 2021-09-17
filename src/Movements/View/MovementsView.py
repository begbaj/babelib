from PyQt5.QtWidgets import QMainWindow, QTableWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

from src.Items.Controllers.ItemManager import ItemManager
from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Movements.View.InfoView import InfoView
from src.Movements.View.LoanView import LoanView
from src.Utils.UI import Popup, DeletePopup
from src.Items.Models.ItemEnumerators import *



class MovementsView(QMainWindow):

    movementM = MovementManager()
    itemM = ItemManager()

    def __init__(self, widget):
        super(MovementsView, self).__init__()
        loadUi("../designer/Movements/MovementView.ui", self)
        self.widget = widget
        self.view = ''
        self.setup()

    def setup(self):
        self.style()
        self.loanButton.clicked.connect(lambda: self.new_loan())
        self.consultationButton.clicked.connect(lambda: self.new_consultation())
        self.infoButton.clicked.connect(lambda: self.movement_info())
        self.backButton.clicked.connect(lambda: self.close())
        self.givingbookButton.clicked.connect(lambda: self.giving())
        self.deleteMovements.clicked.connect(lambda: self.delete())

        self.loanRadio.setChecked(True)

        self.searchField.textChanged.connect(lambda: self.search())

        self.loanRadio.toggled.connect(lambda: self.search())
        self.consultationRadio.toggled.connect(lambda: self.search())
        self.backRadio.toggled.connect(lambda: self.search())

        self.load_data()



    def style(self):
        # Button Style
        self.loanButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.consultationButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.infoButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        # Line Edit Style
        self.searchField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        # Table Style
        self.movementTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())

    def new_consultation(self):
        self.view = LoanView(self.widget, self.load_data, 0)
        self.view.show()

    def new_loan(self):
        self.view = LoanView(self.widget, self.load_data, 1)
        self.view.show()

    def movement_info(self):
        rowtable = self.movementTable.currentRow()
        if rowtable == -1:
            self.popUp = Popup("Selezionare prima un movimento!")
            self.popUp.show()
        else:
            movement = self.movements[rowtable]
            self.view = InfoView(self.widget, movement)
            #self.view = LoanView(self.widget, self.load_data, 1)
            self.view.show()



    def load_data(self):
        self.movements = self.movementM.find_all(self.radio_selection(), 5)
        self.load_table()

    def load_table(self):
        """
        Questo metodo permette di rimpire la QTableWidget presente nella view con una lista di utenti
        :param users:
        :return: None
        """
        row = 0
        self.movementTable.setRowCount(len(self.movements))
        for movement in self.movements:
            self.movementTable.setItem(row, 0, QtWidgets.QTableWidgetItem(movement.timestamp.strftime('%d/%m/%Y %H:%M:%S')))
            self.movementTable.setItem(row, 1, QtWidgets.QTableWidgetItem(movement.item.isbn))
            self.movementTable.setItem(row, 2, QtWidgets.QTableWidgetItem(movement.item.title))
            self.movementTable.setItem(row, 3, QtWidgets.QTableWidgetItem(movement.user.fiscal_code))
            self.movementTable.setItem(row, 4, QtWidgets.QTableWidgetItem(movement.user.name + " " + movement.user.surname))
            self.movementTable.setItem(row, 5, QtWidgets.QTableWidgetItem(movement.user.first_cellphone))
            row = row + 1
        self.movementTable.setEditTriggers(QTableWidget.NoEditTriggers)


    def search(self):

        numSearchMode = 0

        if self.searchField.text() != '':
            if self.searchMode.currentText() == 'In tutti i campi':
                numSearchMode = 0
            elif self.searchMode.currentText() == 'Utente':
                numSearchMode = 1
            elif self.searchMode.currentText() == 'Titolo':
                numSearchMode = 2
            elif self.searchMode.currentText() == 'Data':
                numSearchMode = 3
            elif self.searchMode.currentText() == 'ISBN':
                numSearchMode = 4


            self.movements = self.movementM.find_all(self.radio_selection(), numSearchMode, self.searchField.text())
        else:
            self.movements = self.movementM.find_all(self.radio_selection(), 5)

        self.load_table()

    def radio_selection(self):
        if self.consultationRadio.isChecked():
            return 0
        elif self.loanRadio.isChecked():
            return 1
        elif self.backRadio.isChecked():
            return 2

    def giving(self):
        rowtable = self.movementTable.currentRow()
        self.movements[rowtable].item.availability = AvailabilityEnum.disponibile
        self.movements[rowtable].item.cataloging_level = CatalogingLevel.max
        self.movements[rowtable].item.publication_state = 0
        self.movements[rowtable].mov_type = 2
        self.movementM.set(self.movements[rowtable])
        self.itemM.edit_item(self.movements[self.movementTable.currentRow()].item)
        self.load_data()
#deleteMovements
    def delete(self):
        rowtable = self.movementTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            text = "Sei sicuro di voler eliminare il movimento?"
            self.pop = DeletePopup(self.delete_movement, text)
            self.pop.show()

    def delete_movement(self):
        """
        Questo metodo permette di rimuovere l'utente selezionato dal sistema
        :return: None
        """
        row = self.movementTable.currentRow()
        self.movementM.delete(self.movements[row].id)
        self.movements.remove(self.movements[row])
        self.movementTable.removeRow(row)





