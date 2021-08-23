import random
import string
from datetime import datetime

from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import *


def string_digits(length):
    sample_string = string.ascii_uppercase + string.digits  # define the specific string
    # define the condition for random string
    return ''.join((random.choice(sample_string)) for x in range(length))


def string_digits_nor(length):
    letters = string.ascii_uppercase + string.digits  # define the specific string
    # define the condition for random.sample() method
    return ''.join((random.sample(letters, length)))


def string_nor(length):
    letters = string.ascii_uppercase  # define the specific string
    # define the condition for random.sample() method
    return ''.join((random.sample(letters, length)))


def generate_random_item(add_to_db=False):
    im = ItemManager()
    item = Item()
    item.id = None
    item.title = 'test - ' + string_nor(12)
    item.author = 'test - ' + string_nor(12)
    item.isbn = string_digits_nor(13)
    item.bid = string_digits_nor(10)
    item.lang = LangEnum(random.randint(1, 9))
    item.material = MaterialEnum(random.randint(1, 7))
    item.type = TypeEnum(random.randint(1, 15))
    item.nature = NatureEnum(random.randint(1, 3))
    item.cataloging_level = CatalogingLevel(random.randint(0, 1))
    item.publication_date = datetime.today().date()
    item.publication_state = random.randint(0, 1)
    item.rack = random.randint(1, 100)
    item.shelf = string_nor(1)
    item.position = random.randint(1, 300)
    item.opac_visibility = random.randint(0, 1)
    item.price = random.random() * 100
    item.quarantine_start_date = None
    item.quarantine_end_date = None
    item.discarded_date = None
    genres = im.get_genres()
    item.genre = [genres[random.randint(1, len(genres) - 1)]]
    item.inner_state = [SMUSIEnum(random.randint(0, len(SMUSIEnum) - 1))]
    item.external_state = [ExternalStateEnum(random.randint(1, len(ExternalStateEnum)))]
    item.note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius in augue sodales semper. " \
                "In ornare ex ultricies mi molestie, vitae euismod lorem vulputate. Nullam nunc dolor, egestas eu " \
                "luctus at, tincidunt vel elit. In commodo, est sed ultricies tincidunt, velit dolor egestas lacus, " \
                "et pretium arcu libero rhoncus libero. Vestibulum augue eros, placerat nec blandit vel, gravida et " \
                "nulla. Maecenas vestibulum ut mi sed sagittis. Etiam eget leo a nibh fermentum malesuada. " \
                "Nulla sed nullam."
    if add_to_db:
        item = im.add_item(item, return_item=True)

    return item

def date_converter(date):
    pass