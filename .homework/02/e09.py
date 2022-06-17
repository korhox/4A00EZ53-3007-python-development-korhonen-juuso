def reverse(text):
    result = ""
    for i in text:
        result = i + result
    return result

print(reverse("Kalle"))