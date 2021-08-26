import datetime

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Controllers.ItemManager import ItemManager


class MovementManager:

    db = DatabaseManager()
    itemM = ItemManager()

    def list(self):
        movements = self.db.get_movements()
        return movements

    def find(self, id):
        movements = self.db.find_movement_by_id(id)
        return movements

    def find_all(self,  search_field_mov_type=None, search_mode=None, search_field=None):
        movements = self.db.find_movement(search_field_mov_type, search_mode, search_field)
        return movements

    def set(self, movement):
        self.db.set_movement(movement)

    def add(self, movement):
        self.db.insert_movement(movement)

    def delete(self, id):
        self.db.delete_movement(id)

    def get_items_available(self):
        self.items = self.itemM.get_items('', 0, False, False)
        self.items_available = []

        for item in self.items:
            if item.availability.value == 1:
                self.items_available.append(item)

        return self.items_available

    def get_movements_by_date(self, date: datetime.date):
        return self.db.get_movements_by_date(date)

    def get_last_movement_id(self):
        ids_mov = self.db.get_movements_id()
        return ids_mov[0].id
