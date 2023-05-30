from tkinter import * 
from PIL import ImageTk ,Image

root= Tk()
root.title("Radio Buttons")

#r=IntVar()
#r.set("2")

modes=[
       ("Cheese","Cheese"),
       ("onion","onion"),
       ("Mushroom","Mushroom"),
       ("chicken","chicken"),]

pizza=StringVar()
#pizza.set("pepperoni")

for text, mode in modes:
     Radiobutton(root , text=text, variable=pizza, value=mode).pack(anchor=W)
   


def clicked(value):
    my_label=Label(root,text=value)
    my_label.pack()


#Radiobutton(root , text="OPtion 1" , variable = r  ,   value=1 ,command=lambda:clicked(r.get())).pack()
#Radiobutton (root , text="OPtion 2" , variable = r  , value=2 ,command=lambda:clicked(r.get()) ).pack()
#Radiobutton (root , text="OPtion 3" , variable = r  , value=3 ,command=lambda:clicked(r.get()) ).pack()

my_label= Label(root,text=pizza.get())
my_label.pack()

myButton = Button(root,text="Click me ",command=lambda:clicked(pizza.get())) 
myButton.pack()
root.mainloop()




