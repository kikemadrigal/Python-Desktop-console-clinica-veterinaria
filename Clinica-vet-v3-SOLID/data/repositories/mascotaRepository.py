from data.repositories.Repository import Repository
from data.entities.Mascota import Mascota
# utils para formatear los textos y floats
from utils.utils import *
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
class MascotaRepository(Repository):
    """
    Representa las consultas a la base de datos de la tabla Mascota

    """
    def __init__(self, sqlite3Client, table_name="T_Mascota"):
        super().__init__(sqlite3Client, table_name)


    def get_all(self)->list:
        """
        Devuelve una lista de mascotas llamando primero a su padre

        Returns:
            list: Una lista de mascotas
        """
        tuplas=super().get_all()
        mascotas=[]
        for tupla in tuplas:
            mascotas.append(Mascota(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8]))
        return mascotas
    def get_last_id(self):
        """
        Devuelve el id de la ultima mascota introducida
        """
        self.cursor.execute("select max(id) from T_Mascota;")
        return self.cursor.fetchone()[0]

    def dame_mascotas_por_campo(self,campo, valor):
        """
        Devuelve una lista de mascotas segun el campo y el valor

        Args:
            campo (str): El campo por el que buscar
            valor (str): El valor del campo
        
        Returns:
            list: Una lista de mascotas
        """
        #Formateamos el nombre para poder tratarlo mejor
        if campo=="id":
            self.cursor.execute("select * from T_mascota where id = ?;",(valor,))
        elif campo=="nombre":
            campo=campo.capitalize().strip()
            self.cursor.execute("select * from T_mascota where nombre like ?;",("%"+valor+"%",))
            #self.cursor.execute("select * from T_Mascota where nombre = ?;",(valor,))
        elif campo=="tipo":
            self.cursor.execute("select * from T_mascota where tipo = ?;",(valor,))
        elif campo=="raza":
            self.cursor.execute("select * from T_mascota where raza = ?;",(valor,))
        elif campo=="fecha_nacimiento":
            self.cursor.execute("select * from T_mascota where fecha_nacimiento = ?;",(valor,))
        elif campo=="peso":
            self.cursor.execute("select * from T_mascota where peso = ?;",(valor,))
        elif campo=="color":
            self.cursor.execute("select * from T_mascota where color like ?;",("%"+valor+"%",))
        tuplas=self.cursor.fetchall()
        if len(tuplas)==0:
            return None
        else:
            mascotas=[]
            for mascota in tuplas:
                mascotas.append(Mascota(mascota[0],mascota[1],mascota[2],mascota[3],mascota[4],mascota[5],mascota[6],mascota[7],mascota[8]))
            return mascotas
        
    def dame_mascotas_por_tipo_agrupadas_por_raza(self, tipo):
        """
        Devuelve una lista de mascotas agrupadas por tipo, raza y contador

        Args:
            tipo (str): El tipo de mascotas que se quieren mostrar

        Returns:
            list: Una lista de tuplas (raza, tipo)
        """

        self.cursor.execute("""select tipo,raza,count(*) 
                            from T_Mascota 
                            where tipo=? 
                            group by raza 
                            order by tipo desc;""",(tipo,))
        return self.cursor.fetchall()
    
    
    def comprobar_existe_propietario(self,id_o_nombe, valor):
        """
        Método utilizado en pedir_mascota y pedir_mascota_conservando_la_que_habia para comprobar si el propietario existe o no

        Args:
            id_o_nombe (str): El campo por el que buscar
            valor (str): El valor del campo

        Returns:    
            bool: True si el propietario existe, False en caso contrario
        """
        if id_o_nombe=="id":
            self.cursor.execute("""select p.id 
                                from T_Propietario p 
                                inner join T_Mascota m 
                                on m.id_propietario=p.id
                                WHERE p.id=?;""",(valor,))
        elif id_o_nombe=="nombre":
            self.cursor.execute("""select p.id 
                                from T_Propietario p 
                                inner join T_Mascota m 
                                on m.id_propietario=p.id
                                WHERE p.nombre=?;""",(valor,)) 
            
        propietario=self.cursor.fetchone()
        if propietario==None:
            return False
        return True
    def dame_mascotas_por_nombre_propietario(self, nombre_propietario):
        self.cursor.execute("""select m.id, m.id_propietario,m.nombre, m.tipo, m.raza, m.fecha_nacimiento, m.peso, m.color, m.notas
                        from T_Propietario p
                        inner join T_Mascota m
                        on m.id_propietario=p.id
                        where p.nombre=?
                        order by p.nombre;""",(nombre_propietario,))
        tuplas=self.cursor.fetchall()
        if len(tuplas)==0:
            return None
        else:
            mascotas=[]
            for tupla in tuplas:
                mascotas.append(Mascota(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8]))
            return mascotas
    def dame_10_primeros_mascotas_propietarios(self):
        """
        Devuelve una lista de tuplas (id, nombre) de los 10 primeros propietarios con mascotas
        """
        self.cursor.execute("""select distinct p.id, p.nombre 
                            from T_Mascota m 
                            inner join T_Propietario p 
                            on m.id_propietario=p.id
                            order by p.id
                            limit 10;""")
        tuplas=self.cursor.fetchall()
        return tuplas
    def dame_tipos(self):
        self.cursor.execute("select distinct tipo from T_Mascota;")
        return self.cursor.fetchall()
    
    




















































