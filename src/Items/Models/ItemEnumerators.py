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
    disponibile = 1
    non_disponibile = 2
    in_quarantena = 3
    scartato = 4
    in_prestito = 5


class NatureEnum(Enum):
    monografia = 1
    analitico = 2
    periodico = 3


class SMUSIEnum(Enum):
    nessuno = 0
    scorretto = 1
    mediocre = 2
    usato = 3
    superato = 4
    inappropriato = 5


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
    italiano = 1
    inglese = 2
    tedesco = 3
    francese = 4
    spagnolo = 5
    cinese = 6
    giapponese = 7
    hindi = 8
    altro = 9
