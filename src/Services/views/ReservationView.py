from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QDialogButtonBox, QTableWidget
from PyQt5.uic import loadUi
from datetime import datetime

from src.Items.View.InventoryView import ErrorMessage
from src.Services.controllers.ServiceReservationManager import ServiceReservationManager
from src.Services.models.SignedServiceReservation import SignedServiceReservation
from src.Services.models.UnsignedServiceReservation import UnsignedServiceReservation
from src.Services.views.NewReservationView import NewReservationView
from src.Users.controllers.UserManager import UserManager


class ReservationView(QMainWindow):
    __reservations = []
    __signed = []
    __unsigned = []

    resM = ServiceReservationManager()
    new_signed = SignedServiceReservation()
    userM = UserManager()

    def __init__(self, widget):
        """
        init method
        :param widget: widget to open view
        """
        self.widget = widget
        super(ReservationView, self).__init__()
        loadUi("../designer/Reservation/ReservationView.ui", self)
        self.return_button.clicked.connect(lambda: self.close())
        self.add_reservation.clicked.connect(lambda: self.go_new_reservation())
        self.delete_reservation.clicked.connect(lambda: self.discard_res())
        self.searchField.textChanged.connect(lambda: self.search())
        self.search()

    def go_new_reservation(self):
        """
        this method allows to go to reservation view
        :return:
        """
        self.new_res = NewReservationView(self.widget, self.search)
        self.new_res.show()

    def __update_table(self):
        """
        this method allows to update the table with all the reservations
        :return: returns a list with the signed and unsigned reservations
        """
        self.reservationTable.clearSelection()
        self.__remove_rows()
        self.__unsigned = self.resM.get_unsigned_(self.searchField.text())
        self.__signed = self.resM.get_all_signed(self.searchField.text())
        if self.__unsigned is not None:
            for res in self.__unsigned:
                row = self.reservationTable.rowCount()
                self.reservationTable.insertRow(row)
                self.reservationTable.setItem(row, 0, QTableWidgetItem(res.fullname))
                self.reservationTable.setItem(row, 2, QTableWidgetItem(res.date_from.strftime("%m/%d/%Y")))
                self.reservationTable.setItem(row, 3, QTableWidgetItem(res.date_from.strftime("%H:%M:%S") + " - " + res.date_to.strftime("%H:%M:%S")))
                self.reservationTable.setItem(row, 1, QTableWidgetItem(res.cellphone))
        if self.__signed is not None:
            for res in self.__signed:
                row = self.reservationTable.rowCount()
                self.reservationTable.insertRow(row)
                self.reservationTable.setItem(row, 0, QTableWidgetItem(res.fullname))
                self.reservationTable.setItem(row, 1, QTableWidgetItem(res.cellphone))
                self.reservationTable.setItem(row, 2, QTableWidgetItem(res.date_from.strftime("%m/%d/%Y")))
                self.reservationTable.setItem(row, 3, QTableWidgetItem(
                    res.date_from.strftime("%H:%M:%S") + " - " + res.date_to.strftime("%H:%M:%S")))
                row = row + 1

        self.reservationTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.__reservations = []
        if self.__unsigned is not None:
            for i in self.__unsigned:
                self.__reservations.append(i)
        if self.__signed is not None:
            for i in self.__signed:
                self.__reservations.append(i)

    def search(self):
        """
        this method refreshed the table
        :return: the table with the refreshed rows
        """
        self.__update_table()

    def discard_res(self):
        """
        this method allows to discard am unsigned or signed reservation
        :return: None
        """
        res = self.__get_selected_res()
        if res is None:
            ErrorMessage("Selezionare un elemento da scartare!").exec_()
            return

        discard = Dialog(f"Sei sicuro? Questa azione è irreversibile!")
        ok = discard.exec_()
        if ok:
            if res.n_fields == 6:
                self.resM.delete_signed(res.id)
            else:
                self.resM.delete_unsigned(res.id)
        self.search()

    def __remove_rows(self):
        """
        this method allows to remove rows from the reservations table
        :return: None
        """
        for i in reversed(range(0, self.reservationTable.rowCount())):
            self.reservationTable.removeRow(i)

    def __get_selected_res(self):
        """
        this method allows to get the selected signed or unsigned reservation
        :return: None if no line is selected, the reservation corresponding to the index if some row is selected
        """
        if self.reservationTable.currentRow() != -1:
            for res in self.__reservations:
                if res is not None:
                    return self.__reservations[self.reservationTable.currentRow()]
                else:
                    return None


class Dialog(QDialog):
    def __init__(self, text):
        """
        init method of class Dialog
        :param text: text to set in the Dialog panel
        """
        super(Dialog, self).__init__()
        loadUi("../designer/Pop-Up/Dialog.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.text.setText(text)


class ErrorMessage(QDialog):
    """
    init method of the class ErrorMessage
    """
    def __init__(self, text, buttons=QDialogButtonBox.Ok):
        super(ErrorMessage, self).__init__()
        loadUi("../designer/Pop-up/ErrorMessage.ui", self)
        self.setModal(True)
        self.setWindowTitle("Errore")
        self.buttonBox.setStandardButtons(buttons)
        self.text.setText(text)
        self.buttonBox.accepted.connect(super(ErrorMessage, self).accept)
        self.buttonBox.rejected.connect(super(ErrorMessage, self).reject)