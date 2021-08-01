import mariadb

from src.Users.models.Nationality import Nationality
from src.Users.models.User import User


class DatabaseManager:
    """
    DatabaseManager handles the connection to the Databse
    ----
    Attributes:
    ----
    Methods:
    """


    _conn = ""
    def __init__(self, user, password, host, port, database):
        """
        Initialize Databse manager
        :param user_: username for db access
        :param password_: password
        :param host_: db host ip/domain
        :param port_: db host port
        :param database_: db name
        """
        _conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        self.cur = _conn.cursor(named_tuple=True)

    def query(self, query: str) -> bool:
        pass

    #def select_user

    def find_user_by_id(self, id):

        try:
            self.cur.execute(f"Select * from users u "
                             f"left join nationalities n on n.id = u.nationality_id "
                             f"left join nationalities n2 on n2.id = u.state_id "
                             f"left join users_types us on us.id = u.user_type_id "
                             f"where u.id = {id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                 , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                 , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                 ,row.first_cellphone, row.telephone, row.email, row.fiscal_code
                 ,row.contect_mode, row.privacy_agreement)

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza

        return user

    # Print List of Contacts
    def get_users(self):
        """Retrieves the list of contacts from the Databse and prints to stdout"""

        # Initialize Variables
        users = []

        # List users
        try:
            self.cur.execute(f"Select * from users u "
                             f"left join nationalities n on n.id = u.nationality_id "
                             f"left join nationalities n2 on n2.id = u.state_id "
                             f"left join users_types us on us.id = u.user_type_id")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement) #row[25] è il code per lo stato di appartenenza

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25]) #row[25] è il code per lo stato di appartenenza


            users.append(user)

        return users


    def set_user(self, user):


        try:
            self.cur.execute(
                f"Update users u "
                f"set u.nationality_id = {user.nationality_id}"
                f", u.state_id = {user.state_id}"
                f", u.user_type_id = {user.user_type_id}"
                f", u.username = {user.username}"
                f", u.registration_date = {user.registration_date}"
                f", u.name = {user.name}"
                f", u.surname = {user.surname}"
                f", u.gender = {user.gender}"
                f", u.birthplace = {user.birthplace}"
                f", u.birthdate = {user.birthdate}"
                f", u.city = {user.city}"
                f", u.address = {user.address}"
                f", u.postal_code = {user.postal_code}"
                f", u.distrit = {user.distrit}"
                f", u.first_cellphone = {user.first_cellphone}"
                f", u.telephone = {user.telephone}"
                f", u.email = {user.email}"
                f", u.fiscal_code = {user.fiscal_code}"
                f", u.contect_mode = {user.contect_mode}"
                f", u.privacy_agreement = {user.privacy_agreement}"
                f" where id = {user.id}")

        except mariadb.Error as e:
            print(f"Error: {e}")



    def insert_user(self, user):
        try:
            self.cur.execute(
                f"Insert into users"
                f" ("
                f"  nationality_id, state_id, user_type_id, username"
                f", registration_date, name, surname, gender, birthplace"
                f", birthdate, city, address, postal_code, distrit, first_cellphone"
                f", telephone, email, fiscal_code, contect_mode, privacy_agreement"
                f")"
                f" values "
                f"("
                f" {user.nationality_id}"
                f", {user.state_id}"
                f", {user.user_type_id}"
                f", {user.username}"
                f", {user.registration_date}"
                f", {user.name}"
                f", {user.surname}"
                f", {user.gender}"
                f", {user.birthplace}"
                f", {user.birthdate}"
                f", {user.city}"
                f", {user.address}"
                f", {user.postal_code}"
                f", {user.distrit}"
                f", {user.first_cellphone}"
                f", {user.telephone}"
                f", {user.email}"
                f", {user.fiscal_code}"
                f", {user.contect_mode}"
                f", {user.privacy_agreement}"
                f")"

            )

            self.cur.commit()

        except mariadb.Error as e:
            print(f"Error: {e}")

    def delete_user(self, id):
        try:
            self.cur.execute(f"delete from user where id = {id}")

        except mariadb.Error as e:
            print(f"Error: {e}")



