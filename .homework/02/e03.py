a = "hello"
b = 'hell\'o'
c = """hello
        world"""
d = '''hell'o
        world'''
e = "hello world"

print(a, b, c, d, sep="\n\n")

name = "Matti"
bmi = 25.11

print(f"Hello, {name}")
print(f"Hello, {name}.  Your BMI is {bmi:.1f}. Your name first and last letters are {name[0]} and {name[-1]}")

# Makes all text upper case
print(e.upper())

# Makes all text lower case
print(e.lower())

# Makes sure string is at least x chars long by adding leading zeros
print(("10").zfill(5))

# Splits string to table cells with provided separator
csv = "1;3;4;5;6;7;8;9;10"
for i in csv.split(sep=";"):
    print(i)

# Replaces string in a string
print(e.replace("world", "tamk"))

# Joins table items in a single string
cars = {"tesla", "porsche", "honda"}
print(", ".join(cars))

# Strips unnecessary spaces at the beginning and the ending of the string
car = "           tesla                                     "
print("At some day I want to own a " + car.strip() + " car.")

a = input("give a: ")
b = input("give b: ")
print(a == b and "true" or "false")

print("value " + a + " in memory address " + str(id(a)) )
print("value " + b + " in memory address " + str(id(b)) )