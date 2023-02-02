def reverse(string, lowercase=False):
    result = ""
    length = len(string) - 1
    while length >= 0:
        result += string[length]
        length -= 1
    if lowercase:
        return result.lower()
    else:
        return result

print(reverse("Kalle")) # outputs "ellaK"
print(reverse("Kalle", lowercase=True)) # outputs "ellak"