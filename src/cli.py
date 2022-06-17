from simple_chalk import *
import os


def clear():
    """Clears the CLI"""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_header(title: str):
    """Creates beautiful header with ascii game name and title

    Args:
        title (string): the title to be added in to the header

    Returns:
        string: the header
    """
    header = green.bold(""",-_/,.             ,-,-,-.\n' |_|/ ,-. ,-. ,-. `,| | |   ,-. ,-.\n /| |  ,-| | | | |   | ; | . ,-| | |\n `' `' `-^ ' ' `-|   '   `-' `-^ ' '\n                ,|'  """)
    header += blue(title)
    header += green.bold("""\n                `\n\n""")
    return header


def create_menu(items: list):
    """creates menu from a list of titles

    Args:
        items (list): list of strings, each string is one menu item

    Returns:
        string: _description_
    """
    menu = ""
    i = 0
    while i < len(items):
        menu += white.bold(i+1) + gray(") ") + white(items[i]) + "\n"
        i += 1
    return menu


def format_input(title: str = "Press enter to return main menu", options: int = 0, subtitle: str = "↩"):
    """Formats input

    The default subtitle is different depending on amount of options. Subtitle parameter overrides this behavior.
        if options == 0: subtitle = "↩"
        if options == 1: subtitle = "y/n"
        if options == 3: subtitle = "1 / 2"
        if options == 4: subtitle = "1 / 2 / 3 / 4"
        if options == 8: subtitle = "1 / 2 / 3 / 4 / 5 / 6 / 8"
        if options >= 2: subtitle = "1 / 2 ..."

    Args:
        title (str, optional): The title to be shown in question Defaults to "Press enter to return main menu".
        options (int, optional): How many options you have. Defaults to 0.
        subtitle (str, optional): Overrides default subtitle which depends on amount of options. Defaults to "↩".

    Returns:
        _type_: _description_
    """
    question = "\n" + blue.bold("» ") + white.bold(title) + gray(" (")
    if subtitle != "↩":
        question += gray(subtitle)
    else:
        if options == 0:
            question += gray("↩")
        elif options == 1:
            question += gray("y/n")
        else:
            i = 0
            while i < options:
                i += 1
                question += gray(i)
                if i != options:
                    question += gray("/")
    question += gray(")") + blue.bold(": ")
    return question
