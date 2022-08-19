import tkinter as tk
from tkinter import ttk

def log(event):
    print('Evento disparo....')

root = tk.Tk()
root.title('Minha aplicação GUI')
root.geometry('600x400+500+200')

btn1 = ttk.Button(root, text='Executar')
btn1.bind('<Any-KeyPress>', log)
btn1.focus()
btn1.pack()

btn2 = ttk.Button(
    root,
    text='Desvincular evento de executar',
    command=lambda: btn1.unbind('<Any-KeyPress>')
)
btn2.pack(

)
btn3 = ttk.Button(
    root,
    text='Vincular evento de executar',
    command=lambda: btn1.bind('<Any-KeyPress>', log)
)
btn3.pack()

root.mainloop()