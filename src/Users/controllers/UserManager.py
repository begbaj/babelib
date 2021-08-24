from src.Database.DatabaseManager import DatabaseManager
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from src.Users.models.User import User


class UserManager:

    db = DatabaseManager()

    def list(self):

        users = []

        for row in self.db.get_users():
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)
            user.id = row.Id

            users.append(user)
        return users

    def find(self, id):
        row = self.db.find_user_by_id(id)

        user = User(row.nationality, row.user_type
                    , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                    , row.birthdate, row.city, row.address, row.postal_code, row.district
                    , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                    , row.contect_mode, row.privacy_agreement)
        user.id = row.Id

        return user

    def findName(self, name):

        users = []

        for row in self.db.find_user_by_name(name):
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.id = row.Id
            users.append(user)

        return users

    def findSurname(self, surname):

        users = []

        for row in self.db.find_user_by_surname(surname):
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.id = row.Id
            users.append(user)

        return users

    def findNameSurname(self, name, surname):

        users = []

        for row in self.db.find_user_by_name_and_surname(name, surname):
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.id = row.Id
            users.append(user)
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


