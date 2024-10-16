class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos

        # Tarkistetaan, ettei nopeus ylitä huippunopeutta
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        # Tarkistetaan, ettei nopeus mene alle nollan
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus


# Pääohjelma
rekt1 = Auto("ABC-123", 142)

# Kiihdytetään auton nopeutta
rekt1.kiihdyta(30)
rekt1.kiihdyta(70)
rekt1.kiihdyta(50)

# Tulostetaan nykyinen nopeus
print(f"Tämänhetkinen nopeus: {rekt1.tamanhetkinen_nopeus} km/h")

# Hätäjarrutus
rekt1.kiihdyta(-200)

# Tulostetaan uusi nopeus
print(f"Tämänhetkinen nopeus hätäjarrutuksen jälkeen: {rekt1.tamanhetkinen_nopeus} km/h")

