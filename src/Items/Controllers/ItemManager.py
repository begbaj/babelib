from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models import ItemEnumerators
from src.Items.Models.Item import Item
from datetime import datetime


class ItemManager:

    def __init__(self):
        self.dbms = DatabaseManager()

    def add_item(cls, item) -> None:
        cls.dbms.insert_item(item)
        pass

    def get_item(cls, id) -> Item:
        return cls.__convert_dbitem(cls.dbms.get_item(id))

    def get_items(self,search_field, search_mode, quarantined=False, discarded=False) -> [Item]:
        fitems = []
        for dbitem in self.dbms.get_items(search_field, search_mode, quarantined, discarded):
            fitems.append(self.__convert_dbitem(dbitem))
        return fitems

    def edit_item(self, item) -> None:
        '''
        edit item
        :param item: edited item
        '''
        # id, bid = "", inventory_num = "", isbn = "", title = "", author = "", catalogation_level = "",
        # material = "", nature = "", type = "", publication_date = "", lang = "", genre = "", inner_state = "",
        # external_state = "", rack = "", shelf = "", position = "", opac_visibility = "", price = "", availability = "",
        # quarantine_start_date = "", quarantine_end_date = "", discarded = "", discarded_date = "", note = 0
        self.dbms.edit_item(item)

    def edit_availability (self,item, availability) -> None:
        item.availability = availability
        self.dbms.edit_item(item)

    def edit_position(self, item, rack, shelf, pos) -> None:
        """
        This method edits the rack, the shelf of the item
        :param item: Item
        :param rack: rack of an item
        :param shelf: shelf of an item
        :param pos: position of an item
        :return: returns an edited item
        """
        item.rack = rack
        item.shelf = shelf
        item.position = pos
        self.dbms.edit_item(item)

    def __convert_dbitem(self, dbitem) -> Item:
        """
        This method converts a DatabaseManager obj into a Item obj
        :param dbitem: DatabaseManager object
        :return: an Item object
        """
        item = Item()
        item.id = dbitem.Id
        item.availability = ItemEnumerators.AvailabilityEnum(int(dbitem.availability))
        item.bid = dbitem.bid
        item.inventory_num = dbitem.inventory_num
        item.isbn = dbitem.isbn
        item.title = dbitem.title
        item.author = dbitem.author
        item.cataloging_level = ItemEnumerators.CatalogingLevel(int.from_bytes(dbitem.cataloging_level, 'big')) #serve per convertire un byte in int ('big' = big endian)
        item.publication_date = datetime.combine(dbitem.publication_date, datetime.min.time())
        item.publication_state = dbitem.pubblication_state
        item.rack = dbitem.rack
        item.shelf = dbitem.shelf
        item.position = dbitem.position
        item.opac_visibility = dbitem.opac_visibility
        item.price = dbitem.price
        item.quaratine_start_date = datetime.combine(dbitem.quarantine_start_date, datetime.min.time())
        item.quarantine_end_date = datetime.combine(dbitem.quarantine_end_date, datetime.min.time())
        item.discarded = dbitem.discarded
        item.discarded_date = dbitem.discarded_date
        item.note = dbitem.note
        # TODO: dobbiamo fare il get dei generi del libro, cosi anche per material nature type lang
        return item

    # def print_label(self, item):
    #     pass

