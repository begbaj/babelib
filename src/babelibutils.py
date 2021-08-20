import random
import string


class Generators:

    @staticmethod
    def string_digits(length):
        sample_string = string.ascii_uppercase+string.digits # define the specific string
        # define the condition for random string
        return ''.join((random.choice(sample_string)) for x in range(length))

    @staticmethod
    def string_digits_nor(length):
        letters = string.ascii_uppercase+string.digits  # define the specific string
        # define the condition for random.sample() method
        return ''.join((random.sample(letters, length)))

    @staticmethod
    def string_nor(length):
        letters = string.ascii_uppercase  # define the specific string
        # define the condition for random.sample() method
        return ''.join((random.sample(letters, length)))
