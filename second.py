from re import T
from tkinter import *
from tkinter.tix import TEXT


root = Tk()

e = Entry(root,width=50)
e.pack() 
e.insert(0,"Enter your Name: ")

# Creating a label widget
def click():
    Text= "Hallo "+e.get()
    myLabel1 = Label(root,  text=Text )
    myLabel1.pack()

myButton= Button(root,text="click me ",command=click,fg="blue",bg="red")
myButton.pack()


#showing it onto the screen


root.mainloop()