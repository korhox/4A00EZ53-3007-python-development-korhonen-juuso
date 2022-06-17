print("Give a number of day:")
day = int(input())
print("Give a number of month:")
month = int(input())

if (day == 1 and month == 5):
    print("It's the first day of may (vappu)!")
if (day == 6 and month == 12):
    print("It's the Finnish independency day!")
else:
    print("It's not vappu or finnish independency day yet!")