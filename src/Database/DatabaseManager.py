from src.Items.Models.ItemEnumerators import CatalogingLevel
from src.Users.models.Nationality import Nationality
from src.Users.models.User import User
import mariadb
import json
import os


class DatabaseManager:
    """
    DatabaseManager handles the connection to the Database
    ----
    Attributes:
    ----
    Methods:
    """
    __conn = ""

    #def __init__(self, user, password, host, port, database):

    def __init__(self):
        """
        Initialize Database manager
        :param user_: username for db access
        :param password_: password
        :param host_: db host ip/domain
        :param port_: db host port
        :param database_: db name
        """

        #"root", "sa", "localhost", 3306, "babelib_db"
        #C:\Users\DanieleB\PycharmProjects\babelib\src\Databse\DB Setting\db.json

        data = json.load(open(os.path.abspath("Database/DB Setting/db.json")))

        _conn = mariadb.connect(
            user=data["user"],
            password=data["password"],
            host=data["host"],
            port=data["port"],
            database=data["database"]
        )
        self.cur = _conn.cursor(named_tuple=True)
        _conn.autocommit = True
        self.__conn = _conn

    def query(self, query: str, returns=False) -> list:
        """
        Executes the given query, returns the result, if any, and commits
        :param query: sql query
        :param returns: set True if a return value is expected
        :return: list of objects
        """

        try:
            a = []
            self.cur.execute(query)
            if returns:
                a = self.cur.fetchall()
            self.__conn.commit()
            return a
        except mariadb.Error as e:
            #TODO: Gestire l'eccezione
            print(f"Error: {e}")

    def login(self, username):
        self.cur.execute(f"SELECT password FROM administrator WHERE username = '{username}'")
        #codice insicuro, ritorna la password in chiaro.
        return self.cur.fetchone()

    # region Users

    def get_users(self):
        """Retrieves the list of contacts from the Database and prints to stdout"""

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
                        , row.contect_mode, row.privacy_agreement)  # row[25] è il code per lo stato di appartenenza

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza

            users.append(user)

        return users

    def set_user(self, user):

        try:
            self.cur.execute(
                f"Update users u "
                f"set u.nationality_id = {user.nationality_id}"
                f", u.state_id = {user.state_id}"
                f", u.user_type_id = {user.user_type_id}"
                f", u.username = '{user.username}'"
                f", u.registration_date = '{user.registration_date}'"
                f", u.name = '{user.name}'"
                f", u.surname = '{user.surname}'"
                f", u.gender = '{user.gender}'"
                f", u.birthplace = '{user.birthplace}'"
                f", u.birthdate = '{user.birthdate}'"
                f", u.city = '{user.city}'"
                f", u.address = '{user.address}'"
                f", u.postal_code = '{user.postal_code}'"
                f", u.distrit = '{user.distrit}'"
                f", u.first_cellphone = '{user.first_cellphone}'"
                f", u.telephone = '{user.telephone}'"
                f", u.email = '{user.email}'"
                f", u.fiscal_code = '{user.fiscal_code}'"
                #f", u.contect_mode = {user.contect_mode}"
                #f", u.privacy_agreement = {user.privacy_agreement}"
                f" where id = {user.id}")
            self.f = 0
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
            self.cur.execute(f"delete from users where id = {id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

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
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza

        return user

    def find_user_by_name(self, name):

        # Initialize Variables
        users = []

        try:
            self.cur.execute(f"SELECT * FROM users u "
                             f"LEFT JOIN nationalities n ON n.id = u.nationality_id "
                             f"LEFT JOIN nationalities n2 ON n2.id = u.state_id "
                             f"LEFT JOIN users_types us ON us.id = u.user_type_id "
                             f"WHERE u.name LIKE '%{name}%'")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza
            users.append(user)


        return users

    def find_user_by_surname(self, surname):

        # Initialize Variables
        users = []

        try:
            self.cur.execute(f"Select * from users u "
                             f"left join nationalities n on n.id = u.nationality_id "
                             f"left join nationalities n2 on n2.id = u.state_id "
                             f"left join users_types us on us.id = u.user_type_id "
                             f"where u.surname LIKE '%{surname}%'")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza
            users.append(user)

        return users

    def find_user_by_name_and_surname(self, name, surname):

        # Initialize Variables
        users = []

        try:
            self.cur.execute(f"Select * from users u "
                             f"left join nationalities n on n.id = u.nationality_id "
                             f"left join nationalities n2 on n2.id = u.state_id "
                             f"left join users_types us on us.id = u.user_type_id "
                             f"where u.name LIKE '%{name}%'"
                             f"and u.surname LIKE '%{surname}%'")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            user = User(row.Id, row.nationality_id, row.state_id, row.user_type_id, row.username
                        , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                        , row.birthdate, row.city, row.address, row.postal_code, row.distrit
                        , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                        , row.contect_mode, row.privacy_agreement)

            user.Nationality_N = Nationality(row.nationality_id, row.code)
            user.Nationality_S = Nationality(row.state_id, row[25])  # row[25] è il code per lo stato di appartenenza
            users.append(user)

        return users

    # endregion

    # region Items

    def insert_item(self,item) -> None:
        if item.cataloging_level == CatalogingLevel.max:
            query = f"INSERT INTO items"\
                    f" (material_id, nature_id, type_id, lang_id, availability, bid, isbn,"\
                    f" title, author, cataloging_level, publication_date, publication_state, rack, shelf, position," \
                    f" opac_visibility, price, quarantine_start_date, quarantine_end_date, discarded_date, note)"\
                    f" VALUES "\
                    f" (" \
                    f" {item.material}, {item.nature}, {item.type}, {item.lang}, {item.availability}, {item.bid},"\
                    f" {item.isbn}, {item.title}, {item.author}, {item.cataloging_level}, {item.publication_date}," \
                    f" {item.rack}, {item.shelf}, {item.position},"\
                    f" {item.opac_visibility},{item.price},{item.quarantine_start_date},{item.quarantine_end_date},"\
                    f" {item.discarded_date},{item.note});"

            for genre in item.genre:
                query += f"INSERT INTO items_genres (item_id, genre_id) VALUES ({item.id, genre});"

            for state in item.inner_state:
                query +=f"INSERT INTO items_inner_states (item_id, inner_state_id) VALUES ({item.id, state});"

            for state in item.external_state:
                query += f"INSERT INTO items_external_states (item_id, external_state_id) VALUES ({item.id,state});"
        else:
            ##TODO: aggiungere min level cataloging
            ##TODO: SISTEMARE CATALOGATION IN CATALOGING
            raise Exception("min level cataloging is not supported yet")

        self.query(query)

    def get_items(self, search_field, search_mode, show_quarantined=False, show_discarded=False) -> [tuple]:
        # id=None, material_id=None, nature_id=None, type_id=None, lang_id=None, availability=None, bid=None,
        # inventory_num=None, isbn=None, title=None, author=None, cataloging_level=None, publication_date=None,
        # publication_state=None, rack=None, shelf=None, position=None, opac_visibility=None, price=None,
        # quarantine_start_date=None, quarantine_end_date=None, discarded=None, discarded_date=None, note=None
        query = ""

        if search_mode == 0:
            query += f"SELECT * FROM items where (bid like '%{search_field}%'" \
                    f"or isbn like '%{search_field}%'" \
                    f"or title like '%{search_field}%'" \
                    f"or author like '%{search_field}%'" \
                    f"or note like '%{search_field}%')"
        elif search_mode == 1: #Title
            query += f"SELECT * FROM items WHERE title LIKE '%{search_field}%'"
        elif search_mode == 2: #Author
            query += f"SELECT * FROM items WHERE author LIKE '%{search_field}%'"
        elif search_mode == 3: #ISBN
            query += f"SELECT * FROM items WHERE isbn LIKE '%{search_field}%'"
        elif search_mode == 4: #BID
            query += f"SELECT * FROM items WHERE bid LIKE '%{search_field}%'"
        elif search_mode == 5: #Note
            query += f"SELECT * FROM items WHERE note LIKE '%{search_field}%'"
        else:
            raise Exception("invalid search_mode")

        if not show_quarantined:
            query += " AND (availability <> 3  or quarantine_end_date <= CURRENT_DATE )"

        if not show_discarded:
            query += " AND availability <> 4"

        return self.query(query, returns=True)

    def get_item(self, id) -> tuple:
        query = f"SELECT * FROM items WHERE id = {id}"
        return self.query(query, returns=True)[0]

    def edit_item(self,item) -> None:
        query = f"update items set " \
                f"material_id = {item.material.value}, nature_id = {item.nature.value}, type_id = {item.type.value}, "\
                f"lang_id = {item.lang.value}, availability = {item.availability.value}, bid = '{item.bid}', "\
                f"isbn= '{item.isbn}', title= '{item.title}', author= '{item.author}', "\
                f"cataloging_level={item.cataloging_level.value}, publication_state = {item.publication_state}, " \
                f"rack={item.rack}, shelf='{item.shelf}', position={item.position}," \
                f"opac_visibility={item.opac_visibility}, price={item.price}, note= '{item.note}', "

        if item.discarded_date is not None:
            query += f"discarded_date='{item.discarded_date}', "
        else:
            query += f"discarded_date=null, "

        if item.publication_date is not None:
            query += f"publication_date=\"{item.publication_date}\", "
        else:
            query += f"publication_date=null, "

        if item.quarantine_start_date is not None:
            query += f"quarantine_start_date = '{item.quarantine_start_date}', "
        else:
            query += f"quarantine_start_date=null, "

        if item.quarantine_end_date is not None:
            query += f"quarantine_end_date = '{item.quarantine_start_date}' "
        else:
            query += f"quarantine_end_date=null "

        query += f"where id = {item.id};"
        self.query(query)

    def remove_item(self, item) -> None:
        """
        remove an item from the table
        :param item: item to remove
        """
        query = f"DELETE FROM items WHERE Id = {item.id};"
        self.query(query)

    def get_item_inner_states(self, id):
        query = f"SELECT * FROM inner_states AS ins " \
                f"INNER JOIN items_inner_states AS iis ON iis.inner_state_id = ins.id "\
                f"WHERE iis.item_id = {id};"
        return self.query(query, returns=True)

    def get_item_external_states(self, id):
        query = f"SELECT * FROM external_states AS es " \
                f"INNER JOIN items_external_states AS ies ON ies.external_state_id = es.id " \
                f"WHERE ies.item_id = {id};"
        return self.query(query, returns=True)

    def get_item_genres(self, id):
        query = f"SELECT * FROM genres AS g " \
                f"INNER JOIN items_genres AS ig ON ig.genre_id = g.id " \
                f"WHERE ig.item_id = {id};"
        return self.query(query, returns=True)



    # endregion

    # region Movements

    # endregion