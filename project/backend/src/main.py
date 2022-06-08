import timer
import filer
import game
import scorer
import validator
from cli import *
from simple_chalk import *

t = timer.Timer()
f = filer.Filer()
g = game.Game()
s = scorer.Scorer()


def print_admin():
    while(g.game_status != "main"):
        Cli.clear()
        if g.game_status == "admin":
            print(Cli.create_header("HANGMAN GAME", "Administration"))
            print("")
            print(Cli.create_menu(["Add words", "List words (or remove)", "Reset wordlist", "Reset scores", "Exit admin menu"]))
            result = input(Cli.format_input("What would you like to do?", 5))
            if int(result) == 1:
                g.game_status = "admin_words_add"
            elif int(result) == 2:
                g.game_status = "admin_word_list"
            else:
                g.game_status = "main"
        elif g.game_status == "admin_words_add":
            print(Cli.create_header("HANGMAN GAME", "Administration - Add word"))
            print("")
            result = input(Cli.format_input("Enter word and press Enter or press Enter to return to admin menu", 0, "Word+Enter/Enter"))
            if (result == ""):
                g.game_status = "admin"
                continue
            else:
                if (validator.Validator.validate_word(result) != True):  # todo: returns always False for some reason
                    print(red("The word must be 2-30 characters long and should contain only a-z letters."))
                    input(Cli.format_input("Press enter to retry"))
                    continue
                else:
                    f.add_word(result)
                    print(red("The has been added successfully!"))
                    input(Cli.format_input("Press enter to retry"))
                    g.game_status = "admin"
                    continue
            g.game_status = "main"
            continue
        elif g.game_status == "admin_word_list":
            print(Cli.create_header("HANGMAN GAME", "Administration - Word list"))
            print("")
            print(bold("#    Word"))
            words = f.get_all_words()
            for i in range(len(words)):
                print(green(i) + gray(")") + (" " * (4 - len(str(i)))) + words[i].capitalize())
            print("")
            result = input(Cli.format_input("Enter the number you would like to remove, or press Enter to return to the main menu", 0, "number/↩"))
            if result == "":
                g.game_status = "main"
            else:
                if result.isnumeric():
                    None  # TODO:
                else:
                    continue
            continue
        else:
            g.game_status = "main"
            continue


def print_scoreboard():
    print(Cli.create_header("HANGMAN GAME", "Scoreboard"))
    print("")
    print(bold("Word                  High Score       Scorer"))
    for x in f.get_all_words():
        highscore = s.get_scores(x)[0]
        line = x.capitalize()
        line += " " * (22 - len(x))
        line += highscore[1]
        line += " " * (17 - len(highscore[1]))
        line += highscore[0]
        print(line)


def print_info():
    print(Cli.create_header("HANGMAN GAME", "Info"))
    print("The game is programmed as school project in basics of Python course. \nGitHub link: " + cyan("https://github.com/korhox/4A00EZ53-3007-python-development-korhonen-juuso/"))


while(g.game_status != "exit"):
    Cli.clear()
    if g.game_status == "main":
        print(Cli.create_header("HANGMAN GAME", "Options"))
        print(Cli.create_menu(["New Game", "Administrate", "View Scoreboards", "Game Info", "Exit Game"]))
        result = input(Cli.format_input("What would you like to do?", 5))
        if int(result) == 1:
            g.game_status = "new"
        elif int(result) == 2:
            g.game_status = "admin"
        elif int(result) == 3:
            g.game_status = "scoreboard"
        elif int(result) == 4:
            g.game_status = "info"
        elif int(result) == 5:
            g.game_status = "exit"
        continue
    elif g.game_status == "admin":
        print_admin()
        input(Cli.format_input())
        g.game_status = "admin"
        continue
    elif g.game_status == "scoreboard":
        print_scoreboard()
        input(Cli.format_input())
        g.game_status = "main"
        continue
    elif g.game_status == "info":
        print_info()
        input(Cli.format_input())
        g.game_status = "main"
        continue
    elif g.game_status == "exit":
        exit()
