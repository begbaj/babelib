from src.Database.DatabaseManager import DatabaseManager
from src.Services.models import SignedServiceReservation, UnsignedServiceReservation


class ServiceReservationManager:

    def __init__(self):
        self.dbms = DatabaseManager()

    def add_signed_reservation(self, signed_reservation: SignedServiceReservation):
        signed_reservation.id = self.dbms.add_signed_reservation(signed_reservation)

    def add_unsigned_reservation(self, unsigned_reservation: UnsignedServiceReservation):
        unsigned_reservation.id = self.dbms.add_unsigned_reservation(unsigned_reservation)

    # def convert_db_un_reservation(dbres):
    #     unsigned = UnsignedServiceReservation()
    #     unsigned.reservation_id =

    def get_unsigned(self, unsigned_reservation):
        unsigned_reservation = self.dbms.get_unsigned_reservation(unsigned_reservation.id)
        return unsigned_reservation

    def get_signed(self, signed_reservation):
        signed_reservation = self.dbms.get_signed_reservation(signed_reservation.id)
        return signed_reservation

    def get_unsigned_(self, search_field: str):
        if self.dbms.get_unsigned_reservations(search_field):
            return self.dbms.get_unsigned_reservations(search_field)

    def get_signed_(self, search_field: str):
        if self.dbms.get_signed_reservations(search_field):
            return self.dbms.get_signed_reservation(search_field)

    def get_all_signed(self, search_field: str):
        return self.dbms.get_signed_user_reservation(search_field)

    def delete_unsigned(self, id):
        return self.dbms.delete_unsigned_by_id(id)

    def delete_signed(self, id):
        if self.dbms.delete_signed_by_id(id) is None:
            return True
        else:
            return False