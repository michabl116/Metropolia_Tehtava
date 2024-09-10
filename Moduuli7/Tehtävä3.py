lentoa_semat= {"LBPL":"Dona Mitropoliya Air Base"}
lentoasema= input('kerro miten tehda S H L:' )
while lentoasema != "L" :
    if lentoasema=='S':
        asemacodi= input('Anna lentoasema codi "ICAO"')
        if asemacodi in lentoa_semat:
            print("Lentoasema on olemassa!")
            asemacodi = input('Anna lentoasema codi "ICAO"')
        if asemacodi == "s":
            print("kiitos Tervetuloa udele!")
            break
        asemanimi= input('Anna lentoasema codi "Nimi"')

        lentoa_semat.update({asemacodi:asemanimi})

    elif lentoasema=='H':
        palautus=input('Anna lentoasema codi "ICAO"')
        if palautus in lentoa_semat:
            print(lentoa_semat[palautus])
print("kitos")