from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models import ItemEnumerators
from src.Items.Models.Item import Item
from datetime import datetime
from src.Items.Models.ItemEnumerators import *


class ItemManager:

    def __init__(self):
        self.dbms = DatabaseManager()

    def add_item(self, item: Item) -> None:
        self.dbms.insert_item(item)
        pass

    def get_item(self, item_id: int) -> Item:
        dbitem = self.dbms.get_items(search_field, search_mode, quarantined, discarded)
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

        return item

    def get_item_genres(self, item_id: int) -> []:
        new_genres = []
        for genre in self.dbms.get_item_genres(item_id):
            new_genres.append({'id': genre.id, 'description': genre.description})
        return new_genres

    def get_genres(self, genres_ids: [int]):
        new_genres = []
        for genre in self.dbms.get_genres(genres_ids):
            new_genres.append({'id': genre.id, 'description': genre.description})
        return new_genres

    def get_inner_states(self, states_id: [int]):
        new_states = []
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
            for external_state in  self.dbms.get_item_external_states(item.id):
                item.external_state.append(ItemEnumerators.ExternalStateEnum(external_state.id))

            fitems.append(item)
        return fitems

    def edit_item(self, item: Item) -> None:
        """
        edit item
        :param item: edited item
        """
        self.dbms.edit_item(item)

    def edit_availability (self, item: Item, availability: AvailabilityEnum) -> None:
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
        self.dbms.remove_item(item.id)

    def discard_item(self, item: Item):
        item.availability = ItemEnumerators.AvailabilityEnum.discarded
        self.dbms.edit_item(item)

    @staticmethod
    def __convert_dbitem(dbitem) -> Item:
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
        item.cataloging_level = ItemEnumerators.CatalogingLevel(int.from_bytes(dbitem.cataloging_level, 'big')) #serve per convertire un byte in int ('big' = big endian)
        item.publication_date = datetime.combine(dbitem.publication_date, datetime.min.time())
        item.publication_state = int.from_bytes(dbitem.publication_state, 'big')
        item.rack = dbitem.rack
        item.shelf = dbitem.shelf
        item.position = dbitem.position
        item.opac_visibility =  int.from_bytes(dbitem.opac_visibility, 'big')
        item.price = dbitem.price

        try:
            if dbitem.quarantine_start_date is not None:
                item.quarantine_start_date =  datetime.combine(dbitem.quarantine_start_date, datetime.min.time())
            else:
                item.quarantine_start_date = None
        except:
            item.quarantine_start_date = None

        try:
            if dbitem.quarantine_end_date is not None:
                item.quarantine_end_date = datetime.combine(dbitem.quarantine_end_date, datetime.min.time())
            else:
                item.quarantine_end_date = None
        except:
            item.quarantine_start_date = None

        item.discarded_date = dbitem.discarded_date
        item.note = dbitem.note
        # TODO: dobbiamo fare il get dei generi del libro, cosi anche per material nature type lang
        return item

    # def print_label(self, item):
    #     pass

