luku = int(input("Anna kokona luku: "))
while luku <= 1:
    print(f"{luku} ei ole alkuluku.")
else:
    alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break
    if alkuluku:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")


