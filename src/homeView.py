from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Users.View.UserView import UserView
from src.Items.View.InventoryView import InventoryView
from src.Services.views.ReservationView import ReservationView
from src.Users.View.UserCardView import UserCardView
from src.Movements.View.MovementsView import MovementsView


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
        self.movementButton.clicked.connect(lambda: self.__go_movement_view())
        self.statsButton.clicked.connect(lambda: self.__go_stats_view())
        # self.reportButton.clicked.connect(self.goreportview())
        # self.serviceButton.clicked.connect(self.goserviceview())
        # self.commButton.clicked.connect(self.gocomunicationview())
        # Shortcut Button
        # self.newloanButton.clicked.connect(self.newloan())
        self.newreservButton.clicked.connect(lambda: self.new_reservation())
        self.newuserButton.clicked.connect(lambda: self.new_user())
        # Setting Button
        # self.settingButton.clicked.connect(self.setting())
        self.style()

    def style(self):
        # Menu Button Style
        self.userButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.catalogingButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.movementButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        # Frame Style
        self.frame.setStyleSheet(open("../designer/style/FrameTheme.txt", "r").read())
        pass

    # region View links
    def __go_user_view(self):
        self.userview = UserView(self.widget)
        self.userview.show()

    def __go_inventory_view(self):
        self.itemview = InventoryView(self.widget, self)
        self.itemview.show()

    def __go_movement_view(self):
        self.moveview = MovementsView(self.widget)
        self.moveview.show()
        pass

    def __go_stats_view(self):
        pass

    def __go_report_view(self):
        pass

    def __go_service_view(self):
        pass

    def __go_communication_view(self):
        pass

    # endregion

    # region Shortcut functions
    def new_loan(self):
        pass

    def new_reservation(self):
        self.reservation = ReservationView(self.widget)
        self.reservation.show()
        pass

    def new_user(self):
        self.newuser = UserCardView(self.widget, None, None)
        self.newuser.show()
        pass

    def setting(self):
        pass
    # end region
