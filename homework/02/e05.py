    print("give me your grade between 0 and 5")
    grade = int(input())
    if grade == 0:
        print("Fail")
    elif 1 <= grade <= 2:
        print("Weak")
    elif 3 <= grade <= 4:
        print("Good")
    elif grade == 5:
        print("Excellent")
    else:
        print("invalid grade. try again")
