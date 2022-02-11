import random


def lotto():
    return [
        random.randint(1, 40),
        random.randint(1, 40),
        random.randint(1, 40),
        random.randint(1, 40),
        random.randint(1, 40),
        random.randint(1, 40),
        random.randint(1, 40)
    ]


print(lotto())
