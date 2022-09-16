import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('620x300+750+350')

# Definir as colunas
columns = ('nome', 'sobrenome', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')
# 'tree', 'headings', 'tree headings', ''

# Definir cabeçalhos
tree.heading('nome', text='Nome')
tree.heading('sobrenome', text='Sobrenome')
tree.heading('email', text='Email')

# Gerar dados de exemplo
contacts = []
for n in range(1, 100):
    contacts.append((f'nome {n}', f'sobrenome {n}', f'email{n}@exemplo.com'))

# Adicionar dados na tabela
tree.insert("", tk.END, values=('Gilberto', 'Tezuka', 'giba@email.com'))
tree.insert('', tk.END, values=('Lillian', 'Duarte', 'lilli@email.com'))
tree.insert('', tk.END, values=('Robin', 'Tezuka', 'robin@email.com'))
tree.insert('', tk.END, values=('Beatriz', 'Silva', 'bia@email.com'))
tree.insert('', tk.END, values=('Lucas', 'Silva', 'lucas@email.com'))

for contact in contacts:
    tree.insert('', tk.END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)

tree.bind("<<TreeviewSelect>>", item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# Adicionar barra de rolagem
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# rodar a aplicação
root.mainloop()