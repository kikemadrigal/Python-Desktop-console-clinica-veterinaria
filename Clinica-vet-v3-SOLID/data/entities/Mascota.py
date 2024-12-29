class Mascota:
    """
    T_Mascota
    ---------
    Id 
    IdPropietario 
    Nombre 
    Tipo (Gato,Perro, Pajaro,Conejo,…) 
    Raza 
    Fecha nacimiento 
    Peso 
    Color - 
    Notas (Opcional)
    """
    def __init__(self, id, id_propietario, nombre, tipo, raza, fecha_nacimiento, peso, color, notas):
        self.id = id
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.color = color
        self.notas = notas
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
    def get_tipo(self):
        return self.tipo
    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_raza(self):
        return self.raza
    def set_raza(self, raza):
        self.raza = raza
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def get_peso(self):
        return self.peso
    def set_peso(self, peso):
        self.peso = peso
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    def get_notas(self):
        return self.notas
    def set_notas(self, notas):
        self.notas = notas
    def __str__(self):  
        return f"Id: {self.get_id()} - id_propietario: {self.get_id_propietario()} - nombre: {self.get_nombre()} - tipo: {self.get_tipo()} - raza: {self.get_raza()} - fecha_nacimiento: {self.get_fecha_nacimiento()} - peso: {self.get_peso()} - color: {self.get_color()} - notas: {self.get_notas()}"
    