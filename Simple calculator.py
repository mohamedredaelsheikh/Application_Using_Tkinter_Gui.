from tkinter import * 
root= Tk()
root.title("Simple calculator")
input = Entry(root,width=35,borderwidth=5)
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)



def Button_click(number):
    current =input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(number))


def Button_clear():
    input.delete(0,END)


def Button_add():
    frist_number =input.get()
    global f_num 
    global math
    math="addition"
    f_num =int( frist_number)
    input.delete(0,END)


def Button_Equal():
    second_number= input.get()
    input.delete(0,END)
    if math == "addition":
        input.insert(0,f_num + int(second_number))

    if math == "Subtraction":
        input.insert(0,f_num - int(second_number)) 

    if math == "Division":
        input.insert(0,f_num / int(second_number))

    if math == "Multiplication":
        input.insert(0,f_num * int(second_number))



def Button_subtract():
    frist_number =input.get()
    global f_num 
    global math
    math="Subtraction"
    f_num =int( frist_number)
    input.delete(0,END)

def Button_divide():
    frist_number =input.get()
    global f_num 
    global math
    math="Division"
    f_num =int( frist_number)
    input.delete(0,END)
    
def Button_multiply():
    frist_number =input.get()
    global f_num 
    global math
    math="Multiplication"
    f_num =int( frist_number)
    input.delete(0,END)




# Creating a label widget
button_1=Button(root , text="1" , padx=40 , pady=20 , command=lambda:Button_click(1))
button_2=Button(root , text="2" , padx=40 , pady=20 , command=lambda:Button_click(2))
button_3=Button(root , text="3" , padx=40 , pady=20 , command=lambda:Button_click(3))
button_4=Button(root , text="4" , padx=40 , pady=20 , command=lambda:Button_click(4))
button_5=Button(root , text="5" , padx=40 , pady=20 , command=lambda:Button_click(5))
button_6=Button(root , text="6" , padx=40 , pady=20 , command=lambda:Button_click(6))
button_7=Button(root , text="7" , padx=40 , pady=20 , command=lambda:Button_click(7))
button_8=Button(root , text="8" , padx=40 , pady=20 , command=lambda:Button_click(8))
button_9=Button(root , text="9" , padx=40 , pady=20 , command=lambda:Button_click(9))
button_0=Button(root , text="0" , padx=40 , pady=20 , command=lambda:Button_click(0))

button_add=Button(root , text="+" , padx=39 , pady=20 , command=Button_add)
button_clear=Button(root , text="Clear" , padx=79 , pady=20 , command=Button_clear)
button_equal=Button(root , text="=" , padx=91 , pady=20 , command=Button_Equal)

button_subtract=Button(root , text="-" , padx=41 , pady=20 , command=Button_subtract)
button_multiply=Button(root , text="*" , padx=40 , pady=20 , command=Button_multiply)
button_divide=Button(root , text="/" , padx=41 , pady=20 , command=Button_divide)



#showing it onto the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_divide.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_subtract.grid(row=6,column=2)


root.mainloop()