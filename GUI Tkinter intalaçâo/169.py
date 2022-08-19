import tkinter as tk
from tkinter import ttk
from turtle import back

root = tk.Tk()
root.title('MInha Aplicação GUI')
root.geometry('600x400+500+200')

def select(arg):
    root.config(background=arg)

btn1 = ttk.Button(
    root, 
    text= 'Vermelho',
    command=lambda:select('red')
    )

btn1.pack()

btn2 = ttk.Button(
    root, 
    text= 'Verde',
    command=lambda:select('green')
    )

btn2.pack()

btn3 = ttk.Button(
    root, 
    text= 'Azul',
    command=lambda:select('blue')
    )

btn3.pack()

root.mainloop()