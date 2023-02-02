def is_palindrome(string, lowercase=False):
    if lowercase:
        string = string.lower()
    return string == reverse(string, lowercase=False)

print(is_palindrome("Saippuakauppias", lowercase=True))
print(is_palindrome("Saippuakauppias", lowercase=False))
print(is_palindrome("Kalle", lowercase=False))