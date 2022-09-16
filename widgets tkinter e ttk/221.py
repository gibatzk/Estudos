from distutils.cmd import Command
import tkinter as tk
from tkinter.tix import COLUMN
from tkinter import ttk
from tracemalloc import start

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')
root.grid()

pb = ttk.Progressbar(
    root,
    orient='horizontal', #vertical
    length=300,
    mode='indeterminate' #derteminate

)

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

start_button = ttk.Button(
    root,
    text='Start',
    command=lambda:pb.start(10)
)

start_button.grid(column=0,row=1, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=lambda: pb.stop()
)
stop_button.grid(column=1,row=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()