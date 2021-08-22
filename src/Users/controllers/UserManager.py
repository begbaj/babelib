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

    def findName(self, name):
        users = self.db.find_user_by_name(name)
        return users

    def findSurname(self, surname):
        users = self.db.find_user_by_surname(surname)
        return users

    def findNameSurname(self, name, surname):
        users = self.db.find_user_by_name_and_surname(name, surname)
        return users

    def set(self, user):
        self.db.set_user(user)

    def add(self, user):
        self.db.insert_user(user)

    def delete(self, id):
        self.db.delete_user(id)

    def get_user_name(self,id):
        return self.db.get_user_name_by_id(id)

    def get_user_surname(self,id):
        return self.db.get_user_surname_by_id(id)


