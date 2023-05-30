from tkinter import *

root=Tk()
root.title("DropdwonMenus")
root.geometry("400x400")


clicked =StringVar()
options=[ "Monday","Tuesday","Wednesday","Thursday","friday","Sunday"]
clicked.set(options[2])
# Drop Dwon Boxs
drop=OptionMenu(root,clicked,*options)
drop.pack()


def show():
    my_label=Label(root,text=clicked.get())
    my_label.pack()


my_button=Button(root,text="Show Selection",command=show)
my_button.pack()


root.mainloop()