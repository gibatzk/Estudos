from distutils.cmd import Command
import tkinter as tk
from tkinter.tix import COLUMN
from tkinter import ttk

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')

pb = ttk.Progressbar(
    root,
    orient='horizontal', #vertical
    length=300,
    mode='determinate' #inderteminate

)

pb.pack()

pb.start(50)

root.mainloop()