from src.Database.DatabaseManager import DatabaseManager
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from src.Users.models.User import User


class UserManager:

    db = DatabaseManager()

    def set_users_to_model(self, rows, one):

        users = []

        for row in rows:
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.id = row.Id
            if one == True:
                return user
            else:
                users.append(user)
        return users

    def list(self):
        return self.set_users_to_model(self.db.get_users(), False)

    def find(self, id):
        return self.set_users_to_model(self.db.find_user_by_id(id), True)

    def findName(self, name):
        return self.set_users_to_model(self.db.find_user_by_name(name), False)

    def findSurname(self, surname):
        return self.set_users_to_model(self.db.find_user_by_surname(surname), False)

    def findNameSurname(self, name, surname):
        return self.set_users_to_model(self.db.find_user_by_name_and_surname(name, surname), False)

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


