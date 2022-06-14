import time
import filer
import os
from simple_chalk import *
from pathlib import Path

score = 0


def add(points: int):
    score += points
    return True


def get_scores(word: str):
    if filer.word_exists(word) != True:
        raise ScorerError("Word does not exist")
        return False
    else:
        path = Path("storage/scores/" + word + ".txt")
        if path.exists() != True:
            os.makedirs(os.path.dirname(path.absolute()), exist_ok=True)
            f = open(path.absolute(), "w+")
            f.write("-:0;-:0;-:0;")
            f.close()
        scores = filer.read(path).split(";")
        i = 0
        while i < len(scores):
            scores[i] = scores[i].split(":")
            i += 1
        return scores
