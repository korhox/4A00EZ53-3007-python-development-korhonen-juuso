import filer
import cli
import scorer
from simple_chalk import *


def scoreboard():
    cli.clear()
    print(cli.create_header("Scoreboard"))

    print(bold("#    Word                  High Score       Scorer"))
    words = filer.get_all_words()
    for i, x in enumerate(words):
        highscore = (scorer.get_scores(x) or [["-", "-"]])[0]
        line = str(i+1) + "."
        line += " " * (4 - len(str(i)))
        line += x.capitalize()
        line += " " * (22 - len(x))
        line += highscore[1]
        line += " " * (17 - len(highscore[1]))
        line += highscore[0]
        print(line)
    result = input(cli.format_input("Give word number to see more scores or press Enter to return main menu", 0, "a number / ↩"))
    if result == "":
        return
    if result.isnumeric() and int(result) <= len(words):
        print_score(words[int(result)-1])


def print_score(word: str):
    cli.clear()
    scores = scorer.get_scores(word)
    print(cli.create_header("Scoreboard for word: " + word))
    print(bold("Scorer                  High Score"))
    for score in scores:
        line = score[0]
        line += " " * (24 - len(score[0]))
        line += score[1]
        print(line)
    input(cli.format_input())


def info():
    print(cli.create_header("Info"))
    print("The game is programmed as school project in basics of Python course. \nGitHub link: " + cyan("https://github.com/korhox/4A00EZ53-3007-python-development-korhonen-juuso/") + "\n")
    print("Hangman art by @ ChristianAuman \nCheck their HangMan!-project on Java: " + cyan("https://replit.com/@ChristianAuman/Hangman") + "\n")
    print("External (non-standard) Python libraries:")
    print("simple-chalk")


def new_game_info(game):
    print(cli.create_header("New Game"))
    print(bold("There is a life of the developer at stake!"))
    print("""You have to guess the word given to you without killing the developer!
You have a certain amount of guesses and each wrong guess brings the executer
closer to pull the lever of a trapdoor under the developer's legs.\n""")
    print(green("Word length: ") + green.bold(len(game.word)))
    print(green("Wrong guess : ") + green.bold(game.guesses))
    print()
    print("Good luck! And be careful!")


def welcome_text():
    print(cli.create_header("Welcome!"))
    print("Please adjust the screen / window to fit the following box + text above and below:")
    print("┏" + "━━" * 48 + "┓")
    for x in range(0, 21):
        print("┃" + 48 * "  " + "┃")
    print("┗" + "━━" * 48 + "┛")


def main_menu():
    print(cli.create_header("Options"))
    print(cli.create_menu(["New Game", "Administrate", "View Scoreboards", "Game Info", "Exit Game"]))


def main_admin():
    print(cli.create_header(red("Administration")))
    print(cli.create_menu(["List words (or remove)", "Add words", "Reset wordlist", "Reset scores", "Exit admin menu"]))
