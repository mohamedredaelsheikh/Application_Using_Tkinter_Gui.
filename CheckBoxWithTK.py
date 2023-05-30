from tkinter import *
from PIL import ImageTk ,Image 
from tkinter import filedialog

root=Tk()
root.title("CheckBoxWithTK")
root.geometry("400x400")

var=StringVar()
checkBox= Checkbutton(root, text="Would You Like Super Size Your Order? Check Here",variable=var,onvalue="Super Size",offvalue="nurmal Size")
checkBox.deselect()
checkBox.pack()

def show():
    my_label=Label(root,text=var.get())
    my_label.pack()


my_button=Button(root,text="Show Selection",command=show)
my_button.pack()

root.mainloop()