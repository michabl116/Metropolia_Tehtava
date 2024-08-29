
luku = input("Anna luku:")
while True:
    print(luku)
    luku = input("Anna luku: ")
    if luku == " ":

        num = int(luku)
        if num < min:
            min = luku
        if luku > max:
            max = luku
            print(f"Pienin luku: {min}")
            print(f"Suurin luku: {max}")



