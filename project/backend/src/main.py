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

            print(Cli.create_menu(["List words (or remove)", "Add words", "Reset wordlist", "Reset scores", "Exit admin menu"]))
            result = input(Cli.format_input("What would you like to do?", 5))
            if (result.isnumeric()):
                if int(result) == 1:
                    g.game_status = "admin_word_list"
                elif int(result) == 2:
                    g.game_status = "admin_words_add"
                elif int(result) == 3:
                    g.game_status = "admin_words_reset"
                elif int(result) == 4:
                    g.game_status = "admin_scores_reset"
                else:
                    g.game_status = "main"
                    break
            continue
        elif g.game_status == "admin_word_list":
            print(Cli.create_header("HANGMAN GAME", "Administration - Word list"))

            print(bold("#    Word"))
            words = f.get_all_words()
            for i in range(len(words)):
                print(green(i) + gray(")") + (" " * (4 - len(str(i)))) + words[i].capitalize())
            print("")
            result = input(Cli.format_input("Enter the number you would like to remove, or press Enter to return to the main menu", 0, "number/↩"))
            if result == "":
                g.game_status = "admin"
            else:
                if result.isnumeric():
                    g.game_status = "admin"
                    f.remove_word(int(result))
                    print(green("The word has been removed successfully!"))
                    input(Cli.format_input("Press enter to return admin menu"))
                else:
                    print(red("The input should be number or empty to return to admin menu"))
                    input(Cli.format_input("Press enter to retry"))
            continue
        elif g.game_status == "game":
            continue
        elif g.game_status == "admin_words_add":
            print(Cli.create_header("HANGMAN GAME", "Administration - Add word"))

            result = input(Cli.format_input("Enter word and press Enter or press Enter to return to admin menu", 0, "Word+Enter/Enter"))
            if (result == ""):
                g.game_status = "admin"
                continue
            else:
                if (validator.Validator.validate_word(result) != True):
                    print(red("The word must be 2-30 characters long and should contain only a-z letters."))
                    input(Cli.format_input("Press enter to retry"))
                    continue
                else:
                    f.add_word(result)
                    print(green("The word has been added successfully!"))
                    input(Cli.format_input("Press enter to return admin menu"))
                    g.game_status = "admin"
                    continue
            g.game_status = "main"
            continue
        elif g.game_status == "admin_words_reset":
            print(Cli.create_header("HANGMAN GAME", "Administration - Reset word list"))
            print("Are you sure you would like to reset the word list?\n")
            print(gray("New word list will be:"))
            print(gray(f.default_wordlist))
            result = input(Cli.format_input("Would you still like to reset the word list?", 1))
            if result == "y":
                f.reset_words()
                print(green("The word list has been reseted successfully!"))
                input(Cli.format_input("Press enter to return admin menu"))
                g.game_status = "admin"
                continue
            else:
                print(green("The word list was not reseted."))
                input(Cli.format_input("Press enter to return admin menu"))
                g.game_status = "admin"
                continue
        else:
            g.game_status = "main"
            break


def print_scoreboard():
    print(Cli.create_header("HANGMAN GAME", "Scoreboard"))

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
    print("The game is programmed as school project in basics of Python course. \nGitHub link: " + cyan("https://github.com/korhox/4A00EZ53-3007-python-development-korhonen-juuso/") + "\n")
    print("Hangman art by @ ChristianAuman \nCheck their HangMan!-project on Java: " + cyan("https://replit.com/@ChristianAuman/Hangman") + "\n")
    print("External (non-standard) Python libraries:")
    print("simple-chalk")


while(g.game_status != "exit"):
    Cli.clear()
    if g.game_status == "main":
        print(Cli.create_header("HANGMAN GAME", "Options"))
        print(Cli.create_menu(["New Game", "Administrate", "View Scoreboards", "Game Info", "Exit Game"]))
        result = input(Cli.format_input("What would you like to do?", 5))
        if (result.isnumeric()):
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
