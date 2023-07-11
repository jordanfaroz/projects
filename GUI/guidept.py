from tkinter import *


root = Tk()
root.geometry("500x500")

lb=Label(root,text="Deptno",width=30)
en=Entry(root,bd=2)
lb1=Label(root,text="Deptname",width=30)
en1=Entry(root,bd=2)
lb2=Label(root,text="Location",width=30)
en2=Entry(root,bd=2)
name1 = Button(root,text="submit",foreground="blue",font=("agencu Fb",20),relief="solid")
name2 = Button(root,text="Show",foreground="red",font=("agencu Fb",20),relief="solid")
name3 = Button(root,text="exit",foreground="red",font=("agencu Fb",20),relief="solid")

lb.place(x=10,y=50)
en.place(x=150,y=50)
lb1.place(x=10,y=100)
en1.place(x=150,y=100)
lb2.place(x=10,y=150)
en2.place(x=150,y=150)
name1.place(x=75,y=200)
name2.place(x=50,y=260)
name3.place(x=150,y=260)

root.mainloop()



