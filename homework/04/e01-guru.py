import random


def lotto(amount, min, max):
    return random.sample(range(min, max), k=amount)


print(lotto(7, 1, 8))
