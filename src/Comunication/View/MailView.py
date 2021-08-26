from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from src.Comunication.Controllers.ComunicationManager import ComunicationManager
import smtplib

from src.Users.controllers.UserManager import UserManager
from src.Utils.UI import Popup


class MailView(QWidget):

    comunicationM = ComunicationManager()

    def __init__(self, widget):
        super(MailView, self).__init__()
        loadUi("../designer/Comunications/MailView.ui", self)
        self.comunications = self.comunicationM.list()
        self.widget = widget
        self.pop = ''
        self.setup()

    def setup(self):
        self.setup_email()
        self.setup_component()

    def set_combo_box(self):
        self.com_sub_list = []
        self.com_sub_list.append('')
        for com in self.comunications:
            self.com_sub_list.append(com.subject)

        self.messageBox.addItems(self.com_sub_list)
        self.messageBox.currentTextChanged.connect(self.on_messageBox_changed)

        self.userM = UserManager()
        self.users = self.userM.list()

        self.users_combo = []

        self.com_rec_list = []
        self.com_rec_list.append('')

        for user in self.users:
            if user.email != '':
                self.com_rec_list.append(user.name + " " + user.surname)
                self.users_combo.append(user)

        self.recipientBox.addItems(self.com_rec_list)
        self.recipientBox.currentTextChanged.connect(self.on_recipientBox_changed)


    def setup_component(self):
        self.sendButton.clicked.connect(self.send)
        self.refreshtextButton.clicked.connect(self.refresh_text)
        self.backButton.clicked.connect(self.close)
        self.refreshtextButton.hide()


        self.mailField.setText(self.sender_email)
        self.mailField.setReadOnly(True)
        self.objectMail.setReadOnly(True)

        self.set_combo_box()


    def setup_email(self):
        self.sender_email = "fake.biblioteca@gmail.com"  # Enter your address
        self.rec_email = ""  # Enter receiver address
        self.password = "biblioteca12345"
        self.message = """\
                               Subject:
                               """

    def on_messageBox_changed(self):
        print(self.messageBox.currentIndex())
        if self.messageBox.currentText() == '':
            self.objectMail.setPlainText('')
            self.textMail.setPlainText('')
            self.refreshtextButton.hide()
            self.objectMail.setReadOnly(False)
        else:
            self.comunication = self.comunicationM.find(self.messageBox.currentIndex())
            self.objectMail.setPlainText(self.comunication.subject)
            self.textMail.setPlainText(self.comunication.text)
            self.refreshtextButton.show()
            self.objectMail.setReadOnly(True)

    def on_recipientBox_changed(self):
        self.rec_email = self.users_combo[self.recipientBox.currentIndex()].email

    def send(self):

        self.sender_email = "fake.biblioteca@gmail.com"  # Enter your address
        self.rec_email = f"{self.users_combo[self.recipientBox.currentIndex()].email}"  # Enter receiver address
        self.password = "biblioteca12345"
        '''self.message = f" Subject:{self.objectMail.toPlainText()}\n"\
                       f" {self.textMail.toPlainText()}"
'''
        self.message = """\
                Subject: {0}

                {1}"""

        self.message.format(self.objectMail.toPlainText(),self.textMail.toPlainText())

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.password)
        print("Login success")
        self.server.sendmail(self.sender_email, self.rec_email, self.message)
        self.pop = Popup("Email inviata con successo!")
        self.pop.show()
        print("Email has been sent to ", self.rec_email)

    def refresh_text(self):
        self.comunication.text = self.textMail.toPlainText()
        #self.comunication.subject = self.objectMail.toPlainText()
        self.comunicationM.set(self.comunication)
        self.pop = Popup("Email predefinita aggiornata!")
        self.pop.show()




