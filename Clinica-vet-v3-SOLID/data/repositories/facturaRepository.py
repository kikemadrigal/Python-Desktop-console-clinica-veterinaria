from data.entities.Factura import Factura
from data.repositories.Repository import Repository
from utils.utils import *
"""
Factura
--------
Id
Id_visita
precio
"""
class FacturaRepository(Repository):
    def __init__(self, sqlite3Client, table_name="T_Factura"):
        super().__init__(sqlite3Client, table_name)


    def get_all(self):
        tuplas= super().get_all()
        if len(tuplas)==0:
            return []
        facturas=[]
        for tupla in tuplas:
            factura=Factura(tupla[0],tupla[1],tupla[2])
            facturas.append(factura)
        return facturas
    



    def dame_factura_por_id(self,id):
        self.cursor.execute(f"select * from T_Factura where id=?;",(id,))
        tuple=self.cursor.fetchone()
        factura=Factura(tuple[0],tuple[1],tuple[2])
        return factura
    def dame_facturas_por_id_visita(self,nombre):
        self.cursor.execute(f"select * from T_Factura where nombre=?;",(nombre,))
        factura=self.cursor.fetchone()
        return factura
    def mostrar_facturas(self):

        self.cursor.execute("select * from T_Factura;")
        propietarios=self.cursor.fetchall()
        if len(propietarios)==0:
            print("No hay propietarios")
        else:
            for propietario in propietarios:
                print(propietario)
    def comprobar_existe_visita(self,id_visita):
        self.cursor.execute("""select v.id 
                            from T_Factura f 
                            inner join T_Visita v 
                            on f.id_visita=v.id
                            WHERE v.id=?;""",(id_visita,))
        visita=self.cursor.fetchone()
        if visita==None:
            return False
        return True
    def dame_facturas_visitas_por_id_visita(self, id_visita):
        """
        T_Visita
        ----------
        Id o NumeroVisita 
        IdMascota 
        Fecha de la visita 
        Descripción 
        Tratamiento
        """
        self.cursor.execute("""
                    SELECT  v.id,v.fecha_visita,f.id
                    FROM T_Factura f
                    INNER JOIN T_Visita v
                    ON f.id_visita=v.id
                    WHERE v.id=?;""",(id_visita,))
        facturas_visitas= self.cursor.fetchall()
        return facturas_visitas
    def dame_10_primeros_id_de_facturas_visitas(self):
        self.cursor.execute("""select distinct m.id 
                            from T_Visita v 
                            inner join T_mascota m 
                            on v.id_mascota=m.id
                            order by m.id
                            limit 10;""")
        tuplas=self.cursor.fetchall()
        return tuplas
    def comprobar_existe_visita(self,id_visita):
        self.cursor.execute("""select v.id 
                            from T_Factura f
                            inner join T_Visita v
                            on f.id_visita=v.id
                            WHERE v.id=?;""",(id_visita,))
        visita=self.cursor.fetchone()
        if visita==None:
            return False
        return True

















    














