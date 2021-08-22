from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QDialogButtonBox
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
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        self.widget = widget
        super(ReservationView, self).__init__()
        loadUi("../designer/Reservation/ReservationView.ui", self)
        self.return_button.clicked.connect(lambda: self.close())
        self.add_reservation.clicked.connect(lambda: self.go_new_reservation())
        self.delete_reservation.clicked.connect(lambda: self.discard_res())
        self.searchField.textChanged.connect(lambda: self.search())
        self.search()

    def go_new_reservation(self):
        self.new_res = NewReservationView(self.widget)
        self.new_res.show()

    def __update_table(self):
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
                self.reservationTable.setItem(row, 2, QTableWidgetItem(res.date_from.strftime("%m/%d/%Y")))
                self.reservationTable.setItem(row, 3, QTableWidgetItem(
                    res.date_from.strftime("%H:%M:%S") + " - " + res.date_to.strftime("%H:%M:%S")))
                self.reservationTable.setItem(row, 1, QTableWidgetItem(res.cellphone))
                row = row + 1
        if self.__unsigned is not None and self.__signed is not None:
            self.__reservations = self.__signed + self.__unsigned

    # def __get_u_s(self):
    #     self.__unsigned_reservations =


    def fill_list(self):
        pass
        # for i in self.resM.get_all_signed():
        #     self.new_signed.reservation_id = i.id
        #     self.new_signed.date_from = i.date_from.strftime("%m/%d/%Y" "%H:%M:%S")
        #     self.new_signed.date_to = i.date_to.strftime("%H:%M:%S")
        #     self.new_signed.name = self.userM.get_user_name(i.user_id)[0].name
        #     self.new_signed.surname = self.userM.get_user_surname(i.user_id)[0].surname
        #     self.new_signed.cellphone = self.userM.find(i.user_id).first_cellphone
        #     self.__signed.append(self.new_signed)
        # if self.resM.get_unsigned_(self.searchField.text()) is not None and self.resM.get_all_signed(self.searchField.text()) is not None:

        #self.__reservations = self.__unsigned + self.__signed

    def search(self):
        self.__update_table()

    def discard_res(self):
        res = self.__get_selected_res()
        if res is None:
            ErrorMessage("Selezionare un elemento da scartare!").exec_()
            return

        discard = Dialog(f"Sei sicuro? Questa azione è irreversibile!")
        ok = discard.exec_()
        if ok:
            if res.n_fields == 6:
                self.resM.delete_signed(res.Id)
            else:
                self.resM.delete_unsigned(res.id)
        self.search()

    def __remove_rows(self):
        for i in reversed(range(0, self.reservationTable.rowCount())):
            self.reservationTable.removeRow(i)

    def __get_selected_res(self):
        if self.reservationTable.currentRow() != -1:
            for res in self.__reservations:
                if res.n_fields == 5:
                    return self.__unsigned[self.reservationTable.currentRow()]
                if res.n_fields == 6:
                    return self.__signed[self.reservationTable.currentRow()]
            else:
                return None


class Dialog(QDialog):
    def __init__(self, text):
        super(Dialog, self).__init__()
        loadUi("../designer/Pop-Up/Dialog.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.text.setText(text)


class ErrorMessage(QDialog):
    def __init__(self, text, buttons=QDialogButtonBox.Ok):
        super(ErrorMessage, self).__init__()
        loadUi("../designer/Pop-up/ErrorMessage.ui", self)
        self.setModal(True)
        self.setWindowTitle("Errore")
        self.buttonBox.setStandardButtons(buttons)
        self.text.setText(text)
        self.buttonBox.accepted.connect(super(ErrorMessage, self).accept)
        self.buttonBox.rejected.connect(super(ErrorMessage, self).reject)