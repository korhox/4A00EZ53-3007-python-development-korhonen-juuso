luku = 0
pienin = -1

while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )

    if pienin > luku and luku >= 0 or pienin == -1:
        pienin = luku

if pienin != -1:
    print("Pienin antamasi luku oli " + str(pienin))
else:
    print("Et antanut lukuja.")