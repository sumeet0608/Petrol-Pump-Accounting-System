from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
from menu import menuOptions

class Login(object):
    def __init__(self,root):

        self.root=root

        self.root.title("Petrol Bunk Accounting System")

        self.root.geometry("1366x700+0+0")
        

        self.root.resizable(False,False)
        self.count=0

        self.loginform()
    
    def loginform(self):

        Frame_login=Frame(self.root,bg="white")

        Frame_login.place(x=0,y=0,height=700,width=1366)

      

        self.img=ImageTk.PhotoImage(file="D:\\VS PYTHON\\Cruder Accounter\\bg.jpg")

        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      

        frame_input=Frame(self.root,bg='white')

        frame_input.place(x=500,y=130,height=450,width=350)



        label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')

        label1.place(x=75,y=20)



        label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

        self.email_txt.place(x=30,y=145,width=270,height=35)

      

        label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',show="*")

        self.password.place(x=30,y=245,width=270,height=35)

   

        self.btn1=Button(frame_input,text="Show Password",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0,command=self.show_pass)

        self.btn1.place(x=125,y=305)



        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered", bd=0,width=15,height=1)

        btn2.place(x=90,y=340)

        

        btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

        btn3.place(x=110,y=390)



    def login(self):

        if self.email_txt.get()=="" or self.password.get()=="":

            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            conn=sqlite3.connect("login.db")
            curr=conn.cursor()
            curr.execute("SELECT * FROM loginDet WHERE username=? AND password=?",(self.email_txt.get(),self.password.get()))

            row=curr.fetchone()

            if row==None:

                messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

                self.loginclear()

                self.email_txt.focus()

            else:

                self.appscreen()

                conn.close()
            

    def Register(self):



        Frame_login1=Frame(self.root,bg="white")

        Frame_login1.place(x=0,y=0,height=1000,width=2000)

      

        self.img=ImageTk.PhotoImage(file="D:\\VS PYTHON\\Cruder Accounter\\bg.jpg")

        img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      

        frame_input2=Frame(self.root,bg='white')

        frame_input2.place(x=210,y=130,height=515,width=915)



        label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')

        label1.place(x=45,y=20)



        label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry.place(x=30,y=145,width=270,height=35)

      

        label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',show="*")

        self.entry2.place(x=30,y=245,width=270,height=35)



        label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label4.place(x=330,y=95)

        self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry3.place(x=330,y=145,width=270,height=35)



        label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label5.place(x=330,y=195)

        self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray',show="*")

        self.entry4.place(x=330,y=245,width=270,height=35)
        label6=Label(frame_input2,text="Company Name",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label6.place(x=630,y=95)

        self.entry5=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray')

        self.entry5.place(x=630,y=145,width=270,height=35)
        label7=Label(frame_input2,text="Petrol Pump Name",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label7.place(x=630,y=195)

        self.entry6=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry6.place(x=630,y=245,width=270,height=35)
        label8=Label(frame_input2,text="Owner Name", font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label8.place(x=30,y=295)

        self.entry7=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray')

        self.entry7.place(x=30,y=345,width=270,height=35)
        label9=Label(frame_input2,text="City", font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label9.place(x=330,y=295)

        self.entry8=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray')

        self.entry8.place(x=330,y=345,width=270,height=35)
        no_of_nozzles=IntVar()
        label10=Label(frame_input2,text="No of Nozzles",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label10.place(x=630,y=295)

        self.entry9=Entry(frame_input2,textvariable=no_of_nozzles,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry9.place(x=630,y=345,width=270,height=35)



        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=15,height=1)

        btn2.place(x=390,y=430)

        

        btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

        btn3.place(x=400,y=470)





    def register(self):

        if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="" or self.entry5.get()=="" or self.entry6.get()=="" or self.entry7.get()=="" or self.entry8.get()=="" or self.entry9.get()=="" or self.entry9.get()==0:

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.entry2.get()!=self.entry4.get():

            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

        else:

            conn=sqlite3.connect("login.db")
            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS loginDet(petrolpumpname text, companyname text, ownername text, city text, noOfNozzles INTEGER,email text, username text primary key, password text)")
            cur.execute("select * from loginDet where username=?",(self.entry.get(),))


            row=cur.fetchone()

            if row!=None:

                messagebox.showerror("Error","User already Exist,Please try with another Email" ,parent=self.root)

                self.regclear()

                self.entry.focus()

            else:

                cur.execute("INSERT INTO loginDet Values(?,?,?,?,?,?,?,?)",(self.entry6.get(),self.entry5.get(),self.entry7.get(),self.entry8.get(),self.entry9.get(),self.entry3.get(),self.entry.get(),self.entry2.get()))

                conn.commit()

                conn.close()

                messagebox.showinfo("Success","Register Succesfull",parent=self.root)

                self.regclear()

            



    def appscreen(self):
        self.password.delete(0,END)
        app=menuOptions(self.email_txt.get())



    def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)
      self.entry5.delete(0,END)
      self.entry6.delete(0,END)
      self.entry7.delete(0,END)
      self.entry8.delete(0,END)
      self.entry9.delete(0,END)



    def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)
      
    def show_pass(self):
        self.count+=1
        if self.count%2==0:
            self.password.config(show="*")
            self.btn1.config(text="Show Password")
        else:
            self.password.config(show="")
            self.btn1.config(text="Hide Password")
      
def main():
    
    root=Tk()

    obj=Login(root)

    root.mainloop()

if __name__=="__main__":
    
    main()