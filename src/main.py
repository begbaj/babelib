from PyQt5.QtCore import QSettings



if __name__ == "__main__":
    #setting up processes
    configman = QSettings("bcdd", "babelib")
    if configman.value("init") is None:
        print("insert Databse user:", end="")
        db_user = input()
        configman.setValue("db_user", db_user)

        print("insert Databse password:",end="")
        db_password = input()
        configman.setValue("db_password", db_password)

        print("insert Databse host:",end="")
        db_host = input()
        configman.setValue("db_host", db_host)

        print("insert Databse port:",end="")
        db_port = input()
        configman.setValue("db_port", db_port)

        print("insert Databse Databse:",end="")
        db_database = input()
        configman.setValue("db_database", db_database)

        configman.setValue("init", "true")