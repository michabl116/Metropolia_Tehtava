from reprlib import aRepr
from stringprep import in_table_c8

kannan=int(input("Anna kannan:"))
korkeuden = int(input("Anna korkeuden:"))
piiri= ((kannan*2)+(korkeuden*2))
Pinta_ala = kannan*korkeuden
print(F"Piiri:  { piiri} cm ")
print(F"Pinta ala: {Pinta_ala} cm2")
