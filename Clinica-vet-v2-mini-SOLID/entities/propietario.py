class Propietario:
    """
        T_Propietario
        -------------
        Nombre 
        DNI 
        Fecha nacimiento 
        Dirección 
        Correo electrónico 
    """
    def __init__(self, id, nombre, dni, fecha_nacimiento, direccion, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.correo_electronico = correo_electronico
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def get_id_propietario(self):   
        return self.id_propietario
    def set_id_propietario(self, id_propietario):
        self.id_propietario = id_propietario
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_dni(self):
        return self.dni
    def set_dni(self, dni):
        self.dni = dni
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion
    def get_correo_electronico(self):
        return self.correo_electronico
    def set_correo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def __str__(self):  
        return f"id: {self.get_id()} - nombre: {self.get_nombre()} - dni: {self.get_dni()} - fecha_nacimiento: {self.get_fecha_nacimiento()} - direccion: {self.get_direccion()} - correo_electronico: {self.get_correo_electronico()}"
    