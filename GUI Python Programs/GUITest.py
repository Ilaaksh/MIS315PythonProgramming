from tkinter import *
from tkinter import ttk

root = Tk() #stores constructor object
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()