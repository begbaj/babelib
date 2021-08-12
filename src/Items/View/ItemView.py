from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets, QtCore
import datetime

from src.Items.Controllers.ItemManager import ItemManager


class ItemView(QMainWindow):

    itmManager = ItemManager()

    def __init__(self, widget):
        super(ItemView, self).__init__()
        loadUi("../designer/Inventory view/InventoryView.ui", self)
        self.widget = widget
        self.searchButton.clicked.connect(lambda: self.getItems())

    def getItems(self):
        row = 0
        items = self.itmManager.get_items(self.searchField.text,self.searchMode.currentIndex,
                                          self.quarantineCheckBox.isChecked(),self.discardedCheckBox.isChecked)
        self.itemTable.setRowCount(len(items))
        for item in items:
            self.itemTable.setItem(row, 0, QtWidgets.QTableWidgetItem(item.title))
            self.userTable.setItem(row, 1, QtWidgets.QTableWidgetItem(item.author))
            self.userTable.setItem(row, 2, QtWidgets.QTableWidgetItem(item.isbn))
            self.userTable.setItem(row, 3, QtWidgets.QTableWidgetItem(item.bid))
            self.userTable.setItem(row, 4, QtWidgets.QTableWidgetItem(item.inventory_num))
            self.userTable.setItem(row, 5, QtWidgets.QTableWidgetItem(item.external_state))
            if item.quarantine_end_date >= datetime.datetime():
                self.userTable.setItem(row, 6, QtWidgets.QTableWidgetItem('Si'))
            else:
                self.userTable.setItem(row, 6, QtWidgets.QTableWidgetItem('No'))
            self.userTable.setItem(row, 6, QtWidgets.QTableWidgetItem(item.note))
            row = row + 1
        pass

    def goBack(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def addItem(self):
        pass

    def deleteButton(self):
        pass


