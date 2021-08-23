from datetime import datetime

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models import ItemEnumerators
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import *


class ItemManager:

    def __init__(self):
        self.dbms = DatabaseManager("config/db.json")

    def add_item(self, item: Item, return_item=None) -> Item:
        item.id = self.dbms.insert_item(item)
        return item

    def get_item(self, item: Item):
        item = self.__convert_dbitem(self.dbms.get_item(item.id))

        item.genre = []
        for genre in self.dbms.get_item_genres(item.id):
            item.genre.append({'id': genre.id, 'description': genre.description})

        item.inner_state = []
        for inner_state in self.dbms.get_item_inner_states(item.id):
            item.inner_state.append(ItemEnumerators.SMUSIEnum(inner_state.id))

        item.external_state = []
        for external_state in self.dbms.get_item_external_states(item.id):
            item.external_state.append(ItemEnumerators.ExternalStateEnum(external_state.id))

        return item

    def get_item_genres(self, item_id: int) -> []:
        new_genres = []
        for genre in self.dbms.get_item_genres(item_id):
            new_genres.append({'id': genre.id, 'description': genre.description})
        return new_genres

    def get_genres(self, genres_ids=None):
        new_genres = []
        if genres_ids is None:
            for genre in self.dbms.get_genres():
                new_genres.append({'id': genre.id, 'description': genre.description})
            return new_genres
        if self.dbms.get_genres(genres_ids) is not None:
            for genre in self.dbms.get_genres(genres_ids):
                new_genres.append({'id': genre.id, 'description': genre.description})
            return new_genres

    def get_inner_states(self, states_id=None):
        new_states = []
        if states_id is None:
            for state in self.dbms.get_inner_states():
                new_states.append(SMUSIEnum(state.id))
            return new_states
        if self.dbms.get_inner_states(states_id) is not None:
            for state in self.dbms.get_inner_states(states_id):
                new_states.append(SMUSIEnum(state.id))
            return new_states

    def get_external_states(self, states_id: [int]):
        new_states = []
        states = self.dbms.get_external_states(states_id)
        if states is not None:
            for state in states:
                new_states.append(ExternalStateEnum(state.id))
        return new_states

    def get_items(self, search_field: str, search_mode: int, quarantined=False, discarded=-1) -> [Item]:
        fitems = []
        for dbitem in self.dbms.get_items(search_field, search_mode, quarantined, discarded):
            item = self.__convert_dbitem(dbitem)

            item.genre = []
            for genre in self.dbms.get_item_genres(item.id):
                item.genre.append({'id': genre.id, 'description': genre.description})

            item.inner_state = []
            for inner_state in self.dbms.get_item_inner_states(item.id):
                item.inner_state.append(ItemEnumerators.SMUSIEnum(inner_state.id))

            item.external_state = []
            for external_state in self.dbms.get_item_external_states(item.id):
                item.external_state.append(ItemEnumerators.ExternalStateEnum(external_state.id))

            fitems.append(item)
        return fitems

    def edit_item(self, item: Item) -> None:
        """
        edit item
        :param item: edited item
        """
        self.dbms.edit_item(item)

    def edit_availability(self, item: Item, availability: AvailabilityEnum) -> None:
        item.availability = availability
        self.dbms.edit_item(item)

    def edit_position(self, item: Item, rack: int, shelf: str, pos: int) -> None:
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

    def delete_item(self, item: Item):
        self.dbms.remove_item(item)

    def discard_item(self, item: Item):
        item.availability = ItemEnumerators.AvailabilityEnum.scartato
        self.dbms.edit_item(item)

    # def check_bid(self, bid) -> bool:
    #     '''
    #     Check if the bid is unique in the database
    #     :param bid:
    #     :return: True if it is unique
    #     '''
    #
    #     qr = self.dbms.check_bid(bid)
    #     if len(qr) == 0:
    #         return True
    #     else:
    #         return False
    #
    # def check_isbn(self, isbn) -> bool:
    #     qr = self.dbms.check_isbn(isbn)
    #     if len(qr) == 0:
    #         return True
    #     else:
    #         return False
    #
    # def check_for_isbn(self, id, isbn):
    #     qr = self.dbms.check_for_isbn(id, isbn)
    #     if len(qr) == 0:
    #         return True
    #     else:
    #         return False
    #
    # def check_for_bid(self, id, bid):
    #     qr = self.dbms.check_for_bid(id, bid)
    #     if len(qr) == 0:
    #         return True
    #     else:
    #         return False

    def __convert_dbitem(self, dbitem) -> Item:
        """
        This method converts a DatabaseManager obj into a Item obj
        :param dbitem: DatabaseManager object
        :return: an Item object
        """
        item = Item()
        item.id = dbitem.id
        item.availability = ItemEnumerators.AvailabilityEnum(int(dbitem.availability))
        item.bid = dbitem.bid
        item.isbn = dbitem.isbn
        item.title = dbitem.title
        item.author = dbitem.author
        item.lang = ItemEnumerators.LangEnum(int(dbitem.lang_id))
        item.cataloging_level = ItemEnumerators.CatalogingLevel(int.from_bytes(dbitem.cataloging_level, 'big'))  # serve per convertire un byte in int ('big' = big endian)
        item.publication_date = dbitem.publication_date
        item.publication_state = int.from_bytes(dbitem.publication_state, 'big')
        item.rack = dbitem.rack
        item.shelf = dbitem.shelf
        item.position = dbitem.position
        item.opac_visibility = int.from_bytes(dbitem.opac_visibility, 'big')
        item.price = dbitem.price

        if dbitem.quarantine_start_date is not None:
            item.quarantine_start_date = dbitem.quarantine_start_date.date()
            item.quarantine_end_date = dbitem.quarantine_end_date.date()
        else:
            item.quarantine_start_date = None
            item.quarantine_end_date = None

        if dbitem.discarded_date is not None:
            item.discarded_date = dbitem.discarded_date.date()
        else:
            item.discarded_date = None
        item.note = dbitem.note
        # TODO: dobbiamo fare il get dei generi del libro, cosi anche per material nature type lang
        return item

    def print_label(self, item):
        '''
        Print item label
        :param item: item to print
        '''
        pass
