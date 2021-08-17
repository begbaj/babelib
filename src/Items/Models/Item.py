import datetime
from src.Items.Models.ItemEnumerators import *


class Item:
    """
    Model for Item objects
    """
    def __init__(self, id=None, bid='A123456789', isbn='AAA123456789', title='', author='', cataloging_level=CatalogingLevel.min):
        self.id = id
        self.bid = bid
        self.isbn = isbn

        self.title = title
        self.author = author
        self.cataloging_level = cataloging_level
        self.material = MaterialEnum.libro_moderno
        self.nature = NatureEnum.analytic
        self.type = TypeEnum.libretto

        self.publication_date = datetime.datetime.now()
        self.publication_state = ""
        self.lang = 1

        self.genre = []
        self.inner_state = [SMUSIEnum.none]
        self.external_state = [ExternalStateEnum.ottimo]

        self.rack = None
        self.shelf = None
        self.position = None

        self.opac_visibility = False
        self.price = 0

        self.availability = AvailabilityEnum.available
        self.quarantine_start_date = None
        self.quarantine_end_date = None
        self.discarded = False
        self.discarded_date = datetime.datetime.now()

        self.note = ""

    def __str__(self):
        return self.title + " " + self.author