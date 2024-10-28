class Hissi:
    nykyinen_kerros = 0
    def __init__(self, alimman, ylimman):
        self.alimman = alimman
        self.ylimman = ylimman

        #print(f"Hissi on kerro {Hissi.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kerros):
        while Hissi.nykyinen_kerros != kerros:
            if Hissi.nykyinen_kerros< kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if Hissi.nykyinen_kerros < self.ylimman:
            Hissi.nykyinen_kerros += 1
            print(f"Hissi on nyt kerro {Hissi.nykyinen_kerros}.")

    def kerros_alas(self):
        if Hissi.nykyinen_kerros > self.alimman:
            Hissi.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerro {Hissi.nykyinen_kerros}.")



class Talo:
    halytus=False
    def __init__(self, ali,yli,luku_mara):

        self.alima = ali
        self.ylima= yli
        self.luku_mara = luku_mara
        self.hissit = []


        for i in range(luku_mara):
            self.hissit.append(Hissi(self.alima,self.ylima))



    def aja_hissia(self,kerro_numero,hissit_kerro):
        if kerro_numero >=1 and kerro_numero<= self.luku_mara:
            self.hissit[kerro_numero-1].siirry_kerrokseen(hissit_kerro)

    def palohalytys(self):
        print()
        print()
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alima)






talo = Talo(1,10,4)
talo.aja_hissia(3,5)
talo.palohalytys()

