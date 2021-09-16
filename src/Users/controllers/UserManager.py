from src.Database.DatabaseManager import DatabaseManager
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from src.Users.models.User import User


class UserManager:

    db = DatabaseManager()

    #the second member when si true you have one user, false more users
    def set_users_to_model(self, rows, one):

        users = []

        for row in rows:
            user = User(row.nationality, row.user_type
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.district
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement, row.disabled)

            user.id = row.Id
            if one == True:
                return user
            else:
                users.append(user)
        return users

    # region LIST AND FIND

    def list(self, disabled=None):
        if disabled is None or disabled == False:
            return self.set_users_to_model(self.db.get_users(), False)
        elif disabled:
            return self.set_users_to_model(self.db.get_users_disabled(), False)

    def find(self, id):
        return self.set_users_to_model(self.db.find_user_by_id(id), True)

    def findName(self, name, disabled=None):
        if disabled is None or disabled == False:
            return self.set_users_to_model(self.db.find_user_by_name(name), False)
        elif disabled:
            return self.set_users_to_model(self.db.find_user_disabled_by_name(name), False)

    def findSurname(self, surname, disabled=None):
        if disabled is None or disabled == False:
            return self.set_users_to_model(self.db.find_user_by_surname(surname), False)
        elif disabled:
            return self.set_users_to_model(self.db.find_user_disabled_by_surname(surname), False)

    def findNameSurname(self, name, surname, disabled=None):
        if disabled is None or disabled == False:
            return self.set_users_to_model(self.db.find_user_by_name_and_surname(name, surname), False)
        elif disabled:
            return self.set_users_to_model(self.db.find_user_disabled_by_name_and_surname(name, surname), False)

    # endregion

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


