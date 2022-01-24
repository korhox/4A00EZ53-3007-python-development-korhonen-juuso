luku = 0
pienin = -1
while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )

    ## tää ei toimi jostakin syystä oikein, aivot sulaa
    if pienin > luku or pienin == -1:
        pienin = luku

if pienin != -1:
    print("Pienin antamasi luku oli " + str(pienin))
else:
    print("Et antanut lukuja.")