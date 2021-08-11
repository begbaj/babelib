from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QAction, QWidget
from PyQt5.uic import loadUi
from src.Database.DatabaseManager import DatabaseManager
from src.homeView import HomeView


class LoginView(QMainWindow):
    db = DatabaseManager()

    def __init__(self, widget):
        super(LoginView, self).__init__()
        loadUi("../designer/Login view/login.ui",self)
        self.setUp()
        self.widget = widget

    def setUp(self):
        self.LoginButton.clicked.connect(self.loginfunction)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setFixedSize(660, 680)

    def passwcompare(self, password, result):
        try:
            if password == result.password:
                self.error_label.setText("")
            else:
                self.error_label.setText("Username o Password Sbagliati")
        except:
            self.error_label.setText("")
            self.error_label.setText("wa")

    def loginfunction(self):
        username = self.UsernameField.text()
        password = self.PasswordField.text()
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Inserisci tutti i campi")
        else:
            result = self.db.loginQuery(username)
            self.passwcompare(password, result)
            self.goHomeView()

    def goHomeView(self):
        homeView = HomeView(self.widget)
        self.widget.addWidget(homeView)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
