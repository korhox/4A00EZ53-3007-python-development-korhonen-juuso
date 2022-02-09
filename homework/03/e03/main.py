from string_helper import is_name

while(True):
    name = input("Please enter your full name: ")
    if(is_name(name, ignore_case=True)):
        print(f"Hello, {name}!")
        break
    else:
        print("Please give a valid name.")
        continue
