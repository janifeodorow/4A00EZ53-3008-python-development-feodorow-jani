def is_name(name):
    if len(name) < 5:
        return False

    first_last = name.split(" ")
    if len(first_last) != 2:
        return False
    if not first_last[0].isalpha() or not first_last[1].isalpha():
        return False
    if not first_last[0][0].isupper() or not first_last[1][0].isupper():
        return False
    return True