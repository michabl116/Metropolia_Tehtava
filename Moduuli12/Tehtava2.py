import requests


kaupunki = input("Anna kaupunki nimi: ")


api_key = "444447bd93919a9d7240569892fafcfd"
url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()
    tiedot = response.json()

    if tiedot["cod"] == 200:
        saakuvaus = tiedot["weather"][0]["description"]
        lampotila_kelvin = tiedot["main"]["temp"]

        lampotila_celsius = lampotila_kelvin - 273.15

        print(f"Säätila: {saakuvaus.capitalize()}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")
    else:
        print("Paikkakuntaa ei löytynyt. Tarkista kirjoitusasu.")

except requests.exceptions.RequestException as e:
    print("Virhe haettaessa säätilaa:", e)