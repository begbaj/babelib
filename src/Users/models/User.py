from src.Users.models.Nationality import Nationality
from src.Users.models.UserType import UserType


class User:

    id = 0
    nationality_id = 0
    state_id = 0
    user_type_id = 0
    username = 0
    registration_date = '2000-01-01 00:00:00'
    name = ''
    surname = ''
    gender = ''
    birthplace = ''
    birthdate = '2000-01-01 00:00:00'
    city = ''
    address = ''
    postal_code = ''
    distrit = ''
    first_cellphone = ''
    telephone = ''
    email = ''
    fiscal_code = ''
    contect_mode = ''
    privacy_agreement = 0

    Nationality_N = None
    Nationality_S = None
    userType = None

    def __init__(self):
        pass

    def __init__(self, nationality_id, state_id, user_type_id, username
                 , registration_date, name, surname, gender, birthplace
                 , birthdate, city, address, postal_code, distrit
                 ,first_cellphone, telephone, email, fiscal_code, contect_mode
                 ,privacy_agreement):

        #self.id = id
        self.nationality_id = nationality_id
        self.state_id = state_id
        self.user_type_id = user_type_id
        self.username = username
        self.registration_date = registration_date
        self.name = name
        self.surname = surname
        self.gender = gender
        self.birthplace = birthplace
        self.birthdate = birthdate
        self.city = city
        self.address = address
        self.postal_code = postal_code
        self.distrit = distrit
        self.first_cellphone = first_cellphone
        self.telephone = telephone
        self.email = email
        self.fiscal_code = fiscal_code
        self.contect_mode = contect_mode
        self.privacy_agreement = privacy_agreement







