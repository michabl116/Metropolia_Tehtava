print("HEMOGLOBIINIARVO")
print('"Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l."')
print('"Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l."')
Sukupuoli =(input('Anna sukupuoli "N" tai "M" :'))
arvo = int(input("Anna verenarvo :"))
if Sukupuoli == "N" :
    if arvo <= 116:
        print("hemoglobiiniarvo alhainen ")
    if arvo >= 176:
        print("hemoglobiiniarvo korkea")
    if 117 <= arvo <= 175:
        print("hemoglobiiniarvo normaali ")
if Sukupuoli == "M" :
    if arvo <= 133:
        print("hemoglobiiniarvo alhainen ")
    if arvo >= 196:
        print("hemoglobiiniarvo korkea")
    if 134 <= arvo <= 195:
        print("hemoglobiiniarvo normaali ")














