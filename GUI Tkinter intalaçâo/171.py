import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print('Tecla ENTER pressionada')

def log(event):
    print(event)
    print(f'keysym....: {event.keysym}')
    print(f'keysym....: {event.keycode}')
    print(f'keysym_num....: {event.keysym_num}')
    print(f'char....: {event.char}')




root = tk.Tk()
root.title('MInha Aplicação GUI')
root.geometry('600x400+500+200')

btn1 = ttk.Button(root, text='Executar!')
# btn1.bind('<Return>', return_pressed)
btn1.bind('<Any-KeyPress>', log)
btn1.focus()
btn1.pack(expand=True)
root.mainloop()