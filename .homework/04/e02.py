import random

# define function


def generate_lotto_numbers(min, max):
    if max - min + 1 < 7:
        raise Exception("The value between min and max must be at least 7")
    # create set, which does not allow duplicates
    lotto = set()

    # while loop until set is 7 ints long (if added value is same as one added before, it will be not added/it is overriden)
    while len(lotto) < 7:
        # generate random number between min and max input variables
        lotto.add(random.randint(min, max))

    return lotto


# print generated set
try:
    print(generate_lotto_numbers(1, 100))
except Exception as e:
    print("An error happened: " + str(e))
