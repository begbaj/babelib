
from src.Databse.DatabaseManager import DatabaseManager

db = DatabaseManager("root", "sa", "localhost", 3306, "babelib_db")

users = db.get_users()

print(users[0].id)