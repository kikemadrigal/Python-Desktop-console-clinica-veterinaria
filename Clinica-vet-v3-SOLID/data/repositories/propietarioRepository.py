from data.entities.Propietario import Propietario
from data.repositories.Repository import Repository

class PropietarioRepository(Repository):
    """
    T_Propietario
    -------------
    Id
    Nombre 
    DNI 
    Fecha nacimiento 
    Dirección 
    Correo electrónico 
    """
    def __init__(self, sqlite3Client, table_name="T_Propietario"):
        super().__init__(sqlite3Client, table_name)

    def get_all(self):
        """
        Devuelve una lista de propietarios que primero obtiene los datos llamando al método del padre get_all
        """
        propietarios=[]
        tuplas=super().get_all()
        for tupla in tuplas:
            propietarios.append(Propietario(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5]))
        return propietarios
    def get_last_id(self):
        self.cursor.execute("select max(id) from T_Propietario;")
        return self.cursor.fetchone()[0]
    def dame_propietarios_por_campo(self,campo,value):
        propietarios=[]
        if campo=="id":
            self.cursor.execute("select * from T_Propietario where id = ?;",(value,))
        elif campo=="nombre":
            self.cursor.execute("select * from T_Propietario where nombre like ?;",("%"+value+"%",))
        elif campo=="dni":
            self.cursor.execute("select * from T_Propietario where dni like ?;",("%"+value+"%",))

        tuplas=self.cursor.fetchall()
        if len(tuplas)==0:
            return None
        else:
            for propietario in tuplas:
                propietarios.append(Propietario(propietario[0],propietario[1],propietario[2],propietario[3],propietario[4],propietario[5]))
            return propietarios

    
    
    def comprobar_existe_propietario_name(self, propietario_name)->bool:
        self.cursor.execute("select * from T_Propietario where nombre=?;",(propietario_name,))
        propietarios=self.cursor.fetchall()
        if len(propietarios)==0:
            return False
        return True
    def comprobar_existe_propietario_dni(self, propietario_dni)->bool:
        self.cursor.execute("select * from T_Propietario where dni=?;",(propietario_dni,))
        propietarios=self.cursor.fetchall()
        if len(propietarios)==0:
            return False
        return True
    def dane_mascotas_de_un_nombre_propietario(self, propietario_name):
        self.cursor.execute("""
                    SELECT p.id, p.nombre,m.id,m.nombre,m.tipo, m.raza 
                    FROM T_Mascota m 
                    INNER JOIN T_Propietario p ON m.id_propietario=p.id
                    WHERE p.nombre=?;""",(propietario_name,))
        mascotas_propietarios= self.cursor.fetchall()
        return mascotas_propietarios
    
    def dane_mascotas_de_un_id_propietario(self, propietario_id):
        """
       Devuleve una lista de tuplas con las mascotas de un propietario

        Args:
            propietario_id (int): El ID del propietario

        Returns:
            list: Una lista de tuplas con los datos de las mascotas
        """
        self.cursor.execute("""
                    SELECT p.id, p.nombre,m.id,m.nombre,m.tipo, m.raza 
                    FROM T_Mascota m    
                    INNER JOIN T_Propietario p 
                    ON m.id_propietario=p.id
                    WHERE p.id=?;""",(propietario_id,))
        tuplas= self.cursor.fetchall()
        return tuplas
    def dane_mascotas_de_un_dni_propietario(self, propietario_dni):
        self.cursor.execute("""
                    SELECT p.id, p.nombre,m.id,m.nombre,m.tipo, m.raza 
                    FROM T_Mascota m 
                    INNER JOIN T_Propietario p 
                    ON m.id_propietario=p.id
                    WHERE p.dni=?;""",(propietario_dni,))
        mascotas_propietarios= self.cursor.fetchall()
        return mascotas_propietarios
    def dame_5_primeros_id_de_propietarios(self)->list:
        propietarios=[]
        self.cursor.execute("select * from T_Propietario order by id  limit 5;")
        tuplas=self.cursor.fetchall()
        for tupla in tuplas:
            propietario=Propietario(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5])
            propietarios.append(propietario)
        return propietarios
    def dane_las_5_primeras_mascotas_propietario(self):
        self.cursor.execute("""
                    SELECT COUNT(*),p.id, p.nombre,m.id,m.nombre,m.tipo, m.raza 
                    FROM T_Mascota m 
                    INNER JOIN T_Propietario p 
                    ON m.id_propietario=p.id
                    GROUP BY p.nombre
                    ORDER BY COUNT(*) DESC
                    LIMIT 5;""")
        mascotas_propietarios= self.cursor.fetchall()
        return mascotas_propietarios
 

    


    

































