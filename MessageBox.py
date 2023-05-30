from tkinter import * 
from PIL import ImageTk ,Image
from tkinter import messagebox

root= Tk()
root.title("MessageBox")

#Types of Message Box
# showerror ,showinfo ,showwarning ,askokcancel ,askyesno ,askquestion 

def popup():
    response=messagebox.showerror("This is my pop_up!","Hello world!")
    Label(root,text=response).pack()
    #if response==1:
    #    Label(root,text="you clicked yes").pack()
    #else:
     #   Label(root,text="you clicked No").pack()


Button_1= Button(root,text="Pop_up",command=popup)
Button_1.pack()

root.mainloop()