from src.Database.DatabaseManager import DatabaseManager
from datetime import date


class StatsManager:
    dbms = DatabaseManager('config/db.json')

    def __init__(self):
        pass

    def get_user_count(self) -> int:
        return self.dbms.get_user_count()[0][0]

    def get_user_count_gender(self,gender):
        return self.dbms.get_user_count_gender(gender)[0][0]

    def get_user_by_bdate(self, date_i: date, date_f: date):
        return self.dbms.get_user_by_birthdate(date_i, date_f)[0][0]
