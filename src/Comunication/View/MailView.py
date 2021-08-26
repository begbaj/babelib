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
        self.load_data()
        self.setup()

    def setup(self):
        self.setup_email()
        self.setup_component()

    def setup_component(self):
        self.sendButton.clicked.connect(self.send)
        self.refreshtextButton.clicked.connect(self.refresh_text)
        self.backButton.clicked.connect(self.close)
        self.mailField.setText(self.sender_email)
        self.mailField.setReadOnly(True)

        com_sub_list = []
        com_sub_list.append('')
        for com in self.comunications:
            com_sub_list.append(com.subject)

        self.messageBox.addItems(com_sub_list)

        self.userM = UserManager()
        self.users = self.userM.list()

        com_rec_list = []
        com_rec_list.append('')

        for user in self.users:
            if user.email != '':
                com_rec_list.append(user.name + " " + user.surname)

        self.recipientBox.addItems(com_rec_list)

    def setup_email(self):
        self.sender_email = "fake.biblioteca@gmail.com"  # Enter your address
        self.rec_email = ""  # Enter receiver address
        self.password = "biblioteca12345"
        self.message = """\
                               Subject:
                               """



    def load_data(self):
        pass

    def send(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.password)
        print("Login success")
        self.server.sendmail(self.sender_email, self.rec_email, self.message)
        pop = Popup("Email inviata con successo!")
        pop.show()
        print("Email has been sent to ", self.rec_email)

    def refresh_text(self):
        #self.comunicationM.set()
        pass



