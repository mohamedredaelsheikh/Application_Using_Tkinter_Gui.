from tkinter import * 
from PIL import ImageTk ,Image


root= Tk()
root.title("CreateNewWindow")
# open Image
my_img= Image.open("D:/Network programming Lab/Tkinter Gui/Images/img1.jpg")
# resize Image
resize_img=my_img.resize((300,225),Image.ANTIALIAS)
picture =ImageTk.PhotoImage(resize_img)

def open():
  # create new window
    top=Toplevel()
    top.title("My Second window")
    my_label=Label(top,image=picture).pack()
    close_button=Button(top,text="close window",command=top.destroy)
    close_button.pack()


#Create a button to open the new window
my_button= Button(root,text="open second window",command=open)
my_button.pack() 


root.mainloop()