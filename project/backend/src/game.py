import time
import art
import cli
import filer
import printer
import admin
from simple_chalk import *


class Game:
    def __init__(self):
        self.word = ""
        self.guess = ""
        self.guesses = 0
        self.wrong_guesses = 0
        self.guessed_letters = []

    def welcome(self):
        cli.clear()
        printer.welcome_text()
        result = input(cli.format_input())
        self.mainMenu()

    def mainMenu(self):
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
                return
        self.mainMenu()

    def admin(self):
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
        cli.clear()

        self.word = filer.get_word()
        self.guess = "_" * len(self.word)
        self.guesses = round(len(self.word) / 2)
        self.wrong_guesses = 0
        self.guessed_letters = []

        printer.new_game_info(self)
        input(cli.format_input())
        self.gameLoop()
        return

    def gameLoop(self):
        while self.wrong_guesses < self.guesses and self.guess != self.word:
            cli.clear()
            print(cli.create_header("Ongoing game"))
            print(art.get_stage(self.wrong_guesses, self))
            response = input(cli.format_input("Enter your guess", 0, "a Letter / :quit"))
            if response != ":quit":
                if len(response) != 1:
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
