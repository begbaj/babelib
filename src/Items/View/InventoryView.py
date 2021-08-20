from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableView, QDialog, QMessageBox, QDialogButtonBox
from PyQt5.uic import loadUi
from datetime import datetime
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.ItemEnumerators import AvailabilityEnum
from src.Items.Models import Item
from src.Items.View.CatalogingView import CatalogingView
from src.Items.View.ShowItemView import ShowItemView


class InventoryView(QMainWindow):
    itmManager = ItemManager()
    __items = []

    # TODO: aggiungi documento
    def __init__(self, widget):
        super(InventoryView, self).__init__()
        loadUi("../designer/Items/InventoryViewNew.ui", self)
        self.widget = widget

        try:
            self.itemTable.setSelectionBehavior(QTableView.SelectRows)

            self.searchField.textChanged.connect(lambda: self.search())
            self.quarantineCheckBox.stateChanged.connect(lambda: self.search())
            self.discardedCheckBox.stateChanged.connect(lambda: self.search())

            self.addButton.clicked.connect(lambda: self.add_item())
            self.modifyButton.clicked.connect(lambda: self.edit_item())
            self.discardButton.clicked.connect(lambda: self.discard_item())
            self.returnButton.clicked.connect(lambda: self.__go_back())
            self.showItemButton.clicked.connect(lambda: self.show_item())

            self.searchMode.currentIndexChanged.connect(lambda: self.search())
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
            self.__go_to_showitem_view()

    def edit_item(self):
        if self.__get_selected_item() is None:
            ErrorMessage("Selezionare un elemento da modificare!").exec_()
            return
        self.__go_to_cataloging_view()

    # region Private

    def __get_items(self):
        self.__items = []
        self.__items = self.itmManager.get_items(self.searchField.text(),
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
            self.itemTable.setItem(row, 4, QTableWidgetItem(str(item.availability.name)))
            self.itemTable.setItem(row, 5, QTableWidgetItem(item.note))
            row = row + 1

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
        if new:
            self.cataloging_view = CatalogingView(self.widget, Item.Item())
        else:
            self.cataloging_view = CatalogingView(self.widget, self.__get_selected_item())
        self.cataloging_view.show()

    def __go_to_showitem_view(self):
        self.showitem_view = ShowItemView(self.widget, self.__get_selected_item())
        self.showitem_view.show()

    # endregion


class Dialog(QDialog):
    def __init__(self, text):
        super(Dialog, self).__init__()
        loadUi("../designer/Pop-Up/Dialog.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.text.setText(text)


class ErrorMessage(QDialog):
    def __init__(self, text, buttons=QDialogButtonBox.Ok):
        super(ErrorMessage, self).__init__()
        loadUi("../designer/Pop-up/ErrorMessage.ui", self)
        self.setModal(True)
        self.setWindowTitle("Errore")
        self.buttonBox.setStandardButtons(buttons)
        self.text.setText(text)
        self.buttonBox.accepted.connect(super(ErrorMessage, self).accept)
        self.buttonBox.rejected.connect(super(ErrorMessage, self).reject)

