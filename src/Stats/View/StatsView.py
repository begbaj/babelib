from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QTableWidget
from src.Stats.Controllers.StatsManager import StatsManager
from PyQt5.uic import loadUi
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from src.Users.controllers.UserManager import UserManager
from src.Users.models.User import User


class StatsView(QMainWindow):
    userM = UserManager()
    __users = []

    def __init__(self, widget):
        super(StatsView, self).__init__()
        self.statsM = StatsManager()
        loadUi("../designer/Stats/Stats.ui", self)
        self.widget = widget
        self.load_user_fields()
        self.loan_stats()
        self.user = User()
        self.users = self.userM.list()
        self.load_data()
        self.pop = ''
        self.nameField.textChanged.connect(self.search)
        self.surnameField.textChanged.connect(self.search)
        self.userTable.itemDoubleClicked.connect(self.load_user_fields)
        self.go_back_button.clicked.connect(lambda: self.close())

    def load_user_fields(self):
        user_count = self.statsM.get_user_count()
        self.n_users.setText(str(user_count))

        self.male.setText(str(round((self.statsM.get_user_count_gender('Maschio(M)') / user_count) * 100, 2)) + '%')
        self.female.setText(str(round((self.statsM.get_user_count_gender('Femmina(F)') / user_count) * 100, 2)) + '%')

        self.zero_seventeen.setText(str(round(
            (self.statsM.get_user_by_bdate(date.today(), date.today() - relativedelta(years=17)) / user_count) * 100,
            2)) + '%')
        self.eighteentfive.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=18),
                                                                            date.today() - relativedelta(
                                                                                years=25)) / user_count) * 100,
                                             2)) + '%')
        self.tsixfifty.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=26),
                                                                        date.today() - relativedelta(
                                                                            years=50)) / user_count) * 100, 2)) + '%')
        self.foneplus.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=50),
                                                                       date.today() - relativedelta(
                                                                           years=200)) / user_count) * 100, 2)) + '%')
        if self.__get_selected_user() is not None:
            [n_mov, rit, perc, average, biggest_delay] = self.generate_reliability_stats()
            self.name_label.setText(self.__get_selected_user().name)
            self.surname_label.setText(self.__get_selected_user().surname)
            self.cf_label.setText(self.__get_selected_user().fiscal_code)
            self.item_borrowed.setText(str(n_mov))
            self.item_late.setText(str(rit))
            self.rating_label.setText(perc)
            self.item_most_late.setText(str(biggest_delay))
            self.average_return_time.setText(str(average))

    def loan_stats(self):
        top_items = self.statsM.get_top_3()
        top_genres = self.statsM.get_top_3_genres()

        self.first_most_loaned.setText(top_items[0].title + " con " + str(top_items[0].count) + " prestiti.")
        self.second_most_loaned.setText(top_items[1].title + " con " + str(top_items[1].count) + " prestiti.")
        self.third_most_loaned.setText(top_items[2].title + " con " + str(top_items[2].count) + " prestiti.")

        self.first_genre.setText(top_genres[0].description + " con " + str(top_genres[0].count) + " prestiti.")
        self.second_genre.setText(top_genres[1].description + " con " + str(top_genres[1].count) + " prestiti.")
        self.third_genre.setText(top_genres[2].description + " con " + str(top_genres[2].count) + " prestiti.")

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
        self.userTable.setEditTriggers(QTableWidget.NoEditTriggers)

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

    def __get_selected_user(self):
        """
        This method allows to get a user from __users list
        :return: None if there is no user selected, a user if a row in the user table is selected
        """
        if self.userTable.currentRow() != -1:
            return self.__users[self.userTable.currentRow()]
        else:
            return None

    def generate_reliability_stats(self):
        if self.__get_selected_user() is not None:
            rit = 0
            n_mov = 0
            delta = []
            for mov in self.statsM.find_dalay(self.__get_selected_user().id):
                delta.append(mov.return_date-mov.loan_date)
                if mov.return_date-mov.loan_date < timedelta(days=30):
                    rit = rit+1
                n_mov = n_mov + 1
            if n_mov != 0:
                perc = str(100- (rit/n_mov * 100)) + ' %'
                average = sum(delta, timedelta(0)) / len(delta)
                biggest_delay = max(delta)
                return n_mov, rit, perc, average, biggest_delay
            else:
                return 0, 0, '100 %', 0, 0
