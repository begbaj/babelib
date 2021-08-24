from src.Database.DatabaseManager import DatabaseManager

class MovementManager:

    db = DatabaseManager()

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