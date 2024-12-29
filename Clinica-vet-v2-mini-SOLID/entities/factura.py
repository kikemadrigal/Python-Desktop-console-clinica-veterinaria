class Factura:
    """
    T_Factura
    --------
    Id o NumeroFactura 
    IdVisita 
    Precio o Factura
    """
    def __init__(self, id, id_visita, precio:float):
        self.id=id
        self.id_visita=id_visita
        self.precio=precio
    def get_id(self):
        return self.id
    def get_id_visita(self):
        return self.id_visita
    def set_id_visita(self, id_visita):
        self.id_visita=id_visita
    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio=precio

    def __str__(self):  
       return f"Id: {self.id} - id_visita: {self.id_visita} - precio: {self.precio}"
    