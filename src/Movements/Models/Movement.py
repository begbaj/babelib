from src.Items.Models.Item import Item
from src.Users.models.User import User


class Movement:
    id = 0
    item_id = 0
    user_id = 0
    mov_type = ''
    timestamp = ''

    item = Item()
    user = User()

    def __int__(self, item_id, user_id, mov_type, timestamp):
        self.item_id = item_id
        self.user_id = user_id
        self.mov_type = mov_type
        self.timestamp = timestamp
