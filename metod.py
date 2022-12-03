import random
import math

sorozat = [-3, 5, 11, -2, 4]
oszto = 0

def nov():
    sorozat[0] += int(random.random()*7+5)
    print(sorozat[0])
def kiir(sep):
    osszefuz = ""
    cv = 0
    while cv < len(sorozat)-1:
        osszefuz += str(sorozat[cv])+sep
        cv +=1
    print(f"{osszefuz}{sorozat[-1]}")

def beker():
    szam = int(input("Adjon meg egy páratlan, hárommal osztható kétjegyűszámot!"))
    while (szam % 2 == 0 and szam % 3 != 0) and (szam < 10 and szam > -10):
        szam = int(input("Adjon meg egy páratlan, hárommal osztható számot!"))
    sorozat.append(szam)
    print(sorozat)

#Add meg az első kétjegyű szám helyét és  értékét a tömbből!
def ketjegy():
    cv = len(sorozat)-1
    elso_ketjegy = 0
    while cv >= 0:
        if sorozat[cv] >= 10 or sorozat[cv] <= -10:
            elso_ketjegy = sorozat[cv]
        cv -= 1
    print(elso_ketjegy)

#Számold meg, hogy hány prímszám van a tömbben! Ehhez készíts külön függvényt, ami eldönti, hogy a paraméterében kapott szám prímszám-e?

def prim_search(szam):
    cv = 1
    oszto = 0
    while cv <= szam:
        if szam % cv == 0:
            oszto += 1
        cv += 1
    print(szam,oszto)
    return oszto


def prim():
    i = 0
    prim_db = 0
    while i < len(sorozat):
        oszto = prim_search(math.fabs(sorozat[i]))
        if oszto > 2:
            i += 1
        else:
            prim_db += 1
            i +=1
    print(f"A sorozatban {prim_db}db prírm szám van")







