import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from Users.View.UserView import UserView


class HomeView(QMainWindow):

    def __init__(self):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
        self.setup()

    def setup(self):
        # Menu Button
        self.userButton.clicked.connect(self.gouserview())
        self.catalogingButton.clicked.connect(self.goinventoryview())
        self.statsButton.clicked.connect(self.gostatsview())
        self.reportButton.clicked.connect(self.goreportview())
        self.serviceButton.clicked.connect(self.goserviceview())
        self.commButton.clicked.connect(self.gocomunicationview())
        self.movementButton.clicked.connect(self.gomovemetview())
        # Shortcut Button
        self.newloanButton.clicked.connect(self.newloan())
        self.newreservButton.clicked.connect(self.newreservation())
        self.newuserButton.clicked.connect(self.newuser())
        # Setting Button
        self.settingButton.clicked.connect(self.setting())

    # region Collegamenti View
    def gouserview(self):
        self.cams = UserView()
        self.cams.show()
        self.close()
        self.hide()

    def gostatsview(self):
        pass

    def goinventoryview(self):
        pass

    def goreportview(self):
        pass

    def goserviceview(self):
        pass

    def gomovemetview(self):
        pass

    def gocomunicationview(self):
        pass
    # endregion

    # region Shortcut function
    def newloan(self):
        pass

    def newreservation(self):
        pass

    def newuser(self):
        pass

    def setting(self):
        pass
    # end region