from string_helper import is_name

name = input("Your name: ")

if is_name(name):
    print("Hello " + name + "!")
else:
    print("You did not give a proper name.")