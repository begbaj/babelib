from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from mariadb import Date

from src.Users.controllers.UserManager import UserManager


class UserCardView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget, user, callback):

        self.callback = callback

        if user is not None:
            super(UserCardView, self).__init__()
            loadUi("../designer/SchedaUtenteView/SchedaUtenteView.ui", self)
            # Variabili di Istanza
            self.widget = widget
            self.user = user
            self.pop = ''
            # Metodi iniziali
            self.setup()
        else:
            super(UserCardView, self).__init__()
            loadUi("../designer/New User View/NewUserView.ui", self)
            # Variabili di Istanza
            self.pop = ''
            # Metodi iniziali
            self.setup_new()


    def setup(self):
        # Button
        self.editButton.setEnabled(True)
        self.returnButton.clicked.connect(self.back)
        self.editButton.clicked.connect(self.enable_filed)
        self.saveButton.clicked.connect(self.save)
        # Disable Field
        self.disable_field()
        # Load User
        self.load_user()

    def setup_new(self):
        # Button
        self.returnButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save_new)

    def disable_field(self):
        # Line Edit disabled
        self.nameField.setReadOnly(True)
        self.surnameField.setReadOnly(True)
        self.fiscalcodeField.setReadOnly(True)
        self.addressField.setReadOnly(True)
        self.cityField.setReadOnly(True)
        self.capField.setReadOnly(True)
        self.cellField.setReadOnly(True)
        self.emailField.setReadOnly(True)
        self.telephonField.setReadOnly(True)
        # Box disabled
        self.genderBox.setDisabled(True)
        self.nationBox.setDisabled(True)
        self.usertypeBox.setDisabled(True)
        self.districtBox.setDisabled(True)
        self.stateBox.setDisabled(True)
        # Date disabled
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setDisabled(True)

    def enable_filed(self):
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
        # Date enable
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setDisabled(False)
        self.editButton.setEnabled(False)

    def load_user(self):
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
        # self.usertypeBox.setText(self.user.userType.description)
        # Date Edit
        self.dateEdit.setDate(self.user.birthdate)

    # TODO implementare contatto preferenziale e privacy agreement
    # Update dell'utente
    def save(self):
        # Line edit update
        self.user.name = self.nameField.text()
        self.user.surname = self.surnameField.text()
        self.user.fiscal_code = self.fiscalcodeField.text()
        self.user.address = self.addressField.text()
        self.user.city = self.cityField.text()
        self.user.postal_code = self.capField.text()
        self.user.first_cellphone = self.cellField.text()
        self.user.email = self.emailField.text()
        self.user.telephone = self.telephonField.text()
        # Combo Box Update
        self.user.gender = self.genderBox.currentText()
        # self.user.contect_mode =
        # f", u.contect_mode = {user.contect_mode}"
        # f", u.privacy_agreement = {user.privacy_agreement}"
        # Date update
        self.user.birthdate = self.dateEdit.date().toPyDate()
        # PopUp per la conferma
        self.show_popup(self.userM, self.user)

    def save_new(self):
        pass

    def back(self):
        self.callback()
        self.close()

    def show_popup(self, userM, user):
        self.pop = SavePopUp(userM, user)
        self.pop.show()


class SavePopUp(QDialog):

    def __init__(self, userM, user):
        super(SavePopUp, self).__init__()
        loadUi("../designer/SavePopUp/savepopup.ui", self)
        self.setWindowTitle('Conferma')
        self.setModal(True)
        self.setup()
        self.userM = userM
        self.user = user

    def setup(self):
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.cancel)

    def cancel(self):
        self.close()

    def confirm(self):
        self.userM.set(self.user)
        self.close()
