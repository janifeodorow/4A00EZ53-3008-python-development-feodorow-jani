# kolmas rivi generoi random numeron 0-5 välistä.

############################################

import random

salainen_luku = random.randint(0, 10)
kayttajan_syote = -1

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (0 - 10)")
    kayttajan_syote = int( input() )

print("oikein!")

##############################################

import random

salainen_luku = random.randint(0, 5)
kayttajan_syote = -1
arvauksia = 0

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (0 - 5)")
    kayttajan_syote = int( input() )
    arvauksia += 1

print("oikein!")
print("Arvauksia tehty: ", arvauksia)
