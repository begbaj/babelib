from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.uic import loadUi
from datetime import datetime

from src.Users.controllers.UserManager import UserManager
from src.Users.models.User import User


class UserCardView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget, user, callback):

        self.callback = callback

        if user is not None:
            # Se l'utente non è un oggetto nullo allora visualizzo le sue informazioni
            super(UserCardView, self).__init__()
            loadUi("../designer/SchedaUtenteView/SchedaUtenteView.ui", self)
            # Variabili di Istanza
            self.widget = widget
            self.user = user
            self.pop = ''
            # Metodi iniziali
            self.setup()
        else:
            # Se l'utente è nullo allora visualizzo la schermata per crearne uno nuovo
            super(UserCardView, self).__init__()
            loadUi("../designer/New User View/NewUserView.ui", self)
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
        # Button
        self.editButton.setEnabled(True)
        self.returnButton.clicked.connect(self.back)
        self.editButton.clicked.connect(self.enable_filed)
        self.saveButton.clicked.connect(self.save)
        # Disable Field
        self.disable_field()
        # Load User
        self.load_user()
        self.style()

    def style(self):
        self.nameField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())

    def setup_new(self):
        # Button
        self.returnButton.clicked.connect(self.back)
        self.saveButton.clicked.connect(self.save_new)


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
        # Combo Box
        self.genderBox.setCurrentText(self.user.gender)
        self.nationBox.setCurrentText(self.user.Nationality_S.code)
        # self.usertypeBox.setText(self.user.userType.description)
        # Date Edit
        self.dateEdit.setDate(self.user.birthdate)

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
        # Combo Box Update
        self.user.gender = self.genderBox.currentText()
        # self.user.contect_mode =
        # f", u.contect_mode = {user.contect_mode}"
        # f", u.privacy_agreement = {user.privacy_agreement}"
        # Date update
        self.user.birthdate = self.dateEdit.date().toPyDate()

    def save(self):
        """
        Questa funzione permette di effettuare l'Update dell'utente con le informazioni modificate
        :param: None
        :return: None
        """
        # TODO implementare contatto preferenziale e privacy agreement
        self.update_user()
        # PopUp per la conferma
        self.show_popup()

    def save_new(self):
        '''
        #inserire tutti gli attributi dell'utente
        #Controllo per i campi obbligaroi
        #if self.nameField.text() == '' or self.surnameField.text() == '': # mettere altri condizioni
        #    self.pop = Popup()
        #    self.pop.label.setText("Inserire tutti i campi obbligatori")
        #    self.pop.show()
        '''



        user = User(# id
                    0,#self.nationBox.currentText(),
                    0,#self.stateBox.currentText(),
                    0,#self.usertypeBox.currentText(),
                    0,#username , non so quale campo
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # data di registrazione
                    self.nameField.text(),
                    self.surnameField.text(),
                    '',#self.genderBox.currentText(),
                    0,#Luogo di Nascita
                    "2000-01-01 00:00:00",#self.dateEdit.date().toPyDate(), # Data di nascita
                    self.cityField.text(),
                    self.addressField.text(),
                    self.capField.text(),
                    0,#self.districtBox.currentText(),
                    self.cellField.text(),
                    0,#self.telephoneField.text(),
                    self.emailField.text(),
                    self.fiscalcodeField.text(),
                    0,# Contatto Preferenziale
                    0,# Privacy
                    )

        self.userM.add(user)
        print("Salvataggio avvenuto correttamente")



    def back(self):
        self.callback()
        self.close()

    def show_popup(self):
        self.pop = SavePopUp(self.userM, self.user)
        self.pop.show()


class SavePopUp(QDialog):

    def __init__(self, userM, user):
        super(SavePopUp, self).__init__()
        loadUi("../designer/Pop-Up/Save Pop-Up/savepopup.ui", self)
        self.setup()
        self.userM = userM
        self.user = user

    def setup(self):
        # Button
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(lambda: self.close())
        # Proprietà Finestra
        self.setModal(True)
        self.setWindowTitle('Conferma')

    def confirm(self):
        self.userM.set(self.user)
        self.close()


class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/Pop-Up/Message Pop-Up/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)
        self.okButton.clicked.connect(self.close)
