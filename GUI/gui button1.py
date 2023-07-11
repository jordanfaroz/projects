from tkinter import *

def test():
    if ln.get ==1:
        lbldisplay.configure(text="java")
    if ln.get ==2:
        lbldisplay.configure(text="python")


root =Tk()
root.geometry("500x500")

ln=IntVar()

lblshow=Label(root,text="select your education",font="bold 20",borderwidth=20,bg="red")
jradio=Radiobutton(root,text="java",font="bold 12",variable=ln,command=test,value=1)
pradio=Radiobutton(root,text="python",font="bold 12",variable=ln,command=test,value=2)
phradio=Radiobutton(root,text="php",font="bold 12",variable=ln,command=test,value=3)
lbldisplay=Label(root,font="bold 30",fg="red")

lblshow.pack()
jradio.pack()
pradio.pack()
phradio.pack()
lbldisplay.pack()

root.mainloop()