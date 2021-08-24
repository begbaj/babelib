import random
import string
from faker import Faker
from datetime import datetime, timedelta
from src.Users.controllers.UserManager import UserManager
import src.Users.View.UserCardView
from src.Movements.Models.Movement import Movement
from src.Users.models.User import User
from src.Users.models.UserType import UserType
from src.Users.models.Nationality import Nationality
from src.Items.Controllers.ItemManager import ItemManager
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import *
from src.Database.DatabaseManager import DatabaseManager


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


def generate_random_test_item(add_to_db=False):
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
    item.note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius in augue sodales semper."

    if add_to_db:
        item = im.add_item(item, return_item=True)

    return item


def generate_random_item():
    locale = "en_US"
    if random.randint(0, 10) < 5:
        locale = "it_IT"
    fake = Faker(locale=locale)
    im = ItemManager()
    item = Item()
    item.id = None
    item.title = fake.catch_phrase()
    item.author = fake.last_name()
    item.isbn = fake.isbn13().replace('-', '')
    item.bid = fake.isbn10().replace('-', '')
    item.lang = random.choice(list(LangEnum))
    item.material = random.choice(list(MaterialEnum))
    item.type = random.choice(list(TypeEnum))
    item.nature = random.choice(list(NatureEnum))
    item.cataloging_level = random.choice(list(CatalogingLevel))
    item.publication_date = fake.date_time()
    item.publication_state = random.randint(0, 1)
    item.rack = random.randint(1, 100)
    item.shelf = string_nor(1)
    item.position = random.randint(1, 300)
    item.opac_visibility = random.randint(0, 1)
    item.price = random.random() * 100

    item.availability = random.choice(list(AvailabilityEnum))
    if item.availability.value == AvailabilityEnum.scartato:
        item.discarded_date = fake.date_time()
    elif item.availability == AvailabilityEnum.in_quarantena:
        item.quarantine_start_date = fake.date_between(datetime.today() - timedelta(4), datetime.today())
        item.quarantine_end_date = item.quarantine_start_date + timedelta(4)

    genres = im.get_genres()
    item.genre = [genres[random.randint(1, len(genres) - 1)]]
    item.inner_state = [SMUSIEnum(random.randint(0, len(SMUSIEnum) - 1))]
    item.external_state = [ExternalStateEnum(random.randint(1, len(ExternalStateEnum)))]
    item.note = fake.sentence()
    return item


def user_generator():
    user = User()
    fake = Faker(locale="it_IT")
    user.id = None
    with open("config/user_type.txt", 'r') as file:
        lines = file.readlines()
        user.user_type = lines[random.randint(0, len(lines) - 1)].rstrip('\n')
    with open("config/district.txt", 'r') as file:
        lines = file.readlines()
        user.district = lines[random.randint(0, len(lines) - 1)].rstrip('\n')
    with open("config/nationality.txt", 'r') as file:
        lines = file.readlines()
        user.nationality = lines[random.randint(0, len(lines) - 1)].rstrip('\n')
    with open("config/gender.txt", 'r') as file:
        lines = file.readlines()
        user.gender = lines[random.randint(0, len(lines) - 1)].rstrip('\n')

    user.registration_date = fake.date()

    if user.gender == "Maschio(M)":
        user.name = fake.first_name_male()
        user.surname = fake.last_name_male()

    if user.gender == "Femmina(F)":
        user.name = fake.first_name_female()
        user.surname = fake.last_name_female()

    user.address = fake.street_address()
    user.birthdate = fake.date_of_birth()
    user.birthplace = fake.city()
    user.first_cellphone = fake.phone_number()
    user.postal_code = fake.postcode()
    user.state_id = "IT"
    user.city = fake.city()
    user.email = fake.email()
    user.fiscal_code = "sdfhsdkjfhsdkhf"
    user.privacy_agreement = 1
    user.contect_mode = "1"

    return user


def movement_generator(im: ItemManager, um: UserManager):
    fake = Faker(locale="it_IT")
    movement = Movement()
    movement.id = 'null'
    movement.item = im.convert_dbitem(im.dbms.query("SELECT * FROM items ORDER BY RAND() LIMIT 1;", returns=True)[0])
    movement.item_id = movement.item.id
    movement.user = um.set_users_to_model(um.db.query("SELECT * FROM users ORDER BY RAND() LIMIT 1;", returns=True), True)
    movement.user_id = movement.user.id
    movement.mov_type = 1
    movement.timestamp = fake.date_time()
    return movement

