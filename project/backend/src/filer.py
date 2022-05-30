from pathlib import Path
import random
import os


class FilerError(Exception):
    """Filer error handler"""


class Filer:
    def __init__(self):
        self.last_file = None

    def read(self, file):
        f = open(file, "r")
        self.last_file = f.read()
        return(self.last_file)

    def get_all_words(self, level="default"):
        path = Path("storage/words/"+level+".txt")
        if path.exists() != True:
            os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
            f = open(path.absolute(), "w+")
            f.write("umbrella,computer,programmer,apple,mac")
            f.close()
        return self.read(path).split(",")

    def get_word(self, level="default"):
        words = self.get_all_words(level)
        r = random.randint(0, len(words)-1)
        return words[r]
