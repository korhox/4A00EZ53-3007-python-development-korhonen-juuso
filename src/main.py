from game import Game


"""
Main module boots up the game loop
"""


def main():
    """
        The main function creates the game object and boots up the game welcome screen
    """
    game = Game()
    game.welcome()


if __name__ == "__main__":
    main()
