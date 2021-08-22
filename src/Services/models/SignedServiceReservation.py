from src.Services.models.ServiceReservation import ServiceReservation


class SignedServiceReservation(ServiceReservation):

    def __init__(self, reservation_id=None, date_from='', date_to='', user_id=None, name='', surname='', cellphone=''):
        super().__init__(reservation_id, date_from, date_to)
        self.name = name
        self.surname = surname
        self.user_id = user_id
        self.cellphone = cellphone
