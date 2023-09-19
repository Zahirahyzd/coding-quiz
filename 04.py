#Program to display Parking fees of given car

i=int(input ('Day:'))
Plate = input('Car Plate:')
Hour = int(input('Hours:'))
Minute= int(input ('Minutes:'))

if (i>0 and i<6):
    Balance= Hour -3
    Total= 3 + Balance
    if (Total >= 20):
        Total = 20
    else:
        Total=Total
elif(i>=6 and i<=7):
    Balance = Hour -2
    Total= 5 + (Balance*2)
    if (Total>= 40):
        Total= 40
    else:
        Total=Total
else:
    print("days not exist")
    Total=print('invalid')

print(f'Net Amount Needed To Paid: RM{Total}')
    


