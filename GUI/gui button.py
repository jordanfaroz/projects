from tkinter import *

def test():
    if ln.get() ==1:
        root.configure(bg="pink")
        lblcolor.configure(bg="pink")
    else:
            root.configure(bg="orange")
            lblcolor.configure(bg="orange")


root=Tk()
root.geometry("500x500")

ln=IntVar()

lblcolor=Label(root,text="change Background color",font="bold 20",borderwidth=20,bg="silver")
pradio=Checkbutton(root,text="pink",font="bold 12",variable=ln,command=test)
oradio=Checkbutton(root,text="orange",font="bold 12",command=test)



lblcolor.pack()
pradio.pack()
oradio.pack()
root.mainloop()