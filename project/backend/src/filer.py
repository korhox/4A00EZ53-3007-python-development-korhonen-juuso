from pathlib import Path
import random
import os


class FilerError(Exception):
    """Filer error handler"""


class Filer:
    @staticmethod
    def read(file):
        f = open(file, "r")
        return(f.read())

    @staticmethod
    def get_all_words(level="default"):
        path = Path("storage/words/"+level+".txt")
        if path.exists() != True:
            os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
            f = open(path.absolute(), "w+")
            f.write("umbrella,computer,programmer,apple,mac")
            f.close()
        return self.read(path).split(",")

    @staticmethod
    def get_word(level="default"):
        words = self.get_all_words(level)
        r = random.randint(0, len(words)-1)
        return words[r]
