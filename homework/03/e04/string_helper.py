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
