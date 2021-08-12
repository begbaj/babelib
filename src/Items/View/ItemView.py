from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets, QtCore

from src.Items.Controllers.ItemManager import ItemManager


class ItemView(QMainWindow):

    itmManager = ItemManager()

    def __init__(self, widget):
        super(ItemView, self).__init__()
        loadUi("../designer/Inventory view/InventoryView.ui", self)
        self.widget = widget

    def getItems(self):
        pass

    def goBack(self):
        pass

    def addItem(self):
        pass

    def deleteButton(self):
        pass

