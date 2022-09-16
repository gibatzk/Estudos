from distutils.cmd import Command
from tkinter import Tk, Text
from turtle import back
from tkinter import ttk


root = Tk()
root.title('Python Tkinter')

text = Text(
    root,
    height=8,
    width=10,
    font='Arial 24',
    background='yellow',
    foreground='red'
)
text.pack()

text.insert('1.0', 'Esta é um widget Text demo')
txt = text.get('1.0', 'end')
# text['state'] = 'normal'

ttk.Button(
    root,
    text='Ativar',
    command=lambda:text.config(state="normal")
).pack()

ttk.Button(
    root,
    text='Desativar',
    command=lambda:text.config(state="disabled")
).pack()

print(txt)
root.mainloop()