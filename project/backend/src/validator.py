import re

"""General validations"""


def validate_name(name: str):
    """Validates names

    Args:
        name (str): The name

    Returns:
        bool: Whether validation succeeded or not
    """
    regex = "\w{2,10}"  # allows classic arcade type names using general alphabet, numbers and underscore
    return bool(re.fullmatch(regex, name))


def validate_word(word: str):
    """Validates words

    Args:
        name (str): The word

    Returns:
        bool: Whether validation succeeded or not
    """
    regex = "[a-z]{2,30}"  # allows only english alphabet
    return bool(re.fullmatch(regex, word))


def validate_word_letter(letter: str):
    """Validates word letters

    Args:
        name (str): The word letter

    Returns:
        bool: Whether validation succeeded or not
    """
    regex = "[a-z]{1}"  # allows only english alphabet
    return bool(e.fullmatch(regex, letter))
