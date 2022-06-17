import time
import filer
import os
from simple_chalk import *
from pathlib import Path

"""Module for recording scores"""


def get_scores(word: str):
    """Gets all scores for a word

    Args:
        word (str): The word, which of scores will be checked for

    Raises:
        Exception: Describing the error

    Returns:
        string: scores for a word
    """
    if filer.word_exists(word) != True:
        raise Exception("Word does not exist")
        return False
    else:
        path = Path("storage/scores/" + word + ".txt")
        scores = filer.read(path)
        if scores == "":
            return []
        scores = scores.split("\n")
        for i in range(len(scores)):
            scores[i] = scores[i].split(":")
        return scores


def reset():
    """Resets all the scores by ereasing the files"""
    words = filer.get_all_words()
    for word in words:
        try:
            path = Path("storage/scores/" + word + ".txt")
            file = open(path.absolute(), "w")
            file.close()
        except:
            continue


def save(name: str, word: str, score: float):
    """Saves a given score for a word with name given

    Args:
        name (str): The scorer
        word (str): The word
        score (float): The score
    """
    path = Path("storage/scores/" + word + ".txt")
    if path.exists() != True:
        os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
    scores = get_scores(word)
    scores.append([name, str(score)])
    scores.sort(key=__sortsecond)
    file = open(path.absolute(), "w")
    file.write("\n".join([":".join(x) for x in scores[:3]]))
    file.close()


def __sortsecond(val: list):
    return float(val[1])
