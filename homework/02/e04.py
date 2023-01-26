ja_bool = True
ja_int = 5
ja_float = 5.5

print(str(ja_bool), type(str(ja_bool)))
print(str(ja_int), type(str(ja_int)))
print(str(ja_float), type(str(ja_float)))

a = "hello"
b = "world"
print(a + b) # tulostaa helloworld yhteen

a = 5
b = 2
print(a + b) #laskee numerot yhteen

a = 5.5
b = int(a)
print(b) #poistaa desimaalit ja tulos on viisi

a = 5
b = float(a)
print(b) # tekee int tyypin muuttujasta float muuttujan ja lisää siihen desimaalit eli 5,0

a = 5
b = 2
c = a + b
print(c, type(c)) #tulostaa ---> 7 <class 'int'>

a = 5
b = 2.0
c = a + b
print(c, type(c)) #tulostaa---> 7.0 <class 'float'> (int+float---> float)

a = 5
b = 2
c = a / b
print(c, type(c)) #tulostaa : 2,5 <class 'int'>