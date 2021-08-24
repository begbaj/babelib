from src.Users.controllers.UserManager import UserManager
from src.Utils.Tools import *


def generate_users(quantity: int) -> None:
    um = UserManager()
    for i in range(0, quantity):
        um.add(user_generator())


def generate_items(quantity: int) -> None:
    im = ItemManager()
    for i in range(0, quantity):
        im.add_item(generate_random_item())


if __name__ == "__main__":
    #generate_users(5000)
    generate_items(5000)


