a = "hello"
b = 'hello'
c = """hello
              world"""
d = '''hello
              world'''

print(a)
print(b)
print(c)
print(d)

name = "Jani"
print("Hello " + name)

name = "Jani"
bmi = 25.112312
print(f"Hello {name}, you have bmi = {bmi:.2f}")

print(name[0], name[-1])

length = len(name)
print(f"First character of {name} is {name[0]} and last character of {name} is {name[length-1]}")

text = "jani,simo,aapo,juho,juhani"
name = "Jani"
print(name.upper()) #kaikki kirjaimet isolla
print(name.lower()) #kaikki kirjaimet pienellä
print(name.replace("J","M")) #vaihtaa kirjaimen J kirjaimeen M eli Mani
print(text.split(",")) #tekee merkkijonon jonka erotin on pilkku
print(name.startswith("J")) #ilmoittaa true tai false ekan kirjaimen
print(name.endswith("i")) # ilmoittaa true tai false vikan kirjaimen
print(name.find("n")) # etsii kirjaimen paikan

print("eka nimi: ")
str1 = input()
print("toka nimi: ")
str2 = input()
print(str1 == str2)

print("eka nimi: ")
str3 = input()
print("toka nimi: ")
str4 = input()
tulos = id(str3) is id(str4)
print(tulos)
