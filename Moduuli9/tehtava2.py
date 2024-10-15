class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,tamanhetkinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyt(self, nop):
        if self.tamanhetkinen_nopeus > 0 or self.tamanhetkinen_nopeus <= 30:
            print("auto nopeuta")
        else:
            print("auto hidasta")
        return


rekt1 = Auto("ABC-123", 142,)
rekt1.kiihdyt(30)
#rek1.kiihdyt()
#rek3.kiihdyt()




print(f"rekisteritunnus :{rekt.rekisteritunnus}")
print(f"huippunopeus: {rekt.huippunopeus}")
print(f"tamanketkinen nopeus:{rekt.tamanhetkinen_nopeus}")
print(f"kuljettu_matka:{rekt.kuljettu_matka}")