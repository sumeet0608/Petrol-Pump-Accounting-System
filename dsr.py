from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3

class Daily_sales_record(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Daily Sales Records")
        self.geometry("1366x700+0+0")
        self.resizable(False,False)
        self.menu()
    
    def menu(self):
        Frame_login=Frame(self,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img=ImageTk.PhotoImage(file="D:\\VS PYTHON\\Cruder Accounter\\bg.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        self.frame_input=Frame(self,bg='white')
        self.frame_input.place(x=210,y=130,height=515,width=915)
        
        self.label1=Label(self.frame_input,text="Daily Sales Records",font=("impact",24,"bold"),fg='black',bg='white')
        self.label1.place(x=200,y=25)
        
        self.label2=Label(self.frame_input,text="Enter Date(dd-mm-yy): ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.label2.place(x=30,y=85)
        self.entry1=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry1.place(x=300,y=85,width=270,height=35)
        
        self.label3=Label(self.frame_input,text="Enter Opening Stock : ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.label3.place(x=30,y=155)
        self.entry2=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry2.place(x=300,y=155,width=270,height=35)
        
        self.label4=Label(self.frame_input,text="Enter Sales By Meter :",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=225)
        self.entry3=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry3.place(x=300,y=225,width=270,height=35)
        
        self.label5=Label(self.frame_input,text="Enter Sales By Dip :",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=295)
        self.entry4=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry4.place(x=300,y=295,width=270,height=35)
        
        self.label6=Label(self.frame_input,text="Enter Tank Sale :",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=365)
        self.entry5=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry5.place(x=300,y=365,width=270,height=35)
        
        self.label7=Label(self.frame_input,text="Calculated Variance :",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=445)
        self.variation=StringVar()
        self.entry6=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',state='disabled',textvariable=self.variation)
        self.entry6.place(x=300,y=445,width=270,height=35)


        self.btn1=Button(self.frame_input,command=self.variationCalc,text="Calculate_Varition ",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=2).place(x=630,y=160)
        
        self.btn3=Button(self.frame_input,command=self.Savetodb,text="Save",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=2)
        self.btn3.place(x=630,y=270)
        
        self.btn2=Button(self.frame_input,command=self.goBack,text="Back",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=2)
        self.btn2.place(x=630,y=380)
        
        
   
    
    def goBack(self):
        self.destroy()
    
    def variationCalc(self):
        if self.entry3.get()=='' or self.entry5.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        else:
            metersale=self.entry3.get()
            tanksale=self.entry5.get()
            variation=float(metersale)-float(tanksale)
            self.variation.set(variation)
    
    def Savetodb(self):
        
        if self.entry1.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="" or self.entry5.get()=="" or self.entry6.get()=="":

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)


        else:

            conn=sqlite3.connect("PetrolBunk.db")

            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS DSR(Date text, opening_stock INTEGER, sales_by_meter INTEGER, sales_by_dip INTEGER, tank_sale INTEGER, variance INTEGER)")
            

            cur.execute("INSERT INTO DSR Values(?,?,?,?,?,?)",(self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry6.get()))

            conn.commit()

            conn.close()

            messagebox.showinfo("Success","Saved  Succesfull")

            self.clear()

        


    def clear(self):

      self.entry1.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)
      self.entry5.delete(0,END)
      self.entry6.delete(0,END)
      
        