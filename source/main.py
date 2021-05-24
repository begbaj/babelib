import database.DatabaseManager as dbman
from source.Users.models.User import User

db = dbman.DatabaseManager("root","sa","localhost",3306,"babelib_db")


#user = db.find_user_by_id(1)
#print(user.nationality_id)
users = []

users = db.get_users()

print(users[0].id)