from ctypes.wintypes import HENHMETAFILE
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from turtle import width


root = tk.Tk()
root.title('Python Tkinter')

st = ScrolledText(root, width=50, height=10, font='Arial 24')

st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)







root.mainloop()