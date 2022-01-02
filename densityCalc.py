from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3

class densityCalculator(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Density Calculator")
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
        
        self.label1=Label(self.frame_input,text="Calculate Density",font=("impact",24,"bold"),fg='black',bg='white')
        self.label1.place(x=45,y=25)
        
        self.label2=Label(self.frame_input,text="Type of Fuel",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.label2.place(x=30,y=85)
        
        fuels=["Petrol","Diesel","Power","Turbo Jet"]
        self.variable = StringVar()
        self.variable.set(fuels[0])
        
        self.label3=Label(self.frame_input,text="Mass",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry1=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        
        self.label4=Label(self.frame_input,text="Volume",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.entry2=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        
        self.label5=Label(self.frame_input,text="",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        self.density=StringVar()
        self.entry3=Entry(self.frame_input,font=("times new roman",15,"bold"),bg='lightgray',state='disabled',textvariable=self.density)
        
        self.btn1=Button(self.frame_input,command=self.densCalc,text="Calculate",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn2=Button(self.frame_input,command=self.goBack,text="Back",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=17,height=1)
        self.btn2.place(x=30,y=365)
        
        dropdown = OptionMenu(self.frame_input, self.variable, *fuels,command=self.display_selected)
        dropdown.pack(expand=True)
        dropdown.place(x=300,y=85,width=270,height=35)
        dropdown.config(bg='orangered',fg="white",font=("times new roman",15,"bold"))
        
    def display_selected(self,choice):
        choice=self.variable.get()
        self.label3.place(x=30,y=155)
        self.label4.place(x=30,y=225)
        self.label5.place(x=30,y=295)
        self.entry1.place(x=300,y=155,width=270,height=35)
        self.entry2.place(x=300,y=225,width=270,height=35)
        self.entry3.place(x=300,y=295,width=270,height=35)
        self.label5.config(text="Density of "+choice)
        self.btn1.place(x=300,y=365)
    
    def goBack(self):
        self.destroy()
    
    def densCalc(self):
        mass=self.entry1.get()
        volume=self.entry2.get()
        if self.entry2.get()=='' or self.entry1.get()=='':
            messagebox.showerror("Error","Please fill all the fields")
        else:
            density=float(mass)/float(volume)
            self.density.set(density)
        
        
        