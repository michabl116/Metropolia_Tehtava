import requests

sivu = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(sivu)
    response.raise_for_status()

    tila = response.json()
    print(tila["value"])
except requests.exceptions.RequestException as e:
    print("Virhe haettaessa vitsiä:", e)