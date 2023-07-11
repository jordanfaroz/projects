from tkinter import *

root = Tk()
root.geometry("500x500")

lb=Label(root,text="name",width=20)
en=Entry(root,bd=2)

lb.grid(row=0,column=0,pady=50)
en.grid(row=0,column=1,pady=50)


root.mainloop()
