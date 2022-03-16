import re


def is_name(name):
    return True if (re.search(r'^[^\W\d_]+(?:-[^\W\d_]+)*[.-]?$', name)) else False
