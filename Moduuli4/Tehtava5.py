from ctypes import pythonapi

Tunnus = "python"
koodi ="rules"
käyttäjätunnuksen = input("Anna käyttäjätunnuksen:")
salasanan = input("Anna salasanan:")
luku = 0
while luku < 5:
    if Tunnus == käyttäjätunnuksen and salasanan == koodi:
        print("Tervetuloa!")
        break

    if käyttäjätunnuksen != Tunnus or salasanan != koodi:

        print("käyttäjätunnuksen tai salasanan  on vääri!  ")
        käyttäjätunnuksen = input("Anna käyttäjätunnuksen:")
        salasanan = input("Anna salasanan:")
        luku +=1
        if luku == 5:
            print("Pääsy evätty")


