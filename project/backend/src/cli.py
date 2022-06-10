from simple_chalk import *
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_header(title: str, subtitle: str):
    header = green.bold(title)
    header += "\n"
    header += green(subtitle)
    header += "\n\n"
    return header


def create_menu(items: list):
    menu = ""
    i = 0
    while i < len(items):
        menu += white.bold(i+1) + gray(") ") + white(items[i]) + "\n"
        i += 1
    return menu


def format_input(title: str = "Press enter to return main menu", options: int = 0, subtitle: str = "↩"):
    if title == None:
        title
    if subtitle == None:
        subtitle = "Press enter to return main menu"
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
