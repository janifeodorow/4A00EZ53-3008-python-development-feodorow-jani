print("day")
päivä = int(input())
print("month")
kuukausi = int(input())

if (kuukausi == 5 and päivä == 1) or (kuukausi == 12 and päivä == 6):
    print("Nyt on vappu tai itsenäisyyspäivä!")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä.")
