from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("PetrolBunk.db")
curr=conn.cursor()
class metreSR(Toplevel):
    def __init__(self,username):
        Toplevel.__init__(self)
        self.title("Metre Scale Reading")
        self.geometry("1366x700+0+0")
        self.username=username
        self.resizable(False,False)
        self.salesTotal=0
        self.msr()
    
    def msr(self):
        Frame_login=Frame(self,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img=ImageTk.PhotoImage(file="D:\\VS PYTHON\\Cruder Accounter\\bg.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        self.frame_input=Frame(self,bg='white')
        self.frame_input.place(x=210,y=130,height=515,width=915)
        
        self.nozzleNo=1
        
        
        curr.execute("SELECT * FROM loginDetails WHERE username=?",(self.username,))
        row=curr.fetchone()
        row=list(row)
        self.nozzles=row[4]
        
        self.label1=Label(self.frame_input,text="Enter input for nozzle "+str(self.nozzleNo),font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.label1.place(x=30,y=25)
        
        self.label2=Label(self.frame_input,text="Type of Fuel",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.label2.place(x=30,y=85)
        fuels=["Petrol","Diesel","Power","Turbo Jet"]
        self.variable = StringVar()
        self.variable.set(fuels[0])
        self.label3=Label(self.frame_input,text=self.variable.get()+" price",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry1=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.lastend=StringVar()
        self.label4=Label(self.frame_input,text="Start metre",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry2=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.lastend)
        
        self.label5=Label(self.frame_input,text="End metre",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry3=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.sales=StringVar()
        self.label6=Label(self.frame_input,text="Total Sale",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry4=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.sales,state='readonly')
        
        self.lastSale=StringVar()
        self.label7=Label(self.frame_input,text="Total Sales for the day",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry5=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.lastSale,state='readonly')
        
        self.btn1=Button(self.frame_input,command=self.salesPerNoz,text="Calculate",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn2=Button(self.frame_input,command=self.nextNoz,text="Next Nozzle",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn3=Button(self.frame_input,command=self.totalSales,text="Compute Total Sales",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn4=Button(self.frame_input,command=self.goBack,text="Back",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn4.place(x=270,y=435)
        self.btn5=Button(self.frame_input,command=self.saveDetails,text="Save",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        
        self.dropdown = OptionMenu(self.frame_input, self.variable, *fuels,command=self.display_selected)
        self.dropdown.pack(expand=True)
        self.dropdown.place(x=300,y=85,width=270,height=35)
        self.dropdown.config(bg='orangered',fg="white",font=("times new roman",15,"bold"))
        
    def display_selected(self,choice):
        choice = self.variable.get()
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.label3.config(text=choice+" price")
        self.label3.place(x=30,y=155)
        self.entry1.place(x=300,y=155,width=270,height=35)
        
        self.label4.place(x=30,y=225)
        self.entry2.place(x=300,y=225,width=270,height=35)
        
        self.label5.place(x=30,y=295)
        self.entry3.place(x=300,y=295,width=270,height=35)
        
        self.label6.place(x=30,y=365)
        self.entry4.place(x=300,y=365,width=270,height=35)
        self.btn1.place(x=630,y=365)
        self.btn2.place(x=630,y=225)
        self.btn5.place(x=630,y=295)
        last_row=curr.execute("SELECT * FROM Nozzle"+str(self.nozzleNo)+" ORDER BY end_meter DESC LIMIT 1").fetchone()
        last_row=list(last_row)
        self.lastend.set(last_row[1])
        if(self.nozzleNo==self.nozzles):
                self.btn2.place_forget()
                self.btn3.place(x=630,y=225)
        
    def salesPerNoz(self):
        if self.entry3.get()=='' or self.entry2.get()=='' or self.entry1.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        else:
            total_sale=(int(self.entry3.get())-int(self.entry2.get()))*int(self.entry1.get())
            self.sales.set(total_sale)
            self.salesTotal+=total_sale
    
    def nextNoz(self):
        if self.entry3.get()=='' or self.entry2.get()=='' or self.entry1.get()=='' or self.entry4.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        elif self.nozzleNo<self.nozzles:
            self.nozzleNo+=1
            self.entry1.delete(0,END)
            self.entry2.delete(0,END)
            self.entry3.delete(0,END)
            self.entry4.config(state='normal')
            self.entry4.delete(0,END)
            self.entry4.config(state='readonly')
            self.label1.config(text="Enter input for nozzle "+str(self.nozzleNo))
            self.label1.place(x=30,y=25)
            self.label2.place(x=30,y=85)
            self.label3.place_forget()
            self.label4.place_forget()
            self.label5.place_forget()
            self.label6.place_forget()
            self.entry1.place_forget()
            self.entry2.place_forget()
            self.entry3.place_forget()
            self.entry4.place_forget()
            self.btn1.place_forget()
            self.btn2.place_forget()
            self.btn5.place_forget()
            
            
    def saveDetails(self):
        if self.entry3.get()=='' or self.entry2.get()=='' or self.entry1.get()=='' or self.entry4.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        else:
            start_meter=self.entry2.get();
            end_meter=self.entry3.get();
            total_sale=self.entry4.get();
            curr.execute("CREATE TABLE IF NOT EXISTS Nozzle"+str(self.nozzleNo)+" (start_meter INTEGER,end_meter INTEGER,total_sale INTEGER)")
            curr.execute("INSERT INTO Nozzle"+str(self.nozzleNo)+" values(?,?,?)",(start_meter,end_meter,total_sale))
            conn.commit()
            
    def totalSales(self):
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()
        self.label5.place_forget()
        self.label6.place_forget()
        self.dropdown.place_forget()
        self.entry1.place_forget()
        self.entry2.place_forget()
        self.entry3.place_forget()
        self.entry4.place_forget()
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn5.place_forget()
        self.btn3.place_forget()
        self.btn4.place(x=270,y=350)
        self.label7.place(x=80,y=200)
        self.entry5.place(x=390,y=200,width=270,height=35)
        self.lastSale.set(self.salesTotal)
        
    
    def goBack(self):
        self.destroy()
        