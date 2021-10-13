getal = int(input("Van welk getal wilt u de tafel zien? "))
def Getal(Vraag):
    for i in range(1,11):
        print(getal, 'x', i, '=', getal*i)
    print(Vraag)

Getal('Dit is de tafel van: ' + str(getal))
