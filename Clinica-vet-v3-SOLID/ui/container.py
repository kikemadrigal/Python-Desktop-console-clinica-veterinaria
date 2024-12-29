from tkinter import *
import tkinter as tk
from ui.propietarios import Propietarios
from ui.mascotas import Mascotas


class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        #Esta ventana container, se va a mostrar en la ventana window
        self.pack()
        self.place(x=0,y=0,width=800,height=400)
        #self.config(bg="#c6d9e3")
        self.config(bg="#c6d9e3")
        self.widgets()
    
    def show_frames(self, container):
        #Vamos a crear una ventana para propietarios y otra para mascotas
        top_level=tk.Toplevel(self)
        frame=container(top_level)
        frame.config(bg="#c6d9e3")   
        frame.pack(fill="both", expand=True)
        top_level.geometry("800x600+120+20")
        top_level.resizable(False, False)

    def propietarios(self):
        self.show_frames(Propietarios)

    def mascotas(self):
        self.show_frames(Mascotas)


    def widgets(self):
        frame1=tk.Frame(self, bg="#c6d9e3")
        frame1.pack(fill="both", expand=True)
        frame1.place(x=0,y=0,width=800,height=400)

        btn_propietarios=tk.Button(frame1, text="Propietarios", bg="#f4b400",fg="black", font="sans 18 bold", command=self.propietarios)
        btn_propietarios.place(x=500, y=50, width=240, height=50)

        btn_mascotas=tk.Button(frame1, text="Mascotas", bg="#f4b400",fg="black", font="sans 18 bold", command=self.mascotas)
        btn_mascotas.place(x=500, y=150, width=240, height=50)

        btn_visitas=tk.Button(frame1, text="Visitas", bg="#f4b400",fg="black", font="sans 18 bold")
        btn_visitas.place(x=500, y=250, width=240, height=50)

        btn_facturas=tk.Button(frame1, text="Facturas", bg="#f4b400",fg="black", font="sans 18 bold")
        btn_facturas.place(x=500, y=350, width=240, height=50)