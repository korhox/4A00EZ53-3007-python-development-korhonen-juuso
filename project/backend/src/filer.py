from pathlib import Path
import random
import validator
import os


def read(file):
    f = open(file, "r")
    return(f.read())


def get_all_words():
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
        f = open(path.absolute(), "w+")
        f.write(default_wordlist)
        f.close()
    return Filer.read(path).split(",")


def save_wordlist(wordlist: list = default_wordlist.split(",")):
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
    f = open(path.absolute(), "w+")
    f.write(",".join(wordlist))
    f.close()
    return True


def reset_words():
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
    f = open(path.absolute(), "w+")
    f.write(Filer.default_wordlist)
    f.close()
    return True


def add_word(word):
    if validator.Validator.validate_word(word) == True:
        words = Filer.get_all_words()
        words.append(word)
        Filer.save_wordlist(words)
    else:
        raise "Word did not pass the validation, please use only 2-30 a-z letters"


def remove_word(index):
    words = Filer.get_all_words()
    words.pop(index)
    Filer.save_wordlist(words)
    return True


def word_exists(word):
    words = Filer.get_all_words()
    if word in words:
        return True
    else:
        return False


def get_word():
    words = Filer.get_all_words()
    r = random.randint(0, len(words)-1)
    return words[r]
