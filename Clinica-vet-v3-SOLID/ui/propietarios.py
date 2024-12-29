from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class Propietarios(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        self.widgets()
    def widgets(self):
        #vamos a dividir la pantall en 2 una para el titulo y otra para los botones
        #Frame1 es el titulo
        frame1= tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0,y=0,width=self.padre.winfo_width(),height=100)

        
        titulo=tk.Label(self, text="Propietarios", bg="#dddddd", fg="black")
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)