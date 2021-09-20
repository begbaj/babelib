from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QAction, QWidget
from PyQt5.uic import loadUi
from src.Database.DatabaseManager import DatabaseManager
from src.homeView import HomeView


class LoginView(QMainWindow):
    __db = DatabaseManager()
    # def __init__(self):
    #     super(LoginView, self).__init__()
    #     loadUi("../designer/Login view/login.ui",self)
    #
    #     self.loginButton.clicked.connect(self.loginfunction)
    #     self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)

    def __init__(self, widget):
        super(LoginView, self).__init__()
        loadUi("../designer/Login View/login.ui", self)

        self.loginButton.clicked.connect(self.login)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.widget = widget

    def pass_compare(self, password, result):
        try:
            if password == result.password:
                self.errorLabel.setText("")
                self.__go_home_view()
            else:
                self.errorLabel.setText("Username o Password Sbagliati")
        except Exception as err:
            self.errorLabel.setText("Username o Password Sbagliati")

    def login(self):
        username = self.usernameField.text()
        password = self.passwordField.text()
        if len(username) == 0 or len(password) == 0:
            self.errorLabel.setText("Inserisci tutti i campi")
        else:
            result = self.__db.login(username, password)
            self.pass_compare(password, result)


    def __go_home_view(self):
        home_view = HomeView(self.widget)
        self.widget.addWidget(home_view)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

