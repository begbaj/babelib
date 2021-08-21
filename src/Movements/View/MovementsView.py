from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from src.Movements.View.LoanView import LoanView


class MovementsView(QMainWindow):

    def __init__(self, widget):
        super(MovementsView, self).__init__()
        loadUi("../designer/Movements/MovementView.ui", self)
        self.widget = widget
        self.setup()

    def setup(self):
        self.style()
        self.loanButton.clicked.connect(lambda: self.new_loan())
        self.consultationButton.clicked.connect(lambda: self.new_consultation())
        self.infoButton.clicked.connect(lambda: self.movement_info())
        self.backButton.clicked.connect(lambda: self.close())
        self.searchField.textChanged.connect(lambda: self.search())

    def style(self):
        # Button Style
        self.loanButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.consultationButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        self.infoButton.setStyleSheet(open("../designer/style/ButtonTheme.txt", "r").read())
        # Line Edit Style
        self.searchField.setStyleSheet(open("../designer/style/TextBoxTheme.txt", "r").read())
        # Table Style
        self.movementTable.setStyleSheet(open("../designer/style/TableTheme.txt", "r").read())

    def new_consultation(self):
        pass

    def new_loan(self):
        self.loanview = LoanView(self.widget)
        self.loanview.show()

    def movement_info(self):
        pass

    def load_table(self):
        pass

    def search(self):
        pass
