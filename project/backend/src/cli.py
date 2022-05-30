from simple_chalk import *
import os


class CliError(Exception):
    """Cli error handler"""


class Cli:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def create_header(title: str, subtitle: str):
        header = green.bold(title)
        header += "\n"
        header += green(subtitle)
        header += "\n"
        return header

    @staticmethod
    def create_menu(items: list):
        menu = ""
        i = 0
        while i < len(items):
            menu += white.bold(i+1) + gray(") ") + white(items[i]) + "\n"
            i += 1
        return menu

    @staticmethod
    def format_input(title: str, options: int):
        question = "\n" + blue.bold("» ") + white.bold(title) + gray(" (")
        i = 0
        while i < options:
            question += gray(i+1)
            if i != options:
                question += gray("/")
            i += 1
        question += gray(")") + blue.bold(": ")
        return question
