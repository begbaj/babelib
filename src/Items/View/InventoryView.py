from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets, QtCore
from datetime import datetime
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.View.CatalogingView import CatalogingView


class InventoryView(QMainWindow):
    itmManager = ItemManager()

    def __init__(self, widget):
        super(InventoryView, self).__init__()
        loadUi("../designer/Inventory view/InventoryView.ui", self)
        self.widget = widget
        try:
            self.searchButton.clicked.connect(lambda: self.get_items())
        except Exception as err:
            print(err)
        try:
            self.addButton.clicked.connect(lambda: self.__go_to_cataloging_view())
        except Exception as err:
            print(err)

    def get_items(self):
        row = 0
        items = self.itmManager.get_items(self.searchField.text(),self.searchMode.currentIndex(),
                                          self.quarantineCheckBox.isChecked(),self.discardedCheckBox.isChecked())
        self.__remove_rows()
        for item in items:
            row = self.itemTable.rowCount()
            self.itemTable.insertRow(row)
            self.itemTable.setItem(row, 0, QTableWidgetItem(item.title))
            self.itemTable.setItem(row, 1, QTableWidgetItem(item.author))
            self.itemTable.setItem(row, 2, QTableWidgetItem(item.isbn))
            self.itemTable.setItem(row, 3, QTableWidgetItem(item.bid))
            self.itemTable.setItem(row, 4, QTableWidgetItem(item.inventory_num))
            self.itemTable.setItem(row, 5, QTableWidgetItem(str(item.availability.value)))
            if item.quarantine_end_date is not None:
                if item.quarantine_end_date >= datetime.now():
                    self.itemTable.setItem(row, 6, QTableWidgetItem('Si'))
                else:
                    self.itemTable.setItem(row, 6, QTableWidgetItem('No'))
            else:
                self.itemTable.setItem(row, 6, QTableWidgetItem('No'))

            self.itemTable.setItem(row, 7, QTableWidgetItem(item.note))
            row = row + 1

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def add_item(self):
        pass

    def __remove_rows(self):
        """
        Remove all rows from table
        :return:
        """
        for i in reversed(range(0, self.itemTable.rowCount())):
            self.itemTable.removeRow(i)

    def __go_to_cataloging_view(self):
        self.catalogingview = CatalogingView(self.widget)
        self.catalogingview.show()

    def remove_button(self):
        pass

