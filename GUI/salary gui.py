from tkinter import *


def HRA():
    no = int(en1.get())
    ans1 = no*10/100
    en2.insert(0,ans1)

def COMM():
    no = int(en1.get())
    ans2 = no*7/100
    en3.insert(0,ans2)

def PF():
    no = int(en1.get())
    ans3 = no*3/100
    en4.insert(0,ans3)


def NET():
    COMM
    HRA
    PF
    no = int(en1.get())
    print("en1=",en1)
    ans1 = no*10/100
    ans2 = no * 7 / 100
    ans3 = no * 3 / 100
    ans4 =ans1+ans2-ans3+ans1*10
    en2.insert(0,ans1)
    en3.insert(0, ans2)
    en4.insert(0, ans3)
    en5.insert(0, ans4)



root = Tk()
root.geometry("500x500")


lb=Label(root,text="name",width=30)
en=Entry(root,bd=2)
lb1=Label(root,text="salary",width=30)
en1=Entry(root,bd=2)
lb2=Label(root,text="HRA",width=30)
en2=Entry(root,bd=2,)
lb3=Label(root,text="Commission",width=30)
en3=Entry(root,bd=2)
lb4=Label(root,text="PF",width=30)
en4=Entry(root,bd=2)
lb5=Label(root,text="net pay",width=30)
en5=Entry(root,bd=2)
name1 = Button(root,text="Net pay",foreground="green",font=("agencu Fb",20),relief="solid",command=NET)


lb.place(x=50,y=50)
en.place(x=200,y=50)
lb1.place(x=50,y=100)
en1.place(x=200,y=100)
lb2.place(x=50,y=150)
en2.place(x=200,y=150)
lb3.place(x=50,y=200)
en3.place(x=200,y=200)
lb4.place(x=50,y=250)
en4.place(x=200,y=250)
lb5.place(x=50,y=300)
en5.place(x=200,y=300)
name1.place(x=200,y=350)


root.mainloop()