import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Entry Widget")
root.geometry("400x200+650+300")

def btn1_clicked(event=None):
    if texto.get() != "insira seu nome...":
        msg = f"Bem vindo(a) {texto.get()}!"
        showinfo(title="Informação", message=msg)
        texto.set("insira seu nome...")
        textBox.select_range(0, tk.END)
        textBox.focus()

# armazena os valores dos textbox
texto = tk.StringVar()
texto.set("insira seu nome...")

textBox = ttk.Entry(
    root,
    textvariable=texto,
    font="Arial 24 italic"
)
textBox.select_range(0, tk.END)
textBox.focus()
textBox.bind("<Return>", btn1_clicked)
textBox.pack()

btn1 = ttk.Button(
    root, 
    text="Executar", 
    command=btn1_clicked
    )
btn1.pack()

root.mainloop()
