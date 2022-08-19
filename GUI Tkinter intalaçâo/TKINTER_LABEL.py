import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Label Widget')
root.geometry('600x400+500+200')

label1 = ttk.Label(
    root,
    text='Este é um Label\nCurso Python Tkinter',
    # font='Arial 15 bold'#tipos de letras
    font=('Verdana', 25, 'bold', 'italic'),
    background='yellow',
    foreground='red',
    padding=20,
    width=25,
    justify='left',#right,left
    anchor=tk.E#N S E W NE NW SE SW CENTER
    )
label1.pack()

foto = tk.PhotoImage(file='GUI Tkinter intalaçâo/imagem/saitama.png')

label2 = ttk.Label(
        root,
        image=foto,
        text='Homem de um soco só',
        font='Arial 15',
        compound='left'
)
label2.pack()

root.mainloop()
