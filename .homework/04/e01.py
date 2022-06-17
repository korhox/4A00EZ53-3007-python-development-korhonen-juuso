import random

# create set, which does not allow duplicates
lotto = set()

# while loop until set is 7 ints long (if added value is same as one added before, it will be not added/it is overriden)
while len(lotto) < 7:
    # generate random number between 1 - 40
    lotto.add(random.randint(1, 40))

# print generated set
print(lotto)
