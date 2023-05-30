from tkinter import *
import sqlite3

root=Tk()
root.title("DropdwonMenus")
root.geometry("400x400")

# DataBase

# Create a DataBase or connect to one 
connection=sqlite3.connect("Address_Book.db")
#Create a Cursor
cursor=connection.cursor() 

#Create a table
cursor.execute(""" CREATE TABLE Citizens_info(
        first_name text,
        last_name text,
        address text,
        city text ,
        state text,
        Zipcode integer,
        phone integer
)""") 

#Commit Changes
connection.commit()
#close connection
connection.close()

root.mainloop()