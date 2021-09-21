import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from loginView import LoginView

# TODO: un view manager per scorrere le varie view senza che rimangano aperte
# TODO: refactoring delle view (sistemare le icone in un unico punto, mettere i nomi delle form con un formato standard...)
# TODO: refactoring del codice (nomi metodi e attributi standardizzati al PEP) e TUTTO IN INGLESE
# TODO: DOCUMENTAZIONE
# TODO: cambiare path dei .txt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main_window = LoginView(widget)
    widget.addWidget(main_window)
    widget.show()
    app.exec()  # Lancia l'applicazione
