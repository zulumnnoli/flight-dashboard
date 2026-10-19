import tkinter as tk
from PIL import Image,ImageTk
import tkinter.messagebox as message
import sqlite3
import dbconnect
from tkinter import ttk
from tkinter import END, ttk

master=tk.Tk()
master.geometry("1000x1000+300+0")
master.title("Admin Dashboard")
master.resizable(0,0)
master.configure(background="#141444")

# a flight with tow user, the admin and front desk
# the customer book flight online and take to front person 
# to give seat number in the flight and admin is able to see 
# or process the user carry out and has permission of deleting such 
# front in database after sack or resign 

def fetch_data():
    con=sqlite3.connect('airline.db')
    cur=con.cursor()
    cur.execute(''' select * from flights   ''')
    rows=cur.fetchall()
    con.close()
    return rows

def display_data():
    for row in fetch_data():
        tree.insert("", END, value=row)

def add():
    flight_number=e1.get()
    origin=e2.get()
    departure_time=e3.get()
    arrival_time=e4.get()
    destination=e5.get()

    if flight_number=="" or origin=="" or departure_time=="" or arrival_time=="" or destination=="" :
        message.showinfo("prompt","Empty record is not allowed, please fill the form")
    elif flight_number and origin and departure_time and arrival_time and destination:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' insert into flights(flight_number,origin,departure_time,arrival_time,destination)
                                        values(?,?,?,?,?)''',(flight_number,origin,departure_time,arrival_time,destination))
        message.showinfo("Alert","records sent successfully to flights table")
        con.commit()
        con.close()
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
        e3.delete(0,tk.END)
        e4.delete(0,tk.END)
        e5.delete(0,tk.END)

def search():
    flight_number=e1.get()
    if flight_number:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' select flight_number,origin,departure_time,arrival_time,destination from flights where flight_number=?
                    ''',(flight_number,))
        result=cur.fetchone()
        con.close()
        if result:
            e2.insert(0,result[1])
            e3.insert(0,result[2])
            e4.insert(0,result[3])
            e5.insert(0,result[4])
        
        else:
            message.showinfo("Prompt", "Record doesnot exists in flights table")
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            e3.delete(0,tk.END)
            e4.delete(0,tk.END)
            e5.delete(0,tk.END)

def update():
    flight_number=e1.get()
    origin=e2.get()
    departure_time=e3.get()
    arrival_time=e4.get()
    destination=e5.get()

    if flight_number and origin and arrival_time and departure_time and destination:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' update flights
                    set origin=?, arrival_time=?, departure_time=?, destination=?
                    where flight_number=? ''',(origin,departure_time,arrival_time,destination,flight_number))
        con.commit()
        con.close()
        if cur.rowcount>0:
            message.showinfo("Alert","Record updated successfully")
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            e3.delete(0,tk.END)
            e4.delete(0,tk.END)
            e5.delete(0,tk.END)
        else:
            message.showinfo("Prompt","Record is not found")
    else:
        message.showinfo("Prompt","Please Enter a flight number")

def delete():
    flight_number=e1.get()
    if flight_number:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' delete from flights where flight_number=? ''',(flight_number,))
        con.commit()
        con.close()
        if cur.rowcount>0:
            message.showinfo("prompt","Record deleted successfully")
        else:
            message.showinfo("prompt","Flight number is not in flights table")
    else:
        message.showinfo("Prompt","Enter a flight number to delete flight")


        
# CRUD 
# create
# Read
# update 
# delete
def search():
    flight_number=e1.get()
    if flight_number:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' select flight_number,origin,departure_time,arrival_time,destination from flights where flight_number=?
                    ''',(flight_number,))
        result=cur.fetchone()
        con.close()
        if result:
            e2.insert(0,result[1])
            e3.insert(0,result[2])
            e4.insert(0,result[3])
            e5.insert(0,result[4])
        
        else:
            message.showinfo("Prompt", "Record doesnot exists in flights table")
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            e3.delete(0,tk.END)
            e4.delete(0,tk.END)
            e5.delete(0,tk.END)

def update():
    flight_number=e1.get()
    origin=e2.get()
    departure_time=e3.get()
    arrival_time=e4.get()
    destination=e5.get()

    if flight_number and origin and arrival_time and departure_time and destination:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' update flights
                    set origin=?, arrival_time=?, departure_time=?, destination=?
                    where flight_number=? ''',(origin,departure_time,arrival_time,destination,flight_number))
        con.commit()
        con.close()
        if cur.rowcount>0:
            message.showinfo("Alert","Record updated successfully")
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            e3.delete(0,tk.END)
            e4.delete(0,tk.END)
            e5.delete(0,tk.END)
        else:
            message.showinfo("Prompt","Record is not found")
    else:
        message.showinfo("Prompt","Please Enter a flight number")

def delete():
    flight_number=e1.get()
    if flight_number:
        con=sqlite3.connect('airline.db')
        cur=con.cursor()
        cur.execute(''' delete from flights where flight_number=? ''',(flight_number,))
        con.commit()
        con.close()
        if cur.rowcount>0:
            message.showinfo("prompt","Record deleted successfully")
        else:
            message.showinfo("prompt","Flight number is not in flights table")
    else:
        message.showinfo("Prompt","Enter a flight number to delete flight")

lbl1=tk.Label(master, text=" Flight Dashbaord", font=("verdana",50,"bold"), fg="#fff", bg="#141444",underline=5)
lbl1.place(x=250, y=0)
leftFrame=tk.Frame(master, width=500, height=1000)
l1=tk.Label(leftFrame, text="Flight Number", fg="#000", font=("verdana",12,"bold"))
l1.place(x=0,y=30)


e1=tk.Entry(leftFrame,width=50,border=5)
e1.place(x=150,y=30)

l2=tk.Label(leftFrame, text="Origin", fg="#000", font=("verdana",12,"bold"))
l2.place(x=0,y=60)


e2=tk.Entry(leftFrame,width=50,border=5)
e2.place(x=150,y=60)

l3=tk.Label(leftFrame, text="Departure_time", fg="#000", font=("verdana",12,"bold"))
l3.place(x=0,y=90)


e3=tk.Entry(leftFrame,width=50,border=5)
e3.place(x=150,y=90)

l4=tk.Label(leftFrame, text="Arrival_time", fg="#000", font=("verdana",12,"bold"))
l4.place(x=0,y=120)


e4=tk.Entry(leftFrame,width=50,border=5)
e4.place(x=150,y=120)

l5=tk.Label(leftFrame, text="Destination", fg="#000", font=("verdana",12,"bold"))
l5.place(x=0,y=150)


e5=tk.Entry(leftFrame,width=50,border=5)
e5.place(x=150,y=150)


leftFrame.place(x=0,y=150)
btnAdd=tk.Button(leftFrame,text="AddFlight", bg="#000",fg="#fff", command=add)
btnAdd.place(x=150,y=180)

btnSearch=tk.Button(leftFrame,text="Search", bg="#000",fg="#fff", command=search)
btnSearch.place(x=210,y=180)

btnUpdate=tk.Button(leftFrame,text="Update Flight", bg="#000",fg="#fff", command=update)
btnUpdate.place(x=250,y=180)

btnDelete=tk.Button(leftFrame,text="Delete Flight", bg="#f00",fg="#fff", command=delete)
btnDelete.place(x=350,y=180)





rightframe=tk.Frame(master,width=500,height=1000, bg="#80184c")
rightframe.place(x=500,y=150)


lbr=tk.Label(rightframe, text="Flight Booking" )
lbr.place(x=0,y=0)
cols=["ID","Flight Number","Origin","Departure Time","Arrival Time","Destination"]
tree=ttk.Treeview(rightframe,columns=cols, show="headings" )
for col in cols:
    tree.heading(col,text=col)
    tree.column(col,width=80)
tree.place(x=0, y=50)

display_data()

master.mainloop()

