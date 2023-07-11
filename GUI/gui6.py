from tkinter import *

root=Tk()
root.geometry("500x500")

f1= Frame(root,bg="yellow")
ms = Message(f1,text="hello yo hola grasias",fg="red",relief="sunken")
f1.pack(side=TOP,pady=100)

ms.pack(padx=20,pady=20)


root.mainloop()
