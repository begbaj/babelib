from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi


class UserCardView(QMainWindow):

    def __init__(self, widget, user):
        super(UserCardView, self).__init__()
        loadUi("../designer/SchedaUtenteView/SchedaUtenteView/SchedaUtenteView.ui", self)
        self.widget = widget
        self.setup()
        self.user = user
        self.fillCard()

    def fillCard(self):
        self.nameField.setText(self.user.name)
        self.surnameField.setText(self.user.surname)
        self.fiscalcodeField.setText(self.user.fiscal_code)
        self.addressField.setText(self.user.address)
        self.cityField.setText(self.user.city)
        self.capField.setText(self.user.postal_code)
        self.cellField.setText(self.user.first_cellphone)
        self.emailField.setText(self.user.email)
        self.telephonField.setText(self.user.telephone)
        #self.genderBox.setText(self.user.gender)
        #self.nationBox.setText(self.user.Nationality_S.code)
        #self.usertypeBox.setText(self.user.userType.description)

    def setup(self):
        self.returnButton.clicked.connect(self.back)
        self.editButton.clicked.connect(self.edituser)
        self.saveButton.clicked.connect(self.save)
        self.genderBox.setDisabled(True)
        self.nationBox.setDisabled(True)
        self.usertypeBox.setDisabled(True)
        self.dateEdit.setDisabled(True)
        self.districtBox.setDisabled(True)
        self.stateBox.setDisabled(True)

    def edituser(self):
        self.enablefiled()
        ## aggiornare campi
        self.save()

    def enablefiled(self):
        self.nameField.setReadOnly(False)
        self.surnameField.setReadOnly(False)
        self.fiscalcodeField.setReadOnly(False)
        self.addressField.setReadOnly(False)
        self.cityField.setReadOnly(False)
        self.capField.setReadOnly(False)
        self.cellField.setReadOnly(False)
        self.emailField.setReadOnly(False)
        self.telephonField.setReadOnly(False)
        self.stateBox.setDisabled(False)
        self.genderBox.setDisabled(False)
        self.nationBox.setDisabled(False)
        self.usertypeBox.setDisabled(False)
        self.districtBox.setDisabled(False)
        #self.provincieBox.setDisabled(False)

    def loaduser(self):
        # metodo che fa una query al database e riempe i campi con
        # quelli dell'utente selezionato dalla vista precedente
        pass

    def save(self):
        # salva le modifiche, fa una query al database e aggiorna i campi dell'utente
        pass

    def back(self):
        #self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        #self.widget.add(UserCardView)
        #self.close()
        self.close()

