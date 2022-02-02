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

# outputs True
print(is_palindrome("Saippuakauppias", lowercase=True)) 
# outputs False
print(is_palindrome("Saippuakauppias", lowercase=False)) 
# outputs False
print(is_palindrome("Kalle", lowercase=False)) 