import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from loginView import LoginView
from homeView import HomeView
from src.Users.View.UserView import UserView
from src.Items.View.InventoryView import InventoryView
from src.Services.views.ReservationView import ReservationView
from src.Movements.View.MovementsView import MovementsView

# TODO: un view manager per scorrere le varie view senza che rimangano aperte
# TODO: refactoring delle view (sistemare le icone in un unico punto, mettere i nomi delle form con un formato standard...)
# TODO: sistemare .gitignore per tutti
# TODO: sistemare connessione al database (creare database centralizzato oppure inserire db.json nel gitignore e spostarla in una directory standardizzata)
# TODO: refactoring del codice (nomi metodi e attributi standardizzati al PEP) e TUTTO IN INGLESE
# TODO: usare qss e qrc per i temi e le icone
# TODO: refactoring del database (molti campi non contengono il tipo giusto e alcuni sono anche scritti male)
# TODO: inserire asterischi nei campi obbligatori e sengalare utente nel caso di mancata compilazione
# TODO: DOCUMENTAZIONE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(LoginView(widget)) #0
    widget.addWidget(HomeView(widget)) #1
    widget.addWidget(UserView(widget)) #2
    widget.addWidget(MovementsView(widget)) #3
    widget.addWidget(InventoryView(widget)) #4
    #widget.addWidget(ReservationView(widget)) #5
    widget.showFullScreen()
    app.exec()  # Lancia l'applicazione
