import re
import tld


def is_date(date):
    """Returns true, if the date follows ISO standard YYYY-MM-DD
    # Parameters
    date : `string`
        The date you would like to validate
    # Returns
    Result : `boolean`
        Whether the date is in the correct format or not
    """
    return re.match(r"[0-9]{4}-((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])", date) and True or False


def is_email(email):
    """Returns true, if the email is correctly formatted email address
    # Parameters
    email : `string`
        The email address you would like to validate
    # Returns
    Result : `boolean`
        Whether the email is correctly formatted or no
    """
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) and True or False


def is_personal_id(personal_id):
    """Returns true, if the personal id is correctly formatted finnish personal id
    # Parameters
    personal_id : `stgring`
        The personal id you would like to validate
    # Returns
    Result : `boolean`
        Whether the personal id is correctly formatted or no
    """
    return re.match(r"^(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])([5-9]\d\+|\d\d-|[01]\dA)\d{3}[\dABCDEFHJKLMNPRSTUVWXY]$", personal_id) and True or False

