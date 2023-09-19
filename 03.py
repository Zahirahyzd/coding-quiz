#Program to calculate the electricity bill 
name = input('Name:')
unit= int(input ('Unit:'))
print (f"(Test Data :  {name} , {unit})" )
print(f"Customer Name: {name}")
print(f"Unit Consumed: {unit}")

if (unit <= 199):
    charge = 1.20
elif(unit >= 200 and unit < 400):
    charge = 1.50
elif(unit >= 400 and unit < 600 ):
    charge = 1.80
else:
    charge = 2.00
    

Total = charge * unit
print(f"Amount Charges @ RM{charge} per unit: RM{Total}" )

if (Total > 400):
    Bill = Total * (15/100)
    print(f"Surchage Amount :{Bill}")

Amount_Paid = Total + Bill
print(f'Net Amount Paid By the Customer: {Amount_Paid}')




    