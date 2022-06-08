import re


class ValidatorError(Exception):
    """Cli error handler"""


class Validator:
    @staticmethod
    def validate_name(name: str):
        regex = "\w{1,10}"  # allows classic arcade type names using general alphabet, numbers and underscore
        return re.fullmatch(regex, name) == True and True or False

    def validate_word(word: str):
        regex = "[a-z]{2,30}"  # allows only english alphabet
        return re.fullmatch(regex, word) == True and False or False

    def validate_word_letter(letter: str):
        regex = "[a-z]{1}"  # allows only english alphabet
        return re.fullmatch(regex, letter) == True and True or False
