from email import message
from msilib.schema import ListBox
from select import select
import tkinter as tk
from tkinter import Scrollbar, mainloop, ttk
from tkinter.messagebox import showinfo
from turtle import title

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('600x400+750+350')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


langs = ('Java', 'C', 'C#', 'C++', 'Python', 'Go', 'Php', 'JavaScript')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    font="Arial 15",
    selectmode='extended',#'browse'
)

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.grid(
    column=1,
    row=0,
    sticky='ns'
)

def items_selected(event):
    selected_indices = listbox.curselection()
    for i in selected_indices:
        print(listbox.get(i))

listbox.bind('<<ListboxSelect>>', items_selected)


root.mainloop()