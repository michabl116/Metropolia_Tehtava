import mysql.connector

def hae_lentokenta_tiedot(ident):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='1Peru20243#',
        autocommit=True

    )

    sql = f"SELECT type FROM airport WHERE iso_country='{ident}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    lentokentat = {}
    for rivi in tulos:
        tyyppi = rivi[0]
        if tyyppi in lentokentat:
            lentokentat[tyyppi] += 1
        else:
            lentokentat[tyyppi] = 1

    kursori.close()
    yhteys.close()

    return lentokentat

indet = input("Anna lentokentän maakoodi: ")
tulokset = hae_lentokenta_tiedot(indet)

print(f"Lentokenttien lukumäärät {indet}:")
for tyyppi, maara in tulokset.items():
    print(f"{tyyppi}: {maara}")




