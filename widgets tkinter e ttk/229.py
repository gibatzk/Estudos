import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('620x300+750+350')

# Definir as colunas
columns = ('nome', 'sobrenome', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')

# Definir cabeçalhos
tree.heading('nome', text='Nome', anchor=tk.W)
tree.heading('sobrenome', text='Sobrenome', anchor=tk.W)
tree.heading('email', text='Email', anchor=tk.W)

tree.column('nome', width=100, anchor=tk.W)
tree.column('sobrenome', width=100, anchor=tk.W)
tree.column('email', width=300, anchor=tk.CENTER)


# Adicionar dados na tabela
tree.insert('', tk.END, values=('Gilberto', 'Tezuka', 'giba@email.com'))
tree.insert('', tk.END, values=('Lillian', 'Duarte', 'lilli@email.com'))
tree.insert('', tk.END, values=('Arthur', 'Maciel', 'arthur@email.com'))
tree.insert('', tk.END, values=('Beatriz', 'Silva', 'bia@email.com'))
tree.insert('', tk.END, values=('Lucas', 'Silva', 'lucas@email.com'))

tree.grid(row=0, column=0, sticky='nsew')

# rodar a aplicação
root.mainloop()