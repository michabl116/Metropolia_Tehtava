class Hissi:
    nykyinen_kerros = 0
    def __init__(self, ali, yli):
        self.alimman = ali
        self.ylimman = yli

        print(f"Hissi on kerro {Hissi.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kerros):
        while Hissi.nykyinen_kerros != kerros:
            if Hissi.nykyinen_kerros< kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if Hissi.nykyinen_kerros < self.ylimman:
            Hissi.nykyinen_kerros += 1
            print(f"Hissi on kerro {Hissi.nykyinen_kerros}.")


    def kerros_alas(self):
        if Hissi.nykyinen_kerros > self.alimman:
            Hissi.nykyinen_kerros -= 1
            print(f"Hissi onkerro {Hissi.nykyinen_kerros}.")



hissi = Hissi(0, 5)
hissi.siirry_kerrokseen(4)