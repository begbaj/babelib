from src.Comunication.Model.Comunication import Comunication
from src.Database.DatabaseManager import DatabaseManager


class ReportManager:

    db = DatabaseManager()

    def set_comunications_to_model(self, rows, one):

        comunications = []

        for row in rows:
            comunication = Comunication(row.text, row.subject)

            comunication.id = row.id
            if one == True:
                return comunication
            else:
                comunications.append(comunication)
        return comunications

    def list(self):
        return self.set_comunications_to_model(self.db.get_comunications(), False)

    def find(self, id):
        return self.set_comunications_to_model(self.db.get_comunications_by_id(id), True)

    def set(self, comunication):
        self.db.set_comunications(comunication)