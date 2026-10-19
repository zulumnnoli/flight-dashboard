import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox as msg

from tkinter import ttk
import dbconnect
import sqlite3
import subprocess

usersRole=[
     "admin",
     "user",
     "other"
]
def frontOffice():
     subprocess.Popen(["python","office.py"])
def main():
    subprocess.Popen(["python3","admin.py"])
def login():
    username=ent1.get()
    password=ent2.get()
    userrole=entuser.get()
    if username=="" or password=="":
        msg.showinfo("alert", "Please enter your username and password")
    elif username=="ur" and password=="":
        msg.showinfo("Propmt","UnAuthorize username and password")
        return 
    con=sqlite3.connect("airline.db")
 
    cur=con.cursor()
   
    cur.execute(''' select * from users where username=? and password=? ''',(username,password))
    result=cur.fetchone
    if result:
        master.destroy()
        if userrole.lower()=="admin":
            msg.showinfo("Alert", "login Successful")
            main()
        elif userrole.lower()=="user":
            msg.showinfo("Alert", "login Successful")
            frontOffice()
      
    else:
            msg.showwarning("Warning","Unauthorized Access")
            con.close()

master=tk.Tk()
master.geometry("490x300+300+0")
master.title("Main Page Grid Example")
master.configure(background="#40ffdc")


master.resizable(0,0)

image=Image.open("bg.jpg")

photo=ImageTk.PhotoImage(image)

imglb=tk.Label(master,image=photo)
imglb.place(relheight=1,relwidth=1)
lbl1=tk.Label(master,text="SignIn Page", font=("verdana",20,"bold"), foreground="#000000", background="#F53E56", underline=5)
lbl1.place(x=180,y=0)

lbl2=tk.Label(master,text="UserName", font=("verdana",16), foreground="#000000", background="white")
lbl2.place(x=0,y=40)

ent1=tk.Entry(master,width=50)
ent1.place(x=150,y=48)

lbluser=tk.Label(master,text="UserRole", font=("verdana",16), foreground="#000000", background="white")
lbluser.place(x=0,y=80)

entuser=ttk.Combobox(width=40, value=usersRole)
entuser.place(x=150,y=80)

lbl3=tk.Label(master,text="Password", font=("verdana",16), foreground="#000000", background="white")
lbl3.place(x=0,y=120)

ent2=tk.Entry(master,width=50, show="*")
ent2.place(x=150,y=120)

btn=tk.Button(master, text="Sign in", foreground="black", background="white", width=20, command=login)
btn.place(x=150,y=160)
master.mainloop()