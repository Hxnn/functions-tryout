# name of student: Enes Tekinbas
# number of student: 99040669
# purpose of program:
# function of program:
# structure of program:

toPay = int(float(input('Amount to pay: ')) * 100)  # hier laat ik weten hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100)  # hier laat ik weten hoeveel je heb betaald
change = paid - toPay  # hier wordt er een berekening gemaakt hoeveel wisselgeld je terug zal krijgen
coin500 = 0
coin300 = 0
coin200 = 0
coin100 = 0
coin50 = 0
coin20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0
if change > 0:  # als het wisselgeld groter is dan 5
    coinValue = 500  # hier krijgt de variable waarde 50

    while change > 0 and coinValue > 0:  # terwijl de waarde van change en waarde van coinValue groter is dan 0
        nrCoins = change // coinValue  # de wisselgeld delen door coinValue

        if nrCoins > 0:  # als de aantal munten groter is dan 0
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  #
            nrCoinsReturned = int(input('How many coins of ' + str(
                coinValue) + ' cents did you return? '))  # hier wordt er gevraag hoeveel munten van 50 je hebt terug gegeven en de aantal laat je dan weten bij de input
            change -= nrCoinsReturned * coinValue  # NRcoinsR * coinV - change = min de uitkomst == change bedrag

        # comment on code below:
        if coinValue == 500:
            coin500 = nrCoinsReturned
            coinValue = 300
        elif coinValue == 300:
            coin300 = nrCoinsReturned
            coinValue = 200
        elif coinValue == 200:
            coin200 = nrCoinsReturned
            coinValue = 100
        elif coinValue == 100:
            coin100 = nrCoinsReturned
            coinValue = 50
        elif coinValue == 50:
            coin50 = nrCoinsReturned
            coinValue = 20
        elif coinValue == 20:
            coin20 = nrCoinsReturned
            coinValue = 10
        elif coinValue == 10:
            coin10 = nrCoinsReturned
            coinValue = 5
        elif coinValue == 5:
            coin5 = nrCoinsReturned
            coinValue = 2
        elif coinValue == 2:
            coin2 = nrCoinsReturned
            coinValue = 1
            coin1 = nrCoinsReturned
        else:
            coinValue = 0

if change > 0:  # als de wisselgeld groter is dan 5 print de onderstaande zin zoniet dan print klaar
    print('Change not returned: ', str(change) + ' cents')
else:

    if coin500 > 0:
        print("je hebt", coin500, "coins van 5 € terug gekregen")
    if coin300 > 0:
        print("je hebt", coin300, "coins van 3 € terug gekregen")
    if coin200 > 0:
        print("je hebt", coin200, "coins van 2 € terug gekregen")
    if coin100 > 0:
        print("je hebt", coin100, "coins van 1 € terug gekregen")
    if coin50 > 0:
        print("je hebt", coin50, "coins van 50 cent terug gekregen")
    if coin20 > 0:
        print("je hebt", coin20, "coins van 20 cent terug gekregen")
    if coin10 > 0:
        print("je hebt", coin10, "coins van 10 cent terug gekregen")
    if coin5 > 0:
        print("je hebt", coin5, "coisn van 5 cent terug gekregen")
    if coin2 > 0:
        print("je hebt", coin2, "coins van 2 cent terug gekregen")
    if coin1 > 0:
        print("je hebt", coin1, "coins van 1 cent terug gekregen")

    print("done")
