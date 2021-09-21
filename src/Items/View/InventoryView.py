from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QMainWindow
from PyQt5.uic import loadUi

from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import AvailabilityEnum
from src.Items.View.CatalogingView import CatalogingView
from src.Items.View.ShowItemView import ShowItemView
from src.Utils.UI import *


class InventoryView(QMainWindow):
    itmManager = ItemManager()
    __items = []

    def __init__(self, widget, parent):
        super(InventoryView, self).__init__(parent)
        loadUi("../designer/Items/InventoryViewNew.ui", self)
        self.widget = widget
        self.show_item_view = ShowItemView(self.widget)
        self.cataloging_view = CatalogingView(self.widget, Item(), self.search)

        try:
            self.itemTable.setSelectionBehavior(QTableView.SelectRows)

            self.searchField.textChanged.connect(self.search)
            self.quarantineCheckBox.stateChanged.connect(self.search)
            self.discardedCheckBox.stateChanged.connect(self.search)

            self.addButton.clicked.connect(self.add_item)
            self.modifyButton.clicked.connect(self.edit_item)
            self.discardButton.clicked.connect(self.discard_item)
            self.returnButton.clicked.connect(self.__go_back)
            self.showItemButton.clicked.connect(self.show_item)

            self.searchMode.currentIndexChanged.connect(self.search)

            self.cataloging_view.go_back_button.connect(self.search)
            self.cataloging_view.save_button.connect(self.search)
            self.show_item_view.go_back_button.connect(self.search)
        except Exception as err:
            print(err)

        self.search()

    def search(self):
        self.__get_items()
        self.__update_table()

    def add_item(self):
        self.__go_to_cataloging_view(new=True)

    def discard_item(self):
        item = self.__get_selected_item()
        if item is None:
            ErrorMessage("Selezionare un elemento da scartare!").exec_()
            return

        discard = Dialog(f"Sei sicuro di voler scartare {item.title} di {item.author}?(Questa azione è irreversibile!)")
        ok = discard.exec_()
        if ok:
            if not self.__get_selected_item().availability == AvailabilityEnum.scartato:
                self.itmManager.discard_item(self.__get_selected_item())
        self.search()

    def show_item(self):
        if self.__get_selected_item() is None:
            ErrorMessage("Selezionare un elemento per visualizzarlo!").exec_()
        else:
            self.__go_to_show_item_view()

    def edit_item(self):
        print(self.__get_selected_item())
        if self.__get_selected_item() is None:
            ErrorMessage("Selezionare un elemento da modificare!").exec_()
            return
        self.__go_to_cataloging_view()

    # region Private

    def __get_items(self):
        self.__items = []
        query = self.searchField.text()
        # if "\'" in query:
        #     query.replace("\'", "\x27")

        self.__items = self.itmManager.get_items(query,
                                                 self.searchMode.currentIndex(),
                                                 self.quarantineCheckBox.isChecked(),
                                                 self.discardedCheckBox.isChecked())

    def __update_table(self):
        self.itemTable.clearSelection()
        self.__remove_rows()
        for item in self.__items:
            row = self.itemTable.rowCount()
            self.itemTable.insertRow(row)
            self.itemTable.setItem(row, 0, QTableWidgetItem(item.title))
            self.itemTable.setItem(row, 1, QTableWidgetItem(item.author))
            self.itemTable.setItem(row, 2, QTableWidgetItem(item.isbn))
            self.itemTable.setItem(row, 3, QTableWidgetItem(item.bid))
            self.itemTable.setItem(row, 4, QTableWidgetItem(str(item.availability.name).replace('_', " ")))
            self.itemTable.setItem(row, 5, QTableWidgetItem(item.note))

        self.itemTable.setEditTriggers(QTableWidget.NoEditTriggers)

    def __get_selected_item(self):
        if self.itemTable.currentRow() != -1:
            return self.__items[self.itemTable.currentRow()]
        else:
            return None

    def __remove_rows(self):
        """
        Remove all rows from table
        :return:
        """
        for i in reversed(range(0, self.itemTable.rowCount())):
            self.itemTable.removeRow(i)

    def __go_back(self):
        # self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.close()

    def __go_to_cataloging_view(self, new=False):
        if not new:
            self.cataloging_view.item = self.__get_selected_item()
        else:
            self.cataloging_view.item = Item()
        self.cataloging_view.show()

    def __go_to_show_item_view(self):
        self.show_item_view.load_item(self.__get_selected_item())
        self.show_item_view.show()

    # endregion

