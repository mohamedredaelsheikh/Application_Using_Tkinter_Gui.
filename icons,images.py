from tkinter import * 
from PIL import ImageTk ,Image


root= Tk()
root.title("Images Viewer")
# change the tkinter icon
#root.iconbitmap('D:/Network programming Lab/Tkinter Gui/icons/codemy.jpg')

# open Image
my_img= Image.open("D:/Network programming Lab/Tkinter Gui/Images/img1.jpg")
# resize Image
resize_img=my_img.resize((300,225),Image.ANTIALIAS)
picture =ImageTk.PhotoImage(resize_img)

# label for image veiw 
my_label= Label(root,image=picture)
my_label.pack()

# Button Exit
Button_quit=Button(root,text='Exit Program',command=root.quit)
Button_quit.pack()


root.mainloop()

