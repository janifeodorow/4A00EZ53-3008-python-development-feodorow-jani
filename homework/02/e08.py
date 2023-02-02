#def get_int(text, min, max):
#    continue_loop = True

def get_int(message, min, max):
    while True:
        try:
            value = int(input(message + ": "))
            if min <= value <= max:
                return value
            else:
                print("Value must be " + str(min) + " - " + str(max))
        except ValueError:
            print("Value must be an integer.")


grade = get_int("Give grade", 4, 10)
print("You gave:", grade)
