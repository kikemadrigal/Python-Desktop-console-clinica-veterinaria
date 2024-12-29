from entities.visita import Visita

class Visitas:
    def __init__(self, sqliteClient):
        self.conexion = sqliteClient.get_conexion()
        self.cursor = sqliteClient.get_cursor()
        self.visitas=[]

    def crear_visita(self, visita):
        """
        Inserta una visita en la base de datos

        Args:
            visita (Visita): Visita a insertar
        """
        self.cursor.execute("insert into T_Visita values (?,?,?,?,?);",
                            (
                                visita.get_id(),
                                visita.get_id_mascota(),
                                visita.get_fecha_visita(),
                                visita.get_descripcion(),
                                visita.get_tratamiento()
                                )
                            )
        self.conexion.commit()

    def modificar_visita(self, visita):
        """
        Modifica una visita
        """
        self.cursor.execute("""update T_Visita set id_mascota=?, fecha_visita=?, descripcion=?, tratamiento=? where id=?;""",
                            (
                                visita.get_id_mascota(),
                                visita.get_fecha_visita(),
                                visita.get_descripcion(),
                                visita.get_tratamiento(),
                                visita.get_id()
                            )
                        )
        self.conexion.commit()
    def get_all_visitas(self):
        tuplas= self.cursor.execute("select * from T_Visita").fetchall()
        if len(tuplas)==0:
            return []
        visitas=[]
        for tupla in tuplas:
            visita=Visita(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4])
            visitas.append(visita)
        return visitas
    def delete_visita(self,id):
        self.cursor.execute(f"DELETE FROM T_Visita WHERE id=?;",(id,))
        self.conexion.commit()
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
    def dame_visita_por_id_visita(self,id:int):
        """
        Devuelve una visita dado el id de la mascota
        """
        self.cursor.execute("select * from T_Visita where id = ?;",(id,))
        tupla=self.cursor.fetchone()
        if tupla==None:
            return None
        return Visita(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4])
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
    def eliminar_visita(self,id):
        self.cursor.execute(f"DELETE FROM T_Visita WHERE id=?;",(id,))
        self.conexion.commit()