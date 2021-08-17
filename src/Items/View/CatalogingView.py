import sys
import PyQt5
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QMainWindow, QComboBox
from PyQt5.uic import loadUi

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models.ItemEnumerators import SMUSIEnum, ExternalStateEnum


class CatalogingView(QMainWindow):
      
    def __init__(self, widget, item):
        
        self.dbms = DatabaseManager()
        
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
        #self.inner_state.setCurrentIndex(self.item.inner_state)

        SMUSIList = []
        for i in range(0, len(SMUSIEnum)):
            SMUSIList.append(SMUSIEnum(i).name)
            #lista di Id
        for index, element in enumerate(SMUSIList):
            self.inner_state.addItem(element)
            item = self.inner_state.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(SMUSIList):
            for k in range(0,len(self.item.inner_state)):
                if element == self.item.inner_state[k].value: #name
                    item = self.inner_state.model().item(index,0)
                    item.setCheckState(Qt.Checked)

        ExternalStateList = []
        for i in range(1, len(ExternalStateEnum)+1):
            ExternalStateList.append(ExternalStateEnum(i).name)
        for index, element in enumerate(ExternalStateList):
            self.external_state.addItem(element)
            item = self.external_state.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(ExternalStateList):
            for k in range(0,len(self.item.external_state)):
                if element == self.item.external_state[k].value:
                    item = self.external_state.model().item(index,0)
                    item.setCheckState(Qt.Checked)

        GenreList = []
        for i in self.dbms.get_genres():
            GenreList.append(i.description)
        for index, element in enumerate(GenreList):
            self.genre.addItem(element)
            item = self.genre.model().item(index, 0)
            item.setCheckState(Qt.Unchecked)

        for index, element in enumerate(GenreList):
            for k in range(0,len(self.item.genre)):
                if element == self.item.genre[k]['description']:
                    item = self.genre.model().item(index,0)
                    item.setCheckState(Qt.Checked)

        # for i in self.item.genre:
        #     self.genre.setCurrentIndex(i['id'])


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

    def hidePopup(self):
        pass

    def check(self, index):
        self.model().itemFromIndex(index).setCheckState(Qt.Checked)

    def uncheck(self, index):
        self.model().itemFromIndex(index).setCheckState(Qt.Unchecked)