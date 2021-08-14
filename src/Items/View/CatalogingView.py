from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class CatalogingView(QMainWindow):

    def __init__(self, widget, item=None):
        super(CatalogingView, self).__init__()
        loadUi("../designer/Cataloging View/CatalogingView.ui", self)
        self.widget = widget
