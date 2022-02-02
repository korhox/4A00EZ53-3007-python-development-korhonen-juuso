def reverse(text, lowercase=False):
    if lowercase == True:
        text = text.lower()
    result = ""
    for i in text:
        result = i + result
    return result

print(reverse("Kalle", True))