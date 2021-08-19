import unittest
from datetime import datetime

import mariadb

from src.Database.DatabaseManager import DatabaseManager
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Database.db_settings import *
from src.Items.Models.ItemEnumerators import MaterialEnum, CatalogingLevel, NatureEnum, TypeEnum, SMUSIEnum, \
    ExternalStateEnum, AvailabilityEnum


class TestItemManager(unittest.TestCase):

    def setUp(self):
        self.item = Item()
        self.item.id = 2
        self.item.genre = []
        self.item_manager = ItemManager()

    def test_get_genres(self):
        self.item_manager.add_item(self.item)
        self.assertEqual(self.item_manager.get_item_genres(1), [3, 22])

    def test_get_inner_states(self):
        self.assertEqual(self.item_manager.get_inner_states(self.item.inner_state(2)), [])

if __name__ == '__main__':
    unittest.main()
