
luku = int(input("Anna luku:"))
while True:
    print(f"{luku}")
    luku = int(input("Anna luku: "))
    num = luku
    if luku == "":

        if num < min:
            min = luku
            if luku > max:
                max = luku
                print(f"Pienin luku: {min}")
                print(f"Suurin luku: {max}")



