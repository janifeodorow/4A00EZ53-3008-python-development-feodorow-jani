def reverse(string):
    result = ""
    length = len(string) - 1
    while length >= 0:
        result += string[length]
        length -= 1
    else:
        return result

print(reverse("Kalle"))
