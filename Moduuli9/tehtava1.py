class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0




rekt = Auto("ABC-123", 142)
print(f"rekisteritunnus :{rekt.rekisteritunnus}")
print(f"huippunopeus: {rekt.huippunopeus}")
print(f"tamanketkinen nopeus:{rekt.tamanhetkinen_nopeus}")
print(f"kuljettu_matka:{rekt.kuljettu_matka}")