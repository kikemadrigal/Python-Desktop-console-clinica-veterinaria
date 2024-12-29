from entities.propietario import Propietario

class Propietarios:
    def __init__(self, sqliteClient):
        self.conexion = sqliteClient.get_conexion()
        self.cursor = sqliteClient.get_cursor()
        self.propietarios=[]
    def crear_propietario(self, propietario):
        self.cursor.execute("insert into T_Propietario values (?,?,?,?,?,?);",
                                (
                                    propietario.get_id(),
                                    propietario.get_nombre(),
                                    propietario.get_dni(),
                                    propietario.get_fecha_nacimiento(),
                                    propietario.get_direccion(),
                                    propietario.get_correo_electronico()
                                )
                            )
        self.conexion.commit()
    def modificar_propietario(self, propietario):
        self.cursor.execute("""update T_Propietario set nombre=?, dni=?, fecha_nacimiento=?, direccion=?, correo_electronico=? where id=?;""",
                                (
                                    propietario.get_nombre(),
                                    propietario.get_dni(),
                                    propietario.get_fecha_nacimiento(),
                                    propietario.get_direccion(),
                                    propietario.get_correo_electronico(),
                                    propietario.get_id()
                                )
                                )
                        
        self.conexion.commit()
    def get_all_propietarios(self):
        tuplas= self.cursor.execute("select * from T_Propietario").fetchall()
        if len(tuplas)==0:
            return []
        propietarios=[]
        for tupla in tuplas:
            propietario=Propietario(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5])
            propietarios.append(propietario)
        return propietarios

    def mostrar_mascotas_propietario(self, propietario):
        self.cursor.execute("select * from T_Mascota where id_propietario=?;",(propietario.get_id(),))
        print(self.cursor.fetchall())

    def comprobar_existe_propietario_name(self,propietario_name)->bool:
        self.cursor.execute("select * from T_Propietario where nombre=?;",(propietario_name,))
        propietarios=self.cursor.fetchall()
        if len(propietarios)==0:
            return False
        return True
    def comprobar_existe_propietario_dni(self,propietario_dni)->bool:
        self.cursor.execute("select * from T_Propietario where dni=?;",(propietario_dni,))
        propietarios=self.cursor.fetchall()
        if len(propietarios)==0:
            return False
        return True
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
        

    def dane_mascotas_de_un_id_propietario(self,propietario_id):
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
    def eliminar_propietario(self,dni):
        self.cursor.execute(f"DELETE FROM T_Propietario WHERE dni=?;",(dni,))
        self.conexion.commit()
    
