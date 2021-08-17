from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.uic import loadUi
from src.Users.View.UserCardView import UserCardView
from src.Users.controllers.UserManager import UserManager


class UserView(QMainWindow):

    userM = UserManager()

    def __init__(self, widget):
        super(UserView, self).__init__()
        loadUi("../designer/User view/UserView.ui", self)
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
        self.deleteButton.clicked.connect(self.delete)
        # Ricerca Dinamica
        self.nameField.textChanged.connect(lambda: self.search())
        self.surnameField.textChanged.connect(lambda: self.search())
        # Metodo per Settare lo stile
        self.style()

    def style(self):
        """
        Questo metodo setta lo stile della view
        :return:
        """
        self.schedaButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.userButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.backButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        # self.nameField.setStyleSheet(open("../designer/style/davtheme.qss", "r").read())
        # self.nameField.setStyleSheet('background-color: orange')

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
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(user.city))
            row = row + 1

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

    def delete(self):
        rowtable = self.userTable.currentRow()
        if rowtable == -1:
            self.show_popup()
        else:
            self.pop = DeletePopup(self.delete_user)
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
        self.userM.delete(self.users[row].id)
        self.users.remove(self.users[row])
        self.userTable.removeRow(row)

    def show_popup(self):
        self.pop = Popup()
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


# Region 'Pop-Up'

class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("../designer/Pop-Up/Message Pop-Up/Popup.ui", self)
        self.setWindowTitle('Errore')
        self.setModal(True)
        self.okButton.clicked.connect(self.close)


class DeletePopup(QDialog):

    def __init__(self, funct):
        super(DeletePopup, self).__init__()
        loadUi("../designer/Pop-Up/Delete Pop-Up/deletepopup.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.funct = funct
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.close)

    def confirm(self):
        self.funct()
        self.close()

    # endregion
