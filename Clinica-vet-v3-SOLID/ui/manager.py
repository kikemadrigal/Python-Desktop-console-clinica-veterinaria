from tkinter import Tk, Frame
from ui.container import Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Veterinaria Avanza Plus")
        self.geometry("800x600+120+20")
        self.resizable(False, False)
        self.configure(bg="#c6d9e3")

        # El container es de tipo frame
        self.container = Frame(self, bg="#c6d9e3")
        # Lo empquetamos en la ventana, fill es para que se expanda y expand es para que se expanda verticalmente
        self.container.pack(fill="both", expand=True)

        # Aquí se alamcenerán todoas las ventanas o frames
        # Fijate que son diccionarios
        self.frames = {
            Container: None
        }

        self.load_frames()
        # Cuando se cargue el manager la primera ventana se muestra la ventana Container
        self.show_frame(Container)
    def load_frames(self):
        # Obtenemos los elementos del diccionario frames
        for ContainerClass in self.frames.keys():
            # Se crean instancias de Container que tiene en el constructor el padre y el controlador o manager
            frame=ContainerClass(self.container, self)
            self.frames[ContainerClass] = frame
    def show_frame(self, frameClass):
        frame = self.frames[frameClass]
        #Con esto se trae las ventanas que se están creando, al frame
        frame.tkraise()

        