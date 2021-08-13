from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QAction, QWidget
from PyQt5.uic import loadUi
from src.Database.DatabaseManager import DatabaseManager
from src.homeView import HomeView


class LoginView(QMainWindow):
    __db = None
    # def __init__(self):
    #     super(LoginView, self).__init__()
    #     loadUi("../designer/Login view/login.ui",self)
    #
    #     self.LoginButton.clicked.connect(self.loginfunction)
    #     self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)

    def __init__(self, widget):
        super(LoginView, self).__init__()
        __db = DatabaseManager()

        loadUi("../designer/Login view/login.ui", self)

        self.LoginButton.clicked.connect(self.login)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.widget = widget

    def pass_compare(self, password, result):
        try:
            if password == result.password:
                self.error_label.setText("")
            else:
                self.error_label.setText("Username o Password Sbagliati")
        except Exception as err:
            self.error_label.setText(err)

    def login(self):
        username = self.UsernameField.text()
        password = self.PasswordField.text()
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Inserisci tutti i campi")
        else:
            result = self.__db.login(username)
            self.pass_compare(password, result)
            self.__go_home_view()

    def __go_home_view(self):
        home_view = HomeView(self.widget)
        self.widget.addWidget(home_view)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
