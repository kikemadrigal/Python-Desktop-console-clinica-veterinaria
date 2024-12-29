class Visita:
    """
    T_Visita
    --------
    Id o NumeroVisita 
    IdMascota 
    Fecha de la visita 
    Descripción 
    Tratamiento
    """
    def __init__(self, id, id_mascota, fecha_visita, descripcion, tratamiento):
        self.id=id
        self.id_mascota=id_mascota
        self.fecha_visita=fecha_visita
        self.descripcion=descripcion
        self.tratamiento=tratamiento
    def get_id(self):
        return self.id
    def get_id_mascota(self):
        return self.id_mascota
    def set_id_mascota(self, id_mascota):
        self.id_mascota=id_mascota
    def get_fecha_visita(self):
        return self.fecha_visita
    def set_fecha_visita(self, fecha_visita):
        self.fecha_visita=fecha_visita
    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    def get_tratamiento(self):
        return self.tratamiento
    def set_tratamiento(self, tratamiento):
        self.tratamiento=tratamiento
    def __str__(self):  
        return f"id: {self.id} - mascota: {self.id_mascota} - visita: {self.fecha_visita} - descripcion: {self.descripcion} - tratamiento: {self.tratamiento}"
    