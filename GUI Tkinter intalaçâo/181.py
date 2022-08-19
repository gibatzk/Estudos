import tkinter as tk
from tkinter import mainloop, ttk

root = tk.Tk()
root.title('Label Widget')
root.geometry('600x400+650+300')

labe1 = ttk.Label(
    root,
    text='Label temático',
    font='Arial 30 ',
    underline=1,
    borderwidth=100,
    relief='groove',
    # width=15,
    wraplength=150,
    cursor='hand2'
    
)
labe1.pack()

labe2 = tk.Label(
    root,
    text='Label padrão\nlinha2\nlinha3',
    font='Arial 24 underline',
   
    borderwidth=10,
    relief='solid',
    width=14,
#     height=5,
#     wraplength=50
    wraplength=200
  )
labe2.pack()
root.mainloop()