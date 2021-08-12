import datetime

from src.Items.Models.ItemEnumerators import *


class Item():
    """
    Model for Item objects
    """
    def __init__(self):
        self.id = 0
        self.bid = ""
        self.inventory_num = 0
        self.isbn = 0

        self.title = ""
        self.author = ""
        self.catalogation_level = RankEnum.min
        self.material = MaterialEnum.graphic_book
        self.nature = NatureEnum.analitic
        self.type = TypeEnum.booklet

        self.publication_date = datetime.datetime.now()
        self.publication_state = ""
        self.lang = LangEnum.italian

        self.genre = [ItemGenreEnum.fantasy]
        self.inner_state = [SMUSIEnum.usato]
        self.external_state = [ExternalStateEnum.evidenziato]

        self.rack = 0
        self.shelf = ''
        self.position = 0

        self.opac_visibility = False
        self.prive = 0

        self.availability = AvailabilityEnum()
        self.quaratine_start_date = datetime.datetime.now()
        self.end_date = datetime.datetime.now()
        self.discarded = False
        self.discarded_date = datetime.datetime.now()

        self.note = ""

    def __init__(self, id, bid, inventory_num, isbn, title, author, catalogation_level):
        self.__init__(self)

        self.id = id
        self.bid = bid
        self.inventory_num = inventory_num
        self.isbn = isbn

        self.title = title
        self.author = author
        self.catalogation_level = catalogation_level


    def __str__(self):
        return self.title + " " + self.author