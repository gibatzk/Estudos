import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# janela.metodo(largura, altura)
# root.resizable(True, True)
# root.minsize(300, 200)
# root.maxsize(800, 600)
print('------------------------------------------------')
#apresentação maximizada
# root.state('zoomed')
#apresentar minimizada
# root.state('iconic')
# root.state('normal')

# print(root.state())
root.attributes("-alpha", 0.5)#transparencia da janela


root.mainloop()
