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


class SavePopUp(QDialog):

    def __init__(self, userm, user):
        super(SavePopUp, self).__init__()
        loadUi("../designer/Pop-Up/Save Pop-Up/savepopup.ui", self)
        self.setup()
        self.userM = userm
        self.user = user

    def setup(self):
        # Button
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(lambda: self.close())
        # Proprietà Finestra
        self.setModal(True)
        self.setWindowTitle('Conferma')

    def confirm(self):
        self.userM.set(self.user)
        self.close()


class Popup(QDialog):
    def __init__(self, text = ''):
        super(Popup, self).__init__()
        loadUi("../designer/Pop-Up/Message Pop-Up/Popup.ui", self)
        self.label.setText(text)
        self.setWindowTitle('Errore')
        self.setModal(True)
        self.okButton.clicked.connect(self.close)


class DeletePopup(QDialog):

    def __init__(self, funct):
        super(DeletePopup, self).__init__()
        loadUi("../designer/Pop-Up/Delete Pop-Up/deletepopup.ui", self)
        self.setWindowTitle('Attenzione')
        self.setModal(True)
        self.funct = funct
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.close)

    def confirm(self):
        self.funct()
        self.close()
