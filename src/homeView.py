from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Users.View.UserView import UserView
from src.Items.View.InventoryView import InventoryView


class HomeView(QMainWindow):

    def __init__(self, widget):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
        # Variabili di Istanza
        self.widget = widget
        # Metodi Iniziali
        self.setup()

    def setup(self):
        # Menu Button
        self.userButton.clicked.connect(lambda: self.__go_user_view())
        self.catalogingButton.clicked.connect(lambda: self.__go_inventory_view())
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
        self.style()

    def style(self):
        self.userButton.setStyleSheet(open("../designer/style/buttonTheame.txt", "r").read())
        self.catalogingButton.setStyleSheet(open("../designer/style/buttonTheame.txt", "r").read())
        self.frame.setStyleSheet(open("../designer/style/FrameTheme.txt", "r").read())
        pass

    # region View links
    def __go_user_view(self):
        self.userview = UserView(self.widget)
        self.userview.show()

    def __go_inventory_view(self):
        self.itemview = InventoryView(self.widget)
        self.itemview.show()

    def __go_stats_view(self):
        pass

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
