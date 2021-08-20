from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.Services.views.NewReservationView import NewReservationView


class ReservationView(QMainWindow):

    def __init__(self, widget):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        self.widget = widget
        super(ReservationView, self).__init__()
        loadUi("../designer/Reservation/ReservationView.ui", self)
        self.return_button.clicked.connect(lambda: self.close())
        self.add_reservation.clicked.connect(lambda: self.go_new_reservation())

    def go_new_reservation(self):
        self.new_res = NewReservationView(self.widget)
        self.new_res.show()
