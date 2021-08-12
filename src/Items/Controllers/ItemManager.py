from src.Database.DatabaseManager import DatabaseManager
from src.Items.Models import ItemEnumerators
from src.Items.Models.Item import Item


class ItemManager:

    def __init__(self):
        self.dbms = DatabaseManager()

    def add_item(self, item):
        self.dbms.insert_item(item)
        pass

    def get_item(self, id) -> Item:
        pass

    def get_items(self,search_field, search_mode,quarantined = False, discarded = False):
        fitems = []
        for dbitem in self.dbms.get_items(search_field, search_mode, quarantined, discarded):
            item = Item()
            item.id = dbitem.Id
            item.availability = ItemEnumerators.AvailabilityEnum(int(dbitem.availability))
            item.bid = dbitem.bid
            item.inventory_num = dbitem.inventory_num
            item.isbn = dbitem.isbn
            item.title = dbitem.title
            item.author = dbitem.author
            item.cataloging_level = ItemEnumerators.RankEnum(int.from_bytes(dbitem.cataloging_level, 'big'))
            item.publication_date = dbitem.publication_date
            item.publication_state = dbitem.pubblication_state
            item.rack = dbitem.rack
            item.shelf = dbitem.shelf
            item.position = dbitem.position
            item.opac_visibility = dbitem.opac_visibility
            item.price = dbitem.price
            item.quaratine_start_date = dbitem.quarantine_start_date
            item.quarantine_end_date = dbitem.quarantine_end_date
            item.discarded = dbitem.discarded
            item.discarded_date = dbitem.discarded_date
            item.note = dbitem.note
            fitems.append(item)
            #TODO: dobbiamo fare il get dei generi del libro, cosi anche per material nature type lang
        return fitems

    def edit_position(self, item, new_pos):
        pass

    def edit_availability(self, ):
        pass

    def edit_item(self,
                  id="", bid="", inventory_num="",
                  isbn="", title="", author="",
                  catalogation_level="", material="", nature="",
                  type="", publication_date="", lang="",
                  genre="", inner_state="", external_state="",
                  rack="", shelf="", position="",
                  opac_visibility="", price="", availability="",
                  quarantine_start_date="", quarantine_end_date="", discarded="",
                  discarded_date="", note=0):
        pass

    def print_label(self, item):
        pass

    def search(self,query, search_type, discarded=False,quarantine=False):
        pass

    def edit_availability (self, availability):
        pass

    def edit_position(self):
        pass

