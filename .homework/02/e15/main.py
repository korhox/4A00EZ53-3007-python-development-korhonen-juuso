def get_first_index(text, letter):
    i = 0
    while i < len(text):
        if text[i] == letter:
            return i
        i = i + 1