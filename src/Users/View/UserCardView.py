from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from datetime import datetime
import os
from src.Users.controllers.UserManager import UserManager
from src.Users.models.User import User
from src.Utils.UI import SavePopUp, Popup


class UserCardView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget, user, callback=None):
        if callback is None:
            self.callback = self.close
        else:
            self.callback = callback
        if user is not None:
            # Se l'utente non è un oggetto nullo allora visualizzo le sue informazioni
            super(UserCardView, self).__init__()
            loadUi("../designer/Users/SchedaUtenteView.ui", self)
            # Variabili di Istanza
            self.widget = widget
            self.user = user
            self.pop = ''
            # Metodi iniziali
            self.setup()
        else:
            # Se l'utente è nullo allora visualizzo la schermata per crearne uno nuovo
            super(UserCardView, self).__init__()
            loadUi("../designer/Users/NewUserView.ui", self)
            # Variabili di Istanza
            self.pop = ''
            # Metodi iniziali
            self.setup_new()

    def setup(self):
        """
        Questa funzione consente di settare la view
        :param: None
        :return: None
        """
        self.editButton.setEnabled(True)
        self.editButton.clicked.connect(self.edit)
        self.saveButton.clicked.connect(self.save)
        self.returnButton.clicked.connect(self.back)
        self.disable_field()
        self.regular_exp_field()
        self.setup_combo_box()
        # Load User
        self.load_user()
        self.style()

    def style(self):
        self.nameField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.surnameField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.fiscalcodeField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.addressField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.cityField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.capField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.cellField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.emailField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.telephonField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.birthplaceField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())

    def setup_new(self):
        self.returnButton.clicked.connect(self.back)
        self.saveButton.clicked.connect(self.save_new)
        self.enable_field()
        self.setup_combo_box()
        self.setup_radio_button()
        self.regular_exp_field()

# region Field Function

    def setup_combo_box(self):
        # Import Gender item
        f = open(os.path.abspath("config/gender.txt"), "r")
        content_list = [line.rstrip('\n') for line in f]
        f.close()
        self.genderBox.addItems(content_list)
        # Import District item
        f = open(os.path.abspath("config/district.txt"), "r")
        content_list = [line.rstrip('\n') for line in f]
        f.close()
        self.districtBox.addItems(content_list)
        # Import UserType item
        f = open(os.path.abspath("config/user_type.txt"), "r")
        content_list = [line.rstrip('\n') for line in f]
        f.close()
        self.usertypeBox.addItems(content_list)
        # Import Nationality item
        f = open(os.path.abspath("config/nationality.txt"), "r")
        content_list = [line.rstrip('\n') for line in f]
        f.close()
        self.nationBox.addItems(content_list)

    def setup_radio_button(self):
        self.cellularRadio.setChecked(True)

    def disable_field(self):
        """
        Questa funzione setta tutti i campi presenti nella view in solo lettura
        :param: None
        :return: None
        """
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
        self.birthplaceField.setReadOnly(True)
        # Box disabled
        self.genderBox.setDisabled(True)
        self.nationBox.setDisabled(True)
        self.usertypeBox.setDisabled(True)
        self.districtBox.setDisabled(True)
        self.stateBox.setDisabled(True)
        # Date disabled
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setDisabled(True)
        # Radio disabled
        self.emailRadio.setDisabled(True)
        self.cellularRadio.setDisabled(True)
        self.telephoneRadio.setDisabled(True)

    def enable_field(self):
        """
        Questa funzione setta tutti i campi presenti nella view come editabili
        :param: None
        :return: None
        """
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
        self.birthplaceField.setReadOnly(False)
        # Combo Box enable
        self.stateBox.setDisabled(False)
        self.genderBox.setDisabled(False)
        self.nationBox.setDisabled(False)
        self.usertypeBox.setDisabled(False)
        self.districtBox.setDisabled(False)
        # Date enable
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setDisabled(False)
        # Radio Button enable
        self.emailRadio.setDisabled(False)
        self.cellularRadio.setDisabled(False)
        self.telephoneRadio.setDisabled(False)
        # Box enable
        self.privacyBox.setDisabled(False)

    def regular_exp_field(self):
        # Strings Field
        self.nameField.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z " "]*$')))
        self.surnameField.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z " "]*$')))
        self.fiscalcodeField.setValidator(QRegExpValidator(QRegExp('^[A-Z 0-9]*$')))
        self.cityField.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z " "]*$')))
        self.addressField.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z " " à è ò 0-9]*$')))
        self.emailField.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z " " @ . 0-9]*$')))
        # Digits Field
        self.cellField.setValidator(QIntValidator())
        self.telephonField.setValidator(QIntValidator())
        self.capField.setValidator(QIntValidator())

# endregion

# region Button Function

    def save(self):
        """
        Questa funzione permette di effettuare l'Update dell'utente con le informazioni modificate
        :param: None
        :return: None
        """
        if self.nameField.text() == '' or self.surnameField.text() == '' or self.fiscalcodeField.text() == '' or self.privacyBox.isChecked() == False:
            self.pop = Popup()
            self.pop.label.setText("Inserire tutti i campi obbligatori.")
            self.pop.show()
            return

        if self.cellularRadio.isChecked() and self.cellField.text() == '' or self.emailRadio.isChecked() and self.emailField.text() == '' or self.telephoneRadio.isChecked() and self.telephonField.text() == '':
            self.pop = Popup()
            self.pop.label.setText("Inserire contatto.")
            self.pop.show()
            return
        self.update_user()
        self.show_popup()

    def edit(self):
        self.enable_field()
        self.editButton.setEnabled(False)

    def back(self):
        self.callback()
        self.close()

    def save_new(self):

        if self.nameField.text() == '' or self.surnameField.text() == '' or self.fiscalcodeField.text() == '' or self.privacyBox.isChecked() == False:
            self.pop = Popup()
            self.pop.label.setText("Inserire tutti i campi obbligatori.")
            self.pop.show()
            return

        if self.cellularRadio.isChecked() and self.cellField.text() == '' or self.emailRadio.isChecked() and self.emailField.text() == '' or self.telephoneRadio.isChecked() and self.telephonField.text() == '':
            self.pop = Popup()
            self.pop.label.setText("Inserire contatto.")
            self.pop.show()
            return

        user = User(self.nationBox.currentText(),
                    self.usertypeBox.currentText(),
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    self.nameField.text(),
                    self.surnameField.text(),
                    self.genderBox.currentText(),
                    self.birthplaceField.text(),
                    self.dateEdit.date().toPyDate(),
                    self.cityField.text(),
                    self.addressField.text(),
                    self.capField.text(),
                    self.districtBox.currentText(),
                    self.cellField.text(),
                    self.telephonField.text(),
                    self.emailField.text(),
                    self.fiscalcodeField.text(),
                    self.update_contact(),
                    self.privacyBox.isChecked(),
                    )
        self.saveButton.setEnabled(False)
        self.userM.add(user)
        self.callback()
        self.close()

    def cell_contact(self):
        if self.cellField.text() == '':
            self.cellularRadio.setChecked(True)
            self.cellularRadio.setChecked(False)
            self.pop = Popup()
            self.pop.label.setText("Prima inserisci il recapito")
            self.pop.show()
        else:
            pass

    def email_contact(self):
        if self.emailField.text() == '':
            self.cellularRadio.setChecked(False)
            self.pop = Popup()
            self.pop.label.setText("Prima inserisci il recapito")
            self.pop.show()
        else:
            pass

    def telephone_contact(self):
        if self.telephonField.text() == '':
            self.pop = Popup()
            self.pop.label.setText("Prima inserisci il recapito")
            self.pop.show()
            self.cellularRadio.setChecked(False)
        else:
            pass
# endregion

# region View Function

    def closeEvent(self, event):
        self.callback()

    def load_user(self):
        """
        Questa funzione riempe i campi della view con le informazioni dell'utente
        di cui si vuole consultare la scheda
        :param: None
        :return: None
        """
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
        self.birthplaceField.setText(self.user.birthplace)
        # Combo Box
        self.nationBox.setCurrentText(self.user.nationality)
        self.genderBox.setCurrentText(self.user.gender)
        self.usertypeBox.setCurrentText(self.user.user_type)
        self.districtBox.setCurrentText(self.user.district)
        # Date Edit
        self.dateEdit.setDate(self.user.birthdate)
        # Combo box
        if self.user.contect_mode == self.user.email:
            self.emailRadio.setChecked(True)
        elif self.user.contect_mode == self.user.first_cellphone:
            self.cellularRadio.setChecked(True)
        elif self.user.contect_mode == self.user.telephone:
            self.telephoneRadio.setChecked(True)
        # Privacy Box
        if self.user.privacy_agreement:
            self.privacyBox.setChecked(True)

    def update_user(self):
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
        self.user.birthplace = self.birthplaceField.text()
        # Combo Box update
        self.user.nationality = self.nationBox.currentText()
        self.user.gender = self.genderBox.currentText()
        self.user.district = self.districtBox.currentText()
        self.user.user_type = self.usertypeBox.currentText()
        # Radio Button update
        self.user.contect_mode = self.update_contact()
        # Date update
        self.user.birthdate = self.dateEdit.date().toPyDate()

        if self.privacyBox.isChecked():
            self.user.privacy_agreement = True

    def update_contact(self):
        if self.emailRadio.isChecked():
            return self.emailField.text()
        elif self.cellularRadio.isChecked():
            return self.cellField.text()
        elif self.telephoneRadio.isChecked():
            return self.telephonField.text()

    def show_popup(self):
        self.pop = SavePopUp(self.userM, self.user)
        self.pop.show()

# endregion
#enableButton