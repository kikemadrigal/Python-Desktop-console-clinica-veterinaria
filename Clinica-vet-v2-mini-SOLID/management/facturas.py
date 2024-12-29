from entities.factura import Factura


class Facturas:
    def __init__(self, sqliteClient):
        self.conexion = sqliteClient.get_conexion()
        self.cursor = sqliteClient.get_cursor()
        self.facturas=[]

    def crear_factura(self, factura):
        self.cursor.execute("insert into T_Factura values(?,?,?)",(None,factura.get_id_visita(),factura.get_precio()))
        self.conexion.commit()

    def modificar_factura(self, factura):
        """
        Modifica una factura
        """
        self.cursor.execute("""update T_Factura set id_visita=?, precio=? where id=?;""",(factura.get_id_visita(),factura.get_precio(),factura.get_id()))
        self.conexion.commit()
    def get_all_facturas(self):
        tuplas= self.cursor.execute("select * from T_Factura").fetchall()
        if len(tuplas)==0:
            return []
        facturas=[]
        for tupla in tuplas:
            factura=Factura(tupla[0],tupla[1],tupla[2])
            facturas.append(factura)
        return facturas
    def eliminar_factura(self,id):
        self.cursor.execute(f"DELETE FROM T_Factura WHERE id=?;",(id,))
        self.conexion.commit()
