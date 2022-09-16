import tkinter as tk
from tkinter import ttk

# criar a janela raiz
root = tk.Tk()
root.title(' Departamento Python Tkinter')
root.geometry('400x200')

# configirar o layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# criar o treeview
tree = ttk.Treeview(root, columns=('text'), show='tree headings')
tree.heading('text', text='Departmentos', anchor='w')

# adicionar dados
tree.insert('', tk.END, values=('Administração'), iid=0, open=False)
tree.insert('', tk.END, values=('Logistica'), iid=1, open=False)
tree.insert('', tk.END, values=('Vendas'), iid=2, open=True)
tree.insert('', tk.END, values=('Financeiro'), iid=3, open=False)
tree.insert('', tk.END, values=('TI'), iid=4, open=False)

# adicionar dados filhos
tree.insert('0', tk.END, values=('Gabriel'), iid=5, open=False)
tree.insert('2', tk.END, values=('Danny'), iid=6, open=False)
tree.insert('2', tk.END, values=('Arthur'), iid=7, open=False)

tree.move(3, 2, 0)

tree.grid(row=0, column=0, sticky='nsew')

root.mainloop()