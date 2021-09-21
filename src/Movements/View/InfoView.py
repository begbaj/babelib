from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

from src.Movements.Controllers.MovementManager import MovementManager
from src.Movements.Models.Movement import Movement
from src.Movements.View.LoanView import LoanView
from datetime import datetime, timedelta

from src.Reports.ReportManager import ReportManager


class InfoView(QDialog):

    movementM = MovementManager()


    def __init__(self, widget, movement):
        super(InfoView, self).__init__()
        loadUi("../designer/Movements/ShowMovementView.ui", self)
        self.widget = widget
        self.view = ''
        self.setup()
        self.movement = movement
        self.fill_movement()

#lblUserDisabled
    def setup(self):
        self.confirmButton.clicked.connect(lambda: self.save())
        self.returnButton.clicked.connect(lambda: self.close())

    def fill_movement(self):
        #Utente
        self.userField.setText(self.movement.user.name + " " + self.movement.user.surname)
        self.fiscalCodeField.setText(self.movement.user.fiscal_code)
        self.contactField.setText(self.movement.user.first_cellphone)
        self.cityField.setText(self.movement.user.city)
        self.addressField.setText(self.movement.user.address)
        self.postalCodeField.setText(self.movement.user.postal_code)
        #self.lblUserDisabled.setVisible(self.movement.user.disabled)
        #print(self.movement.user.disabled)
        if self.movement.user.disabled == b'\x00':
            self.lblUserDisabled.setVisible(False)
        elif self.movement.user.disabled == b'\x01':
            self.lblUserDisabled.setVisible(True)

        #Libro
        self.isbnField.setText(self.movement.item.isbn)
        self.titleField.setText(self.movement.item.title)
        self.bidField.setText(self.movement.item.bid)
        self.authorField.setText(self.movement.item.author)
        self.rackField.setText(str(self.movement.item.rack))
        self.shelfField.setText(self.movement.item.shelf)
        self.positionField.setText(str(self.movement.item.position))

        #Movimento
        self.dateTimeIni.setDate(self.movement.timestamp)
        self.dateTimeEnd.setDate(self.movement.timestamp + timedelta(30))

        if self.movement.mov_type == 0:
            self.movtypeField.setText("Consultazione")
        elif self.movement.mov_type == 1:
            self.movtypeField.setText("Presitito")
        elif self.movement.mov_type == 2:
            self.movtypeField.setText("Rientrato")

        self.noteField.setText(self.movement.note)

    def save(self):
        self.movement.note = self.noteField.toPlainText()
        self.movementM.set(self.movement)
        self.close()