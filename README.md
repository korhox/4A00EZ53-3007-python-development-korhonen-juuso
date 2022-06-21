<img src="img/hangman-logo.png" height="100px">


This hangman game is compeletely programmed in Python, relying only one external extension, simple-chalk.


# Running the latest release
* On **Windows**, download `hangman.exe` from releases/tags and run it as you would run any executable file.
* On **Mac** & **Linux** download from releases/tags file named `hangman` and run it. If it won't open, use this command in terminal:
```
chmod +x ./hangman && ./hangman
```

**NOTE:** After launching the game, please resize the window to show the full view of game logo and contents to ensure best gaming experience.

# Running from source code

Download repository, unarchive it and run the app in the unarchived directory wit the following command:

```
python3 src/main.py
```

# Building

To create build manually, you need [Pyinstaller](https://pyinstaller.org/en/stable/). After you have installed the Pyinstaller (using Pip3: `pip3 install pyinstaller`), you can simply download the repository and run:
```
pyinstaller src/main.py --onefile
```

Run the command in the environment you want to create onefiler for. For example, on Windows for windows .exe and on mac/linux for binary files.

# Author

Juuso Korhonen


# Credits

The project is entirely made using Python as programming lanuage.

Hangman art by [@ChristianAuman](https://replit.com/@ChristianAuman/Hangman)

External (non-standard) Python libraries used:
* [simple-chalk](https://pypi.org/project/simple-chalk/)