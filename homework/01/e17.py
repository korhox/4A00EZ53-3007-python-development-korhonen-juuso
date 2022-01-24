import random

randomNo = random.randint(0, 10)
lastInput = -1
inputs = 0

while lastInput != randomNo:
    print("Please give a secret number... (0 - 10)")
    lastInput = int( input() )
    inputs = inputs + 1

print("Success! You got it right at try #" + str(inputs) + "!")