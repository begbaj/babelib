from enum import Enum


class CatalogingLevel(Enum):
    min = 0
    max = 1


class TypeEnum(Enum):
    cartografia_a_stampa = 1
    cartografia_manoscritta = 2
    libretto = 3
    test_a_stampa = 4
    materiale_grafico = 5
    materiale_multimediale = 6
    musica_manoscritta = 7
    musica_a_stampa = 8
    materiale_video = 9
    nota_illustrativa = 10
    oggetto_tred = 11
    risorsa_elettronica = 12
    registrazione_non_musicale = 13
    registrazione_musicale = 14
    testo_manoscritto = 15


class AvailabilityEnum(Enum):
    available = 1
    unavailable = 2
    quarantined = 3
    discarded = 4
    on_loan = 5


class NatureEnum(Enum):
    monograph = 1
    analytic = 2
    periodic = 3


class SMUSIEnum(Enum):
    none = 0
    incorrect = 1
    mediocre = 2
    used = 3
    outmoded = 4
    inappropriate = 5


class MaterialEnum(Enum):
    cartografia = 1
    libro_analitico = 2
    grafica = 3
    audio_video = 4
    risorsa_elettronica = 5
    libro_moderno = 6
    musica = 7


class ExternalStateEnum(Enum):
    strappato = 1
    evidenziato = 2
    deteriorato = 3
    sottolineato = 4
    scarabocchiato = 5
    pagine_mancanti = 6
    attesa_scarto = 7
    rovinato = 8
    buono = 9
    discreto = 10
    ottimo = 11
    nuovo = 12


class LangEnum(Enum):
    italian = 1
    english = 2
    german = 3
    french = 4
    spanish = 5
    chinese = 6
    japanese = 7
    hindi = 8
    other = 9
