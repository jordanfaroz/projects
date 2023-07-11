from tkinter import *

def add():
    no1 = int(en.get(lb))
    no2 = int(en.get(lb1))
    ans = no1+no2
    name1.config(text="square is "+str(ans))

def cbe():
    no = int(en.get())
    ans1 = no*no*no
    name2.config(text="cube is "+str(ans1))

root = Tk()
root.geometry("500x500")


name = Label(root,text="calculator",foreground="black",font=("agencu Fb",20),relief="solid")
lb=Label(root,text="Number 1",width=30)
en=Entry(root,bd=2)
lb1=Label(root,text="Number 2",width=30)
en1=Entry(root,bd=2)
plus = Button(root,text="+",foreground="green",font=("agencu Fb",20),relief="solid")


name.place(x=200,y=0)
lb.place(x=50,y=100)
en.place(x=200,y=100)
lb1.place(x=50,y=150)
en1.place(x=200,y=150)

root.mainloop()

