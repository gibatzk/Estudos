from select import select
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')

selected_size = tk.StringVar()

ttk.Label(
    root,
    text='Qual é o tamanho da sua camiseta?'
).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text='Pequeno',
    value='p',
    variable=selected_size

).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text='Médio',
    value='m',
    variable=selected_size

).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text='Grande',
    value='g',
    variable=selected_size

).pack(fill='x', padx=5, pady=5)

ttk.Button(
    root,
    text='Obter o tamanho selecionado',
    command=lambda: showinfo(title='Resultado', message=selected_size.get())
).pack(fill='x', padx=5, pady=5)

root.mainloop()