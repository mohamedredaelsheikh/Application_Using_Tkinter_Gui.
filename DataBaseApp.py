from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.title("DataBaseApp")
root.geometry("400x450")

# DataBase

# Create a DataBase or connect to one 
connection=sqlite3.connect("Address_Book.db")
#Create a Cursor
cursor=connection.cursor() 
'''
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
'''
# Create Entry Text Boxs
first_name=Entry(root,width=30)
first_name.grid(row=0,column=1,padx=20,pady=(10,0))

last_name=Entry(root,width=30)
last_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

Zipcode=Entry(root,width=30)
Zipcode.grid(row=5,column=1,padx=20)

phone=Entry(root,width=30)
phone.grid(row=6,column=1,padx=20)

select_Id=Entry(root,width=30)
select_Id.grid(row=10,column=1, pady=5)


# Create Labels Text Boxs
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

City_label=Label(root,text="City")
City_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

Zipcode_label=Label(root,text="Zipcode")
Zipcode_label.grid(row=5,column=0)

phone_label=Label(root,text="Phone")
phone_label.grid(row=6,column=0)

select_Id_label=Label(root,text="Select_ID")
select_Id_label.grid(row=10,column=0, pady=5)

#crate submit function 
def submit():
    # Create a DataBase or connect to one 
    connection=sqlite3.connect("Address_Book.db")
    #Create a Cursor
    cursor=connection.cursor()
    # Insert Into Table
    cursor.execute("INSERT INTO Citizens_info VALUES (:first_name,:last_name,:address,:city,:state,:Zipcode,:phone)",
                       {
                            "first_name":first_name.get(),
                            "last_name":last_name.get(),
                            "address":address.get(),
                            "city":city.get(),
                            "state":state.get(),
                            "Zipcode":Zipcode.get(),
                            "phone":phone.get()
                       })
    #Commit Changes
    connection.commit()
    #close connection
    connection.close()
     # Clear The Text Boxes 
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    Zipcode.delete(0,END)
    phone.delete(0,END)

#crate submit function
def query():
    # Create a DataBase or connect to one 
    connection=sqlite3.connect("Address_Book.db")
    #Create a Cursor
    cursor=connection.cursor()
    #query The DateBase
    cursor.execute("SELECT * , oid  FROM Citizens_info")
    records= cursor.fetchall()
    print(records)
    
    print_records=""
    # loop throw the results
    for record in records:
        print_records += str(record[0]) +" "+str(record[1])+" "+"\t"+str(record[7]) +"\n"

    query_label= Label(root,text=print_records)
    query_label.grid(row=14,column=0,columnspan=2)


    #Commit Changes
    connection.commit()
    #close connection
    connection.close()

#crate Delete function
def delete():
    # Create a DataBase or connect to one 
    connection=sqlite3.connect("Address_Book.db")
    #Create a Cursor
    cursor=connection.cursor()
    #Delete a record from a DataBase
    cursor.execute("Delete FROM Citizens_info where oid = " + select_Id.get())

    select_Id.delete(0,END)

    #Commit Changes
    connection.commit()
    #close connection
    connection.close()


# Create update function
def update():
    # Create a DataBase or connect to one 
    connection=sqlite3.connect("Address_Book.db")
    #Create a Cursor
    cursor=connection.cursor()
    record_id = select_Id.get()

    cursor.execute(""" Update Citizens_info Set
        first_name = :first ,
        last_name = :last ,
        address = :address ,
        city = :city  ,
        state = :state ,
        Zipcode = :Zipcode  ,
        phone = :phone     
        WHERE oid = :oid""",
        {
            'first': first_name_editor.get(),
            'last' : last_name_editor.get(),
            'address' : address_editor.get(),
            'city' : city_editor.get(),
            'state': state_editor.get(),
            'Zipcode' : Zipcode_editor.get(),
            'phone' : phone_editor.get(), 
            'oid' : record_id

        })

    #Commit Changes
    connection.commit()
    #close connection
    connection.close()
    select_Id.delete(0,END)
    editor.destroy()
   


#crate edit function
def edit():
    # create new Edit Window
    global editor
    editor=Tk()
    editor.title("Edit Window")
    editor.geometry("400x450")
    
    # Create a DataBase or connect to one 
    connection=sqlite3.connect("Address_Book.db")
    #Create a Cursor
    cursor=connection.cursor()
    record_id = select_Id.get()
    #query The DateBase
    cursor.execute("SELECT *   FROM Citizens_info where oid = " + record_id)
    records= cursor.fetchall()
    #Create globel variable Boxs
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global Zipcode_editor
    global state_editor
    global  phone_editor
    
    # Create Entry For Edit Text Boxs
    first_name_editor=Entry(editor,width=30)
    first_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    last_name_editor=Entry(editor,width=30)
    last_name_editor.grid(row=1,column=1,padx=20)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1,padx=20)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=3,column=1,padx=20)

    state_editor=Entry(editor,width=30)
    state_editor.grid(row=4,column=1,padx=20)

    Zipcode_editor=Entry(editor,width=30)
    Zipcode_editor.grid(row=5,column=1,padx=20)

    phone_editor=Entry(editor,width=30)
    phone_editor.grid(row=6,column=1,padx=20)

    # Create Labels for editor Text Boxs
    f_name_label_editor=Label(editor,text="First Name")
    f_name_label_editor.grid(row=0,column=0,pady=(10,0))

    l_name_label_editor=Label(editor,text="Last Name")
    l_name_label_editor.grid(row=1,column=0)
    
    address_label_editor=Label(editor,text="Address")
    address_label_editor.grid(row=2,column=0)

    City_label_editor=Label(editor,text="City")
    City_label_editor.grid(row=3,column=0)

    state_label_editor=Label(editor,text="State")
    state_label_editor.grid(row=4,column=0)

    Zipcode_label_editor=Label(editor,text="Zipcode")
    Zipcode_label_editor.grid(row=5,column=0)

    phone_label_editor=Label(editor,text="Phone")
    phone_label_editor.grid(row=6,column=0)


    # loop throw  record items
    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        Zipcode_editor.insert(0,record[5])
        phone_editor.insert(0,record[6])

    #Create save Button
    update_button=Button(editor,text="Save Record ",command=update)
    update_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=145)


    #select_Id.delete(0,END)

    #Commit Changes
    connection.commit()
    #close connection
    connection.close()


#Create Submit Button
submit_button=Button(root,text="Add Record to DataBase",command=submit)
submit_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=105)

#Create Query Button
query_button=Button(root,text="Show Record ",command=query)
query_button.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create Delete Button
delete_button=Button(root,text="Delete Record ",command=delete)
delete_button.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

#Create Update Button
update_button=Button(root,text="Edit Record ",command=edit)
update_button.grid(row=13,column=0,columnspan=2,padx=10,pady=10,ipadx=143)


#Commit Changes
connection.commit()
#close connection
connection.close()

root.mainloop()
    