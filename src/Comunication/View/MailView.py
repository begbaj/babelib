from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
#from src.Comunication.Controllers.ComunicationManager import ComunicationManager

class MailView(QWidget):

    comunicationM = ComunicationManager()

    def __init__(self, widget):
        super(MailView, self).__init__()
        loadUi("../designer/Users/UserView.ui", self)

        self.widget = widget
        self.pop = ''
        self.load_data()
        self.setup()

