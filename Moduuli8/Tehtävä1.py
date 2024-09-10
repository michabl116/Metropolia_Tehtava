import mysql.connector

def hae_lentokenta_tiedot(ident):
    sql=f"SELECT name, municipality From airport where ident='{ident}' "

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)
    return


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1Peru20243#',
         autocommit=True
         )


indet=input("Anna lento kenta kodi:")
hae_lentokenta_tiedot(indet)








