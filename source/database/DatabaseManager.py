import mariadb

class DatabaseManager:
    """
    DatabaseManager handles the connection to the database

    ----
    Attributes:

    ----
    Methods:

    """

    _conn: mariadb.connect()
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

    def query(self, query: str) -> bool:
        pass

    def select(self, table:str, values:str):
        pass

    def select(self, table:str, values:str, where:str):
        pass

    def insert(self):
        pass

    def delete(self):
        pass



