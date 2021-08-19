from src.Database.DatabaseManager import DatabaseManager

class UserManager:

    db = DatabaseManager()

    def list(self):
        movements = self.db.get_movements()
        return movements

    def find(self, id):
        movements = self.db.find_movement_by_id(id)
        return movements

    def findAll(self, search_field, search_mode):
        movements = self.db.find_movement(search_field, search_mode)
        return movements

    def set(self, movement):
        self.db.set_movement(movement)

    def add(self, movement):
        self.db.insert_movement(movement)

    def delete(self, id):
        self.db.delete_movement(id)