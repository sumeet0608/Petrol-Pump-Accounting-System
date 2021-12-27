from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3

class metreSR(Toplevel):
    def __init__(self,username):
        Toplevel.__init__(self)
        self.title("Metre Scale Reading")
        self.geometry("1366x700+0+0")
        self.username=username
        self.resizable(False,False)
        self.msr()
    
    def msr(self):
        Frame_login=Frame(self,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img=ImageTk.PhotoImage(file="bg.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        self.frame_input=Frame(self,bg='white')
        self.frame_input.place(x=210,y=130,height=515,width=915)
        
        self.nozzleNo=1
        
        conn=sqlite3.connect("login.db")
        curr=conn.cursor()
        curr.execute("SELECT * FROM loginDet WHERE username=?",(self.username,))
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
        
        self.label4=Label(self.frame_input,text="Start metre",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry2=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        
        self.label5=Label(self.frame_input,text="End metre",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry3=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.sales=StringVar()
        self.label6=Label(self.frame_input,text="Total Sale",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry4=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.sales,state='readonly')
        
        self.btn1=Button(self.frame_input,command=self.salesPerNoz,text="Calculate",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn2=Button(self.frame_input,command=self.nextNoz,text="Next Nozzle",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn3=Button(self.frame_input,command=self.totalSales,text="Compute Total Sales",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn4=Button(self.frame_input,command=self.goBack,text="Back",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn4.place(x=30,y=435)
        
        dropdown = OptionMenu(self.frame_input, self.variable, *fuels,command=self.display_selected)
        dropdown.pack(expand=True)
        dropdown.place(x=300,y=85,width=270,height=35)
        dropdown.config(bg='orangered',fg="white",font=("times new roman",15,"bold"))
        
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
        self.btn2.place(x=350,y=435)
        
    def salesPerNoz(self):
        if self.entry3.get()=='' or self.entry2.get()=='' or self.entry1.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        else:
            total_sale=(int(self.entry3.get())-int(self.entry2.get()))*int(self.entry1.get())
            self.sales.set(total_sale)
    
    def nextNoz(self):
        if self.entry3.get()=='' or self.entry2.get()=='' or self.entry1.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        elif self.nozzleNo<self.nozzles:
            self.nozzleNo+=1
            self.entry1.delete(0,END)
            self.entry2.delete(0,END)
            self.entry3.delete(0,END)
            self.entry4.delete(0,END)
            self.label1.config(text="Enter input for nozzle "+str(self.nozzleNo))
            self.label1.place(x=30,y=25)
            self.label2.place(x=30,y=85)
            self.label3.place(x=30,y=155)
            self.label4.place(x=30,y=225)
            self.label5.place(x=30,y=295)
            self.label6.place(x=30,y=365)
            self.entry1.place(x=300,y=155,width=270,height=35)
            self.entry2.place(x=300,y=225,width=270,height=35)
            self.entry3.place(x=300,y=295,width=270,height=35)
            self.entry4.place(x=300,y=365,width=270,height=35)
            self.btn1.place(x=630,y=365)
            self.btn2.place(x=350,y=435)
            
    def totalSales(self):
        pass
    
    def goBack(self):
        self.destroy()
        
