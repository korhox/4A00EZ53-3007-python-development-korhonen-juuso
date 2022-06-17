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
    user_lotto = {1, 2, 3, 4, 5, 6, 7}

    highscore = 1
    weeks = 0

    while(True):
        inters = len(user_lotto.intersection(generate_lotto_numbers(1, 40, 7)))
        weeks = weeks + 1
        if inters > highscore:
            s = weeks > 1 and "s" or ""
            print(
                f"You got {highscore} correct! New highscore!",
                f"It took {weeks} week{s}.",
                sep="\n",
                end="\n\n"
            )
            highscore = highscore + 1
        if highscore == 7:
            print("Completed!")
            break


except Exception as e:
    print("An error happened: " + str(e))
