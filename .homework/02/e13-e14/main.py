def calculate_sum(x, y):
    return x + y

def get_max(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest

def is_palindrome(text, lowercase=False):
    if lowercase == True:
        text = text.lower()
    result = ""
    for i in text:
        result = i + result
    if text == result:
        return True
    else:
        return False