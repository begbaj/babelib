import sys
from datetime import date, datetime, timedelta

import PyQt5
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QMainWindow, QComboBox
from PyQt5.uic import loadUi

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models.ItemEnumerators import *
from src.Items.Models.Item import Item
from src.Items.Controllers.ItemManager import ItemManager


class CatalogingView(QMainWindow):
    '''
    CatalogingView script
    '''

    def __init__(self, widget, item):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        super(CatalogingView, self).__init__()
        loadUi("../designer/Items/CatalogingView.ui", self)

        self.__dbms = DatabaseManager()
        self.__im = ItemManager()

        self.widget = widget
        self.item = item
        self.__qsd = None #data inizio quarantena
        self.__qed = None #data fine quarantena

        self.inner_state = CheckableComboBox(self.admin_frame) #make ComboBox a CheckableComboBox
        self.external_state = CheckableComboBox(self.admin_frame)
        self.genre = CheckableComboBox(self.cataloging_frame)

        self.inner_state.setGeometry(QRect(220, 30, 121, 21)) #position of the combobox
        self.external_state.setGeometry(QRect(220, 60, 121, 21))
        self.genre.setGeometry(QRect(210, 180, 231, 21))

        self.load_item(self.item)

        self.quarantine_start_button.clicked.connect(lambda: self.__start_quarantine())
        self.save_button.clicked.connect(lambda: self.__save_button())
        self.go_back_button.clicked.connect(lambda: self.close())

    # TODO: add inventory_num, go back button, asterischi, controllo campi vuoti
    def load_item(self, item) -> None:
        self.id.setText(str(item.id))
        self.bid.setText(str(item.bid))
        self.isbn.setText(str(item.isbn))
        self.title.setText(item.title)
        self.author.setText(item.author)
        self.publication_date.setDate(item.publication_date)
        self.shelf.setText(str(item.shelf))
        self.rack.setText(str(item.rack))
        self.position.setText(str(item.position))
        self.price.setText(str(item.price))
        self.note.setText(item.note)

        if item.quarantine_start_date is not None:
            if item.quarantine_end_date is not None:
                self.quarantine_due_time.setText(str(item.quarantine_end_date-item.quarantine_start_date))
                self.quarantine_end_date.setText(str(item.quarantine_end_date))

        genre_list = []
        for i in self.__dbms.get_genres():
            genre_list.append(i.description)
        for index, element in enumerate(genre_list):
            self.genre.addItem(element)
            nitem = self.genre.model().item(index, 0)
            nitem.setCheckState(Qt.Unchecked)
        for k in range(0, len(item.genre)):
            for index, element in enumerate(genre_list):
                if element == self.item.genre[k]['description']:
                    nitem = self.genre.model().item(index, 0)
                    nitem.setCheckState(Qt.Checked)

        self.__fill_checkable_with_enum(SMUSIEnum, self.inner_state, item.inner_state, starts_at=0)
        self.__fill_checkable_with_enum(ExternalStateEnum, self.external_state, item.external_state)
        self.__fill_with_enum(TypeEnum, self.type)
        self.__fill_with_enum(MaterialEnum, self.material)
        self.__fill_with_enum(NatureEnum, self.nature)
        self.__fill_with_enum(LangEnum, self.lang)
        self.__fill_with_enum(CatalogingLevel, self.cataloging_level, starts_at=0)
        self.__fill_with_enum(AvailabilityEnum, self.availability)

        self.cataloging_level.setCurrentIndex(item.cataloging_level.value)
        self.material.setCurrentIndex(item.material.value)
        self.nature.setCurrentIndex(item.nature.value - 1)
        self.type.setCurrentIndex(item.type.value - 1)
        self.opac_visibility.setCurrentIndex(item.opac_visibility)
        self.availability.setCurrentIndex(item.availability.value - 1)
        self.publication_state.setCurrentIndex(item.publication_state)
        self.lang.setCurrentIndex(item.lang.value - 1)

        if len(item.genre) > 0:
            self.genre.setCurrentIndex(item.genre[0]['id'] - 1)
        if len(item.inner_state) > 0:
            self.inner_state.setCurrentIndex(item.inner_state[0].value)
        if len(item.external_state) > 0:
            self.external_state.setCurrentIndex(item.external_state[0].value - 1)

        self.opac_visibility.addItem("Non Visibile")
        self.opac_visibility.addItem("Visibile")

        self.publication_state.addItem("Non Pubblicato")
        self.publication_state.addItem("Pubblicato")

    @staticmethod
    def __fill_with_enum(enum, obj, starts_at=1, selected_index=None) -> None:
        en_list = []
        en_id = []
        for i in range(starts_at, len(enum)+starts_at):
            en_list.append(enum(i).name.capitalize().replace("_", " "))
            en_id.append(enum(i).value)
        for index, element in enumerate(en_list):
            obj.addItem(element)

    @staticmethod
    def __fill_checkable_with_enum(enum, obj, item_list, starts_at=1) -> None:
        en_list = []
        en_id = []
        for i in range(starts_at, len(enum)+starts_at):
            en_list.append(enum(i).name)
            en_id.append(enum(i).value)
        for index, element in enumerate(en_list):
            obj.addItem(element)
            obj.model().item(index, 0).setCheckState(Qt.Unchecked)

        if len(item_list) > 0:
            for index, element in enumerate(en_id):
                for k in item_list:
                    if element - starts_at == k.value:
                        obj.model().item(index, 0).setCheckState(Qt.Checked)

    def __get_from_view(self):
        new_item = self.item
        new_item.title = self.title.text()
        new_item.author = self.author.text()

        new_item.material = MaterialEnum(self.material.currentIndex()+1)
        new_item.type = TypeEnum(self.type.currentIndex()+1)
        new_item.nature = NatureEnum(self.nature.currentIndex()+1)

        new_item.publication_date = self.publication_date.dateTime().toString("yyyy-MM-dd")
        new_item.isbn = self.isbn.text()
        new_item.bid = self.bid.text()
        new_item.price = self.price.text()
        new_item.lang = LangEnum(self.lang.currentIndex()+1)

        new_item.quarantine_start_date = self.__qsd
        new_item.quarantine_end_date = self.__qed

        new_item.rack = self.rack.text()
        new_item.shelf = self.shelf.text()
        new_item.position = self.position.text()

        new_item.availability = AvailabilityEnum(self.availability.currentIndex()+1)
        new_item.cataloging_level = CatalogingLevel(self.cataloging_level.currentIndex())
        new_item.publication_state = self.publication_state.currentIndex()
        new_item.opac_visibility = self.opac_visibility.currentIndex()

        new_item.note = self.note.toPlainText()

        new_item.genre = self.__im.get_genres(self.genre.checkedItems())
        new_item.inner_state = self.__im.get_inner_states(self.inner_state.checkedItems())
        new_item.external_state = self.__im.get_external_states(self.external_state.checkedItems())

        return new_item

    def __start_quarantine(self) -> None:
        self.__qsd = datetime.today().date()
        self.__qed = self.__qsd + timedelta(days=4)
        self.quarantine_due_time.setText(str(self.__qed - self.__qsd))
        self.quarantine_end_date.setText(str(self.__qed))
        self.availability.setCurrentIndex(AvailabilityEnum.quarantined.value - 1)

    def __save_button(self) -> None:
        if self.item.id is None:
            self.__im.add_item(self.__get_from_view())
        else:
            self.__im.edit_item(self.__get_from_view())
        self.close()

    def close(self) -> bool:
        self.item = None
        return super(CatalogingView, self).close()



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