import re


def is_name(name, ignore_case=False):
    """Checks if given name is valid name
    Parameters
    ----------
    name : `string`
        The name to be checked

    ignore_case : `boolean`
        Will case be ignored?
    Returns
    -------
    Result : `boolean`
        True, if given name is valid and False if name is invalid
    """
    if ignore_case == True:
        regex = r'^[ÄÖÅA-Z]{1}[äöåa-z]+ [ÄÖÅA-Z]{1}[äöåa-z]+$'
    else:
        regex = r'[äöåa-zÄÖÅA-Z]+ [äöåa-zÄÖÅA-Z]+'

    if re.search(regex, name):
        return True
    else:
        return False


def get_title(title, amount, char):
    """Generates ascii title
    Parameters
    ----------
    title : `string`
        The title to be beautified

    amount : `int`
        The width of the title

    char : `string`
        The charactcher to be used to generate the title borders
    Returns
    -------
    Title : `string`
        3 line string title

    """
    title_len = len(title)
    if title_len > amount:
        return "invalid values, title length is > graph length"
    else:
        spacing = int(round((amount - title_len) / 2))

        result = ""
        result = result + char * (amount + 4)
        result = result + "\n"

        result = result + char + " "
        result = result + " " * spacing
        result = result + title
        result = result + " " * spacing
        result = result + char

        result = result + "\n"
        result = result + char * (amount + 4)

        return result
