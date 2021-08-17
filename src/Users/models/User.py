from src.Users.models.Nationality import Nationality
from src.Users.models.UserType import UserType


class User:

    id = 0
    nationality = 0
    state_id = 0
    user_type = 0
    registration_date = '2000-01-01 00:00:00'
    name = ''
    surname = ''
    gender = ''
    birthplace = ''
    birthdate = '2000-01-01 00:00:00'
    city = ''
    address = ''
    postal_code = ''
    district = ''
    first_cellphone = ''
    telephone = ''
    email = ''
    fiscal_code = ''
    contect_mode = ''
    privacy_agreement = 0


    def __init__(self):
        pass

    def __init__(self, nationality, user_type
                 , registration_date, name, surname, gender, birthplace
                 , birthdate, city, address, postal_code, district
                 ,first_cellphone, telephone, email, fiscal_code, contect_mode
                 ,privacy_agreement):

        #self.id = id
        self.nationality = nationality
        self.user_type = user_type
        self.registration_date = registration_date
        self.name = name
        self.surname = surname
        self.gender = gender
        self.birthplace = birthplace
        self.birthdate = birthdate
        self.city = city
        self.address = address
        self.postal_code = postal_code
        self.district = district
        self.first_cellphone = first_cellphone
        self.telephone = telephone
        self.email = email
        self.fiscal_code = fiscal_code
        self.contect_mode = contect_mode
        self.privacy_agreement = privacy_agreement







