import re


def is_name(name):
    if (re.search(r'^[ÄÖÅA-Z]{1}[äöåa-z]+ [ÄÖÅA-Z]{1}[äöåa-z]+$', name)):
        return True
    else:
        return False
