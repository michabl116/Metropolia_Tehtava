from numpy.testing.print_coercion_tables import print_new_cast_table

lista=[]

luku= input("Anna luku: ")

while luku != "":
    print(luku)
    lista.append(int(luku))
    luku= input("Anna luku: ")

lista.sort(reverse=True)
print("luku on:",lista[:5])






















