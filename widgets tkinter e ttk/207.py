import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')

ttk.Label(
    root,
    text='Primeiro Label',
    font='Arial 24'
).pack()

separador = ttk.Separator(root,orient='horizontal')
separador.pack(fill='x')

ttk.Label(
    root,
    text='Segundo Label',
    font='Arial 24'
).pack()

root.mainloop()