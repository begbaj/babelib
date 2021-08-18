import sys
from datetime import date, datetime, timedelta

import PyQt5
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QMainWindow, QComboBox
from PyQt5.uic import loadUi

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models.ItemEnumerators import *
from src.Items.Controllers.ItemManager import ItemManager


class CatalogingView(QMainWindow):

    def __init__(self, widget, item):
        self.dbms = DatabaseManager()
        self.itemManager = ItemManager()
        
        super(CatalogingView, self).__init__()
        loadUi("../designer/Cataloging View/CatalogingView.ui", self)
        self.widget = widget
        self.item = item

        self.inner_state = CheckableComboBox(self.frame_15)
        self.inner_state.setGeometry(QRect(190, 20, 241, 31))

        self.external_state = CheckableComboBox(self.frame_15)
        self.external_state.setGeometry(QRect(190, 70, 241, 31))

        self.genre = CheckableComboBox(self.frame_11)
        self.genre.setGeometry(QRect(190, 230, 251, 21))

        self.load_item()

        self.startQuarantine.clicked.connect(lambda: self.start_quarantine())
        self.saveButton.clicked.connect(lambda: self.save_button())


    # TODO: add inventory_num, quarantina readonly showitem, go back button, asterischi, controllo campi vuoti
    def load_item(self):
        self.title.setText(self.item.title)
        self.author.setText(self.item.author)
        self.publicationDate.setDate(self.item.publication_date)
        self.isbn.setText(str(self.item.isbn))
        self.shelf.setText(str(self.item.shelf))
        self.rack.setText(str(self.item.rack))
        self.position.setText(str(self.item.position))
        self.nature.setCurrentIndex(self.item.nature.value-1)
        self.type.setCurrentIndex(self.item.type.value-1)
        self.note.setText(self.item.note)
        if self.item.quarantine_start_date is not None:
            if self.item.quarantine_end_date is not None:
                self.leftDays.setText(str(self.item.quarantine_end_date-self.item.quarantine_start_date))
                self.availableOn.setText(str(self.item.quarantine_end_date))

        SMUSIList = []
        SMUSIId = []
        for i in range(0, len(SMUSIEnum)):
            SMUSIList.append(SMUSIEnum(i).name)
            SMUSIId.append(SMUSIEnum(i).value)
        for index, element in enumerate(SMUSIList):
            self.inner_state.addItem(element)
            item = self.inner_state.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(SMUSIId):
            for k in range(0, len(self.item.inner_state)):
                if element+1 == self.item.inner_state[k].value:
                    item = self.inner_state.model().item(index, 0)
                    item.setCheckState(Qt.Checked)

        ExternalStateList = []
        ExternalStateId = []
        for i in range(1, len(ExternalStateEnum)+1):
            ExternalStateList.append(ExternalStateEnum(i).name)
            ExternalStateId.append(ExternalStateEnum(i).value)
        for index, element in enumerate(ExternalStateList):
            self.external_state.addItem(element)
            item = self.external_state.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(ExternalStateId):
            for k in range(0, len(self.item.external_state)):
                if element+1 == self.item.external_state[k].value:
                    item = self.external_state.model().item(index, 0)
                    item.setCheckState(Qt.Checked)

        GenreList = []
        for i in self.dbms.get_genres():
            GenreList.append(i.description)
        for index, element in enumerate(GenreList):
            self.genre.addItem(element)
            item = self.genre.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(GenreList):
            for k in range(0, len(self.item.genre)):
                if element == self.item.genre[k]['description']:
                    item = self.genre.model().item(index, 0)
                    item.setCheckState(Qt.Checked)

        # for i in self.item.genre:
        #     self.genre.setCurrentIndex(i['id'])

    def get_from_view(self):
        new_item = self.item
        new_item.title = self.title.text()
        new_item.author = self.author.text()

        new_item.type = NatureEnum(self.nature.currentIndex()+1)
        new_item.type = TypeEnum(self.type.currentIndex()+1)
        new_item.material = MaterialEnum(self.material.currentIndex()+1)

        new_item.publication_date = self.publicationDate.dateTime().toString("yyyy-MM-dd")
        #quarantena

        new_item.isbn = self.isbn.text()
        new_item.rack = self.rack.text()
        new_item.isbn = self.shelf.text()
        new_item.isbn = self.position.text()
        new_item.note = self.note.toPlainText()

        new_item.genre = self.itemManager.get_genres(self.genre.checkedItems())
        new_item.inner_state = self.itemManager.get_inner_states(self.inner_state.checkedItems())
        new_item.external_state = self.itemManager.get_external_states(self.external_state.checkedItems())
        return new_item

    def start_quarantine(self):
        self.item.quarantine_start_date = date.today()
        self.item.quarantine_end_date = self.item.quarantine_start_date + timedelta(days=20)
        self.leftDays.setText(str(self.item.quarantine_end_date - self.item.quarantine_start_date))
        self.availableOn.setText(str(self.item.quarantine_end_date))

    def save_button(self):
        self.dbms.edit_item(self.get_from_view())
        self.close()


class CheckableComboBox(QComboBox):

    def __init__(self, parent = None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def checkedItems(self):
        checkedItems = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == Qt.Checked:
                checkedItems.append(index)
        return checkedItems

    def hidePopup(self):
        pass