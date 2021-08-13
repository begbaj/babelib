import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from Users.View.UserView import UserView
from src.Items.View.ItemView import ItemView


class HomeView(QMainWindow):

    def __init__(self, widget):
        super(HomeView, self).__init__()
        self.setFixedSize(660, 500)
        loadUi("../designer/Home view/HomeView.ui", self)
        self.widget = widget
        self.setup()

    def setup(self):
        # Menu Button
        self.userButton.clicked.connect(lambda: self.__go_user_view())
        self.catolgingButton.clicked.connect(lambda: self.__go_inventory_view())
        # self.statsButton.clicked.connect(self.gostatsview())
        # self.reportButton.clicked.connect(self.goreportview())
        # self.serviceButton.clicked.connect(self.goserviceview())
        # self.commButton.clicked.connect(self.gocomunicationview())
        # self.movementButton.clicked.connect(self.gomovemetview())
        # Shortcut Button
        # self.newloanButton.clicked.connect(self.newloan())
        # self.newreservButton.clicked.connect(self.newreservation())
        # self.newuserButton.clicked.connect(self.newuser())
        # Setting Button
        # self.settingButton.clicked.connect(self.setting())
        pass

    # region View links

    def __go_user_view(self):
        self.userview = UserView(self.widget)
        self.userview.show()

        #self.widget.addWidget(view)
        #self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def __go_stats_view(self):
        pass

    def __go_inventory_view(self):
        self.itemview = ItemView(self.widget)
        self.itemview.show()

        #self.widget.addWidget(view)
        #self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def __go_report_view(self):
        pass

    def __go_service_view(self):
        pass

    def __go_movement_view(self):
        pass

    def __go_communication_view(self):
        pass

    # endregion

    # region Shortcut functions
    def new_loan(self):
        pass

    def new_reservation(self):
        pass

    def new_user(self):
        pass

    def setting(self):
        pass
    # end region
