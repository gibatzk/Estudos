from logging import RootLogger
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def download_clicked():
    showinfo(
        title='Informação',
        message='Botão de downoad clicado'
    )

root = tk.Tk()
root.title('Button Widget')
root.geometry('600x400+650+300')

btnIcon = tk.PhotoImage(file='GUI Tkinter intalaçâo\imagem\download3.png')

btn1 = ttk.Button(
    root,
    image = btnIcon,
    text = 'Download',
    compound=tk.TOP,#right,top,buttom,left
    command=download_clicked
)

btn1.pack(ipadx=5, ipady=5,expand=True)

root.mainloop()