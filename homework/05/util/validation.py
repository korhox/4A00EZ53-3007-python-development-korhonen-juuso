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
    email : `email`
        The email address you would like to validate
    # Returns
    Result : `boolean`
        Whether the email is correctly formatted or no
    """
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) and True or False
