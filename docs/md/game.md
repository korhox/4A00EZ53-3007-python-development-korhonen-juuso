Module game
===========

Classes
-------

`Game()`
:   The Game class contains the main functions of the game
    
    Initializes the object default variables

    ### Methods

    `admin(self)`
    :   Prints the admin menu and awaits the user selection

    `gameLoop(self)`
    :   The main game loop, awaits characters one by one and prints the correct ending

    `lose(self)`
    :   Prints the "you lose" -screen

    `mainMenu(self)`
    :   Prints the main menu and awaits the user selection

    `newGame(self)`
    :   Starts up the game loop after the game variables are reseted

    `welcome(self)`
    :   Prints the game welcome screen

    `win(self)`
    :   Prints the "you win" -screen and asks for highscore name, if new highscore is achieved