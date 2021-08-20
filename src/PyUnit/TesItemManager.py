import unittest
from datetime import datetime

import mariadb

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Database.db_settings import *
from src.Items.Models.ItemEnumerators import *

class TestItemManager(unittest.TestCase):

    dbms = DatabaseManager()
    im = ItemManager()

    def setUp(self):

        self.item = Item()

        self.item.id = None
        self.item.title = 'test'
        self.item.author = 'test'
        self.item.isbn = 'AAAAAAAAAAAAA'
        self.item.bid = 'AAAAAAAAAA'
        self.item.lang = LangEnum.italiano
        self.item.material = MaterialEnum.libro_moderno
        self.item.type = TypeEnum.test_a_stampa
        self.item.nature = NatureEnum.analitico
        self.item.cataloging_level = CatalogingLevel.max
        self.item.publication_date = datetime.today().date()
        self.item.publication_state = 1
        self.item.rack = 101
        self.item.shelf = 'Z'
        self.item.position = 101
        self.item.opac_visibility = 0
        self.item.price = 69.420
        self.item.quarantine_start_date = None
        self.item.quarantine_end_date = None
        self.item.discarded_date = None
        self.item.note = "ITEM DI PROVA TESTING TESTING TESTING TESTING ADD TI AMO"

        self.dbms.insert_item(self.item)

    def tearDown(self) -> None:
        self.dbms.remove_item(self.item)

    def test_add_item(self):
        self.dbms.remove_item(self.item)
        self.item.cataloging_level = CatalogingLevel.min
        with self.assertRaises(Exception):
            self.im.add_item(self.item)

        self.item.cataloging_level = CatalogingLevel.max
        self.im.add_item(self.item)

    def test_get_item(self):
        self.item.id = 1
        self.assertEquals(self.im.get_item(self.item.id), self.item)

    # def test_get_genres(self):
    #     self.item_manager.add_item(self.item)
    #     self.assertEqual(self.item_manager.get_item_genres(1), [3, 22])
    #
    # def test_get_inner_states(self):
    #     self.assertEqual(self.item_manager.get_inner_states(self.item.inner_state(2)), [])

if __name__ == '__main__':
    unittest.main()
