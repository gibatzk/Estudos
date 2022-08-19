from logging import root
import tkinter as tk
from turtle import window_height, window_width

# tk._test()
root = tk.Tk()

root.title("Minha Aplicação GUI")
lbl = tk.Label(root, text="Olá, Mundo!")
lbl.pack()
window_width = 300
window_height = 200
#obter as dimensões da telas
screen_width = root.winfo_screenwidth()
screnn_height = root.winfo_screenheight()
#encontrar o ponto central
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screnn_height / 2 - window_height / 2)

#definir a posição da janela no centro da tela

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.mainloop()
