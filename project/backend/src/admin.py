import filer
import cli
import validator
import scorer
from simple_chalk import *


def wordlist():
    cli.clear()
    print(cli.create_header(red("Administration - Word list")))

    print(bold("#    Word"))
    words = filer.get_all_words()
    for i in range(len(words)):
        print(green(i) + gray(")") + (" " * (4 - len(str(i)))) + words[i].capitalize())
    print("")
    result = input(cli.format_input("Enter the number you would like to remove, or press Enter to return to the main menu", 0, "number/↩"))
    if result == "":
        return
    if result.isnumeric():
        filer.remove_word(int(result))
        print(green("The word has been removed successfully!"))
        input(cli.format_input("Press enter to return admin menu"))
    else:
        print(red("The input should be number or empty to return to admin menu"))
        input(cli.format_input("Press enter to retry"))


def words_add():
    cli.clear()
    print(cli.create_header(red("Administration - Add word")))

    result = input(cli.format_input("Enter word and press Enter or press Enter to return to admin menu", 0, "Word+Enter/Enter"))
    if (result == ""):
        return
    else:
        if (validator.validate_word(result) != True):
            print(red("The word must be 2-30 characters long and should contain only a-z letters."))
            input(cli.format_input("Press enter to retry"))
            return
        else:
            filer.add_word(result)
            print(green("The word has been added successfully!"))
            input(cli.format_input("Press enter to return admin menu"))
            return


def words_reset():
    cli.clear()
    print(cli.create_header(red("Administration - Reset word list")))
    print("Are you sure you would like to reset the word list?\n")
    print(gray("New word list will be:"))
    print(gray(filer.default_wordlist))
    result = input(cli.format_input("Would you still like to reset the word list?", 1))
    if result == "y":
        filer.reset_words()
        print(green("The word list has been reseted successfully!"))
        input(cli.format_input("Press enter to return admin menu"))
        return
    else:
        print(green("The word list was not reseted."))
        input(cli.format_input("Press enter to return admin menu"))
        return


def scores_reset():
    cli.clear()
    print(cli.create_header(red("Administration - Reset highscores")))
    print("Are you sure you would like to reset the highscores?\n")
    result = input(cli.format_input("Would you still like to reset the highscores?", 1))
    if result == "y":
        scorer.reset()
        print(green("The highscores have been reseted successfully!"))
        input(cli.format_input("Press enter to return admin menu"))
        return
    else:
        print(green("The highscores were not reseted."))
        input(cli.format_input("Press enter to return admin menu"))
        return
