from factura import Factura



def crear_factura(conexion, cursor, factura):
    cursor.execute("insert into T_Factura values(?,?,?)",(None,factura.get_id_visita(),factura.get_precio()))
    conexion.commit()


def modificar_factura(conexion, cursor, factura):
    """
    Modifica una factura
    """
    cursor.execute("""update T_Factura set id_visita=?, precio=? where id=?;""",(factura.get_id_visita(),factura.get_precio(),factura.get_id()))
    conexion.commit()
def get_all_facturas(cursor):
    tuplas= cursor.execute("select * from T_Factura").fetchall()
    if len(tuplas)==0:
        return []
    facturas=[]
    for tupla in tuplas:
        factura=Factura(tupla[0],tupla[1],tupla[2])
        facturas.append(factura)
    return facturas
def eliminar_factura(conexion,cursor,id):
    cursor.execute(f"DELETE FROM T_Factura WHERE id=?;",(id,))
    conexion.commit()
