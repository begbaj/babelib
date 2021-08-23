from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from src.Users.controllers.UserManager import UserManager
from src.Users.models.User import User
from src.Services.controllers.ServiceReservationManager import ServiceReservationManager
from src.Services.models.SignedServiceReservation import SignedServiceReservation
from src.Services.models.UnsignedServiceReservation import UnsignedServiceReservation


class NewReservationView(QMainWindow):
    userM = UserManager()
    serviceM = ServiceReservationManager()
    s_s_r = SignedServiceReservation()
    u_s_r = UnsignedServiceReservation()
    user = -1

    def __init__(self, widget):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        self.__users = []
        super(NewReservationView, self).__init__()
        loadUi("../designer/Reservation/AddReservationView.ui", self)
        self.widget = widget
        self.user = User()
        self.users = self.userM.list()
        self.load_data()
        self.nameField.textChanged.connect(lambda: self.search())
        self.surnameField.textChanged.connect(lambda: self.search())
        self.get_field.clicked.connect(lambda: self.get_fields())
        self.clear_field.clicked.connect(lambda: self.clear_fields())
        self.save_button.clicked.connect(lambda: self.set_fields())

    def load_table(self, users):
        """
        Questo metodo permette di rimpire la QTableWidget presente nella view con una lista di utenti
        :param users:
        :return: None
        """
        row = 0
        self.__users = []
        self.userTable.setRowCount(len(users))
        for user in self.users:
            self.userTable.setItem(row, 0, QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QTableWidgetItem(user.fiscal_code))
            row = row + 1
            self.__users.append(user)

    def load_data(self):
        self.users = self.userM.list()
        self.load_table(self.users)

    # Region 'User Operation'

    def search(self):
        """
        Questo metodo consente la ricerca degli utenti all'interno del sistema
        :return:
        """
        # Reload all the Users
        if (self.nameField.text() == '') and (self.surnameField.text() == ''):
            self.load_data()
        # Search User by name
        elif (self.nameField.text() != '') and (self.surnameField.text() == ''):
            self.load_data_research(self.userM.findName(self.nameField.text()))
        # Search User by surname
        elif (self.nameField.text() == '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findSurname(self.surnameField.text()))
        # Search User by both
        elif (self.nameField.text() != '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findNameSurname(self.nameField.text(), self.surnameField.text()))

    # endregion

    def load_data_research(self, users):
        """
        Questo metodo riempe la tabella con quegli utenti che sono il risultato della ricerca
        :param users:
        :return: None
        """
        self.users = users
        self.load_table(self.users)

    def delete_user(self):
        """
        Questo metodo permette di rimuovere l'utente selezionato dal sistema
        :return: None
        """
        row = self.userTable.currentRow()
        self.userM.delete(self.users[row].id)
        self.users.remove(self.users[row])
        self.userTable.removeRow(row)

    def get_fields(self):
        if self.__get_selected_user() is not None:
            self.name.setText(self.__get_selected_user().name)
            self.surname.setText(self.__get_selected_user().surname)
            self.telephone.setText(self.__get_selected_user().telephone)
            self.name.setReadOnly(True)
            self.surname.setReadOnly(True)
            self.telephone.setReadOnly(True)

        # else popup

    def clear_fields(self):
        self.name.setReadOnly(False)
        self.surname.setReadOnly(False)
        self.telephone.setReadOnly(False)
        self.name.setText('')
        self.surname.setText('')
        self.telephone.setText('')

    def __get_selected_user(self):
        if self.userTable.currentRow() != -1:
            return self.__users[self.userTable.currentRow()]
        else:
            return None

    def set_fields(self):
        if self.__get_selected_user() is not None:
            self.serviceM.add_signed_reservation(self.__get_selected_user().id,
                                                 self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                 self.timeEdit.dateTime().toString("hh:mm:ss"),
                                                 self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                 self.timeEdit_2.dateTime().toString("hh:mm:ss"))
        else:
            self.serviceM.add_unsigned_reservation(self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                   self.timeEdit.dateTime().toString("hh:mm:ss"),
                                                   self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                   self.timeEdit_2.dateTime().toString("hh:mm:ss"), self.telephone.text(), self.name.text()+' '+self.surname.text())
        self.close()


