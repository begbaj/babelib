from datetime import datetime, timedelta
from datetime import datetime, timedelta

import PyQt5
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import src.Utils.UI
from src.Database.DatabaseManager import DatabaseManager
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.ItemEnumerators import *
from src.Utils.UI import CheckableComboBox
from src.Utils.UI import ErrorMessage


class CatalogingView(QMainWindow):
    """
    CatalogingView script
    """

    def __init__(self, widget, item, update_func):
        '''
        CatalogingView script, handles CatalogingView behaviour which adds/edits an item
        :param widget: QWidget
        :param item: Item to edit
        '''
        super(CatalogingView, self).__init__()
        loadUi("../designer/Items/CatalogingView.ui", self)

        self.update = update_func
        self.something_changed = False
        self.validators_status = None
        self.__field_with_validator = []
        self.__dbms = DatabaseManager()
        self.__im = ItemManager()

        self.widget = widget
        self.item = item
        self.__qsd = None  # data inizio quarantena
        self.__qed = None  # data fine quarantena

        self.inner_state = CheckableComboBox(self.admin_frame)  # make ComboBox a CheckableComboBox
        self.external_state = CheckableComboBox(self.admin_frame)
        self.genre = CheckableComboBox(self.cataloging_frame)

        self.inner_state.setGeometry(QRect(220, 30, 121, 21))  # position of the combobox
        self.external_state.setGeometry(QRect(220, 60, 121, 21))
        self.genre.setGeometry(QRect(210, 180, 231, 21))

        self.load_item(self.item)

        self.quarantine_start_button.clicked.connect(self.__start_quarantine)
        self.save_button.clicked.connect(self.__save_button)
        self.go_back_button.clicked.connect(self.close)

        self.title.textChanged.connect(self.check_qline_state)
        self.author.textChanged.connect(self.check_qline_state)
        self.bid.textChanged.connect(self.check_qline_state)
        self.isbn.textChanged.connect(self.check_qline_state)
        self.rack.textChanged.connect(self.check_qline_state)
        self.shelf.textChanged.connect(self.check_qline_state)
        self.position.textChanged.connect(self.check_qline_state)
        self.price.textChanged.connect(self.check_qline_state)

        self.title.textChanged.connect(self.something_changed_set)
        self.author.textChanged.connect(self.something_changed_set)
        self.bid.textChanged.connect(self.something_changed_set)
        self.isbn.textChanged.connect(self.something_changed_set)
        self.rack.textChanged.connect(self.something_changed_set)
        self.shelf.textChanged.connect(self.something_changed_set)
        self.position.textChanged.connect(self.something_changed_set)
        self.price.textChanged.connect(self.something_changed_set)
        self.quarantine_start_button.clicked.connect(self.something_changed_set)

        self.set_validators()
        self.check_validators()

    def load_item(self, item) -> None:
        """
        this method loads item
        :param item:
        :return:
        """
        self.bid.setText(str(item.bid))
        self.isbn.setText(str(item.isbn))
        self.title.setText(item.title)
        self.author.setText(item.author)
        if item.publication_date is not None:
            self.publication_date.setDate(item.publication_date)

        if item.id is None:
            self.id.setText('')
        else:
            self.id.setText(str(item.id))

        if item.shelf is None:
            self.shelf.setText('')
        else:
            self.shelf.setText(str(item.shelf))

        if item.rack is None:
            self.rack.setText('')
        else:
            self.rack.setText(str(item.rack))

        if item.position is None:
            self.position.setText('')
        else:
            self.position.setText(str(item.position))
        self.price.setText(str(item.price))
        self.note.setText(item.note)

        if item.quarantine_start_date is not None:
            if item.quarantine_end_date is not None:
                self.quarantine_due_time.setText(str(item.quarantine_end_date - item.quarantine_start_date))
                self.quarantine_end_date.setText(str(item.quarantine_end_date))

        genre_list = []
        self.genre.clear()
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

        self.opac_visibility.clear()
        self.opac_visibility.addItem("Non Visibile")
        self.opac_visibility.addItem("Visibile")

        self.publication_state.clear()
        self.publication_state.addItem("Non Pubblicato")
        self.publication_state.addItem("Pubblicato")

        self.something_changed = False

    def check_qline_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if sender.property("isUpper"):
            sender.setText(sender.text().upper())

        if state == PyQt5.QtGui.QValidator.Acceptable:
            color = 'background-color:rgba(23, 28, 78, 100); color:rgba(255, 255, 255); border-radius: 20px;' \
                    'border-style: solid; border:none; text-align: center;'  # green'
        elif state == PyQt5.QtGui.QValidator.Intermediate:
            color = 'background-color:rgba(255, 255, 0, 200); color:rgba(0, 0, 0); border-radius: 20px;' \
                    'border-style: solid; border:none; text-align: center;'  # yellow
        else:
            color = 'background-color:rgba(255, 0, 0, 100); color:rgb(0, 0, 0); border-radius: 20px;' \
                    'border-style: solid; border:none; text-align: center;'  # red
        sender.setStyleSheet('QLineEdit { %s }' % color)

    def set_validators(self):
        self.__field_with_validator = []
        self.title.setValidator(QRegExpValidator(QRegExp('^[\\w\\s\'\*\.\-,!`?@"\[\]{}=_+():]{1,150}$')))
        self.author.setValidator(QRegExpValidator(QRegExp('^[\\w\\s\'\*\.\-,!`?@"\[\]{}=_+():]{1,150}$')))
        self.bid.setValidator(QRegExpValidator(QRegExp('^\\w{10}$')))
        self.isbn.setValidator(QRegExpValidator(QRegExp('^\\w{13}$')))

        self.rack.setValidator(QRegExpValidator(QRegExp('^\\d{1,4}$')))
        self.shelf.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z]{1}$')))
        self.position.setValidator(QRegExpValidator(QRegExp('^\\d{1,3}$')))

        self.price.setValidator(QRegExpValidator(QRegExp('^(\\d+)\.(\\d{0,2})$')))

        self.__field_with_validator.append(self.title)
        self.__field_with_validator.append(self.author)
        self.__field_with_validator.append(self.bid)
        self.__field_with_validator.append(self.isbn)
        self.__field_with_validator.append(self.rack)
        self.__field_with_validator.append(self.shelf)
        self.__field_with_validator.append(self.position)
        self.__field_with_validator.append(self.price)

        # self.quarantine_due_time.setValidator(QRegExpValidator(QRegExp('^\\d{1,4}$')))
        # self.quarantine_end_date.setValidator(QRegExpValidator(QRegExp('^\\d{1,4}$')))

        # QRegExpValidator(QRegExp('^[a-zA-Z]*$'))

    @staticmethod
    def __fill_with_enum(enum, obj, starts_at=1, selected_index=None) -> None:
        obj.clear()
        en_list = []
        en_id = []
        for i in range(starts_at, len(enum) + starts_at):
            en_list.append(enum(i).name.capitalize().replace("_", " "))
            en_id.append(enum(i).value)
        for index, element in enumerate(en_list):
            obj.addItem(element)

    @staticmethod
    def __fill_checkable_with_enum(enum, obj, item_list, starts_at=1) -> None:
        obj.clear()
        en_list = []
        en_id = []
        for i in range(starts_at, len(enum) + starts_at):
            en_list.append(enum(i).name.replace('_', ' ').capitalize())
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
        # if len(new_item.title) == 0 or len(new_item.author) == 0:
        #     self.title.setStyleSheet('border-color:rgb(255,0,0)')
        #     self.author.setStyleSheet('border-color:rgb(255,0,0)')

        new_item.material = MaterialEnum(self.material.currentIndex() + 1)
        # if self.material.currentIndex() < 0:
        #     self.material.setStyleSheet('border-color:rgb(255,0,0)')

        new_item.type = TypeEnum(self.type.currentIndex() + 1)
        # if self.type.currentIndex() < 0:
        #     self.material.setStyleSheet('border-color:rgb(255,0,0)')

        new_item.nature = NatureEnum(self.nature.currentIndex() + 1)
        # if self.nature.currentIndex() < 0:
        #     self.nature.setStyleSheet('border-color:rgb(255,0,0)')

        new_item.publication_date = self.publication_date.dateTime().toString("yyyy-MM-dd")

        new_item.isbn = self.isbn.text()




        # if len(new_item.isbn) != 13:
        #     self.isbn.setStyleSheet('border-color:rgb(255,0,0')

        new_item.bid = self.bid.text()

        new_item.price = self.price.text()
        new_item.lang = LangEnum(self.lang.currentIndex() + 1)

        new_item.quarantine_start_date = self.__qsd
        new_item.quarantine_end_date = self.__qed

        new_item.rack = self.rack.text()
        new_item.shelf = self.shelf.text()
        new_item.position = self.position.text()

        new_item.availability = AvailabilityEnum(self.availability.currentIndex() + 1)
        new_item.cataloging_level = CatalogingLevel(self.cataloging_level.currentIndex())
        new_item.publication_state = self.publication_state.currentIndex()
        new_item.opac_visibility = self.opac_visibility.currentIndex()

        new_item.note = self.note.toPlainText()

        new_item.genre = self.__im.get_genres(self.genre.checkedItems(1))

        # if self.genre.checkedItems() == []:
        #     self.genre.setStyleSheet('border-color:rgb(255,0,0)')

        new_item.inner_state = self.__im.get_inner_states(self.inner_state.checkedItems())
        new_item.external_state = self.__im.get_external_states(self.external_state.checkedItems())

        return new_item

    def __start_quarantine(self) -> None:
        self.__qsd = datetime.today().date()
        self.__qed = self.__qsd + timedelta(days=4)
        self.quarantine_due_time.setText(str(self.__qed - self.__qsd))
        self.quarantine_end_date.setText(str(self.__qed))
        self.availability.setCurrentIndex(AvailabilityEnum.in_quarantena.value - 1)

    def __save_button(self) -> None:
        if len(self.bid.text()) < 10 and len(self.bid.text()) > 0 and len(self.isbn.text()) < 13 and len(self.isbn.text()) > 0:
            src.Utils.UI.ErrorMessage("ISBN e BID troppo corti").exec_()
            return
        if len(self.isbn.text()) < 13 and len(self.isbn.text()) > 0:
            src.Utils.UI.ErrorMessage("ISBN troppo corto").exec_()
            return
        if len(self.bid.text()) < 10 and len(self.bid.text()) > 0:
            src.Utils.UI.ErrorMessage("BID troppo corto").exec_()
            return
        self.check_validators()
        if self.something_changed:
            if self.validators_status:
                if self.item.id is not None:
                    self.__im.edit_item(self.__get_from_view())
                else:
                    self.__im.add_item(self.__get_from_view())
                self.close()
            else:
                src.Utils.UI.ErrorMessage("Non sono stati riempiti tutti i campi obbligatori! Ricontrollare.").exec_()
        else:
            self.close()


    def check_validators(self):
        self.validators_status = None
        for validator in self.__field_with_validator:
            status = validator.validator().validate(validator.text(), 0)
            if validator.property("isMandatory") and self.validators_status is not False:
                if status[0] == 2:
                    self.validators_status = True
                else:
                    self.validators_status = False


    def close(self) -> bool:
        self.item = None
        self.update()
        return super(CatalogingView, self).close()

    def something_changed_set(self):
        self.something_changed = True

    def show(self):
        self.load_item(self.item)
        super(CatalogingView, self).show()
