from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class NewReservationView(QMainWindow):

    def __init__(self, widget):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        super(NewReservationView, self).__init__()
        loadUi("../designer/Reservation/AddReservationView.ui", self)
        self.widget = widget
        #self.return_button.connect.clicked(self.close())
