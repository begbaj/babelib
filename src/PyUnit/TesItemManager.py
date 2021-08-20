import random
import unittest
from datetime import datetime

import mariadb

import src.babelibutils
from src.Database.DatabaseManager import DatabaseManager
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Database.db_settings import *
from src.Items.Models.ItemEnumerators import *


class TestItemManager(unittest.TestCase):

    dbms = DatabaseManager()
    im = ItemManager()
    item = Item()

    @classmethod
    def setUpClass(cls) -> None:
        cls.item.id = None
        cls.item.title = 'test'
        cls.item.author = 'test'
        cls.item.isbn = src.babelibutils.Generators.string_digits_nor(13)
        cls.item.bid = src.babelibutils.Generators.string_digits_nor(10)
        cls.item.lang = LangEnum(random.randint(1, 9))
        cls.item.material = MaterialEnum(random.randint(1, 7))
        cls.item.type = TypeEnum(random.randint(1, 15))
        cls.item.nature = NatureEnum(random.randint(1, 3))
        cls.item.cataloging_level = CatalogingLevel(random.randint(0, 1))
        cls.item.publication_date = datetime.today().date()
        cls.item.publication_state = random.randint(0, 1)
        cls.item.rack = random.randint(1, 100)
        cls.item.shelf = src.babelibutils.Generators.string_nor(1)
        cls.item.position = random.randint(1, 300)
        cls.item.opac_visibility = random.randint(0, 1)
        cls.item.price = random.random() * 100
        cls.item.quarantine_start_date = None
        cls.item.quarantine_end_date = None
        cls.item.discarded_date = None
        genres = cls.im.get_genres()
        cls.item.genre = [genres[random.randint(1, len(genres))]]
        cls.item.inner_state = [SMUSIEnum(random.randint(0, len(SMUSIEnum) - 1))]
        cls.item.external_state = [ExternalStateEnum(random.randint(1, len(ExternalStateEnum)))]
        cls.item.note = "ITEM DI PROVA TESTING TESTING TESTING TESTING ADD TI AMO"

    def test_add_item(self):
        self.item.id = self.im.add_item(self.item)

    def test_get_item(self):
        self.assertEqual(self.im.get_item(self.item).id, self.item.id)

    def test_get_item_genres(self):
        self.assertEqual(self.im.get_item_genres(self.item.id), self.item.genre)

    def test_get_genres(self):
        self.assertEqual(len(self.im.get_genres()), 49)
        genres = self.im.get_genres([1, 49])
        self.assertEqual(genres[0]['description'], "Mimo")
        self.assertEqual(genres[1]['description'], "Ucronia")

    def test_get_inner_states(self):
        self.assertEqual(len(self.im.get_inner_states()), 5)

    def test_get_items(self):
        def new_test_item():
            item = Item()
            item.id = None
            item.title = 'test'
            item.author = 'test'
            item.isbn = src.babelibutils.Generators.string_digits_nor(13)
            item.bid = src.babelibutils.Generators.string_digits_nor(10)
            item.lang = LangEnum(random.randint(1, 9))
            item.material = MaterialEnum(random.randint(1, 7))
            item.type = TypeEnum(random.randint(1, 15))
            item.nature = NatureEnum(random.randint(1, 3))
            item.cataloging_level = CatalogingLevel(random.randint(0, 1))
            item.publication_date = datetime.today().date()
            item.publication_state = random.randint(0, 1)
            item.rack = random.randint(1, 100)
            item.shelf = src.babelibutils.Generators.string_nor(1)
            item.position = random.randint(1, 300)
            item.opac_visibility = random.randint(0, 1)
            item.price = random.random() * 100
            item.quarantine_start_date = None
            item.quarantine_end_date = None
            item.discarded_date = None
            genres = self.im.get_genres()
            item.genre = [genres[random.randint(1, len(genres))]]
            item.inner_state = [SMUSIEnum(random.randint(0, len(SMUSIEnum) - 1))]
            item.external_state = [ExternalStateEnum(random.randint(1, len(ExternalStateEnum)))]
            item.note = "ITEM DI PROVA TESTING TESTING TESTING TESTING ADD TI AMO"
            item.id = self.im.add_item(item)
            return item

        test_items = [self.item]
        for i in range(1,10):
            test_items.append(new_test_item())

        self.assertEqual(self.im.get_items("test", 0), test_items)
        self.assertEqual(self.im.get_items("test", 1), test_items)
        self.assertEqual(self.im.get_items("test", 2), test_items)

        i = random.randint(1, len(test_items))
        self.assertEqual(self.im.get_items(test_items[i], 3), test_items[i])
        i = random.randint(1, len(test_items))
        self.assertEqual(self.im.get_items(test_items[i], 4), test_items[i])
        i = random.randint(1, len(test_items))
        self.assertEqual(self.im.get_items(test_items[i], 5), test_items[i])
        i = random.randint(1, len(test_items))
        self.assertEqual(self.im.get_items(test_items[i], 6), test_items[i])

    # def test_edit_item(self):
    #     pass
    #
    # def test_edit_availability(self):
    #     pass
    #
    # def test_edit_position(self):
    #     pass
    #
    # def test_delete_item(self):
    #     pass
    #
    # def test_discard_item(self):
    #     pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.dbms.query("DELETE FROM items WHERE title = 'test'")


if __name__ == '__main__':
    unittest.main()
