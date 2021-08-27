from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from src.Comunication.Controllers.ComunicationManager import ComunicationManager
import smtplib
from email.mime.text import MIMEText
from src.Users.controllers.UserManager import UserManager
from src.Utils.UI import Popup


class MailView(QWidget):

    # Manager
    comunicationM = ComunicationManager()
    userM = UserManager()

    # Variabili per email
    sender_email = ''
    rec_email = ''
    password = ''
    server = ''
    msg = ''

    def __init__(self, widget):
        super(MailView, self).__init__()
        loadUi("../designer/Comunications/MailView.ui", self)
        # Variaibili
        self.widget = widget
        self.comunications = self.comunicationM.list()
        self.users = ''
        self.comunication = ''
        self.pop = ''
        self.com_sub_list = ''
        self.users_combo = []
        self.com_rec_list = []
        # Metodi Iniziali
        self.setup()

# Region Set-Up

    def setup(self):
        self.setup_email()
        self.setup_component()

    def setup_component(self):
        # Function Button
        self.sendButton.clicked.connect(self.send)
        self.refreshtextButton.clicked.connect(self.refresh_text)
        self.backButton.clicked.connect(self.close)
        # Field Properties
        self.refreshtextButton.hide()
        self.mailField.setText(self.sender_email)
        self.mailField.setReadOnly(True)
        self.objectMail.setReadOnly(True)
        # ComboBox
        self.set_combo_box()

    def set_combo_box(self):
        # Lista dei Messaggi Predefiniti
        self.com_sub_list = []
        self.com_sub_list.append('')
        for com in self.comunications:
            self.com_sub_list.append(com.subject)
        self.messageBox.addItems(self.com_sub_list)
        # Al cambiare del contenuto della comboBox cambia l'oggetto e il testo
        self.messageBox.currentTextChanged.connect(self.on_message_box_changed)

        # Lista Utenti che hanno registrato una mail
        self.users = self.userM.list()
        self.users_combo = []
        self.com_rec_list = []
        self.com_rec_list.append('')
        for user in self.users:
            if user.email != '':
                self.com_rec_list.append(user.name + " " + user.surname)
                self.users_combo.append(user)
        self.recipientBox.addItems(self.com_rec_list)
        # Al cambiare dell'utente selezionato cambia il destinatario
        self.recipientBox.currentTextChanged.connect(self.on_recipient_box_changed)

    def setup_email(self):
        # Credenziali per la mail
        self.sender_email = "fake.biblioteca@gmail.com"  # Enter your address
        self.password = "biblioteca12345"

# endregion

# Region Button Function

    def on_message_box_changed(self):
        # Eventi della Combo Box dei messaggi
        if self.messageBox.currentText() == '':
            self.objectMail.setPlainText('')
            self.textMail.setPlainText('')
            self.refreshtextButton.hide()
            self.objectMail.setReadOnly(False)
        else:
            self.objectMail.setPlainText(self.comunicationM.find(self.messageBox.currentIndex()).subject)
            self.textMail.setPlainText(self.comunicationM.find(self.messageBox.currentIndex()).text)
            self.refreshtextButton.show()
            self.objectMail.setReadOnly(True)

    def on_recipient_box_changed(self):
        self.rec_email = self.users_combo[self.recipientBox.currentIndex() - 1].email

    def send(self):
        # Destinatario
        self.rec_email = f"{self.users_combo[self.recipientBox.currentIndex()-1].email}"
        # Contenuto del Messaggio
        self.msg = MIMEText(self.textMail.toPlainText())
        self.msg['Subject'] = self.objectMail.toPlainText()
        # Connessione con il Server
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.password)
        print("Login success")
        # Inoltro e-mail
        self.server.sendmail(self.sender_email, self.rec_email, self.msg.as_string())
        self.pop = Popup("Email inviata con successo!")
        self.pop.show()
        print("Email has been sent to ", self.msg)

    def refresh_text(self):
        self.comunication.text = self.textMail.toPlainText()
        self.comunicationM.set(self.comunication)
        self.pop = Popup("Email predefinita aggiornata!")
        self.pop.show()

# endregion
