import tkinter as tk
from tkinter import mainloop, ttk

root = tk.Tk()
root.title('Label Widget')
root.geometry('600x400+650+300')

def executar():
    root.quit()

btn1 = ttk.Button(
    root,
    text='SAIR',
    command=executar
)
btn1.pack()
btn1.state(['!disabled'])

btn2 = ttk.Button(
    root,
    text='SAIR',
    command=lambda:root.quit()
)

btn2.pack()

btn3 = ttk.Button(
    root,
    text='DESABILITAR',
    command=lambda: btn1.state(['disabled'])
)

btn3.pack()

btn4 = ttk.Button(
    root,
    text='HABILITAR',
    command=lambda: btn1.state(['!disabled'])
)

btn4.pack()
root.mainloop()