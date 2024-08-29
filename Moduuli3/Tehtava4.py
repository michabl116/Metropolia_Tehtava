lukuvuosi=int(input("Anna  vuosi:"))
if lukuvuosi % 4 == 0:
    if lukuvuosi % 100 != 0 or lukuvuosi % 400 == 0:
           print("lukuvuosi on karkausvuosi")
    else:
        print("lukuvuosi ei ole karkausvuosi")

