kerraus_nimi=set()

nimi = input("Anna nimiä :")

while nimi != "":

    kerraus_nimi.add(nimi)
    nimi = input("Anna nimiä :")

    if nimi in kerraus_nimi:
        print("Nimi aiemmin syötetty!")
    elif nimi == "":
        for i in kerraus_nimi:
            print(i)


