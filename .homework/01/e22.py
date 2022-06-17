print("Give a number to iterate from: ", end="")
n = int(input())
print()

i = n
if (n > 0):
    while i >= 0:
        print(i)
        i = i - 1
else:
    while i <= 0:
        print(i)
        i = i + 1