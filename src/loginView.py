import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from homeView import HomeView


class LoginView(QMainWindow):
    def __init__(self):
        super(LoginView, self).__init__()
        loadUi("../designer/Login view/login.ui",self) #importa il designer
        self.LoginButton.clicked.connect(self.loginfunction) #quando il bottone viene cliccato chiama la funzione submitfunction
        self.PassworField.setEchoMode(QtWidgets.QLineEdit.Password) #fa comparire gli asterischi quando si mette la password

    def submitfunction(self):
        username = self.UsernameField.text()
        password = self.PasswordField.text()
        print("Accesso eseguito correttamente come: ", username)

    def loginfunction(self):
        username = self.UsernameField.text()
        password = self.PasswordField.text()

        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Inserisci tutti i campi")
        else:
            conn = mariadb.connect(
                user="root",
                password="sa",
                host="127.0.0.1",
                port=3306,
                database="babelib_db"
            )
            cur = conn.cursor(named_tuple=True)
            conn.autocommit = True
            cur.execute(f"SELECT password FROM administrator WHERE username = '{username}'")
            result = cur.fetchone()
            print(result)

            if password == result.password:
                print('Accesso eseguito correttamente')
                self.goHomeView()
                self.error_label.setText("")
            else:
                self.error_label.setText("Username o Password errati")

    def goHomeView(self):
        self.cams = HomeView()
        self.cams.show()
        self.close()