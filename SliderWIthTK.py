from tkinter import *
from PIL import ImageTk ,Image 
from tkinter import filedialog 
root =Tk()
root.title("SliderWithTK")
root.geometry("400x400")
# vertical slider
vertical = Scale(root, from_=600 ,to=0 )
vertical.pack()
# horizontal silder
horizontal= Scale(root, from_=400 ,to=0 , orient=HORIZONTAL)
horizontal.pack()
# function horizontal slider
def  slider():
    my_label =Label(root,text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

my_label =Label(root,text=horizontal.get())
my_label.pack()
my_button=Button(root,text="slider",command= slider)
my_button.pack()

root.mainloop()