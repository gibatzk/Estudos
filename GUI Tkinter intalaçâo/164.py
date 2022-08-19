import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('MInha Aplicação GUI')
root.geometry('600x400+500+200')

#ordem de empilhamento da janela sempre no topo
# root.attributes('-topmost',1)

# root.lift()#mover janela para cima

# root.lower()#mover para baixo na pilha

root.iconbitmap('GUI Tkinter intalaçâo/python.ico')

tk.Label(root, text="Label Classico").pack()
ttk.Label(root, text="Label Temático").pack()


tk.Button(root, text="Button Classico").pack()
ttk.Button(root, text="Button Temático").pack()



root.mainloop()