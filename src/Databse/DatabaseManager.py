import mariadb

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
            self.cur.execute(f"Select * from users u left join nationalities n on n.id = u.nationality_id left join nationalities n2 on n2.id = u.state_id left join users_types us on us.id = u.user_type_id where u.id = {id}")
        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                 , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                 , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                 ,row.first_cellphone, row.telephone, row.email, row.fiscal_code
                 ,row.contect_mode, row.privacy_agreement, row.code, row[25], row.description)

        return user

    # Print List of Contacts
    def get_users(self):
        """Retrieves the list of contacts from the Databse and prints to stdout"""

        # Initialize Variables
        users = []

        # List users
        try:
            self.cur.execute(f"Select * from users u left join nationalities n on n.id = u.nationality_id left join nationalities n2 on n2.id = u.state_id left join users_types us on us.id = u.user_type_id")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement, row.code, row[25], row.description) #row[25] è il code per lo stato di appartenenza
            users.append(user)

        return users


    def select(self, table:str, values:str, where:str):
        pass

    def insert(self, into:str, items:str, values:str):
        pass

    def delete(self):
        pass



