print("Enter the date to find the day")
x= int (input("Enter The Date:"))
y= int (input("Enter The Month:"))
if y == 1 :
    y=0
elif y == 2:
    y=3
elif y == 3:
    y=3
elif y == 4:
    y=6
elif y == 5:
    y=1
elif y == 6:
    y=4
elif y == 7:
    y=6
elif y == 8:
    y=2
elif y == 9:
    y=5
elif y == 10:
    y=0
elif y == 11:
    y=3
elif y == 12:
    y=5
z= int (input("Enter The Year:"))
if 1600<=z<=1699:
    a=z-1600
    z=6
elif 1700<=z<=1799:
    a=z-1700
    z=4
elif 1800<=z<=1899:
    a=z-1800
    z=2
elif 1900<=z<=1999:
    a=z-1900
    z=0
elif 2000<=z<=2099:
    a=z-2000
    z=6
b=a//4


c=a+b+x+y+z
if c%7==0:
    print("Sunday")
elif c%7==1:
    print("Monday")
elif c%7==2:
    print("Tuesday")
elif c%7==3:
    print("Wednesday")
elif c%7==4:
    print("Thrusday")
elif c%7==5:
    print("Friday")
elif c%7==6:
    print("Saturday")
m= int (input("Enter any key to Exit "))

