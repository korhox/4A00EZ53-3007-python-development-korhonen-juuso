import time
import art
import cli
import filer
import printer
import admin
import validator
import math
import scorer
from timer import Timer
from simple_chalk import *


class Game:
    """The Game class contains the main functions of the game"""

    def __init__(self):
        """Initializes the object default variables"""

        self.word = ""
        self.guess = ""
        self.guesses = 0
        self.wrong_guesses = 0
        self.guessed_letters = []
        self.gameTimer = Timer()

    def welcome(self):
        """Prints the game welcome screen"""

        cli.clear()
        printer.welcome_text()
        result = input(cli.format_input())
        self.mainMenu()

    def mainMenu(self):
        """Prints the main menu and awaits the user selection"""

        cli.clear()
        printer.main_menu()
        result = input(cli.format_input("What would you like to do?", 5))
        if (result.isnumeric()):
            if int(result) == 1:
                self.newGame()
            elif int(result) == 2:
                self.admin()
            elif int(result) == 3:
                printer.scoreboard()
            elif int(result) == 4:
                printer.info()
            elif int(result) == 5:
                exit()
                return
        self.mainMenu()

    def admin(self):
        """Prints the admin menu and awaits the user selection"""

        cli.clear()
        printer.main_admin()
        result = input(cli.format_input("What would you like to do?", 5))
        if (result.isnumeric()):
            if int(result) == 1:
                admin.wordlist()
            elif int(result) == 2:
                admin.words_add()
            elif int(result) == 3:
                admin.words_reset()
            elif int(result) == 4:
                admin.scores_reset()
            else:
                self.mainMenu()
        self.admin()

    def newGame(self):
        """Starts up the game loop after the game variables are reseted"""

        cli.clear()

        self.word = filer.get_word()
        self.guess = "_" * len(self.word)
        self.guesses = round(len(self.word) / 2)
        self.wrong_guesses = 0
        self.guessed_letters = []
        self.gameTimer.reset()

        printer.new_game_info(self)
        input(cli.format_input())
        self.gameLoop()
        return

    def gameLoop(self):
        """The main game loop, awaits characters one by one and prints the correct ending"""

        self.gameTimer.start()
        while self.wrong_guesses < self.guesses and self.guess != self.word:
            cli.clear()
            print(cli.create_header("Ongoing game"))
            print(art.get_stage(math.ceil((self.wrong_guesses / self.guesses) * 7), self))
            response = input(cli.format_input("Enter your guess", 0, "a Letter / :quit"))
            if response != ":quit":
                if validator.validate_word_letter(response) != True:
                    continue
                if response in self.word:
                    for i, v in enumerate(self.word):
                        if response == v:
                            temp_guess = list(self.guess)
                            temp_guess[i] = v
                            self.guess = "".join(temp_guess)
                else:
                    if response not in self.guessed_letters:
                        self.guessed_letters.append(response)
                        self.wrong_guesses += 1
            else:
                response = input(cli.format_input("Are you sure you want to quit?", 1))
                if response == "y":
                    break
        if self.wrong_guesses >= self.guesses:
            self.lose()
        if self.guess == self.word:
            self.win()

    def lose(self):
        """Prints the "you lose" -screen"""

        cli.clear()
        print(cli.create_header(red.bold("You Lose")))
        print(art.get_stage(7, self))
        input(cli.format_input())

    def win(self):
        """Prints the "you win" -screen and asks for highscore name, if new highscore is achieved"""
        cli.clear()
        score = round(self.gameTimer.get(), 2)
        print(cli.create_header(green.bold("You Win!")))
        print(art.get_win())
        print()
        print("Score / time: " + str(score) + " seconds")
        scores = scorer.get_scores(self.word)
        if len(scores) >= 3 and float(scores[-1][1]) < score:
            input(cli.format_input())
            return
        name = None
        while(name == None):
            temp_name = input(cli.format_input("Enter your name for highscore or press Enter to skip", 0, "Name / Enter"))
            if temp_name == "":
                sure = input(cli.format_input("Are you sure you don't want to save your highscore?", 1))
                if sure == "y":
                    return
                else:
                    continue
            if validator.validate_name(temp_name) != True:
                print(red("The name should contain only alphabet and numbers. Please try again."))
                continue
            name = temp_name
        scorer.save(name, self.word, score)
        input(cli.format_input())
