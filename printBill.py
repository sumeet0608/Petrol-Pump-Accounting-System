from tkinter import *
from PIL import ImageTk

from random import randint

class PrintBill(Toplevel):
    def __init__(self,vehicleNO,amount,fuelPrice,fuelType):
        Toplevel.__init__(self)
        self.title("Bill")
        self.geometry("1366x700+0+0")
        self.resizable(False,False)
        self.vehicleNO=vehicleNO
        self.litres=float(amount)/float(fuelPrice)
        self.amount=amount
        self.fuelPrice=fuelPrice
        self.fuelType=fuelType
        self.print()
    
    def print(self):
        Frame_login=Frame(self,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img=ImageTk.PhotoImage(file="D:\\VS PYTHON\\Cruder Accounter\\bg.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        self.frame_input=Frame(self,bg='white')
        self.frame_input.place(x=500,y=130,height=350,width=390)
        
        scroll_y = Scrollbar(self.frame_input, orient=VERTICAL)
        self.txt = Text(self.frame_input, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)
        bill_number=randint(10000,100000)
        self.txt.delete('1.0',END)
        self.txt.insert(END,"\n\n\n           Welcome To Our Bunk\n")
        self.txt.insert(END,f"\nBill No. : {str(bill_number)}")
        self.txt.insert(END,f"\nFuel Type : {str(self.fuelType)}")
        self.txt.insert(END,"\n===========================================")
        self.txt.insert(END,"\nVehicle No.          Litre(s)         Total")
        self.txt.insert(END,"\n===========================================")
        self.txt.insert(END,f"\n{str(self.vehicleNO)}          {str(round(self.litres,2))}            {self.amount}")
        self.txt.insert(END,"\n===========================================")
        self.txt.insert(END,f"\n                       Total : ₹{self.amount}\n\n")
        self.txt.insert(END,"\n         Thank you for visiting...")
        
