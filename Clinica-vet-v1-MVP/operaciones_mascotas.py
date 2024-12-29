from mascota import Mascota

def crear_mascota(conexion, cursor, mascota):
    cursor.executemany("insert into T_Mascota values (?,?,?,?,?,?,?,?,?);",
                                [
                                    (
                                        None,
                                        mascota.get_id_propietario(),
                                        mascota.get_nombre(),
                                        mascota.get_tipo(),
                                        mascota.get_raza(),
                                        mascota.get_fecha_nacimiento(),
                                        mascota.get_peso(),
                                        mascota.get_color(),
                                        mascota.get_notas()
                                    )
                                ]
                            )
    conexion.commit()

def modificar_mascota(conexion, cursor, mascota):
    cursor.execute("""update T_Mascota set id_propietario=?, nombre=?, tipo=?, raza=?, fecha_nacimiento=?, peso=?, color=?, notas=? where id=?;""",
                            (
                                mascota.get_id_propietario(),
                                mascota.get_nombre(),
                                mascota.get_tipo(),
                                mascota.get_raza(),
                                mascota.get_fecha_nacimiento(),
                                mascota.get_peso(),
                                mascota.get_color(),
                                mascota.get_notas(),
                                mascota.get_id()
                            )
                            )
    conexion.commit()
def get_all_mascotas(cursor):
    tuplas= cursor.execute("select * from T_Mascota").fetchall()
    if len(tuplas)==0:
        return []
    mascotas=[]
    for tupla in tuplas:
        mascota=Mascota(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8])
        mascotas.append(mascota)
    return mascotas

def dame_tipos(cursor):
    cursor.execute("select distinct tipo from T_Mascota;")
    return cursor.fetchall()
def dame_10_primeros_mascotas_propietarios(cursor):
    """
    Devuelve una lista de tuplas (id, nombre) de los 10 primeros propietarios con mascotas
    """
    cursor.execute("""select distinct p.id, p.dni, p.nombre 
                        from T_Mascota m 
                        inner join T_Propietario p 
                        on m.id_propietario=p.id
                        order by p.id
                        limit 10;""")
    tuplas=cursor.fetchall()
    return tuplas
def comprobar_existe_propietario(cursor,id_o_nombe, valor):
    """
    Método utilizado en pedir_mascota y pedir_mascota_conservando_la_que_habia para comprobar si el propietario existe o no

    Args:
        id_o_nombe (str): El campo por el que buscar
        valor (str): El valor del campo

    Returns:    
        bool: True si el propietario existe, False en caso contrario
    """
    if id_o_nombe=="id":
        cursor.execute("""select p.id 
                            from T_Propietario p 
                            inner join T_Mascota m 
                            on m.id_propietario=p.id
                            WHERE p.id=?;""",(valor,))
    elif id_o_nombe=="nombre":
        cursor.execute("""select p.id 
                            from T_Propietario p 
                            inner join T_Mascota m 
                            on m.id_propietario=p.id
                            WHERE p.nombre=?;""",(valor,)) 
        
    propietario=cursor.fetchone()
    if propietario==None:
        return False
    return True

def dame_mascotas_por_campo(cursor,campo, valor):
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
        cursor.execute("select * from T_mascota where id = ?;",(valor,))
    elif campo=="nombre":
        campo=campo.capitalize().strip()
        cursor.execute("select * from T_mascota where nombre like ?;",("%"+valor+"%",))
        #self.cursor.execute("select * from T_Mascota where nombre = ?;",(valor,))
    elif campo=="tipo":
        cursor.execute("select * from T_mascota where tipo = ?;",(valor,))
    elif campo=="raza":
        cursor.execute("select * from T_mascota where raza = ?;",(valor,))
    elif campo=="fecha_nacimiento":
        cursor.execute("select * from T_mascota where fecha_nacimiento = ?;",(valor,))
    elif campo=="peso":
        cursor.execute("select * from T_mascota where peso = ?;",(valor,))
    elif campo=="color":
        cursor.execute("select * from T_mascota where color like ?;",("%"+valor+"%",))
    tuplas=cursor.fetchall()
    if len(tuplas)==0:
        return None
    else:
        mascotas=[]
        for mascota in tuplas:
            mascotas.append(Mascota(mascota[0],mascota[1],mascota[2],mascota[3],mascota[4],mascota[5],mascota[6],mascota[7],mascota[8]))
        return mascotas
    

def dame_mascotas_por_tipo_agrupadas_por_raza(cursor, tipo):
    """
    Devuelve una lista de mascotas agrupadas por tipo, raza y contador

    Args:
        tipo (str): El tipo de mascotas que se quieren mostrar

    Returns:
        list: Una lista de tuplas (raza, tipo)
    """

    cursor.execute("""select tipo,raza,count(*) 
                        from T_Mascota 
                        where tipo=? 
                        group by raza 
                        order by tipo desc;""",(tipo,))
    return cursor.fetchall()

def eliminar_mascota(conexion,cursor,id):
    cursor.execute(f"DELETE FROM T_Mascota WHERE id=?;",(id,))
    conexion.commit()