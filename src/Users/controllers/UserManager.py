from src.Database.DatabaseManager import DatabaseManager
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from src.Users.models.User import User


class UserManager:

    db = DatabaseManager()

    def list(self):
        users = self.db.get_users()
        return users

    def find(self, id):
        user = self.db.find_user_by_id(id)
        return user

    def set(self, user):
        self.db.set_user(user)

    def add(self, user):
        self.db.insert_user(user)

    def delete(self, id):
        self.db.delete_user(id)


