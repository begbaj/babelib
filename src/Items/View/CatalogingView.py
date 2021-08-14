from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class CatalogingView(QMainWindow):

    __mode = -1

    def __init__(self, widget, item=None):
        super(CatalogingView, self).__init__()
        loadUi("../designer/Cataloging View/CatalogingView.ui", self)
        self.widget = widget
        if item is None:
            __mode = 0 #inserimento
        else:
            __mode = 1 #modifica/visualizzazione
            self.load_item(item)

    def load_item(self, item):
        self.title.setText(item.title)
        self.author.setText(item.author)
        #self.nature
        #self.type
        #self.genre
        self.publicationDate.setDate(item.publication_date)
        self.ISBN.setText(str(item.isbn))
        self.InventoryNum.setText(str(item.inventory_num))
        self.shelf.setText(str(item.shelf))
        self.rack.setText(str(item.rack))
        #self.position.setCurrentText(str(item.position))
        #TODO finire

