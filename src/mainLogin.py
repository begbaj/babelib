import mariadb
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("Login view/login.ui",self) #importa il designer
        self.LoginButton.clicked.connect(self.loginfunction) #quando il bottone viene cliccato chiama la funzione submitfunction
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) #fa comparire gli asterischi quando si mette la password

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
                password="5885",
                host="127.0.0.1",
                port=3306,
                database="babelib"
            )
            cur = conn.cursor(named_tuple=True)
            conn.autocommit = True
            cur.execute(f"SELECT password FROM administrator WHERE username = '{username}'")
            result = cur.fetchone()
            print(result)

            if password == result.password:
                print('Accesso eseguito correttamente')
                self.error_label.setText("")
            else:
                self.error_label.setText("Username o Password errati")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(600)
    widget.setFixedHeight(600)
    widget.show()
    app.exec_() #Lancia l'applicazione