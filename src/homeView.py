from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget
from PyQt5.uic import loadUi
from src.Movements.Controllers.MovementManager import MovementManager
from src.Services.controllers.ServiceReservationManager import ServiceReservationManager

from src.Stats.View.StatsView import StatsView
from Users.View.UserView import UserView
from src.Items.View.InventoryView import InventoryView
from src.Services.views.NewReservationView import NewReservationView
from src.Services.views.ReservationView import ReservationView
from src.Users.View.UserCardView import UserCardView
from src.Movements.View.MovementsView import MovementsView


class HomeView(QMainWindow):

    def __init__(self, widget):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
        # Variabili di Istanza
        self.widget = widget
        self.movem = MovementManager()
        self.resM = ServiceReservationManager()
        # Metodi Iniziali
        self.setup()

    def setup(self):
        # Menu Button
        self.userButton.clicked.connect(self.__go_user_view)
        self.catalogingButton.clicked.connect(self.__go_inventory_view)
        self.movementButton.clicked.connect(self.__go_movement_view)
        self.statsButton.clicked.connect(self.__go_stats_view)
        # self.reportButton.clicked.connect(self.goreportview())
        self.serviceButton.clicked.connect(self.__go_service_view)
        # self.commButton.clicked.connect(self.gocomunicationview())
        # Shortcut Button
        # self.newloanButton.clicked.connect(self.newloan())
        self.newreservButton.clicked.connect(self.new_reservation)
        self.newuserButton.clicked.connect(self.new_user)
        self.service_reservation_calendar_widget.selectionChanged.connect(self.__update_reservation_table)
        self.service_reservation_calendar_widget.selectionChanged.connect(self.load_movement_table)
        self.__update_reservation_table()
        self.load_movement_table()
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
        self.statsview = StatsView(self.widget)
        self.statsview.show()

    def __go_report_view(self):
        pass

    def __go_service_view(self):
        self.services = ReservationView(self.widget)
        self.services.show()
        pass

    def __go_communication_view(self):
        pass

    # endregion

    # region Shortcut functions

    def new_loan(self):
        pass

    def new_reservation(self):
        self.res = NewReservationView(self.widget)
        self.res.show()
        pass

    def new_user(self):
        self.newuser = UserCardView(self.widget, None, None)
        self.newuser.show()
        pass

    def setting(self):
        pass

    def __update_reservation_table(self):
        """
        this method allows to update the table with all the reservations
        :return: returns a list with the signed and unsigned reservations
        """
        self.reservation_table_widget.clearSelection()
        self.__remove_rows()
        self.__unsigned = self.resM.get_unsigned_by_date(self.service_reservation_calendar_widget.selectedDate().toPyDate())
        self.__signed = self.resM.get_all_signed_by_date(self.service_reservation_calendar_widget.selectedDate().toPyDate())
        if len(self.__unsigned) > 0:
            for res in self.__unsigned:
                row = self.reservation_table_widget.rowCount()
                self.reservation_table_widget.insertRow(row)
                self.reservation_table_widget.setItem(row, 0, QTableWidgetItem(res.fullname))
                self.reservation_table_widget.setItem(row, 2, QTableWidgetItem(res.date_from.strftime("%m/%d/%Y")))
                self.reservation_table_widget.setItem(row, 3, QTableWidgetItem(res.date_from.strftime("%H:%M:%S") + " - " + res.date_to.strftime("%H:%M:%S")))
                self.reservation_table_widget.setItem(row, 1, QTableWidgetItem(res.cellphone))
        if len(self.__signed) > 0:
            for res in self.__signed:
                row = self.reservation_table_widget.rowCount()
                self.reservation_table_widget.insertRow(row)
                self.reservation_table_widget.setItem(row, 0, QTableWidgetItem(res.fullname))
                self.reservation_table_widget.setItem(row, 1, QTableWidgetItem(res.cellphone))
                self.reservation_table_widget.setItem(row, 2, QTableWidgetItem(res.date_from.strftime("%m/%d/%Y")))
                self.reservation_table_widget.setItem(row, 3, QTableWidgetItem(
                    res.date_from.strftime("%H:%M:%S") + " - " + res.date_to.strftime("%H:%M:%S")))
                row = row + 1

        self.reservation_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.__reservations = []
        if self.__unsigned is not None:
            for i in self.__unsigned:
                self.__reservations.append(i)
        if self.__signed is not None:
            for i in self.__signed:
                self.__reservations.append(i)

    def __remove_rows(self):
        """
        this method allows to remove rows from the reservations table
        :return: None
        """
        for i in reversed(range(0, self.reservation_table_widget.rowCount())):
            self.reservation_table_widget.removeRow(i)

    def load_movement_table(self):
        """
        Questo metodo permette di rimpire la QTableWidget presente nella view con una lista di utenti
        :param users:
        :return: None
        """
        row = 0
        movements = self.movem.get_movements_by_date(self.service_reservation_calendar_widget.selectedDate().toPyDate())
        self.movement_table_widget.setRowCount(len(movements))
        for movement in movements:
            self.movement_table_widget.setItem(row, 0, QTableWidgetItem(movement.timestamp.strftime('%d/%m/%Y %H:%M:%S')))
            self.movement_table_widget.setItem(row, 1, QTableWidgetItem(movement.item.isbn))
            self.movement_table_widget.setItem(row, 2, QTableWidgetItem(movement.item.title))
            self.movement_table_widget.setItem(row, 3, QTableWidgetItem(movement.user.fiscal_code))
            self.movement_table_widget.setItem(row, 4, QTableWidgetItem(movement.user.name + " " + movement.user.surname))
            self.movement_table_widget.setItem(row, 5, QTableWidgetItem(movement.user.first_cellphone))
            row = row + 1

    # endregion
