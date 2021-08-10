from src.Databse.DatabaseManager import DatabaseManager
from src.Users.models.User import User


class UserManager:

    db = DatabaseManager()

    def list(self):
        user = self.db.get_users()
        return user

    def find(self, id):
        user = self.db.find_user_by_id(id)
        return user

    def set(self, user):
        self.db.set_user(user)

    def add(self, user):
        self.db.insert_user(user)

    def delete(self, id):
        self.db.delete_user(id)


