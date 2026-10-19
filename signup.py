#crud
from tkinter import *
from tkinter import ttk
import subprocess
import dbconnect
from tkinter import messagebox as msg
from PIL import Image, ImageTk
#pillow module is used to import images and videos
import sqlite3
userRole = ["admin", "user", "other"]

top = Tk()
top.geometry("500x400+300+0")
top.title("SignUp Page")
top.configure(bg="white")

top.resizable(0,0)
image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)

def signup():
   subprocess.Popen(["python","signin.py"])
   #subprocess helps us import anothr file

   


def sign():
  fullname = ent2.get()
  username = ent3.get()
  userrole = ent4.get()
  password = ent5.get()
  remark = txt6.get("1.0", "end")

  if username=="" or password=="" or remark=="":
    msg.showinfo("Alert","Empty record is not allowed, please fill the form")
  else:
      con=sqlite3.connect('airline.db')
      cur=con.cursor()
  try:
      cur.execute('''INSERT INTO users(fullname,username,userrole,password,remark)
                      VALUES(?,?,?,?,?)''',(fullname,username,userrole,password,remark))
      # for record to show in the table of database you comit
      con.commit()
      msg.showinfo("Alert","Successfully registered")
      top.destroy() 
      signup()

  except:
      msg.showinfo("Alert","Record Already Exists")




imglb = Label(top, image = photo)
imglb.place(relheight=1, relwidth=1)

lbl1=Label(top,text="SignUp Page", font=("verdana",20,"bold"), foreground="#000000", background="white", underline=5)
lbl1.grid(row=0, column=1)

lbl2=Label(top,text="Full Name:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl2.grid(row=1,column=0, pady=10)

ent2=Entry(top,width=50, relief=FLAT)
ent2.grid(row=1,column=1)

lbl3=Label(top,text="UserName:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl3.grid(row=2,column=0, pady=10)
ent3=Entry(top,width=50, relief=FLAT)
ent3.grid(row=2,column=1)

lbl4=Label(top,text="User Role:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl4.grid(row=3,column=0)
ent4=ttk.Combobox(width=40, value=userRole)
ent4.grid(row=3,column=1)

lbl5=Label(top,text="PASSWORD:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl5.grid(row=4,column=0)
ent5=Entry(top,width=50, relief=FLAT, show="*")
ent5.grid(row=4,column=1, pady=10)

lbl6=Label(top,text="REMARK:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl6.grid(row=5,column=0)
txt6=Text(top,width=40,height=10)
txt6.grid(row=5,column=1, pady=10)

btn=Button(top, text="Sign Up", foreground="black", background="white", width=20, command=sign)
btn.grid(row=6,column=1)

# install pillow to put the image inside


top.mainloop()