from enum import Enum


class CatalogingLevel(Enum):
    min = 0
    max = 1


class TypeEnum(Enum):
    printed_cartography = 1
    handwritten_cartography = 2
    booklet = 3
    printed_modern_text = 4
    #anche altri


class AvailabilityEnum(Enum):
    available = 1
    unavailable = 2
    quarantine = 3
    maintainance = 4
    #anche altri


class NatureEnum(Enum):
    monography = 1
    analitic = 2
    periodic = 3


class SMUSIEnum(Enum):
    none = 0
    incorrect = 1
    mediocre = 2
    used = 3
    outmoded = 4
    inappropriate = 5


class MaterialEnum(Enum):
    modern_book = 1
    graphic_book = 2
    audiovideo = 3
    e_resource = 4
    music = 5


class ItemGenreEnum(Enum):
    #TODO: forse meglio rimuovere, troppo lungo
    fantasy = 1
    sci_fi = 2
    historic = 3
    #anche altri


class ExternalStateEnum(Enum):
    #TODO: da completare
    evidenziato = 1
    strappato = 2
    #anche altri


class LangEnum(Enum):
    #TODO: forse meglio rimuovere, troppo lungo
    italian = 1
    english = 2
    #etc
