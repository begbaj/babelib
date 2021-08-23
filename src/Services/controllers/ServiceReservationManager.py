from src.Database.DatabaseManager import DatabaseManager
from src.Services.models import SignedServiceReservation, UnsignedServiceReservation


class ServiceReservationManager:

    def __init__(self):
        """
        init method
        """
        self.dbms = DatabaseManager()

    def add_signed_reservation(self, id, d_from, d_to):
        """
        this method allows to add a signed reservation to database
        :param id: id of the user
        :param d_from: start date and start time of the reservation
        :param d_to: end date and end time of the reservation
        :return: None
        """
        self.dbms.add_signed_reservation(id, d_from, d_to)

    def add_unsigned_reservation(self, date_from, date_to, cell_phone, full_name):
        """
        this method allows to add an unsigned reservation to database
        :param date_from: start date and start time of the reservation
        :param date_to: end date and end time of the reservation
        :param cell_phone: cellphone of the unregistered user
        :param full_name: name and surname of the unregistered user
        :return: None
        """
        self.dbms.add_unsigned_reservation(date_from, date_to, cell_phone, full_name)

    def get_unsigned_(self, search_field: str):
        """
        this method gets an unsigned reservation searching over rows in database that have fields similar to searching
        field
        :param search_field: text to compare to database fields
        :return: a mariadb row depending on search_field
        """
        if self.dbms.get_unsigned_reservations(search_field):
            return self.dbms.get_unsigned_reservations(search_field)

    def get_all_signed(self, search_field: str):
        """
        this method will get all the signed reservations searching over rows in database that have fields similar to searching
        :param search_field: text to compare to database fields
        :return: a mariadb row depending on search_field
        """
        return self.dbms.get_signed_user_reservation(search_field)

    def delete_unsigned(self, id):
        """
        this method will delete an unsigned reservation
        :param id: id of the unsigned reservation to delete
        :return: None
        """
        return self.dbms.delete_unsigned_by_id(id)

    def delete_signed(self, id):
        """
        this method will delete a signed reservation
        :param id: id of the signed reservation to delete
        :return: None
        """
        if self.dbms.delete_signed_by_id(id) is None:
            return True
        else:
            return False
