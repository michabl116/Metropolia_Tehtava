vuosi_aika= ("kevät", "kesä", "syksy", "talvi")
luku = int(input("Anna kuukauden numeron:"))
if luku >=1 and luku <=3:
    print(vuosi_aika[0])
elif luku >=4 and luku <=6:
    print(vuosi_aika[1])
elif luku >=7 and luku <=9:
    print(vuosi_aika[2])
elif luku >=10 and luku <=12:
    print(vuosi_aika[3])