from data.entities.Visita import Visita
from data.repositories.Repository import Repository
from utils.utils import *
"""
T_Visita
----------
Id o NumeroVisita 
IdMascota 
Fecha de la visita 
Descripción 
Tratamiento
"""
class VisitaRepository(Repository):
    def __init__(self, sqlite3Client, table_name="T_Visita"):
        super().__init__(sqlite3Client, table_name)


   

    def get_all(self):
        """
        Devuelve una lista de visitas pero primero llamando a su padre
        """
        tuplas = super().get_all()
        visitas = []
        for tupla in tuplas:
            visitas.append(Visita(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]))
        return visitas


    def dame_visita_por_id_mascota(self,id):
        """
        Devuelve una visita dado el id de la mascota
        """
        self.cursor.execute("select * from T_Visita where id_mascota = ?;",(id,))
        tupla=self.cursor.fetchone()
        if tupla==None:
            return None
        return Visita(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5])
    def dame_visita_por_id_visita(self,id:int):
        """
        Devuelve una visita dado el id de la mascota
        """
        self.cursor.execute("select * from T_Visita where id = ?;",(id,))
        tupla=self.cursor.fetchone()
        if tupla==None:
            return None
        return Visita(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4])
      
    def dame_todas_las_visitas(self):
        """
        devuelve todas las visitas
        """
        visitas=[]
        self.cursor.execute("select * from T_Visita;")
        visitas=self.cursor.fetchall()
        if len(visitas)==0:
            print("No hay visitas")
        else:
            for visita in visitas:
                visita=Visita(visita[0],visita[1],visita[2],visita[3],visita[4],visita[5])
                visitas.append(visita)
        return visitas
    def dame_mascota_con_mas_visitas(self):
        self.cursor.execute("""
                   SELECT  COUNT(*),m.nombre
                   FROM T_Visita v
                   INNER JOIN T_Mascota m 
                   ON v.id_mascota=m.id
                   GROUP BY m.raza
                   ORDER BY COUNT(*) DESC;
                   """)
        lineas= self.cursor.fetchall()
        return lineas

    def dame_visitas_por_nombre_mascota(self, nombre_mascota):
        self.cursor.execute("""
                    SELECT v.id, v.id_mascota,v.fecha_visita,v.descripcion,v.tratamiento
                    FROM T_Visita v
                    INNER JOIN T_Mascota m
                    ON v.id_mascota=m.id
                    WHERE m.nombre like ?;""",("%" + nombre_mascota + "%",))
        tuplas= self.cursor.fetchall()
        if len(tuplas)==0:
            return None
        mascotas_propietarios=[]
        for tupla in tuplas:
            mascotas_propietarios.append(Visita(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4]))
        return mascotas_propietarios
    def dame_10_primeros_id_de_visitas_mascotas(self):
        """
        Devuelve los 10 primeros id y nombres de las mascotas que han tenido visitas

        returns:
            list: Una lista de tuplas
        """
        self.cursor.execute("""select distinct m.id, m.nombre 
                            from T_Visita v 
                            inner join T_mascota m 
                            on v.id_mascota=m.id
                            order by m.id
                            limit 10;""")
        tuplas=self.cursor.fetchall()
        return tuplas
    def comprobar_existe_mascota(self,id_mascota):
        """
        Comprueba si la mascota existe  

        Args:
            id_mascota (int): id de la mascota
        returns:
            bool: True si la mascota existe
        """
        self.cursor.execute("""select m.id 
                            from T_Visita v
                            inner join T_Mascota m 
                            on v.id_mascota=m.id
                            WHERE m.id=?;""",(id_mascota,))
        mascota=self.cursor.fetchone()
        if mascota==None:
            return False
        return True
    









































