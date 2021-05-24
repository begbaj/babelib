import mariadb

from src.Users.models.User import User


class DatabaseManager:
    """
    DatabaseManager handles the connection to the database

    ----
    Attributes:


    ----
    Methods:

    """


    _conn = ""
    def __init__(self, user_, password_, host_, port_, database_):
        """
        Initialize database manager
        :param user_: username for db access
        :param password_: password
        :param host_: db host ip/domain
        :param port_: db host port
        :param database_: db name
        """
        _conn = mariadb.connect(
            user=user_,
            password=password_,
            host=host_,
            port=port_,
            database=database_
        )
        self.cur = _conn.cursor(named_tuple=True)

    def query(self, query: str) -> bool:
        pass

    #def select_user

    def find_user_by_id(self, id):

        try:
            self.cur.execute(f"Select * from users where id = {id}")
        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                 , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                 , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                 ,row.first_cellphone, row.telephone, row.email, row.fiscal_code
                 ,row.contect_mode, row.privacy_agreement)

        return user

    # Print List of Contacts
    def get_users(self):
        """Retrieves the list of contacts from the database and prints to stdout"""

        # Initialize Variables
        users = []

        # List users

        try:
            self.cur.execute(f"Select * from users")
        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)
            users.append(user)

        return users


    def select(self, table:str, values:str, where:str):
        pass

    def insert(self):
        pass

    def delete(self):
        pass



