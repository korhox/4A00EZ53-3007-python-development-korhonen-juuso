print("Please give the shape height: ", end="")
height = int(input())
print()

i = 0
while i < height:
    j = 0
    while j < i:
        print(" ", end="")
        j = j + 1
    print("X")
    i = i + 1