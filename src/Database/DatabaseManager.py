import src
from src.Items.Models.Item import Item
from src.Items.Models.ItemEnumerators import CatalogingLevel
from src.Movements.Models.Movement import Movement
from src.Users.models.Nationality import Nationality
from src.Users.models.User import User
import mariadb
import json
import os
import decimal
# from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta


class DatabaseManager:
    """
    DatabaseManager handles the connection to the Database
    ----
    Attributes:
    ----
    Methods:
    """

    conn = ""
    cur = ""

    def __init__(self, directory="config/db.json"):
        """
        Initialize Database manager
        :param user_: username for db access
        :param password_: password
        :param host_: db host ip/domain
        :param port_: db host port
        :param database_: db name
        """

        # "root", "sa", "localhost", 3306, "babelib_db"
        # C:\Users\DanieleB\PycharmProjects\babelib\src\Databse\db_settings\db.json

        with open(os.path.abspath(directory)) as file:
            data = json.load(file)

        _conn = None
        try:
            _conn = mariadb.connect(
                user=data['user'],
                password=data['password'],
                host=data['host'],
                port=data['port'],
                database=data['database']
            )
        except FileNotFoundError as err:
            src.Utils.UI.ErrorMessage(err).show()
        except PermissionError as err:
            src.Utils.UI.ErrorMessage(err).show()

        self.cur = _conn.cursor(named_tuple=True)
        _conn.autocommit = True
        self.conn = _conn

    def query(self, query: str, args=None, returns=False) -> list:
        """
        Executes the given query, returns the result, if any, and commits
        :param args:
        :param query: sql query
        :param returns: set True if a return value is expected
        :return: list of objects
        """

        try:
            a = []
            self.cur.execute(query, args)
            if returns:
                a = self.cur.fetchall()
            self.conn.commit()
            return a
        except mariadb.Error as e:
            print(f"Error: {e}")

    def login(self, username):
        """
        Returns the password of the selected user (this is to AVOID for security reasons)
        :param username: username od the administrator
        :return: passowrd
        """
        self.cur.execute(f"SELECT password FROM administrator WHERE username = '{username}'")
        # codice insicuro, ritorna la password in chiaro.
        return self.cur.fetchone()

    # region Users

    def get_users(self):
        """Retrieves the list of contacts from the Database and prints to stdout"""
        query = f"Select * from users u "
        return self.query(query, returns=True)

    def set_user(self, user):

        try:
            self.cur.execute(
                f"Update users u "
                f"set u.nationality = '{user.nationality}'"
                f", u.user_type = '{user.user_type}'"
                f", u.registration_date = '{user.registration_date}'"
                f", u.name = '{user.name}'"
                f", u.surname = '{user.surname}'"
                f", u.gender = '{user.gender}'"
                f", u.birthplace = '{user.birthplace}'"
                f", u.birthdate = '{user.birthdate}'"
                f", u.city = '{user.city}'"
                f", u.address = '{user.address}'"
                f", u.postal_code = '{user.postal_code}'"
                f", u.district = '{user.district}'"
                f", u.first_cellphone = '{user.first_cellphone}'"
                f", u.telephone = '{user.telephone}'"
                f", u.email = '{user.email}'"
                f", u.fiscal_code = '{user.fiscal_code}'"
                f", u.contect_mode = '{user.contect_mode}'"
                # f", u.privacy_agreement = {user.privacy_agreement}"
                f" where id = {user.id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

    def insert_user(self, user):
        try:
            query = f"Insert into users" \
                    f" (nationality, user_type, registration_date, name, surname, gender, birthplace, birthdate, city," \
                    f" address, postal_code, district, first_cellphone, telephone, email, fiscal_code, contect_mode," \
                    f" privacy_agreement) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d);"

            self.query(query, (user.nationality, user.user_type, user.registration_date, user.name, user.surname,
                                    user.gender, user.birthplace, user.birthdate, user.city, user.address,
                                    user.postal_code, user.district, user.first_cellphone, user.telephone, user.email,
                                    user.fiscal_code, user.contect_mode, user.privacy_agreement))
        except mariadb.Error as e:
            print(f"Error: {e}")

    def delete_user(self, user_id):
        try:
            self.cur.execute(f"delete from users where id = {user_id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

    def find_user_by_id(self, user_id):
        query = f"Select * from users where Id = {user_id}"
        #users = self.query(query, returns=True)
        return self.query(query, returns=True)

    def get_users_with_email(self, search_field):
        query = f"SELECT * FROM users where (name like '%{search_field}%' " \
                 f"or surname like '%{search_field}%' " \
                 f"or fiscal_code like '%{search_field}%') " \
                f" and email like '%{search_field}%' "
        return self.query(query, returns=True)

    def get_user_name_by_id(self, user_id):
        query = f"Select name from users where Id = {user_id}"
        return self.query(query, returns=True)

    def get_user_surname_by_id(self, user_id):
        query = (f"Select surname from users where Id = {user_id}")
        return self.query(query, returns=True)

    def find_user_by_name(self, name):
        query = (f"Select * from users u where u.name like '%{name}%'")
        return self.query(query, returns=True)

    def find_user_by_surname(self, surname):
        query = (f"Select * from users u where u.surname like '%{surname}%'")
        return self.query(query, returns=True)

    def find_user_by_name_and_surname(self, name, surname):
        query = (f"Select * from users u where u.name LIKE '%{name}%' and u.surname LIKE '%{surname}%'")
        return self.query(query, returns=True)

    # endregion

    # region Items

    def insert_item(self, item):
        """
        Insert a new item to the database. No id is required since the database is set in AUTO_INCREMENT for that.
        This method will return the id associated to the item.
        :param item: new item
        :return: new item id
        """
        query = f"INSERT INTO items" \
                f" (material_id, nature_id, type_id, lang_id, availability, bid, isbn," \
                f" title, author, cataloging_level, publication_state, rack, shelf, position," \
                f" opac_visibility, price, publication_date, quarantine_start_date, quarantine_end_date, discarded_date, note)" \
                f" VALUES " \
                f" (" \
                f" {self.__check_value(item.material.value, int)}," \
                f" {self.__check_value(item.nature.value, int)}," \
                f" {self.__check_value(item.type.value, int)}," \
                f" {self.__check_value(item.lang.value, int)}," \
                f" {self.__check_value(item.availability.value, int)}," \
                f" '{self.__check_value(item.bid, str)}'," \
                f" '{self.__check_value(item.isbn, str)}',"
        query +=" %s, "
        query +=" %s, "
        query +=f" {self.__check_value(item.cataloging_level.value, int)}, " \
                f" {self.__check_value(item.publication_state, int)}," \
                f" {self.__check_value(item.rack, int, 0)}," \
                f" '{self.__check_value(item.shelf, str, '')}'," \
                f" {self.__check_value(item.position, int, 0)}, " \
                f" {self.__check_value(item.opac_visibility, int, 0)}," \
                f" {round(self.__check_value(item.price, decimal.Decimal, 0), 2)}," \
                f" {self.__set_date_str(item.publication_date)}," \
                f" {self.__set_date_str(item.quarantine_start_date)}," \
                f" {self.__set_date_str(item.quarantine_end_date)}," \
                f" {self.__set_date_str(item.discarded_date)}," \
                f" %s);"
        self.query(query, (item.title, item.author, item.note))

        query = f"SELECT id FROM items ORDER BY id DESC LIMIT 1;"
        nid = self.query(query, returns=True)[0].id

        if item.genre is not None and len(item.genre) > 0:
            for genre in item.genre:
                query = f"INSERT INTO items_genres (item_id, genre_id) VALUES ({nid}, {genre['id']});"
                self.query(query)

        if item.inner_state is not None and len(item.inner_state) > 0:
            for state in item.inner_state:
                query = f"INSERT INTO items_inner_states (item_id, inner_state_id) VALUES ({nid}, {state.value});"
                self.query(query)

        if item.external_state is not None and len(item.external_state) > 0:
            for state in item.external_state:
                query = f"INSERT INTO items_external_states (item_id, external_state_id) VALUES ({nid},{state.value});"
                self.query(query)

        return nid

    def get_genre_value(self, genre_id):
        """
        Returns the genre description.
        :param genre_id: Genre id
        :return: id and description
        """
        query = f"SELECT * FROM genres WHERE id={genre_id}"
        return self.query(query, returns=True)

    def get_items(self, search_field='', search_mode=0, show_quarantined=False, show_discarded=False) -> [tuple]:
        """
        Get a list of items that matches the search query
        :param search_field: string corresponding to the search query
        :param search_mode: 0: all the fields; 1: title; 2: author; 3: ISBN; 4: BID; 5: id/inventory; 6: note
        :param show_quarantined: True: search also for quarantined items
        :param show_discarded: True: search only discarded items
        :return:
        """
        query = ""

        if search_mode == 0:  # eccetto numero di inventario
            query += f"SELECT * FROM items where (bid like '%{search_field}%' " \
                     f"or isbn like '%{search_field}%' " \
                     f"or title like '%{search_field}%' " \
                     f"or author like '%{search_field}%' " \
                     f"or note like '%{search_field}%') "
        elif search_mode == 1:  # Title
            query += f"SELECT * FROM items WHERE title LIKE  '%{search_field}%' "
        elif search_mode == 2:  # Author
            query += f"SELECT * FROM items WHERE author LIKE  '%{search_field}%' "
        elif search_mode == 3:  # ISBN
            query += f"SELECT * FROM items WHERE isbn LIKE  '%{search_field}%' "
        elif search_mode == 4:  # BID
            query += f"SELECT * FROM items WHERE bid LIKE  '%{search_field}%' "
        elif search_mode == 5:  # id / numero di inventario
            query += f"SELECT * FROM items WHERE id LIKE  '%{search_field}%' "
        elif search_mode == 6:  # Note
            query += f"SELECT * FROM items WHERE note LIKE  '%{search_field}%' "
        else:
            raise Exception("invalid search_mode")

        if show_discarded:
            query += " AND availability = 4"
        else:
            if not show_quarantined:
                query += " AND (availability <> 3)"
            query += " AND availability <> 4 "

        query += " LIMIT 100;"
        field = "%"+search_field+"%"
        return self.query(query, returns=True)

    def get_item(self, item_id) -> tuple:
        '''
        Get item from database by item id
        :param item_id: item id
        :return: item
        '''
        query = f"SELECT * FROM items WHERE id = {self.__check_value(item_id, int)}"
        dbitem = self.query(query, returns=True)
        return dbitem[0]

    def edit_item(self, item) -> None:
        query = f"UPDATE items SET " \
                f" material_id = {self.__check_value(item.material.value, int)}," \
                f" nature_id = {self.__check_value(item.nature.value, int)}," \
                f" type_id = {self.__check_value(item.type.value, int)}, " \
                f" lang_id = {self.__check_value(item.nature.value, int)}," \
                f" availability = {self.__check_value(item.availability.value, int)}," \
                f" bid = '{self.__check_value(item.bid, str)}', " \
                f" isbn= '{self.__check_value(item.isbn, str)}'," \
                f" title= '{self.__check_value(item.title, str)}', " \
                f" author= '{self.__check_value(item.author, str)}', " \
                f" cataloging_level={self.__check_value(item.cataloging_level.value, int)}," \
                f" publication_state = {self.__check_value(item.publication_state, int)}, " \
                f" rack={self.__check_value(item.rack, int)}," \
                f" shelf='{self.__check_value(item.shelf, str)}'," \
                f" position={self.__check_value(item.position, int)}," \
                f" opac_visibility={self.__check_value(item.publication_state, int)}," \
                f" price= {round(self.__check_value(item.price, decimal.Decimal), 2)}," \
                f" note= '{self.__check_value(item.note, str)}', " \
                f" discarded_date= {self.__set_date_str(item.discarded_date)}, " \
                f" publication_date= {self.__set_date_str(item.publication_date)}, " \
                f" quarantine_start_date = {self.__set_date_str(item.quarantine_start_date)}, " \
                f" quarantine_end_date = {self.__set_date_str(item.quarantine_end_date)}" \
                f" WHERE id = {self.__check_value(item.id, int)}; "

        self.query(query)

        self.edit_genre(item)
        self.edit_external_states(item)
        self.edit_inner_states(item)

    def edit_genre(self, item, return_query=False):
        if item.genre is not None:
            query = f"DELETE FROM items_genres WHERE item_id = {item.id};\n"
            self.query(query)
            for genre in item.genre:
                query = f"INSERT INTO items_genres (item_id, genre_id) VALUES ({item.id}, {genre['id']});\n"
                self.query(query)
            if return_query:
                return query
        else:
            return None

    def edit_inner_states(self, item, return_query=False):
        query = f"DELETE FROM items_inner_states WHERE item_id = {item.id};"
        self.query(query)
        for state in item.inner_state:
            query = f"INSERT INTO items_inner_states (item_id, inner_state_id) VALUES ({item.id}, {state.value}); "
            self.query(query)
        if return_query:
            return query

    def edit_external_states(self, item, return_query=False):
        query = f"DELETE FROM items_external_states WHERE item_id = {item.id}; "
        self.query(query)
        for state in item.external_state:
            query = f"INSERT INTO items_external_states (item_id, external_state_id) VALUES ({item.id}, {state.value}); "
            self.query(query)
        if return_query:
            return query

    def remove_item(self, item) -> None:
        """
        remove an item from the table
        :param item: item to remove
        """
        query = f"DELETE FROM items WHERE Id = {item.id};"
        self.query(query)

    def get_item_inner_states(self, item_id):
        query = f"SELECT * FROM inner_states AS ins " \
                f"INNER JOIN items_inner_states AS iis ON iis.inner_state_id = ins.id " \
                f"WHERE iis.item_id = {item_id};"
        return self.query(query, returns=True)

    def get_item_external_states(self, item_id):
        query = f"SELECT * FROM external_states AS es " \
                f"INNER JOIN items_external_states AS ies ON ies.external_state_id = es.id " \
                f"WHERE ies.item_id = {item_id};"
        return self.query(query, returns=True)

    def get_genres(self, genre_ids=None):
        if genre_ids is None:
            query = f"SELECT * FROM genres;"
        else:
            query = "SELECT * FROM genres WHERE "
            first = True
            for gid in genre_ids:
                if not first:
                    query += " OR "
                else:
                    first = False
                query += f"id = {gid}"
            query += ";"
        return self.query(query, returns=True)

    def get_inner_states(self, states_id=None):
        if states_id is None:
            query = f"SELECT * FROM inner_states"
        else:
            query = "SELECT * FROM inner_states WHERE "
            first = True
            for sid in states_id:
                if not first:
                    query += " OR "
                else:
                    first = False
                query += f"id = {sid}"
            query += ";"
        return self.query(query, returns=True)

    def get_external_states(self, states_id: [int]):
        if len(states_id) == 0:
            return None
        query = "SELECT * FROM external_states WHERE "
        first = True
        for sid in states_id:
            if not first:
                query += " OR "
            else:
                first = False
            query += f"id = {sid}"
        query += ";"
        return self.query(query, returns=True)

    def get_item_genres(self, item_id):
        query = f"SELECT * FROM genres AS g " \
                f"INNER JOIN items_genres AS ig ON ig.genre_id = g.id " \
                f"WHERE ig.item_id = {item_id};"
        return self.query(query, returns=True)

    # def check_bid(self, bid):
    #     query = f"SELECT id FROM items WHERE bid = '{bid}' "
    #     return self.query(query, returns=True)
    #
    # def check_isbn(self, isbn):
    #     query = f"SELECT id FROM items WHERE isbn = '{isbn}' "
    #     return self.query(query, returns=True)
    #
    # def check_for_isbn(self, id, isbn):
    #     query = f"SELECT id FROM items WHERE id <> {id} and isbn = '{isbn}' "
    #     return self.query(query, returns=True)
    #
    # def check_for_bid(self, id, bid):
    #     query = f"SELECT id FROM items WHERE id <> {id} and isbn = '{bid}' "
    #     return self.query(query, returns=True)

    # endregion

    # region Movements

    def get_movements(self):
        """Retrieves the list of contacts from the Database and prints to stdout"""

        # Initialize Variables
        movements = []

        # itemM = ItemManager()

        # List movements
        try:
            self.cur.execute(f"Select * from movements m "
                             f"left join users u on u.id = m.user_id "
                             f"left join items i on i.id = m.item_id "
                             f"")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            movements.append(self.set_movement_to_model(row))

        return movements

    def set_movement(self, movement):
        try:
            self.cur.execute(
                f"Update movements m "
                f"set m.mov_type = {movement.mov_type} "
                f", m.timestamp = '{movement.timestamp}' "
                f", m.note = '{movement.note}' "
                f" where m.id = {movement.id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

    def insert_movement(self, movement):
        try:
            self.cur.execute(
                f"Insert into movements"
                f" ("
                f"  item_id, user_id"
                f", mov_type, timestamp, note"
                f")"
                f" values "
                f"("
                f" {movement.item_id}"
                f", {movement.user_id}"
                f", {movement.mov_type}"
                f", '{movement.timestamp}'"
                f", '{movement.note}'"
                f")"
            )

        except mariadb.Error as e:
            print(f"Error: {e}")

    def delete_movement(self, id):
        try:
            self.cur.execute(f"delete from movements where id = {id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

    def find_movement(self, search_field_mov_type=None, search_mode=None, search_field=None):
        # itemM = ItemManager()

        # List movements
        movements = []

        try:
            if search_mode == 0:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where (u.name like '%{search_field}%' "
                                 f"or u.surname like '%{search_field}%' "
                                 f"or i.title like '%{search_field}%' "
                                 f"or i.isbn like '%{search_field}%' "
                                 f"or m.timestamp like '%{search_field}%')"
                                 f"and m.mov_type = {search_field_mov_type} ")
            elif search_mode == 1:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where (u.name like '%{search_field}%' "
                                 f"or u.surname like '%{search_field}%') "
                                 f"and m.mov_type = {search_field_mov_type} ")
            elif search_mode == 2:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where i.title like '%{search_field}%' "
                                 f"and m.mov_type = {search_field_mov_type} ")
            elif search_mode == 3:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where i.isbn like '%{search_field}%' "
                                 f"and m.mov_type = {search_field_mov_type} ")

            elif search_mode == 4:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where m.timestamp like '%{search_field}%' "
                                 f"and m.mov_type = {search_field_mov_type} ")

            elif search_mode == 5:
                self.cur.execute(f"Select * from movements m "
                                 f"left join users u on u.id = m.user_id "
                                 f"left join items i on i.id = m.item_id "
                                 f"where m.mov_type = {search_field_mov_type} ")

        except mariadb.Error as e:
            print(f"Error: {e}")

        for row in self.cur.fetchall():
            movements.append(self.set_movement_to_model(row))

        return movements

    def find_mov_by_user_id(self,u_id):
        query = f"SELECT * FROM movements WHERE user_id = {u_id}"
        return self.query(query, returns=True)

    def find_delay(self,id):
        query = f"SELECT m.item_id, m.user_id, m.TIMESTAMP AS 'loan_date', r.timestamp AS 'return_date' FROM movements AS m JOIN movements AS r ON (m.item_id = r.item_id AND m.user_id = r.user_id) WHERE m.user_id = {id} AND m.mov_type = 1 AND r.mov_type = 2"
        return self.query(query, returns=True)

    def find_movement_by_id(self, id):

        # itemM = ItemManager()

        # List movements
        try:
            self.cur.execute(f"Select * from movements m "
                             f"left join users u on u.id = m.user_id "
                             f"left join items i on i.id = m.item_id "
                             f" where m.id = {id}"
                             f"")

        except mariadb.Error as e:
            print(f"Error: {e}")

        return self.set_movement_to_model(self.cur.fetchone())

    def get_movements_id(self):
        query = f"select m.id from movements m order by m.id desc"
        return self.query(query, returns=True)

    def set_movement_to_model(self, row):

        movement = Movement(row.item_id, row.user_id, row.mov_type, row.timestamp, row.note)
        movement.id = row.id

        movement.user = User(row.nationality, row.user_type
                             , row.registration_date, row.name, row.surname, row.gender, row.birthplace
                             , row.birthdate, row.city, row.address, row.postal_code, row.district
                             , row.first_cellphone, row.telephone, row.email, row.fiscal_code
                             , row.contect_mode, row.privacy_agreement)

        movement.user.id = row.user_id

        movement.item = Item()
        movement.item.id = row.item_id

        movement.item.isbn = row.isbn
        movement.item.title = row.title
        movement.item.note = row.note
        movement.item.rack = row.rack
        movement.item.author = row.author
        movement.item.availability = row.availability
        movement.item.bid = row.bid
        movement.item.cataloging_level = row.cataloging_level
        movement.item.discarded_date = row.discarded_date
        # movement.item.external_state = row.external_state
        # movement.item.genre = row.genre
        # movement.item.inner_state = row.inner_state
        # movement.item.lang = row.lang
        # movement.item.material = row.material
        # movement.item.nature = row.nature
        movement.item.opac_visibility = row.opac_visibility
        movement.item.position = row.position
        movement.item.price = row.price
        movement.item.publication_date = row.publication_date
        movement.item.publication_state = row.publication_state
        movement.item.quarantine_end_date = row.quarantine_end_date
        movement.item.quarantine_start_date = row.quarantine_start_date
        movement.item.shelf = row.shelf
        # movement.item.type = row.type

        return movement


    def get_movements_by_date(self, m_date: date):
        query = f"Select * from movements m "\
                f"left join users u on u.id = m.user_id "\
                f"left join items i on i.id = m.item_id "\
                f" where m.timestamp like '%{self.__set_date_str(m_date, no_apici=True)}%';"
        movs = []
        for mov in self.query(query, returns=True):
            movs.append(self.set_movement_to_model(mov))
        return movs
    # endregion

    # region Comunication

    def get_comunications(self):
        query = f"Select * from email_default_message order by id asc "
        return self.query(query, returns=True)

    def get_comunications_by_id(self, id):
        query = f"Select * from email_default_message where id = {id} "
        #comunications = self.query(query, returns=True)
        return self.query(query, returns=True)

    def set_comunications(self, comunication):

        try:
            self.cur.execute(
                f"Update email_default_message edm "
                f"set edm.text = '{comunication.text}'"
                f", edm.subject = '{comunication.subject}'"            
                f" where edm.id = {comunication.id}")

        except mariadb.Error as e:
            print(f"Error: {e}")

    # endregion

    def add_signed_reservation(self, user_id, date_from, date_to):
        try:
            self.cur.execute(
                f"Insert into signed_service_reservation"
                f" ( user_id"
                f", date_from, date_to"
                f")"
                f" values "
                f"("
                f" {user_id}"
                f", '{date_from}'"
                f", '{date_to}'"
                f")"
            )

        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_unsigned_reservation(self, date_from, date_to, cell_phone, full_name):
        try:
            self.cur.execute(
                f"Insert into unsigned_service_reservations"
                f" ("
                f"  date_from"
                f", date_to, fullname, cellphone"
                f")"
                f" values "
                f"("
                f" '{date_from}'"
                f", '{date_to}'"
                f", '{full_name}'"
                f", '{cell_phone}')"
            )


        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_signed_reservation(self, reservation_id) -> tuple:
        query = f"SELECT * FROM signed_service_reservation WHERE id = {reservation_id}"
        res = self.query(query, returns=True)
        return res[0]

    def get_unsigned_reservation(self, reservation_id) -> tuple:
        query = f"SELECT * FROM unsigned_service_reservations WHERE id = {reservation_id}"
        res = self.query(query, returns=True)
        return res[0]

    def get_unsigned_reservations(self, search_field='') -> [tuple]:
        query = f"SELECT * FROM unsigned_service_reservations where (fullname like '%{search_field}%')"
        return self.query(query, returns=True)

    def get_unsigned_reservations_by_date(self, date=datetime.date)-> [tuple]:
        query = f"SELECT * FROM unsigned_service_reservations where (date_from like '%{self.__set_date_str(date, no_apici=True)}%')"
        return self.query(query, returns=True)

    def get_signed_reservations_by_date(self, date=datetime.date)-> [tuple]:
        query = f"SELECT * FROM signed_service_reservation where (date_from like '%{self.__set_date_str(date, no_apici=True)}%')"
        return self.query(query, returns=True)

    def get_signed_reservation_by_user_id(self, user_id) -> [tuple]:
        query = f"SELECT * FROM signed_service_reservation where (user_id like '%{user_id}%')"
        return self.query(query, returns=True)

    def get_all_signed(self):
        query = f"SELECT * FROM signed_service_reservation"
        dbsigned = self.query(query, returns=True)
        return dbsigned

    def get_user_id_in_signed_res(self):
        query = f"SELECT user_id FROM signed_service_reservation"
        return self.query(query, returns=True)

    def get_signed_user_reservation(self, search_field):
        query = f"SELECT ssr.id, u.Id AS 'user_id',concat(u.name,' ',u.surname) AS 'fullname' ,u.first_cellphone AS cellphone,ssr.date_from,ssr.date_to FROM users AS u JOIN signed_service_reservation AS ssr ON u.id = ssr.user_id WHERE concat(u.name,' ',u.surname) LIKE '%{search_field}%'"
        return self.query(query, returns=True)

    def get_signed_user_reservation_by_date(self, search_field):
        query = f"SELECT ssr.id, u.Id AS 'user_id',concat(u.name,' ',u.surname) AS 'fullname' ,u.first_cellphone AS cellphone,ssr.date_from,ssr.date_to FROM users AS u JOIN signed_service_reservation AS ssr ON u.id = ssr.user_id WHERE ssr.date_from LIKE '%{self.__set_date_str(search_field, no_apici=True)}%'"
        return self.query(query, returns=True)

    # region Stats
    def get_user_count(self):
        query = f"SELECT COUNT(*) AS 'count' FROM users"
        return self.query(query, returns=True)

    def get_user_count_gender(self, gender):
        query = f"SELECT COUNT(*) AS 'count' FROM users WHERE gender = '{self.__check_value(gender, str)}';"
        return self.query(query, returns=True)

    def get_user_by_birthdate(self, data_in: date, data_fi: date):
        query = f"SELECT COUNT(*) AS 'count' FROM users WHERE {self.__set_date_str(data_in)}" \
                f" > birthdate AND birthdate > {self.__set_date_str(data_fi)}"
        return self.query(query, returns=True)

    def get_top_3_items(self):
        query = f"SELECT i.title, i.author, i.isbn, COUNT(*) AS 'count' FROM movements AS m JOIN items AS i ON m.item_id = i.id GROUP BY i.isbn ORDER BY COUNT(*) DESC LIMIT 3"
        return self.query(query, returns=True)

    def get_top_3_genres(self):
        query = f"SELECT g.description, COUNT(*) AS 'count' FROM movements AS m JOIN items AS i ON m.item_id = i.id JOIN items_genres AS ig ON ig.item_id = i.id JOIN genres AS g ON g.id = ig.genre_id GROUP BY g.description ORDER BY COUNT(*) DESC LIMIT 3"
        return self.query(query, returns=True)

    # endregion

    def __set_date_str(self, item_date, no_apici=False) -> str:
        value = "null"
        if no_apici:
            if isinstance(item_date, datetime):
                value = f"{str(item_date.date())}"
            elif isinstance(item_date, date):
                value = f"{str(item_date)}"
            return value
        else:
            if isinstance(item_date, datetime):
                value = f"'{str(item_date.date())}'"
            elif isinstance(item_date, date):
                value = f"'{str(item_date)}'"
            return value

    def __check_value(self, item_value, type_value, return_this=None):
        value = item_value
        if not isinstance(item_value, type_value):
            # try conversion
            try:
                value = type_value(item_value)
                # if type_value is str:
                #     value.replace("'", "\x27")
            except:
                if return_this is None:
                    raise TypeError(f" {item_value} is not an instance of {type_value}")
                else:
                    return return_this
        return value

    def delete_unsigned_by_id(self, id):
        query = f"DELETE FROM unsigned_service_reservations WHERE id={id};"
        return self.query(query, returns=True)

    def delete_signed_by_id(self, id):
        query = f"DELETE FROM signed_service_reservation WHERE id ={id};"
        return self.query(query, returns=True)

    def count_signed(self, date_from):
        query = f"SELECT COUNT(*) AS 'count' FROM signed_service_reservation WHERE date_from LIKE '%{date_from}%'"
        return self.query(query, returns=True)

    def count_unsigned(self,date_from):
        query = f"SELECT COUNT(*) AS 'count' FROM unsigned_service_reservations WHERE date_from LIKE '%{date_from}%'"
        return self.query(query, returns=True)

