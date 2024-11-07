class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0               #
    def kiihdyta(self, uusi_nopeus):
        if 0 <= uusi_nopeus <= self.huippunopeus:
            self.nopeus = uusi_nopeus
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = 0

    def kulje(self, tunnit=1):
        self.kuljettu_matka += self.nopeus * tunnit
class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankin_koko):
        super().__init__(rekisteri, huippunopeus)
sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
sahkoauto.kiihdyta(120)
polttomoottoriauto.kiihdyta(140)
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)
print(f"{sahkoauto.rekisteri}: Kuljettu matka = {sahkoauto.kuljettu_matka} km")
print(f"{polttomoottoriauto.rekisteri}: Kuljettu matka = {polttomoottoriauto.kuljettu_matka} km")