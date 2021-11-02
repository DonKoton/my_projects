from tkinter import *

def storeVar():
    AutoConnect = E1.get()
    Email = E2.get()
    Password = E3.get()
    Url = E4.get()
    print(AutoConnect)
    print(Email)
    print(Password)
    print(Url)

    global variables
    variables = [AutoConnect, Email, Password, Url]

root = Tk()

L1 = Label(root, text="Auto-Connect",).grid(row=0,column=0)
L2 = Label(root, text="EMAIL",).grid(row=1,column=0)
L3 = Label(root, text="PASSWORD",).grid(row=2,column=0)
L4 = Label(root, text="URL",).grid(row=3,column=0)

E1 = Entry(root, bd =5)
E1.grid(row=0,column=1)

E2 = Entry(root, bd =5)
E2.grid(row=1,column=1)

E3 = Entry(root, bd =5)
E3.grid(row=2,column=1)

E4 = Entry(root, bd =5)
E4.grid(row=3,column=1)

submit = Button(root, text= "Submit", command = storeVar)
submit.grid(row=4)


root.mainloop()
