
import random

def noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan  määrä: "))
maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    tulos = noppaa(tahkot)
    print(f"Heitit: {tulos}")
    if tulos == maksimi:
        break


