import timer
import filer
import game
from cli import *
from simple_chalk import *

t = timer.Timer()
f = filer.Filer()
g = game.Game()
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
    elif g.game_status == "info":
        print(Cli.create_header("HANGMAN GAME", "Info"))
        print("The game is programmed as school project in basics of Python course. \nGitHub link: " + cyan("https://github.com/korhox/4A00EZ53-3007-python-development-korhonen-juuso/"))
        result = input(Cli.format_input("Return to main menu?", 0))
        if result == "y":
            g.game_status = "main"
        else:
            continue
