import random
import time
import unittest
from datetime import datetime, timedelta

import src.Utils.Tools
from src.Database.DatabaseManager import DatabaseManager as dbms
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import *


class TestItemManager(unittest.TestCase):
    im = ItemManager()
    item = Item()

    @classmethod
    def setUpClass(cls) -> None:
        cls.dbms = dbms("../config/db.json")

    def setUp(self) -> None:
        self.item = src.Utils.Tools.generate_random_item()
        self.item = self.im.add_item(self.item) #gia questo permette di testare la funzione add_item, se fallisce qualcosa non va
        print(self.item)

    def test_get_item(self):
        self.assertEqual(self.im.get_item(self.item).id, self.item.id)

    def test_get_item_genres(self):
        self.assertEqual(self.im.get_item_genres(self.item.id), self.item.genre)

    def test_get_genres(self):
        self.assertEqual(len(self.im.get_genres()), 49)
        genres = self.im.get_genres([1, 49])
        self.assertEqual(genres[0]['description'], "Mimo")
        self.assertEqual(genres[1]['description'], "Ucronia")
        del genres

    def test_get_inner_states(self):
        self.assertEqual(len(self.im.get_inner_states()), 5)

    def test_get_items(self):
        test_items = []
        for i in range(1,10):
            test_items.append(self.im.add_item(src.Utils.Tools.generate_random_item()))

        for item in test_items:
            for i, s in enumerate(self.im.get_items(item.title, 0)):
                self.assertEqual(s.id, item.id)
            for i, s in enumerate(self.im.get_items(item.title, 1)):
                self.assertEqual(s.id, item.id)
            for i, s in enumerate(self.im.get_items(item.author, 2)):
                self.assertEqual(s.id, item.id)

        self.assertNotEqual(len(self.im.get_items(test_items[1].isbn, 3)), 0)
        self.assertNotEqual(len(self.im.get_items(test_items[2].bid, 4)), 0)
        self.assertNotEqual(len(self.im.get_items(test_items[3].id, 5)), 0)
        self.assertNotEqual(len(self.im.get_items(test_items[4].note, 6)), 0)

        for it in test_items:
            self.im.delete_item(it)

        del test_items

    def test_edit_item(self):
        self.item.quarantine_start_date = datetime.today().date()
        self.item.quarantine_end_date = self.item.quarantine_start_date + timedelta(4)
        self.item.availability = AvailabilityEnum.in_quarantena

        self.im.edit_item(self.item)
        self.assertEqual(self.item.quarantine_start_date, self.im.get_item(self.item).quarantine_start_date)
        self.assertEqual(self.item.quarantine_end_date, self.im.get_item(self.item).quarantine_end_date)
        self.assertEqual(self.item.availability, self.im.get_item(self.item).availability)
        self.assertEqual(self.item.discarded_date, self.im.get_item(self.item).discarded_date)

        genres = self.im.get_genres()
        self.item.genre = [genres[random.randint(0,len(genres)-1)], genres[random.randint(0,len(genres)-1)]]
        #inserisco un SMUSIEnum.nessuno per verificare che questo non venga aggiunto nel database
        self.item.inner_state = [SMUSIEnum(0),SMUSIEnum(random.randint(1,len(SMUSIEnum)-1))]
        self.item.external_state = [ExternalStateEnum(random.randint(1,len(ExternalStateEnum)-1)),
                                    ExternalStateEnum(random.randint(1,len(ExternalStateEnum)-1))]

        self.im.edit_item(self.item)
        time.sleep(1)
        self.assertEqual(self.im.get_item_genres(self.item.id), self.item.genre)
        # quando si inserisce SMUSIEnum.nessuno (indice 0), questo non viene inserito nel database e
        # quando viene richiesto ritorna una lista vuota!
        self.assertEqual(self.im.get_item(self.item).inner_state, [self.item.inner_state[1]])
        self.assertEqual(self.im.get_item(self.item).external_state, self.item.external_state)

    def tearDown(self) -> None:
        self.im.delete_item(self.item)

    @classmethod
    def tearDownClass(cls) -> None:
        for item in cls.dbms.get_items("test -", 0):
            cls.im.delete_item(item)


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


if __name__ == '__main__':
    unittest.main()
