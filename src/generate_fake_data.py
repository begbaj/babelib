from src.Users.controllers.UserManager import UserManager
from src.Utils.Tools import *
from src.Movements.Controllers.MovementManager import MovementManager


def generate_users(quantity: int) -> None:
    um = UserManager()
    for i in range(0, quantity):
        um.add(user_generator())


def generate_items(quantity: int) -> None:
    im = ItemManager()
    for i in range(0, quantity):
        im.add_item(generate_random_item())


def generate_movement(quantity: int) -> None:
    im = ItemManager()
    um = UserManager()
    mm = MovementManager()
    for i in range(0, quantity):
        mm.add(movement_generator(im, um))


if __name__ == "__main__":
    #generate_users(100)
    #generate_items(100)
    generate_movement(10000)