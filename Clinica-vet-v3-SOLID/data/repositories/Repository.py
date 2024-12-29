class Repository:
    def __init__(self,sqlite3Client, table_name):
        self.sqlite3Client=sqlite3Client
        self.conexion=self.sqlite3Client.get_conexion()
        self.cursor=self.sqlite3Client.get_cursor()
        self.tabla=table_name
    def set_tabla(self,tabla):
        self.tabla=tabla
    def get_tabla(self):
        return self.tabla
    def insert(self, **kwargs):
        # Estructurar la sentencia SQL
        sql = f"INSERT INTO {self.tabla} VALUES ({','.join('?'*len(kwargs))})"
        valores = tuple(kwargs.values())
        # Ejecutar la consulta
        self.conexion.cursor()
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def selects(self, **kwargs):
        # Construir la sentencia SQL dinámicamente
        if kwargs:  # Si hay filtros
            condiciones = " AND ".join(f"{col} = ?" for col in kwargs.keys())
            sql = f"SELECT * FROM {self.tabla} WHERE {condiciones}"
            valores = tuple(kwargs.values())
        else:  # Si no hay filtros, seleccionar todo
            sql = "SELECT * FROM {self.tabla}"
            valores = ()

        # Ejecutar la consulta
        self.conexion.cursor()
        self.cursor.execute(sql, valores)
        return self.cursor.fetchall()

    def show_all(self):
        self.cursor.execute(f"select * from {self.tabla};")
        result=self.cursor.fetchall()
        if len(result)==0:
            print("No hay resultados.")
        else:
            for item in result:
                print(item)
    def get_all(self):
        items=[]
        self.cursor.execute(f"select * from {self.tabla};")
        result=self.cursor.fetchall()
        if len(result)==0:
            print("No hay resultados.")
        else:
            for item in result:
                items.append(item)
        return items
    def update(self, id, **kwargs):
        # Construir la sentencia SQL dinámicamente
        columnas = ", ".join(f"{col} = ?" for col in kwargs.keys())
        sql = f"UPDATE {self.tabla} SET {columnas} WHERE id = ?"
        valores = tuple(kwargs.values()) + (id,)
        self.conexion.cursor()
        self.cursor.execute(sql, valores)
        self.conexion.commit()


    def delete(self,id):
        self.cursor.execute(f"DELETE FROM {self.tabla} WHERE id=?;",(id,))
        self.conexion.commit()
 