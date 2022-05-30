import time
from simple_chalk import *


class GameError(Exception):
    """Game error handler"""


class Game:
    def __init__(self):
        self.game_status = "main"
