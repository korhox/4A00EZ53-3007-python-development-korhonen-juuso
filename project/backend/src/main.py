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
    print(Cli.create_header("HANGMAN GAME", "Options"))
    print(Cli.create_menu(["New Game", "View Scoreboards", "Game Info", "Exit Game"]))
    result = input(Cli.format_input("What would you like to do?", 4))
    if result == 4:
        g.game_status = "exit"
