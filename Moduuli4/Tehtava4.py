import  random
arpa_luku= int(input("Arpa luku 1 - 10: "))
num_ramdon = random.randint(1,10)

while arpa_luku < num_ramdon:
    print("Liian pieni arvaus")
    arpa_luku = int(input("Arpa luku 1 - 10: "))

else:
    print("Liian suuri arvaus")
    arpa_luku = int(input("Arpa luku 1 - 10: "))

if arpa_luku == num_ramdon:
        print("Oikein")



