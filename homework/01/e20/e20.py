luku = 1
pienin = -1
while luku >= 0:
    print("Anna numero (lopetus negatiivisella luvulla)")
    luku = int( input() )
    if luku >= 0:
        if luku < pienin or pienin == -1:
            pienin = luku

if pienin != -1:
    print("Pienin antamasi luku oli ")
    print(pienin)
else:
    print("Et antanut lukuja.")