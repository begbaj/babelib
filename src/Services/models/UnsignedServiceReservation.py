from src.Services.models.ServiceReservation import ServiceReservation


class UnsignedServiceReservation(ServiceReservation):

    def __init__(self, reservation_id=None, date_from='', date_to='', full_name='', cell_phone=''):
        super().__init__(reservation_id, date_from, date_to)
        self.service_reservation = ServiceReservation()
        self.full_name = full_name
        self.cell_phone = cell_phone
