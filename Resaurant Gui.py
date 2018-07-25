from tkinter import *
import random
import time;
root = Tk()
root.geometry("1600x1800+0+0")
root.title("Billing System")


text_Input = StringVar()
operator =  ""


Tops = Frame(root, width = 1600, height=50 , relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300 ,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Billing System",fg="steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',30,'bold'),text=localtime,fg="steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
    
def btnEqualDisplay():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x= random.randint(10908,500876)
    randomRef= str(x)
    rand.set(randomRef)

    CoF =float(fries.get())
    Cojamun =float(jamun.get())
    Comomo =float(momo.get())
    Coroll =float(roll.get())
    Cosand =float(sand.get())
    Corost =float(rost.get())
    CoDrinks =float(Drinks.get())
    

    A = CoF * 75.0
    B = Cojamun * 5.0
    C = Comomo * 50.0
    D = Coroll * 35.0
    E = Cosand * 20.0
    F = Corost * 250.0
    G = CoDrinks * 95.0

    CostofMeal="₹",str('%.2f' % (A + B + C + D + E + F + G))
    GST = ((A + B + C + D + E + F + G)* 0.025)
    TotalCost = (A + B + C + D + E + F + G)
    Ser_Charge=((A + B + C + D + E + F + G)/99)
    Servic ="₹",str('%.2f' % Ser_Charge)
    OverAllCost = "₹",str('%.2f' % (GST + GST + TotalCost + Ser_Charge))
    PaidTax="₹",str('%.2f' % GST)
    Service.set(Servic)
    Cost.set(CostofMeal)
    SGST.set(PaidTax)
    CGST.set(PaidTax)
    sTotal.set(CostofMeal)
    Total_Cost.set(OverAllCost)

def qExit():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    jamun.set("")
    momo.set("")
    roll.set("")
    sand.set("")
    rost.set("")
    Drinks.set("")
    Cost.set("")
    Service.set("")
    CGST.set("")
    SGST.set("")
    sTotal.set("")
    Total_Cost.set("")
    
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
btn7= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="7",bg="Gray",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="8",bg="Gray",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="9",bg="Gray",command=lambda: btnClick(9)).grid(row=2,column=2)
Addition= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
btn4= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="4",bg="Gray",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="5",bg="Gray",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="6",bg="Gray",command=lambda: btnClick(6)).grid(row=3,column=2)
Subtraction= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
btn1= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="1",bg="Gray",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="2",bg="Gray",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="3",bg="Gray",command=lambda: btnClick(3)).grid(row=4,column=2)
Equal= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEqualDisplay).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
btnc= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=0)
btn0= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="0",bg="Gray",command=lambda: btnClick(0)).grid(row=5,column=1)
Division= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=2)
Multiply= Button(f2,padx=16,pady=16,bd=8,fg="black" ,font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=5,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
rand = StringVar()
fries= StringVar()
jamun=StringVar()
momo=StringVar()
roll=StringVar()
sand=StringVar()
rost=StringVar()
lbl_reference = Label(f1,font=('arial',16,'bold'), text="Reference",bd=16,anchor='w')
lbl_reference.grid(row=0,column=0)
lbl_reference = Entry(f1,font=('arial',16,'bold'), textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_reference.grid(row=0,column=1)

lbl_fries = Label(f1,font=('arial',16,'bold'), text="Fries",bd=16,anchor='w')
lbl_fries.grid(row=1,column=0)
lbl_fries = Entry(f1,font=('arial',16,'bold'), textvariable=fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_fries.grid(row=1,column=1)

lbl_Gualbjamun = Label(f1,font=('arial',16,'bold'), text="Gulab Jamun",bd=16,anchor='w')
lbl_Gualbjamun.grid(row=2,column=0)
lbl_Gualbjamun = Entry(f1,font=('arial',16,'bold'), textvariable=jamun,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Gualbjamun.grid(row=2,column=1)

lbl_vegmomo = Label(f1,font=('arial',16,'bold'), text="Veg MoMo",bd=16,anchor='w')
lbl_vegmomo.grid(row=3,column=0)
lbl_vegmomo = Entry(f1,font=('arial',16,'bold'), textvariable=momo,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_vegmomo.grid(row=3,column=1)

lbl_Eggroll = Label(f1,font=('arial',16,'bold'), text="Egg Roll",bd=16,anchor='w')
lbl_Eggroll.grid(row=4,column=0)
lbl_Eggroll= Entry(f1,font=('arial',16,'bold'), textvariable=roll,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Eggroll.grid(row=4,column=1)

lbl_Sand = Label(f1,font=('arial',16,'bold'), text="Sandwich",bd=16,anchor='w')
lbl_Sand.grid(row=5,column=0)
lbl_Sand = Entry(f1,font=('arial',16,'bold'), textvariable=sand,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Sand.grid(row=5,column=1)

lbl_Rosted = Label(f1,font=('arial',16,'bold'), text="Rosted Chicken",bd=16,anchor='w')
lbl_Rosted.grid(row=6,column=0)
lbl_Rosted= Entry(f1,font=('arial',16,'bold'), textvariable=rost,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Rosted.grid(row=6,column=1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Drinks = StringVar()
Cost= StringVar()
Service=StringVar()
CGST=StringVar()
SGST=StringVar()
sTotal=StringVar()
Total_Cost=StringVar()
lbl_Drinks = Label(f1,font=('arial',16,'bold'), text="Drinks",bd=16,anchor='w')
lbl_Drinks.grid(row=0,column=2)
lbl_Drinks = Entry(f1,font=('arial',16,'bold'), textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Drinks.grid(row=0,column=3)

lbl_Cost = Label(f1,font=('arial',16,'bold'), text="Cost",bd=16,anchor='w')
lbl_Cost.grid(row=1,column=2)
lbl_Cost = Entry(f1,font=('arial',16,'bold'), textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Cost.grid(row=1,column=3)

lbl_Service = Label(f1,font=('arial',16,'bold'), text="Service",bd=16,anchor='w')
lbl_Service.grid(row=2,column=2)
lbl_Service = Entry(f1,font=('arial',16,'bold'), textvariable=Service,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Service.grid(row=2,column=3)

lbl_CGST = Label(f1,font=('arial',16,'bold'), text="CGST(2.5%)",bd=16,anchor='w')
lbl_CGST.grid(row=3,column=2)
lbl_CGST = Entry(f1,font=('arial',16,'bold'), textvariable=CGST,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_CGST.grid(row=3,column=3)

lbl_SGST = Label(f1,font=('arial',16,'bold'), text="SGST(2.5%)",bd=16,anchor='w')
lbl_SGST.grid(row=4,column=2)
lbl_SGST= Entry(f1,font=('arial',16,'bold'), textvariable=SGST,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_SGST.grid(row=4,column=3)

lbl_Total = Label(f1,font=('arial',16,'bold'), text="Sub Total",bd=16,anchor='w')
lbl_Total.grid(row=5,column=2)
lbl_Total = Entry(f1,font=('arial',16,'bold'), textvariable=sTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Total.grid(row=5,column=3)

lbl_Total_Cost = Label(f1,font=('arial',16,'bold'), text="Total Cost",bd=16,anchor='w')
lbl_Total_Cost.grid(row=6,column=2)
lbl_Total_Cost= Entry(f1,font=('arial',16,'bold'), textvariable=Total_Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Total_Cost.grid(row=6,column=3)
#************************************************************************************************************************************************************************

btnTotal= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Total",bg="Gray",command = Ref).grid(row=7,column=1)
btnReset= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Reset",bg="Blue",command = reset).grid(row=7,column=2)
btnqExit= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Exit",bg="Red",command = qExit).grid(row=7,column=3)
root.mainloop()
