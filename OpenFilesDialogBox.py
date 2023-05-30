from tkinter import *
from PIL import ImageTk ,Image 
from tkinter import filedialog 
root =Tk()
root.title("OpenFileDialog")

root.filename= filedialog.askopenfilename(initialdir="D:/Network programming Lab/Tkinter Gui/Images",title="Select file name",
                                          filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))


def open():
    global my_image 
    my_label=Label(root,text=root.filename )
    my_label.pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

my_Button=Button(root,text="Open file",command=open).pack()
root.mainloop()