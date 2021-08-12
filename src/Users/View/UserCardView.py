from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from src.Users.controllers.UserManager import UserManager


class UserCardView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget, user):
        super(UserCardView, self).__init__()
        loadUi("../designer/SchedaUtenteView/SchedaUtenteView.ui", self)

        self.widget = widget
        self.user = user
        self.pop = ''

        self.setup()
        self.loaduser()

    def setup(self):
        # Button
        self.editButton.setEnabled(True)
        self.returnButton.clicked.connect(self.back)
        self.editButton.clicked.connect(self.enablefiled)
        self.saveButton.clicked.connect(self.save)
        # Disable Field
        self.disablefield()

    def disablefield(self):
        # Line Edit enable
        self.nameField.setReadOnly(True)
        self.surnameField.setReadOnly(True)
        self.fiscalcodeField.setReadOnly(True)
        self.addressField.setReadOnly(True)
        self.cityField.setReadOnly(True)
        self.capField.setReadOnly(True)
        self.cellField.setReadOnly(True)
        self.emailField.setReadOnly(True)
        self.telephonField.setReadOnly(True)
        # Box
        self.genderBox.setDisabled(True)
        self.nationBox.setDisabled(True)
        self.usertypeBox.setDisabled(True)
        self.districtBox.setDisabled(True)
        self.stateBox.setDisabled(True)
        # Date
        self.dateEdit.setDisabled(True)

    def loaduser(self):
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
        # Date Edit
        self.dateEdit.setDate(self.user.birthdate)
        # self.usertypeBox.setText(self.user.userType.description)

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
        self.editButton.setEnabled(False)

    # TODO implementare contatto preferenziale e privacy agreement
    def save(self):
        # Update dell'utente
        self.user.name = self.nameField.text()
        self.user.surname = self.surnameField.text()
        self.user.fiscal_code = self.fiscalcodeField.text()
        self.user.address = self.addressField.text()
        self.user.city = self.cityField.text()
        self.user.postal_code = self.capField.text()
        self.user.first_cellphone = self.cellField.text()
        self.user.email = self.emailField.text()
        self.user.telephone = self.telephonField.text()
        self.showpopup(self.userM, self.user)
        # self.pop.close()
        # self.user.contect_mode =
        # f", u.contect_mode = {user.contect_mode}"
        # f", u.privacy_agreement = {user.privacy_agreement}"

    def back(self):
        self.close()

    def showpopup(self, userM, user):
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
