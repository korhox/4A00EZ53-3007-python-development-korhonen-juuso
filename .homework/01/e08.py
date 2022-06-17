print("Give number 1")
number1 = int(input())

print("Give number 2")
number2 = int(input())

if number1 > number2:
    print("Number one is greather than number two")
elif number1 == number2:
    print("The numbers are same")
else:
    print("Number two is greather than number one")

if number1 != 0 and number2 != 0:
    division = number1 / number2
    print(division)
else:
    print("Division by zero is not possible, dumbass.")