import math

leiviska_luku = float(input("Anna leiviskä:"))
naula_luku =float(input("Anna naula:"))
luoti_luku= float(input("Anna luoti:"))
Luoti= 13.3
Naula= 32 * Luoti
Leiviska=20* Naula
luku1 = leiviska_luku*Leiviska
luku2 = naula_luku*Naula
luku3 = luoti_luku*Luoti
kokosumma= luku1+luku2+luku3
sum= str(kokosumma)
print((sum[0:2])+" Kilogramma ja "+(sum[2:])+ " grammaa")
