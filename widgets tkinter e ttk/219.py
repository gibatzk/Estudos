from distutils.cmd import Command
import tkinter as tk
from tkinter.tix import COLUMN
from tkinter import ttk

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')

lf = ttk.Labelframe(root, text='Alinhamento', labelanchor='nw')
lf.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()

rb1 = ttk.Radiobutton(lf, text='Esquerda',value='E' , variable=alignment_var)
rb1.grid(column=0, row=0, padx=10, pady=10)

rb1 = ttk.Radiobutton(lf, text='Cetro',value='C' ,variable=alignment_var)
rb1.grid(column=1, row=0, padx=10, pady=10)

rb1 = ttk.Radiobutton(lf, text='Direita',value='D' ,variable=alignment_var)
rb1.grid(column=2, row=0, padx=10, pady=10)
 

root.mainloop()