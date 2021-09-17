from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget
from PyQt5.uic import loadUi
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager
from src.Utils.UI import Popup, DeletePopup, EnableDisableUserPopup


class UserView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget):
        super(UserView, self).__init__()
        loadUi("../designer/Users/UserView.ui", self)
        self.users = self.userM.list()
        self.widget = widget
        self.pop = ''
        self.load_data()
        self.setup()

    def setup(self):
        # Funzionalità dei Bottoni
        self.userButton.clicked.connect(self.__go_new_user)
        self.backButton.clicked.connect(self.close)
        self.schedaButton.clicked.connect(self.__go_user_card)
        self.disableButton.clicked.connect(self.enable_disable)
        self.enableButton.clicked.connect(self.enable_disable)
        self.deleteButton.clicked.connect(self.delete)

        self.disableButton.setVisible(True)
        self.enableButton.setVisible(False)
        #enableButton
        # Ricerca Dinamica
        self.nameField.textChanged.connect(lambda: self.search())
        self.surnameField.textChanged.connect(lambda: self.search())
        self.style()
        #checkbox
        self.checkBoxUserDisabled.stateChanged.connect(lambda: self.search())

    def style(self):
        self.schedaButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        """
        Questo metodo setta lo stile della view
        :return:
        """
        self.userButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.backButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.userTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())
        self.nameField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        self.surnameField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())

    def load_table(self, users):
        """
        Questo metodo permette di rimpire la QTableWidget presente nella view con una lista di utenti
        :param users:
        :return: None
        """
        row = 0
        self.userTable.setRowCount(len(users))
        for user in self.users:
            self.userTable.setItem(row, 0, QtWidgets.QTableWidgetItem(user.name))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(user.surname))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.fiscal_code))
            self.userTable.setItem(row, 3, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1
        self.userTable.setEditTriggers(QTableWidget.NoEditTriggers)


    def load_data(self, users=None):
        if users is None:
            self.users = self.userM.list(self.checkBoxUserDisabled.isChecked())
            self.load_table(self.users)
        else:
            self.load_table(users)

    # Region 'User Operation'

    def search(self):

        self.disableButton.setVisible(not self.checkBoxUserDisabled.isChecked())
        self.enableButton.setVisible(self.checkBoxUserDisabled.isChecked())

        if (self.nameField.text() == '') and (self.surnameField.text() == ''):
            self.load_data()
        # Search User by name
        elif (self.nameField.text() != '') and (self.surnameField.text() == ''):
            self.load_data_research(self.userM.findName(self.nameField.text(), self.checkBoxUserDisabled.isChecked()))
        # Search User by surname
        elif (self.nameField.text() == '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findSurname(self.surnameField.text(), self.checkBoxUserDisabled.isChecked()))
        # Search User by both
        elif (self.nameField.text() != '') and (self.surnameField.text() != ''):
            self.load_data_research(self.userM.findNameSurname(self.nameField.text(), self.surnameField.text(), self.checkBoxUserDisabled.isChecked()))

    def delete(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            self.pop = DeletePopup(self.delete_user)
            self.pop.show()

    def enable_disable(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:

            if self.checkBoxUserDisabled.isChecked():
                text = 'Sicuro di voler abilitare l" utente?'
            else:
                text = 'Sicuro di voler disabilitare l" utente?'

            self.pop = EnableDisableUserPopup(self.enable_disable_user, text)
            self.pop.show()

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

        if self.userM.count_movement_with_the_same_user_id(self.users[row].id) == 0:
            self.userM.delete(self.users[row].id)
            self.users.remove(self.users[row])
            self.userTable.removeRow(row)
        else:
            self.pop = Popup("Utente già presente in almeno 1 movimento.")
            self.pop.show()

    def enable_disable_user(self):
        """
        Questo metodo permette di disabilitare l'utente selezionato dal sistema
        :return: None
        """
        row = self.userTable.currentRow()
        #self.userM.delete(self.users[row].id)
        self.users[row].disabled = not self.checkBoxUserDisabled.isChecked()
        self.userM.set(self.users[row])
        self.users.remove(self.users[row])
        self.userTable.removeRow(row)


    def show_popup(self):
        self.pop = Popup("Selezionare un utente")
        self.pop.show()

    # Region 'View Links'

    def __go_new_user(self):
        """
        Questo metodo consente di andare nella view che permette di creare un nuovo utente
        :return: None
        """
        user = None
        self.view = UserCardView(self.widget, user, self.load_data)
        self.view.show()

    def __go_user_card(self):
        """
        Questo metodo consente di andare nella view che permette di visualizzare le informazioni
        dell'utente selezionato a schermo
        :return: None
        """
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            user = self.users[rowtable]
            self.view = UserCardView(self.widget, user, self.load_data)
            self.view.show()

    # endregion
