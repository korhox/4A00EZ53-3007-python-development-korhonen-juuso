from pathlib import Path
import random
import validator
import os

default_wordlist = "umbrella,computer,programmer,apple,mac,doorbell,paper,usb,speaker,mouse,printer,lamp,camera,webcam,remote,microphone,desk,stool,clock,bill,magnet,microsoft,facebook,discord,slack,game,steam,ubisoft,window,file,directory,desktop,trackpad,headpohones,keyboard"


def read(file: str):
    """Reads the file in given path

    Args:
        file (string): The path to the file to be read

    Returns:
        string: The file content, empty string on error
    """
    try:
        f = open(file, "r")
        return(f.read())
    except:
        return("")


def get_all_words():
    """Gets all words from words.txt

    Returns:
        string: All the words from words.txt
    """
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
        f = open(path.absolute(), "w+")
        f.write(default_wordlist)
        f.close()
    return read(path).split(",")


def save_wordlist(wordlist: list = default_wordlist.split(",")):
    """Saves the entire wordlist replacing the old one

    Args:
        wordlist (list, optional): _description_. Defaults to default_wordlist.split(",").
    """
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
    f = open(path.absolute(), "w+")
    f.write(",".join(wordlist))
    f.close()

    """Resets the word list to default"""


def reset_words():
    path = Path("storage/words.txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
    f = open(path.absolute(), "w+")
    f.write(default_wordlist)
    f.close()


def add_word(word: str):
    """Adds a word

    Args:
        word (string): Word to be added
    """
    if validator.validate_word(word) == True:
        words = get_all_words()
        words.append(word)
        save_wordlist(words)
    else:
        raise "Word did not pass the validation, please use only 2-30 a-z letters"


def remove_word(index: int):
    """Removes a word by its index number

    Args:
        index (int): An index of the word to be removed
    """
    words = get_all_words()
    words.pop(index)
    save_wordlist(words)


def word_exists(word: str):
    """Chec whether the word exists or not

    Args:
        word (str): a word to be checked

    Returns:
        bool: True when word exists, False when not
    """
    words = get_all_words()
    return word in words


def get_word():
    """Returns a random word from the word list

    Returns:
        str: Random word
    """
    words = get_all_words()
    r = random.randint(0, len(words)-1)
    return words[r]
