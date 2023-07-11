from tkinter import *

root = Tk()
root.geometry("500x500")


name = Label(root,text="black market",foreground="black",font=("agencu Fb",40),relief="solid")
name1 = Label(root,text="weed",foreground="green",font=("agencu Fb",20),relief="solid")
name2 = Label(root,text="ganja",foreground="brown",font=("agencu Fb",20),relief="solid")
name3 = Label(root,text="cocane",foreground="grey",font=("agencu Fb",20),relief="solid")



'''name.pack()
name1.pack()
name2.pack()
name3.pack()'''

'''name.grid(row=0,column=0)
name1.grid(row=1,column=0)
name2.grid(row=2,column=0)
name3.grid(row=3,column=0)'''

name.place(x=50,y=50)
name1.place(x=50,y=130)
name2.place(x=50,y=150)
name3.place(x=50,y=180)


root.mainloop()