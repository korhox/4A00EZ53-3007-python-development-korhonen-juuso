def get_int(message, min, max):
    while (True):
        x = int(input(message + ": "))
        if x < min or x > max:
            print(f"Please give an integer between {min} and {max}")
            continue
        else:
            return x
            break

min = 0
max = 120
message = "give age"
value = get_int(message, min, max)