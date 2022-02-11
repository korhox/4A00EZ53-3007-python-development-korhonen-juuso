import random

# define function


def generate_lotto_numbers(min=1, max=40, amount=7):
    if max - min + 1 < amount:
        raise Exception(
            f"The value between min and max must be at least the amount given ({amount})")
    # create set, which does not allow duplicates
    lotto = set()

    # while loop until set is 7 ints long (if added value is same as one added before, it will be not added/it is overriden)
    while len(lotto) < amount:
        # generate random number between min and max input variables
        lotto.add(random.randint(min, max))

    return lotto


# print generated set
try:
    # outputs seven random unique numbers between 1 - 40
    print(generate_lotto_numbers(1, 40, 7))

    # outputs seven random unique numbers between 1 - 40
    print(generate_lotto_numbers(min=1, max=40, amount=7))

    # outputs seven random unique numbers between 1 - 40
    print(generate_lotto_numbers())

    # outputs four (4) random unique numbers between 1 - 10
    print(generate_lotto_numbers(min=1, max=10, amount=4))

    # outputs six (6) random unique numbers between 1 - 6
    # (which basically is 1 2 3 4 5 6)
    print(generate_lotto_numbers(min=1, max=6, amount=6))

    # crashes the app, you cannot choose seven (7) unique numbers
    # between 1 - 6.
    print(generate_lotto_numbers(min=1, max=6, amount=7))
except Exception as e:
    print("An error happened: " + str(e))
