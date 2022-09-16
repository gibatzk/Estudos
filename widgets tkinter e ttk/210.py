from email import message
from select import select
import tkinter as tk
from tkinter import mainloop, ttk
from tkinter.messagebox import showinfo
from turtle import title

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')

selected_day = tk.StringVar()

def day_chaged(event):
    showinfo(title='Resultado', 
    message=f'Você selecionou {day_cb.get()}!'
)

day_cb = ttk.Combobox(root,
    state='readonly',
    textvariable=selected_day
)

day_cb['values'] = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
# day_cb.set('Segunda')
selected_day.set('Segunda')
day_cb.pack(fill=tk.X, padx=5, pady=5)
day_cb.bind('<<ComboboxSelected>>', day_chaged)


root.mainloop()