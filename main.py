from tkinter import *
from tkinter import messagebox as mb
import sqlite3

window=Tk()
window.geometry("300x150")

def login():
	def login_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM loginDet WHERE username=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		if(len(row)==0):
			mb.showinfo("Error","Invalid username or password")
		else:
			mb.showinfo("Success","Login Successful")



	window.destroy()
	login_window=Tk()
	login_window.geometry("300x150")
	l1=Label(login_window,text="Username",font="arial 15")
	l1.grid(row=1,column=1)
	l2=Label(login_window,text="Password",font="arial 15")
	l2.grid(row=2,column=1)
	l3=Label(login_window,font="times 20")
	l3.grid(row=5,column=2)

	email_text=StringVar()
	e1=Entry(login_window,textvariable=email_text,width=30)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_window,textvariable=password_text,width=30)
	e2.grid(row=2,column=2)


	b1=Button(login_window,text="login",width=20,command=login_database)
	b1.grid(row=4,column=2)
	login_window.mainloop()




def signup():


	def signup_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS loginDet(petrolpumpname text, companyname text, ownername text, city text, noOfNozzles INTEGER,email text, username text primary key, password text)")
		cur.execute("INSERT INTO loginDet Values(?,?,?,?,?,?,?,?)",(e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e2.get(),e1.get(),e3.get()))
		l4=Label(signup_window,text="Account created",font="times 15")
		l4.grid(row=11,column=2)
		conn.commit()
		conn.close()





	window.destroy()
	signup_window=Tk()
	signup_window.geometry("500x350")
	l1=Label(signup_window,text="Username",font="arial 15")
	l1.grid(row=1,column=1)
	l2=Label(signup_window,text="Email",font="arial 15")
	l2.grid(row=2,column=1)
	l3=Label(signup_window,text="Password",font="arial 15")
	l3.grid(row=3,column=1)
	l4=Label(signup_window,text="Petrol Pump Name",font="arial 15")
	l4.grid(row=4,column=1)
	l5=Label(signup_window,text="Company Name",font="arial 15")
	l5.grid(row=5,column=1)
	l6=Label(signup_window,text="Owner Name",font="arial 15")
	l6.grid(row=6,column=1)
	l7=Label(signup_window,text="City",font="arial 15")
	l7.grid(row=7,column=1)
	l8=Label(signup_window,text="No of Nozzles",font="arial 15")
	l8.grid(row=8,column=1)
	l9=Label(signup_window,text=" ",font="arial 15")
	l9.grid(row=9,column=1,columnspan=2)

	user_name=StringVar()
	e1=Entry(signup_window,textvariable=user_name,width=30)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_window,textvariable=email_text,width=30)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_window,textvariable=password_text,width=30)
	e3.grid(row=3,column=2)
	petrol_pump_name=StringVar()
	e4=Entry(signup_window,textvariable=petrol_pump_name,width=30)
	e4.grid(row=4,column=2)
	company_name=StringVar()
	e5=Entry(signup_window,textvariable=company_name,width=30)
	e5.grid(row=5,column=2)
	owner_name=StringVar()
	e6=Entry(signup_window,textvariable=owner_name,width=30)
	e6.grid(row=6,column=2)
	address=StringVar()
	e7=Entry(signup_window,textvariable=address,width=30)
	e7.grid(row=7,column=2)
	no_of_nozzles=IntVar()
	e8=Entry(signup_window,textvariable=no_of_nozzles,width=30)
	e8.grid(row=8,column=2)

	b1=Button(signup_window,text="Sign up",width=20,command=signup_database)
	b1.grid(row=10,column=2)







l1=Label(window,text="Welcome!",font="arial 20")
l1.grid(row=1,column=2,columnspan=2)

l2=Label(window,text=" ",font="times 20")
l2.grid(row=2,column=2,columnspan=2)

b1=Button(window,text="Login",width=20,command=login)
b1.grid(row=3,column=2)

b2=Button(window,text="Signup",width=20,command=signup)
b2.grid(row=3,column=3)


window.mainloop()
