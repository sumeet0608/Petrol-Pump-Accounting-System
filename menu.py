from tkinter import *
from PIL import ImageTk
from tkinter import messagebox as mb
from MSR import metreSR
from densityCalc import densityCalculator

class menuOptions(Toplevel):
    def __init__(self,username):
        Toplevel.__init__(self)
        self.title("Menu")
        self.geometry("1366x700+0+0")
        self.resizable(False,False)
        self.username=username
        self.menu()
    
    def menu(self):
        Frame_login=Frame(self,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img=ImageTk.PhotoImage(file="transbg.png")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        frame_input=Frame(self)
        frame_input.place(x=500,y=130,height=450,width=350)
        
        
        label1=Label(frame_input,text="Menu",font=('impact',32,'bold'),fg="black")
        label1.place(x=125,y=30)
        
        btn1=Button(frame_input,command=self.meter_reading,text="Metre Scale Reading",cursor="hand2",font=("times new roman",15),fg="white", bg="#7380aa",bd=0,width=17,height=1)
        btn1.place(x=85,y=120)
        
        btn2=Button(frame_input,command=self.den_calc,text="Density Calc",cursor="hand2",font=("times new roman",15),fg="white", bg="#7380aa",bd=0,width=17,height=1)
        btn2.place(x=85,y=180)
        
        btn3=Button(frame_input,command=self.meter_reading,text="DSR Calulator",cursor="hand2",font=("times new roman",15),fg="white", bg="#7380aa",bd=0,width=17,height=1)
        btn3.place(x=85,y=230)
        
        btn4=Button(frame_input,command=self.meter_reading,text="Make a Bill",cursor="hand2",font=("times new roman",15),fg="white", bg="#7380aa",bd=0,width=17,height=1)
        btn4.place(x=85,y=290)
        
        btn5=Button(frame_input,command=self.onClick,text="Exit",cursor="hand2",font=("times new roman",15),fg="white", bg="#7380aa",bd=0,width=17,height=1)
        btn5.place(x=85,y=340)
        
    def meter_reading(self):
        msr=metreSR(self.username)
        
    def den_calc(self):
        density=densityCalculator()
    
    def onClick(self):
        self.destroy()
        
