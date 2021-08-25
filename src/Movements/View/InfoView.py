from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Movements.View.LoanView import LoanView
from datetime import datetime, timedelta


class InfoView(QMainWindow):

    movementM = MovementManager()

    '''def __init__(self, widget, movement):
        super(InfoView, self).__init__()
        loadUi("../designer/Movements/ShowMovementView.ui", self)
        self.widget = widget
        #self.view = ''
        #self.setup()
        self.movement = movement
        #self.fill_movement()'''

    def __init__(self, movement):
        super(InfoView, self).__init__()
        loadUi("../designer/Movements/ShowMovementView.ui", self)
        self.movement = movement
        #self.setup()


    def setup(self):
        self.confirmButton.clicked.connect(self.save)
        self.returnButton.clicked.connect(self.close)

    def fill_movement(self):
        #Utente
        self.userField.setText(self.movement.user.name + " " + self.movement.user.surname)
        self.fiscalCodeField.setText(self.movement.user.fiscal_code)
        self.contactField.setText(self.movement.user.first_cellphone)
        self.cityField.setText(self.movement.user.city)
        self.addressField.setText(self.movement.user.address)
        self.postalCodeField.setText(self.movement.user.postal_code)

        #Libro
        self.isbnField.setText(self.movement.item.isbn)
        self.titleField.setText(self.movement.item.title)
        self.bidField.setText(self.movement.item.bid)
        self.authorField.setText(self.movement.item.author)
        self.rackField.setText(self.movement.item.rack)
        self.shelfField.setText(self.movement.item.shelf)
        self.positionField.setText(self.movement.item.position)

        #Movimento
        self.dateTimeIni.setDate(self.movement.timestamp)
        self.dateTimeEnd.setDate(self.movement.timestamp + timedelta(30))

        if self.movement.mov_type == 0:
            self.movtypeField.setext("Consultazione")
        elif self.movement.mov_type == 1:
            self.movtypeField.setext("Presitito")
        elif self.movement.mov_type == 2:
            self.movtypeField.setext("Rientrato")

        self.noteField.setText(self.movement.note)

    def save(self):
        self.movement.note = self.self.noteField.text()
        self.movementM.set(self.movement)
        self.close()