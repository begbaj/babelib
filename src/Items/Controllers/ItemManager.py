from src.Database.DatabaseManager import DatabaseManager
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
        return self.dbms.get_items(search_field, search_mode, quarantined, discarded)

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