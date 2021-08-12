from time import strptime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from datetime import datetime

class UserCardView(QMainWindow):

    def __init__(self, widget, user):
        super(UserCardView, self).__init__()
        loadUi("../designer/SchedaUtenteView/SchedaUtenteView.ui", self)

        self.widget = widget
        self.user = user

        self.setup()
        self.fillcard()

    def fillcard(self):
        # Line Edit
        self.nameField.setText(self.user.name)
        self.surnameField.setText(self.user.surname)
        self.fiscalcodeField.setText(self.user.fiscal_code)
        self.addressField.setText(self.user.address)
        self.cityField.setText(self.user.city)
        self.capField.setText(self.user.postal_code)
        self.cellField.setText(self.user.first_cellphone)
        self.emailField.setText(self.user.email)
        self.telephonField.setText(self.user.telephone)
        # Combo Box
        self.genderBox.setCurrentText(self.user.gender)
        self.nationBox.setCurrentText(self.user.Nationality_S.code)
        #self.usertypeBox.setText(self.user.userType.description)
        # Date Edit
        self.dateEdit.setDate(self.user.birthdate)

    def setup(self):
        # Button
        self.returnButton.clicked.connect(self.back)
        self.editButton.clicked.connect(self.edituser)
        self.saveButton.clicked.connect(self.save)

        self.disablefield()

    def edituser(self):
        self.enablefiled()
        ## aggiornare campi
        self.save()

    def disablefield(self):
        # Box
        self.genderBox.setDisabled(True)
        self.nationBox.setDisabled(True)
        self.usertypeBox.setDisabled(True)
        self.districtBox.setDisabled(True)
        self.stateBox.setDisabled(True)
        # Date
        self.dateEdit.setDisabled(True)

    def enablefiled(self):
        # Line Edit enable
        self.nameField.setReadOnly(False)
        self.surnameField.setReadOnly(False)
        self.fiscalcodeField.setReadOnly(False)
        self.addressField.setReadOnly(False)
        self.cityField.setReadOnly(False)
        self.capField.setReadOnly(False)
        self.cellField.setReadOnly(False)
        self.emailField.setReadOnly(False)
        self.telephonField.setReadOnly(False)
        # Combo Box enable
        self.stateBox.setDisabled(False)
        self.genderBox.setDisabled(False)
        self.nationBox.setDisabled(False)
        self.usertypeBox.setDisabled(False)
        self.districtBox.setDisabled(False)
        # Date Enable
        self.dateEdit.setDisabled(False)

    def loaduser(self):
        # metodo che fa una query al database e riempe i campi con
        # quelli dell'utente selezionato dalla vista precedente
        pass

    def save(self):
        # salva le modifiche, fa una query al database e aggiorna i campi dell'utente
        pass

    def back(self):
        #self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        #self.widget.add(UserCardView)
        #self.close()
        self.close()

