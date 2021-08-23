from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5.uic import loadUi
from src.Users.controllers.UserManager import UserManager
from src.Users.models.User import User
from src.Services.controllers.ServiceReservationManager import ServiceReservationManager
from src.Services.models.SignedServiceReservation import SignedServiceReservation
from src.Services.models.UnsignedServiceReservation import UnsignedServiceReservation
from PyQt5.QtCore import QDate, QDateTime

from datetime import date


class NewReservationView(QMainWindow):
    userM = UserManager()
    serviceM = ServiceReservationManager()
    s_s_r = SignedServiceReservation()
    u_s_r = UnsignedServiceReservation()
    __users = []

    def __init__(self, widget):
        """
        init method
        :param widget: widget to open view
        """
        super(NewReservationView, self).__init__()
        loadUi("../designer/Reservation/AddReservationView.ui", self)
        self.widget = widget
        self.user = User()
        self.users = self.userM.list()
        self.load_data()
        self.pop = ''
        self.nameField.textChanged.connect(lambda: self.search())
        self.surnameField.textChanged.connect(lambda: self.search())
        self.get_field.clicked.connect(lambda: self.get_fields())
        self.clear_field.clicked.connect(lambda: self.clear_fields())
        self.save_button.clicked.connect(lambda: self.set_fields())
        self.telephone.setValidator(QIntValidator())
        self.name.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z]*$')))
        self.surname.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z]*$')))


    def load_table(self, users):
        """
        this method allows to fill the user table
        :param users: list of reservations
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
        """
        this method fill the user table with the data from the user list
        :return: None
        """
        self.users = self.userM.list()
        self.load_table(self.users)

    # Region 'User Operation'

    def search(self):
        """
        This method allows to search for users
        :return: None
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
        This method fills the userTable with the searched users
        :param users: list of users
        :return: None
        """
        self.users = users
        self.load_table(self.users)

    def delete_user(self):
        """
        This method allows to remove the user selected by the program
        :return: None
        """
        row = self.userTable.currentRow()
        self.userM.delete(self.users[row].id)
        self.users.remove(self.users[row])
        self.userTable.removeRow(row)

    def get_fields(self):
        """
        this method sets the name, the surname and the telephone from the selected user in the user list
        :return: None
        """
        if self.__get_selected_user() is not None:
            self.name.setText(self.__get_selected_user().name)
            self.surname.setText(self.__get_selected_user().surname)
            self.telephone.setText(self.__get_selected_user().telephone)
            self.name.setReadOnly(True)
            self.surname.setReadOnly(True)
            self.telephone.setReadOnly(True)
        else:
            self.pop = Popup()
            self.pop.label.setText("Selezionare un utente.")
            self.pop.show()


    def clear_fields(self):
        '''
        this method allows to clear the name,surname and telephone fields
        :return: None
        '''
        self.name.setReadOnly(False)
        self.surname.setReadOnly(False)
        self.telephone.setReadOnly(False)
        self.name.setText('')
        self.surname.setText('')
        self.telephone.setText('')

    def __get_selected_user(self):
        """
        This method allows to get a user from __users list
        :return: None if there is no user selected, a user if a row in the user table is selected
        """
        if self.userTable.currentRow() != -1:
            return self.__users[self.userTable.currentRow()]
        else:
            return None

    def set_fields(self):
        """
        this method gets the name, surname, telephone, date and time of the reservation and makes a query to add the fields to database
        :return: None
        """
        if self.__get_selected_user() is not None:
            self.serviceM.add_signed_reservation(self.__get_selected_user().id,
                                                 self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                 self.timeEdit.dateTime().toString("hh:mm:ss"),
                                                 self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                 self.timeEdit_2.dateTime().toString("hh:mm:ss"))
            self.close()
        else:
            if self.telephone.text() == '' or self.name.text() == '' or self.surname.text() == '':
                self.pop = Popup()
                self.pop.label.setText("Inserire tutti i campi obbligatori.")
                self.pop.show()
            # elif self.dateEdit.currentDate().toPyDate() < date.today():
            #     self.pop = Popup()
            #     self.pop.label.setText("Data non valida.")
            #     self.pop.show()
            else:
                self.serviceM.add_unsigned_reservation(self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                       self.timeEdit.dateTime().toString("hh:mm:ss"),
                                                       self.dateEdit.dateTime().toString("yyyy-MM-dd") + ' ' +
                                                       self.timeEdit_2.dateTime().toString("hh:mm:ss"),
                                                       self.telephone.text(),
                                                       self.name.text() + ' ' + self.surname.text())
                self.close()



class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/Pop-Up/Message Pop-Up/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)
        self.okButton.clicked.connect(self.close)


