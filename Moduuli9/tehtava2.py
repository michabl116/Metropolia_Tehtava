class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyt(self, nop):
        if nop < 0:
            self.tamanhetkinen_nopeus = 0
            print("Hätäjarrutus ")
        elif nop < self.tamanhetkinen_nopeus:
            self.tamanhetkinen_nopeus = nop
            print("Auto hidastuu")
        elif nop > self.tamanhetkinen_nopeus and nop <= self.huippunopeus:
            self.tamanhetkinen_nopeus = nop
            print("Auto nopeuttaa")
        elif nop == self.tamanhetkinen_nopeus:
            print(f"Auto mantiene la velocidad a {nop} km/h")
        elif nop > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
            print("Auto saavutti huippunopeuden")
        return

    def kulje(self, tuntimaara):

        matka = self.tamanhetkinen_nopeus * tuntimaara
        self.kuljettu_matka += matka
        print(f"Auto on kulkenut yhteensä {self.kuljettu_matka} km")

rekt1 = Auto("ABC-123", 142)


rekt1.kiihdyt(30)
rekt1.kiihdyt(70)
rekt1.kiihdyt(50)

rekt1.kuljettu_matka = 2000
rekt1.kulje(1.5)
rekt1.kiihdyt(-200)

print(f"rekisteritunnus: {rekt1.rekisteritunnus}")
print(f"huippunopeus: {rekt1.huippunopeus}")
print(f"tamanhetkinen nopeus: {rekt1.tamanhetkinen_nopeus}")
print(f"kuljettu matka: {rekt1.kuljettu_matka}")


