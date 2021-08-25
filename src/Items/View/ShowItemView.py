from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.Items.Models import ItemEnumerators


class ShowItemView(QMainWindow):

    def __init__(self, widget):
        super(ShowItemView, self).__init__(widget)
        loadUi("../designer/Items/ShowItemView.ui", self)
        self.widget = widget

    def load_item(self, item):
        text = f"### Generalità\n\n" \
               f"**Disponibilità**: {item.availability.name}\n\n" \
               f"**Livello catalogazione**: {item.cataloging_level.name}\n\n" \
               f"**Titolo**: {item.title}\n\n" \
               f"**Autore**: {item.author}\n\n" \
               f"**Genere**: "
        for genre in item.genre:
            text += f"{genre['description']} "

        text += f"\n\n**Stato interno**: "
        for state in item.inner_state:
            text += f"{state.name} "

        text += f"\n\n**Stato esterno**: "
        for state in item.external_state:
            text += f"{state.name} "

        text += f"\n\n### Identificativo\n\n" \
                f"**ISBN**: {item.isbn}\n\n" \
                f"**BID**: {item.bid}\n\n\n\n" \
                f"**Lingua**: {item.lang.name}\n\n" \
                f"### Pubblicazione\n\n" \
                f"**Data di pubblicazione**: {item.publication_date}\n\n" \
                f"**Stato pubblicazione**: {item.publication_state}\n\n" \
                f"### Collocazione\n\n" \
                f"**Posizione**: {item.rack} - {item.shelf} - {item.position}\n\n" \
                f"**Stato visibilità database OPAC**: {item.opac_visibility}\n\n" \
                f"### Dettagli\n\n" \
                f"**Materiale**: {item.material.name}\n\n" \
                f"**Natura**: {item.nature.name}\n\n" \
                f"**Tipo**: {item.type.name}\n\n" \
                f"**Prezzo**: {item.price}€\n\n"

        if item.availability == ItemEnumerators.AvailabilityEnum.in_quarantena:
            text += f"### Stato Quarantena\n\n" \
                    f"**Data inizio qurantena**: {item.quarantine_start_date}\n\n" \
                    f"**Data fine quarantena**: {item.quarantine_end_date}\n\n"

        if item.availability == ItemEnumerators.AvailabilityEnum.scartato:
            text += f"### Informazioni sullo scarto \n\n" \
                    f"**Data di scarto**: {item.discarded_date}\n\n"

        self.itemInfo.setText(text)


