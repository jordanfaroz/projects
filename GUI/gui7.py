from tkinter import *

top = Tk()
sb = Scrollbar (top, jump=False)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(top, yscrollcommand=sb.set)
for line in range (30):
    mylist.insert(END, "Number " + str (line))
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)
top.mainloop ()