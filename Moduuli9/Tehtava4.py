import random


class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit=1):
        self.kuljettu_matka += self.nopeus * tunnit

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteri = f"ABC-{i}"
    autot.append(Auto(rekisteri, huippunopeus))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje()
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteri':<8} | {'Huippunopeus':<11} | {'Nopeus':<6} | {'Kuljettu matka':<10}")
print("-" * 40)
for auto in autot:
    print(f"{auto.rekisteri:<8} | {auto.huippunopeus:<11} | {auto.nopeus:<6} | {auto.kuljettu_matka:<10}")
