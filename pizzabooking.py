from tkinter import *
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title(" PIZZA SERVICE")

Tops=Frame(root, width=1600)
Tops.pack(side=TOP)
f1=Frame(root,width=1300,height=900)
f1.pack(side=LEFT)


localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text=" PIZZA SERVICE ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    name.get()
    number.get()

    if (Pep.get()==""):
        CoPep=0
    else:
        CoPep=float(Pep.get())

    if (Marg.get()==""):
        CoMarg=0
    else:
        CoMarg=float(Marg.get())

    if (Dch.get()==""):
        CoDch=0
    else:
        CoDch=float(Dch.get())

    if (Chic.get()==""):
        CoChic=0
    else:
        CoChic=float(Chic.get())

    if (Farm.get()==""):
        CoFarm=0
    else:
        CoFarm=float(Farm.get())

    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())
                
    CostofPep =CoPep * 350
    CostofDrinks=CoD * 50
    CostofMarg = CoMarg* 250
    CostofDch = CoDch * 250
    CostChic = CoChic* 350
    CostFarm=CoFarm * 200
    CostofMeal= "Rs", str('%.2f' % (CostofPep+CostofDrinks+CostofMarg+CostofDch+CostChic+CostFarm))
    PayTax=((CostofPep+CostofDrinks+CostofMarg+CostofDch+CostChic+CostFarm) * 0.025)
    SGST=((CostofPep+CostofDrinks+CostofMarg+CostofDch+CostChic+CostFarm) * 0.025)
    TotalCost=(CostofPep+CostofDrinks+CostofMarg+CostofDch+CostChic+CostFarm)
    Ser_Charge= ((CostofPep+CostofDrinks+CostofMarg+CostofDch+CostChic+CostFarm)*0.1)
    Service = "Rs", str ('%.2f' % Ser_Charge)
    OverAllCost ="Rs", str ('%.2f' % (PayTax+SGST+TotalCost+Ser_Charge))
    PaidTax= "Rs", str ('%.2f' % PayTax)
    SGST1="Rs", str ('%.2f' % SGST)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTax.set(SGST1)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    name.set("")
    number.set("")
    rand.set("") 
    Pep.set("")
    Marg.set("")
    Dch.set("")
    SubTax.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chic.set("")
    Farm.set("")


name=StringVar()
number=StringVar()
rand = StringVar()
Pep=StringVar()
Marg=StringVar()
Dch=StringVar()
SubTax=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chic=StringVar()
Farm=StringVar()

lblName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
lblName.grid(row=0, column=0)
txtName=Entry(f1, font=('arial',16,'bold'),textvariable=name,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtName.grid(row=0,column=1)

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Bill no ",bd=16,anchor="w")
lblReference.grid(row=1, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=1,column=1)

lblPep= Label(f1, font=('arial', 16, 'bold'),text="Pepperoni",bd=16,anchor="w")
lblPep.grid(row=2, column=0)
txtPep=Entry(f1, font=('arial',16,'bold'),textvariable=Pep,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPep.grid(row=2,column=1)

lblMarg= Label(f1, font=('arial', 16, 'bold'),text="Margerita",bd=16,anchor="w")
lblMarg.grid(row=3, column=0)
txtMarg=Entry(f1, font=('arial',16,'bold'),textvariable=Marg,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtMarg.grid(row=3,column=1)

lblDch= Label(f1, font=('arial', 16, 'bold'),text="Double Cheese",bd=16,anchor="w")
lblDch.grid(row=4, column=0)
txtDch=Entry(f1, font=('arial',16,'bold'),textvariable=Dch,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDch.grid(row=4,column=1)

lblChic= Label(f1, font=('arial', 16, 'bold'),text="Chicken",bd=16,anchor="w")
lblChic.grid(row=5, column=0)
txtChic=Entry(f1, font=('arial',16,'bold'),textvariable=Chic,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChic.grid(row=5,column=1)

lblFarm= Label(f1, font=('arial', 16, 'bold'),text="Farmhouse",bd=16,anchor="w")
lblFarm.grid(row=6, column=0)
txtFarm=Entry(f1, font=('arial',16,'bold'),textvariable=Farm,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFarm.grid(row=6,column=1)


lblNumber= Label(f1, font=('arial', 16, 'bold'),text="Number",bd=16,anchor="w")
lblNumber.grid(row=0, column=2)
txtNumber=Entry(f1, font=('arial',16,'bold'),textvariable=number,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNumber.grid(row=0,column=3)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=1, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=1,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=2, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=2,column=3)

lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge @10%",bd=16,anchor="w")
lblService.grid(row=3, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=3,column=3)

lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="CGST @2.5%",bd=16,anchor="w")
lblStateTax.grid(row=4, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=4,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="SGST @2.5%",bd=16,anchor="w")
lblSubTotal.grid(row=5, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=5,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=6, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=6,column=3)

lblMenu= Label(root, font=('arial', 20, 'bold'),text="MENU \n\nPepperoni RS.350 \nMargerita RS.250 \nDouble Cheese RS.250 \nChicken RS.350 \nFarmhouse RS.200 \nDrinks Rs.50",bd=16,anchor="e")
lblMenu.place(x=1100,y=300)


btnTotal=Button(f1,padx=16,pady=8,bd=16,font=('arial',16,'bold'),width=10,text="Order",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()
