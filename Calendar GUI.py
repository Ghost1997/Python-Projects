from tkinter import *
import time
root = Tk()
root.geometry("1440x1620+0+0")
root.title("Find The Day Of Perticular Date Between 1600-2099 ")
text_Input = StringVar()
operator =  ""
Tops = Frame(root, width = 800, height=50 , relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, width = 800,height=700,relief=SUNKEN)
f1.pack(side= TOP)
localtime=time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('arial',30,'bold'),text="Find The Day Of Perticular Date Between 1600-2099",fg="steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
Date= StringVar()
Month= StringVar()
Year=StringVar()
Day=StringVar()
def qExit():
    root.destroy()

def reset():
    Date.set("")
    Month.set("")
    Year.set("")
    Day.set("")
def Ref():
    D =int(Date.get())
    M =int(Month.get())
    Y =int(Year.get())
    if M== 1 :
        M=0
    elif M == 2:
        M=3
    elif M== 3:
       M=3
    elif M== 4:
        M=6
    elif M == 5:
        M=1
    elif M== 6:
        M=4
    elif M== 7:
        M=6
    elif M== 8:
        M=2
    elif M== 9:
        M=5
    elif M== 10:
        M=0
    elif M== 11:
        M=3
    elif M== 12:
        M=5
    
    if 1600<=Y<=1699:
        a=Y-1600
        Y=6
    elif 1700<=Y<=1799:
        a=Y-1700
        Y=4
    elif 1800<=Y<=1899:
        a=Y-1800
        Y=2
    elif 1900<=Y<=1999:
        a=Y-1900
        Y=0
    elif 2000<=Y<=2099:
        a=Y-2000
        Y=6
    
    b=a//4
    c=a+b+D+M+Y
    if c%7==0:
        sDay= str ('Sunday')
    elif c%7==1:
        sDay= str ('Monday')
    elif c%7==2:
        sDay= str ('Tuesday')
    elif c%7==3:
        sDay= str ('Wednesday')
    elif c%7==4:
        sDay= str ('Thrusday')
    elif c%7==5:
        sDay=str ('Friday')
    elif c%7==6:
        sDay= str ('Saturday')
    Day.set(sDay)



lbl_Date = Label(f1,font=('arial',16,'bold'), text="Date",bd=16,anchor='w')
lbl_Date.grid(row=2,column=0)
lbl_Date = Entry(f1,font=('arial',16,'bold'), textvariable=Date,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Date.grid(row=2,column=1)

lbl_Month = Label(f1,font=('arial',16,'bold'), text="Month",bd=16,anchor='w')
lbl_Month.grid(row=3,column=0)
lbl_Month = Entry(f1,font=('arial',16,'bold'), textvariable=Month,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Month.grid(row=3,column=1)

lbl_Year = Label(f1,font=('arial',16,'bold'), text="Year",bd=16,anchor='w')
lbl_Year.grid(row=4,column=0)
lbl_Year = Entry(f1,font=('arial',16,'bold'), textvariable=Year,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Year.grid(row=4,column=1)

lbl_Day = Label(f1,font=('arial',16,'bold'), text="Day",bd=16,anchor='w')
lbl_Day.grid(row=6,column=0)
lbl_Day= Entry(f1,font=('arial',16,'bold'), textvariable=Day,bd=10,insertwidth=4,bg="powder blue",justify='right')
lbl_Day.grid(row=6,column=1)

btnTotal= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Equal",bg="yellow",command = Ref).grid(row=7,column=1)
btnReset= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Reset",bg="Blue",command = reset).grid(row=8,column=1)
btnqExit= Button(f1,padx=16,pady=8,bd=8,fg="black" ,font=('arial',20,'bold'),width=10,text="Exit",bg="Red",command = qExit).grid(row=9,column=1)

    


root.mainloop()
