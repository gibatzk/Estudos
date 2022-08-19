import tkinter as tk
from tkinter import mainloop, ttk

root = tk.Tk()
root.title('Label Widget')
root.geometry('600x400+650+300')

btnIcon =tk.PhotoImage(file='GUI Tkinter intalaçâo/imagem/download1.png')

btn1 = ttk.Button(
    root,
    image=btnIcon
)
btn1.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()