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
               f"**Disponibilità**: {item.availability.name.replace('_',' ').capitalize()}\n\n" \
               f"**Livello catalogazione**: {item.cataloging_level.name.replace('max','Massimo').replace('min','Minimo')}\n\n" \
               f"**Titolo**: {item.title}\n\n" \
               f"**Autore**: {item.author}\n\n" \
               f"**Genere**: "
        for genre in item.genre:
            text += f"{genre['description']} "

        text += f"\n\n**Stato interno**: "
        for state in item.inner_state:
            text += f"{state.name.replace('_',' ').capitalize()} "

        text += f"\n\n**Stato esterno**: "
        for state in item.external_state:
            text += f"{state.name.replace('_',' ').capitalize()} "

        text += f"\n\n### Identificativo\n\n" \
                f"**ISBN**: {item.isbn}\n\n" \
                f"**BID**: {item.bid}\n\n\n\n" \
                f"**Lingua**: {item.lang.name.replace('_',' ').capitalize()}\n\n" \
                f"### Pubblicazione\n\n" \
                f"**Data di pubblicazione**: {item.publication_date}\n\n" \
                f"**Stato pubblicazione**: {str(item.publication_state).replace('0','Pubblicato').replace('1','Non Pubblicato')}\n\n" \
                f"### Collocazione\n\n" \
                f"**Posizione**: {item.rack} - {item.shelf} - {item.position}\n\n" \
                f"**Stato visibilità database OPAC**: {str(item.opac_visibility).replace('1','Presente').replace('0','Non presente')}\n\n" \
                f"### Dettagli\n\n" \
                f"**Materiale**: {item.material.name.replace('_',' ').capitalize()}\n\n" \
                f"**Natura**: {item.nature.name.replace('_',' ').capitalize()}\n\n" \
                f"**Tipo**: {item.type.name.replace('_',' ').capitalize()}\n\n" \
                f"**Prezzo**: {item.price}€\n\n"

        if item.availability == ItemEnumerators.AvailabilityEnum.in_quarantena:
            text += f"### Stato Quarantena\n\n" \
                    f"**Data inizio qurantena**: {item.quarantine_start_date}\n\n" \
                    f"**Data fine quarantena**: {item.quarantine_end_date}\n\n"

        if item.availability == ItemEnumerators.AvailabilityEnum.scartato:
            text += f"### Informazioni sullo scarto \n\n" \
                    f"**Data di scarto**: {item.discarded_date}\n\n"

        self.itemInfo.setText(text)