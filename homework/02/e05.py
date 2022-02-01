
while(True):
    userinput = int(input("Please give a grade: "))
    if userinput < 0 or userinput > 5:
        print("Please give a integer between 1-5.")
        continue
    elif userinput == 0:
        print("Fail")
    elif userinput == 1 or userinput == 2:
        print("Weak")
    elif userinput == 3 or userinput == 4:
        print("Good")
    elif userinput == 5:
        print("Excellent")
    break