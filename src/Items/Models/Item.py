import datetime
from src.Items.Models.ItemEnumerators import *


# TODO: disponibilità, quarantena, aggiorna liste dinamicamente (le drop down devono essere agiornate a seconda dei valori presenti nel db), bottone per tornare indietro, aggiungi documento
# TODO: controlli nella view, constraints nel database, gestione eccezioni

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
        self.nature = NatureEnum.monografia
        self.type = TypeEnum.cartografia_a_stampa

        self.publication_date = datetime.datetime.now()
        self.publication_state = 0
        self.lang = LangEnum.altro

        self.genre = []
        self.inner_state = [SMUSIEnum.nessuno]
        self.external_state = [ExternalStateEnum.nuovo]

        self.rack = None
        self.shelf = None
        self.position = None

        self.opac_visibility = False
        self.price = 0

        self.availability = AvailabilityEnum.disponibile
        self.quarantine_start_date = None
        self.quarantine_end_date = None
        self.discarded_date = None

        self.note = ""

    def __str__(self):
        return self.title + " " + self.author
