from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class ReservationView(QMainWindow):

    def __init__(self, widget, item):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        super(ReservationView, self).__init__()
        loadUi("../designer/Reservation/ReservationView.ui", self)
        #self.return_button.connect.clicked(self.close())
