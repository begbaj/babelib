from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Movements.View.LoanView import LoanView


class MovementsView(QMainWindow):

    movementM = MovementManager()

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

        self.loanRadio.setChecked(True)

        self.searchField.textChanged.connect(lambda: self.search())
        self.loanRadio.toggled.connect(lambda: self.search())

        self.movements = self.movementM.find_all(self.loanRadio.isChecked(), 5)
        self.load_table()




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
        pass

    def new_loan(self):
        self.view = LoanView(self.widget)
        self.view.show()

    def movement_info(self):
        pass



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

            self.movements = self.movementM.find_all(self.loanRadio.isChecked(), numSearchMode, self.searchField.text())
        else:
            self.movements = self.movementM.find_all(self.loanRadio.isChecked(), 5)

        self.load_table()





