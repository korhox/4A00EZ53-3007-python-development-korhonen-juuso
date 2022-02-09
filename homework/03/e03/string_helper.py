import re


def is_name(name, ignore_case=False):
    if ignore_case == True:
        regex = r'^[ÄÖÅA-Z]{1}[äöåa-z]+ [ÄÖÅA-Z]{1}[äöåa-z]+$'
    else:
        regex = r'[äöåa-zÄÖÅA-Z]+ [äöåa-zÄÖÅA-Z]+'

    if re.search(regex, name):
        return True
    else:
        return False
