import datetime

from src.Items.Models.ItemEnumerators import *


class Item():
    """
    Model for Item objects
    """
    def __init__(self, id=0, bid="", inventory_num=0, isbn=0, title="", author="", cataloging_level=RankEnum.min):
        self.id = id
        self.bid = bid
        self.inventory_num = inventory_num
        self.isbn = isbn

        self.title = title
        self.author = author
        self.cataloging_level = cataloging_level
        self.material = MaterialEnum.graphic_book
        self.nature = NatureEnum.analitic
        self.type = TypeEnum.booklet

        self.publication_date = datetime.datetime.now()
        self.publication_state = ""
        self.lang = LangEnum.italian

        self.genre = [ItemGenreEnum.fantasy]
        self.inner_state = [SMUSIEnum.used]
        self.external_state = [ExternalStateEnum.evidenziato]

        self.rack = 0
        self.shelf = ''
        self.position = 0

        self.opac_visibility = False
        self.price = 0

        self.availability = AvailabilityEnum.unavailable
        self.quaratine_start_date = datetime.datetime.now()
        self.quarantine_end_date = datetime.datetime.now()
        self.discarded = False
        self.discarded_date = datetime.datetime.now()

        self.note = ""

    def __str__(self):
        return self.title + " " + self.author