print("luku 1")
luku1 = int( input() )
print("luku 2")
luku2 = int( input() )
print("minkä laskutoimituksen haluat tehdä? +, -, /, *")
operaattori = input()

if operaattori == "+":
    print(luku1 + luku2)
elif operaattori == "-":
    print(luku1 - luku2)
elif operaattori == "/":
    print(luku1 / luku2)
elif operaattori == "*":
    print(luku1 * luku2)
else:
    print("Anna +, -, /, * laskutoimituksen syötteeksi")