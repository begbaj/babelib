from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QComboBox
from PyQt5.uic import loadUi


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


class Dialog(QDialog):
    def __init__(self, text):
        super(Dialog, self).__init__()
        loadUi("../designer/Pop-Up/Dialog.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.text.setText(text)


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