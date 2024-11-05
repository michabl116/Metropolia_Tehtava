import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))

    def kulje(self, tunnit=1):
        self.kuljettu_matka += self.nopeus * tunnit
    def __str__(self):
        return f"{self.rekisteritunnus:<8} | {self.huippunopeus:<11} | {self.nopeus:<6} | {self.kuljettu_matka:<10}"



autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:

        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        auto.kulje()


        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break


print(f"{'Rekisteri':<8} | {'Huippunopeus':<11} | {'Nopeus':<6} | {'Kuljettu matka'}")
print("-" * 40)
for auto in autot:
    print(auto)


