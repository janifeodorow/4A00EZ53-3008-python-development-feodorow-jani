print("luku 1:")
luku1 = int(input())
print("luku 2:")
luku2 = int(input())
print("minkä laskutoimituksen haluat tehdä? +, -, /, *")
operaattori = input()

if operaattori == "+":
    print(luku1 + luku2)
elif operaattori == "-":
    print(luku1 - luku2)
elif operaattori == "*":
    print(luku1 * luku2)
elif operaattori == "/":
    if luku2 != 0:
        print(luku1 / luku2)
    else:
        print("Annettu luku 2 ei voi olla 0")
else:
    print("Anna +, -, /, * syötteeksi")