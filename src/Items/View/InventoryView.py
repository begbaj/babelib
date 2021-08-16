from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableView, QDialog
from PyQt5.uic import loadUi
from datetime import datetime
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.View.CatalogingView import CatalogingView


class InventoryView(QMainWindow):
    itmManager = ItemManager()
    __items = []

    # TODO: modifica documento, aggiungi documento, popup per scarta documento
    def __init__(self, widget):
        super(InventoryView, self).__init__()
        loadUi("../designer/Inventory view/InventoryView.ui", self)
        self.widget = widget

        try:
            self.searchButton.clicked.connect(lambda: self.get_items())
            self.addButton.clicked.connect(lambda: self.__go_to_cataloging_view(0))
            self.modifyButton.clicked.connect(lambda: self.__go_to_cataloging_view(1))
            self.discardButton.clicked.connect(lambda: self.discard_item())
            self.itemTable.setSelectionBehavior(QTableView.SelectRows)
            self.returnButton.clicked.connect(lambda: self.__go_back_button())
            self.showItemButton.clicked.connect(lambda: self.go_to_show_item())
        except Exception as err:
            print(err)

        self.itemTable.clearSelection()
        self.__remove_rows()

    def get_items(self):
        self.__items = []
        self.__items = self.itmManager.get_items(self.searchField.text(), self.searchMode.currentIndex(),
                                                 self.quarantineCheckBox.isChecked(),
                                                 self.discardedCheckBox.isChecked())
        self.__remove_rows()
        for item in self.__items:
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

    def discard_item(self):
        if not self.__get_selected_item().discarded:
            self.itmManager.discard_item(self.__get_selected_item())

    def show_item(self):
        pass

    def __go_back_button(self):
        # TODO: fare in modo che ritorni indietro
        self.close()

    def __get_selected_item(self):
        if self.itemTable.currentRow() != -1:
            return self.__items[self.itemTable.currentRow()]

    def __remove_rows(self):
        """
        Remove all rows from table
        :return:
        """
        for i in reversed(range(0, self.itemTable.rowCount())):
            self.itemTable.removeRow(i)

    def __go_to_cataloging_view(self, mode):
        if mode == 0:
            self.cataloging_view = CatalogingView(self.widget)
        elif mode == 1:
            self.cataloging_view = CatalogingView(self.widget, self.__get_selected_item())
        self.cataloging_view.show()


class DiscardModalDialog(QDialog):
    def __init__(self, item):
        super(DiscardModalDialog, self).__init__()
        loadUi("../designer/Pop-Up/DiscardPopUp.ui", self)
        self.setWindowTitle('Error')
        self.setModal(True)

