import timer
import filer
import game
import scorer
import validator
import cli
from simple_chalk import *


def print_admin():
    while(game.game_status != "main"):
        cli.clear()
        if game.game_status == "admin":
            print(cli.create_header("HANGMAN GAME", "Administration"))

            print(cli.create_menu(["List words (or remove)", "Add words", "Reset wordlist", "Reset scores", "Exit admin menu"]))
            result = input(cli.format_input("What would you like to do?", 5))
            if (result.isnumeric()):
                if int(result) == 1:
                    game.game_status = "admin_word_list"
                elif int(result) == 2:
                    game.game_status = "admin_words_add"
                elif int(result) == 3:
                    game.game_status = "admin_words_reset"
                elif int(result) == 4:
                    game.game_status = "admin_scores_reset"
                else:
                    game.game_status = "main"
                    break
            continue
        elif game.game_status == "admin_word_list":
            print(cli.create_header("HANGMAN GAME", "Administration - Word list"))

            print(bold("#    Word"))
            words = filer.get_all_words()
            for i in range(len(words)):
                print(green(i) + gray(")") + (" " * (4 - len(str(i)))) + words[i].capitalize())
            print("")
            result = input(cli.format_input("Enter the number you would like to remove, or press Enter to return to the main menu", 0, "number/↩"))
            if result == "":
                game.game_status = "admin"
            else:
                if result.isnumeric():
                    game.game_status = "admin"
                    filer.remove_word(int(result))
                    print(green("The word has been removed successfully!"))
                    input(cli.format_input("Press enter to return admin menu"))
                else:
                    print(red("The input should be number or empty to return to admin menu"))
                    input(cli.format_input("Press enter to retry"))
            continue
        elif game.game_status == "game":
            continue
        elif game.game_status == "admin_words_add":
            print(cli.create_header("HANGMAN GAME", "Administration - Add word"))

            result = input(cli.format_input("Enter word and press Enter or press Enter to return to admin menu", 0, "Word+Enter/Enter"))
            if (result == ""):
                game.game_status = "admin"
                continue
            else:
                if (validator.Validator.validate_word(result) != True):
                    print(red("The word must be 2-30 characters long and should contain only a-z letters."))
                    input(cli.format_input("Press enter to retry"))
                    continue
                else:
                    filer.add_word(result)
                    print(green("The word has been added successfully!"))
                    input(cli.format_input("Press enter to return admin menu"))
                    game.game_status = "admin"
                    continue
            game.game_status = "main"
            continue
        elif game.game_status == "admin_words_reset":
            print(cli.create_header("HANGMAN GAME", "Administration - Reset word list"))
            print("Are you sure you would like to reset the word list?\n")
            print(gray("New word list will be:"))
            print(gray(filer.default_wordlist))
            result = input(cli.format_input("Would you still like to reset the word list?", 1))
            if result == "y":
                filer.reset_words()
                print(green("The word list has been reseted successfully!"))
                input(cli.format_input("Press enter to return admin menu"))
                game.game_status = "admin"
                continue
            else:
                print(green("The word list was not reseted."))
                input(cli.format_input("Press enter to return admin menu"))
                game.game_status = "admin"
                continue
        else:
            game.game_status = "main"
            break


def print_scoreboard():
    print(cli.create_header("HANGMAN GAME", "Scoreboard"))

    print(bold("Word                  High Score       Scorer"))
    for x in filer.get_all_words():
        highscore = scorer.get_scores(x)[0]
        line = x.capitalize()
        line += " " * (22 - len(x))
        line += highscore[1]
        line += " " * (17 - len(highscore[1]))
        line += highscore[0]
        print(line)


def print_info():
    print(cli.create_header("HANGMAN GAME", "Info"))
    print("The game is programmed as school project in basics of Python course. \nGitHub link: " + cyan("https://github.com/korhox/4A00EZ53-3007-python-development-korhonen-juuso/") + "\n")
    print("Hangman art by @ ChristianAuman \nCheck their HangMan!-project on Java: " + cyan("https://replit.com/@ChristianAuman/Hangman") + "\n")
    print("External (non-standard) Python libraries:")
    print("simple-chalk")


while(game.game_status != "exit"):
    cli.clear()
    if game.game_status == "main":
        print(cli.create_header("HANGMAN GAME", "Options"))
        print(cli.create_menu(["New Game", "Administrate", "View Scoreboards", "Game Info", "Exit Game"]))
        result = input(cli.format_input("What would you like to do?", 5))
        if (result.isnumeric()):
            if int(result) == 1:
                game.game_status = "new"
            elif int(result) == 2:
                game.game_status = "admin"
            elif int(result) == 3:
                game.game_status = "scoreboard"
            elif int(result) == 4:
                game.game_status = "info"
            elif int(result) == 5:
                game.game_status = "exit"
        continue
    elif game.game_status == "admin":
        print_admin()
        continue
    elif game.game_status == "scoreboard":
        print_scoreboard()
        input(cli.format_input())
        game.game_status = "main"
        continue
    elif game.game_status == "info":
        print_info()
        input(cli.format_input())
        game.game_status = "main"
        continue
    elif game.game_status == "exit":
        exit()
