def print_me():
    print("Juuso")
print_me()


def return_me():
    return "Juuso"
print(return_me())


def output(text, times):
    print(text * times)
output("hello", 2)

def largest(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest
