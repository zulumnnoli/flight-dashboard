#sql = structured query language
import sqlite3

con = sqlite3.connect("airline.db")

cur = con.cursor()
# this means that we are creating a table


cur.execute('''  create table if not exists users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullName VARCHAR(20) NOT NULL,
            userName VARCHAR(20) UniQUE NOT NULL,
            userRole VARCHAR(20) NOT NULL,
            password VARCHAR(20) UniQUE NOT NULL,
            remark VARCHAR(50) NOT NULL
            )
            ''')

cur.execute('''  create table if not exists flights(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number VARCHAR(20) UniQUE NOT NULL,
            origin VARCHAR(20) UniQUE NOT NULL,
            departure_time VARCHAR(20) UniQUE NOT NULL,
            arrival_time VARCHAR(20) UniQUE NOT NULL,
            destination VARCHAR(50) UniQUE NOT NULL
            )
            ''')