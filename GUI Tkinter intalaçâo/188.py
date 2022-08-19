
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Entry Widget')
root.geometry('600x400+650+300')

textbox = ttk.Entry(
    root
)
textbox.focus()
textbox.pack()

btn1 = ttk.Button(
    root,
    text='Executar',
    command=lambda :print(textbox.get())
)
btn1.pack()
root.mainloop()