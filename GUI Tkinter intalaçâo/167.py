import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('MInha Aplicação GUI')
root.geometry('600x400+500+200')

ttk.Label(root, text='Olá Mundo!').pack()

#usando índice de dicionário usando widget
lbl1 = ttk.Label(root)
lbl1['text'] = 'Outro Olá Mundo!'
lbl1.pack()

#usando o método config() com atributos de palavra-chave
lbl2 = ttk.Label(root)
lbl2.config(text='Mais um Olá Mundo')
lbl2.pack()

root.mainloop()