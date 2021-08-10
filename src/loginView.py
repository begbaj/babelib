import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from homeView import HomeView


class LoginView(QMainWindow):

    def __init__(self):
        super(LoginView, self).__init__()
        loadUi("../designer/Login view/login.ui",self)
        self.setUp()

    def setUp(self):
        self.LoginButton.clicked.connect(self.loginfunction)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setFixedSize(660, 680)

    def passwcompare(self, password, result):
        try:
            if password == result.password:
                self.error_label.setText("")
                self.goHomeView()
            else:
                self.error_label.setText("Username o Password Sbagliati")
        except:
            self.error_label.setText("")
            self.error_label.setText("Username o Password Sbagliati")


    def loginfunction(self):
        username = self.UsernameField.text()
        password = self.PasswordField.text()

        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Inserisci tutti i campi")
        else:
            conn = mariadb.connect(
                user="root",
                password="2810",
                host="127.0.0.1",
                port=3306,
                database="babelib_db"
            )
            cur = conn.cursor(named_tuple=True)
            conn.autocommit = True
            cur.execute(f"SELECT password FROM administrator WHERE username = '{username}'")
            result = cur.fetchone()
            self.passwcompare(password,result)

    def goHomeView(self):
        self.cams = HomeView()
        self.cams.show()
        self.close()