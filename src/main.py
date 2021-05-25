import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QSettings
from HomeView import *
from LoginView import *

configman = QSettings("bcdd", "babelib")

def setup_configuration():
    print("insert Databse user:", end="")
    db_user = input()
    configman.setValue("db_user", db_user)

    print("insert Databse password:", end="")
    db_password = input()
    configman.setValue("db_password", db_password)

    print("insert Databse host:", end="")
    db_host = input()
    configman.setValue("db_host", db_host)

    print("insert Databse port:", end="")
    db_port = input()
    configman.setValue("db_port", db_port)

    print("insert Databse Databse:", end="")
    db_database = input()
    configman.setValue("db_database", db_database)

    configman.setValue("init", "true")

def login_button():
    login.close()
    home.show()

if __name__ == "__main__":
    configman.setValue("init", None)
    #setting up processes
    app = QtWidgets.QApplication(sys.argv)

    login = QtWidgets.QMainWindow()
    login_ui = Ui_LoginView()
    login_ui.setupUi(login)
    login_ui.db_name_txt.setText(configman.value("db_database"))
    login_ui.db_username_txt.setText(configman.value("db_user"))
    login_ui.db_password_txt.setText(configman.value("db_password"))
    login_ui.db_host_txt.setText(configman.value("db_host"))
    login_ui.db_port_txt.setText(configman.value("db_port"))
    login_ui.login_button.clicked.connect(login_button)

    home = QtWidgets.QMainWindow()
    home_ui = Ui_Home()
    home_ui.setupUi(home)

    if configman.value("save_db_config"):
        login_ui.save_db_config_cb.setCheckState(2)
        login_ui.save_db_config_cb_changed(True)

    login.show()
    sys.exit(app.exec_())

