import enum

class RankEnum(enum.Enum):
    min = 0
    max = 1

class TypeEnum(enum.Enum):
    printed_cartography = "pcar"
    handwritten_cartography = "hcar"
    booklet = "bklt"
    printed_modern_text = "pmtx"
    #anche altri

class AvailabilityEnum(enum.Enum):
    available = "a"
    unavailable = "u"
    quarantine = "q"
    maintainance = "m"
    #anche altri

class NatureEnum(enum.Enum):
    monography = "mono"
    analitic = "anlit"
    periodic = "prod"

class SMUSIEnum(enum.Enum):
    none = "none"
    incorrect = "scor"
    mediocre = "medi"
    used = "usat"
    outmoded = "supe"
    inappropriate = "inap"

class MaterialEnum(enum.Enum):
    modern_book = "modb"
    graphic_book = "grph"
    audiovideo = "audv"
    e_resource = "eres"
    music = "musc"

class ItemGenreEnum(enum.Enum):
    fantasy = "fantasy"
    sci_fi = "sci-fi"
    historic = "historic"
    #anche altri

class ExternalStateEnum(enum.Enum):
    evidenziato = "ev"
    strappato = "st"
    #anche altri

class LangEnum(enum.Enum):
    italian = "IT"
    english = "EN"
    #etc
