from tkinter import *


def sqr():
    en1.delete(0,END)
    no = int(en.get())
    ans = no*no
    en1.insert(0,ans)


def cbe():
    en1.delete(0,END)
    no = int(en.get())
    ans1 = no*no*no
    en1.insert(0,ans1)

root = Tk()
root.geometry("500x500")


lb=Label(root,text="Number 1",width=30)
en=Entry(root,bd=2)
name1 = Radiobutton(root,text="square",foreground="green",font=("agencu Fb",20),relief="solid",command=sqr,)
name2 = Radiobutton(root,text="cube",foreground="green",font=("agencu Fb",20),relief="solid",command=cbe,)
ans=Label(root,text="Answer",width=30)
en1=Entry(root,bd=2)



lb.grid(row=0,column=0)
en.grid(row=0,column=1,pady=50)
name1.grid(row=1,column=0)
name2.grid(row=1,column=2)
ans.grid(row=2,column=0)
en1.grid(row=2,column=1,pady=50)


root.mainloop()