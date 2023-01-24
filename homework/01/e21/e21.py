print("korkeus?")
korkeus = int( input() )
print("leveys?")
leveys = int( input() )
rivi = 0
while rivi < korkeus:
    sarake = 0
    while sarake < leveys:
        print("X", end='')
        sarake = sarake + 1
        
    print()
    rivi = rivi + 1
