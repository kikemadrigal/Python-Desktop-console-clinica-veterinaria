import sqlite3
#El os sirve para saber si existe el archivo
import os
# Para trabajar con archivos ccsv
import csv
class SqliteCliente:
    def __init__(self):
        path_database="veterinario-Avanza-Plus.db"
        inicializar_bd=False
        if not os.path.exists(path_database):
            inicializar_bd=True
        try:
            self.conexion=sqlite3.connect(path_database)
            self.cursor=self.conexion.cursor()
        except:
            print("Error al conectar con la base de datos")


        if inicializar_bd:
            self.crear_tabla_propietario()
            self.crear_tabla_mascota()
            self.crear_tabla_visita()
            self.crear_tabla_factura()
            #self.anadir_propietarios()
            self.anadir_propietarios_desde_arrchivo_csv("assets/propietarios.csv")
            #self.anadir_mascotas()
            self.anadir_mascotas_desde_arrchivo_csv("assets/mascotas.csv")
            self.anadir_visitas()
            self.anadir_facturas()
        
    def get_conexion(self):
        return self.conexion
    def get_cursor(self):
        return self.cursor
    



    ####################################
    #  Create Tables
    ####################################
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
    def crear_tabla_propietario(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS T_Propietario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                dni TEXT,
                fecha_nacimiento TEXT,
                direccion TEXT,
                correo_electronico TEXT
        );   
                    
        ''')
        self.conexion.commit()
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
    def crear_tabla_mascota(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS T_Mascota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_propietario TEXT,
            nombre TEXT,
            tipo TEXT,
            raza TEXT,
            fecha_nacimiento DATE,
            peso REAL,
            color TEXT,
            notas TEXT,
            foreign key (id_propietario) references T_Propietario(id)       
        );           
        ''')
        self.conexion.commit()
    """
    T_Visita
    --------
    Id o NumeroVisita 
    IdMascota 
    Fecha de la visita 
    Descripción 
    Tratamiento
    """
    def crear_tabla_visita(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS T_Visita (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_mascota TEXT,
                fecha_visita DATETIME,
                descripcion REAL,
                tratamiento TEXT,
                foreign key (id_mascota) references T_Mascota(id)    
        );   
                    
        ''')
        self.conexion.commit()
    """
    T_Factura
    --------
    Id o NumeroFactura 
    IdVisita 
    Precio o Factura
    """
    def crear_tabla_factura(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS T_Factura (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_visita TEXT,
                precio REAL,
                foreign key (id_visita) references T_Visita(id) 
        );   
                    
        ''')
        self.conexion.commit()




    ####################################
    #  Insert Data
    ####################################

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
    def anadir_propietarios(self):
        self.cursor.executemany("insert into T_Propietario values (?,?,?,?,?,?);",
            [
                (None,'Loreto','36581601D','04-05-1998','Calle Gutierrez mellado, 13','Loreto@gmail.com'),
                (None,'Carlos','56396587N','05-11-180','Calle princesa, 6','Carlos@gmail.com'),
                (None,'Pablo','25649656X','10-09-1990','Avenida del mar, 12','Pablo@gmail.com'),
                (None,'David','65365246M','05-06-2000','Calle Fiesta, 2','David@gmail.com'),
                (None,'Sergio','25469632F','01-08-2005','Calle reina Sofía, 4','Sergio@gmail.com'),
                (None,'Angel','45635423L','14-11-1983','Calle de los apóstoles, 54','Angel@gmail.com'),

            ])
        self.conexion.commit()
    def anadir_propietarios_desde_arrchivo_csv(self,archivo_csv):
        try:
            with open(archivo_csv, encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for linea,fila in enumerate(reader):
                        #Comprobamos que la fila tenga 3 columnas, si no, se borra
                        if len(fila) !=6:
                            input(f"Se ha detectado un problema en el csv en la fila {linea+2}: {fila} y se borrará. ")
                        else:
                            self.cursor.execute("insert into T_Propietario values (?,?,?,?,?,?);",(None,fila[1],fila[2],fila[3],fila[4],fila[5]))   
                            print(f"Insertando propietario {fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}, {fila[5]} en la base de datos")
                            self.conexion.commit()    
        except Exception as e:
            print("error: ",e)

    """
    T_Mascota
    -----------
    Id 
    IdPropietario 
    Nombre 
    Tipo (Gato,Perro, Pajaro, Conejo,…) 
    Raza 
    Fecha nacimiento 
    Peso 
    Color 
    Notas (Opcional)
    """
    #El propietario 4 (David) tiene 3 mascotas y el usuario 6 (Angel) tiene 2
    def anadir_mascotas(self):
        """
        1 Loreto tiene 2 mascotas
        2 Carlos tiene 1 mascota
        3 Pablo tiene 3 mascotas
        4 David tiene 4 mascotas
        5 Sergio tiene 2 mascotas
        6 Angel tiene 1 mascota
        """

        self.cursor.executemany("insert into T_Mascota values (?,?,?,?,?,?,?,?,?);",
            [
                (None,1,'Coco','Gato','Persa','01-10-2020',3.5,'Gris','Mascota 1'),
                (None,3,'Pipo','Conejo','Salvaje','01-01-2022',1.2,'Verd','Mascota 2'),
                (None,4,'Hugo','Perro','Pastor','31-07-2019',13.5,'Azul','Mascota 3'),
                (None,4,'Pluto','Perro','Pastor','25-01-2021',10.7,'Rosa','Mascota 4'),
                (None,4,'Robin','Gato','siamés','26-03-2023',4.8,'Negro','Mascota 5'),
                (None,6,'Simba','Perro','Chihuahua','10-05-2023',10.0,'Marrón claro','Mascota 6'),
                (None,2,'Nemo','Gato','angora','01-01-2020',2.7,'Blanco','Mascota 7'),
                (None,5,'Bobi','Perro','Terrier','01-01-2020',15.5,'Manchas negras','Mascota 8'),
                (None,5,'Dartacan','Perro','Terrier','01-01-2020',4.5,'Manchas blancas','Mascota 9'),
                (None,4,'Leo','Perro','Terrier','01-01-2020',4.0,'Gris claro','Mascota 10'),
                (None,1,'Piolin','Pájaro','Canario','01-01-2020',0.5,'Amarillo','Mascota 11'),
                (None,3,'Sansón','Perro','Labrador','01-01-2020',0.5,'Blanco con machas marrones','Mascota 12'),
                (None,3,'Cani','Gato','Persa','01-01-2020',0.5,'Negro claro','Mascota 13')
            ])
        self.conexion.commit()

    def anadir_mascotas_desde_arrchivo_csv(self,archivo_csv):
        try:
            with open(archivo_csv, encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for linea,fila in enumerate(reader):
                        #Comprobamos que la fila tenga 3 columnas, si no, se borra
                        if len(fila) !=9:
                            input(f"Se ha detectado un problema en el csv en la fila {linea+2}: {fila} y se borrará. ")
                        else:
                            self.cursor.execute("insert into T_Mascota values (?,?,?,?,?,?,?,?,?);",(None,fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8]))   
                            print(f"Insertando propietario {fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}, {fila[5]}, {fila[6]}, {fila[7]}, {fila[8]} en la base de datos")
                            self.conexion.commit()    
        except Exception as e:  
            print(e)
    """
    T_Visita
    ----------
    Id o NumeroVisita 
    IdMascota 
    Fecha de la visita 
    Descripción 
    Tratamiento
    """
    def anadir_visitas(self):
        """
        La mascota 1 (Coco) tiene 2 visitas
        La mascota 2 (Pipo) tiene 2 visitas
        La mascota 3 (Hugo) tiene 1 visita
        la mascota 4 (Pluto) tiene 3 visitas
        La mascota 5 (Robin) no tiene visitas 
        La mascota 6 (Simba) tiene 1 visita
        """
        self.cursor.executemany("insert into T_Visita values (?,?,?,?,?);",
            [
                (None,3,'11-03-2023','Visita 1, Hugo está cansado y siempre se duerme','Hacer ejercicio con Hugo'),
                (None,4,'14-05-2023','Visita 2, Pluto se muestra agresivo con los demás','Pastillas para calmarlo'),
                (None,1,'05-11-2023','Visita 3, Coco está muy gordo y nos tiene preocupados','Adelgazamiento con pastillas'),
                (None,2,'01-01-2024','Visita 4, Cada cosa que come Pipo la vomita','Pichazos para desparasitar'),
                (None,1,'01-02-2024','Visita 5, Coco sigoue gordo','Revisión adelgazamiento'),
                (None,1,'10-05-2024','Visita 6, Coco aún sigue gordo','Revisión adelgazamiento por segunda vez'),
                (None,4,'11-06-2024','Visita 7, Pluto tiene que vacunarse','Vacuna anual'),
                (None,4,'18-08-2024','Visita 8, Pluto siempre está durmiendo','Coprarle jueguetes y sacarlo a pasear'),
                (None,6,'21-09-2024','Visita 9, Simba ladra mucho','Ver agresividad'),
                (None,2,'04-11-2024','Visita 10, Pipo ahora está cojeando','Radigrafía y reposo')
            ])
        self.conexion.commit()
    def anadir_visitas_desde_arrchivo_csv(self,archivo_csv):
        try:
            with open(archivo_csv, encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for linea,fila in enumerate(reader):
                        #Comprobamos que la fila tenga 3 columnas, si no, se borra
                        if len(fila) !=5:
                            input(f"Se ha detectado un problema en el csv en la fila {linea+2}: {fila} y se borrará. ")
                        else:    
                            self.cursor.execute("insert into T_Visita values (?,?,?,?,?);",(None,fila[1],fila[2],fila[3],fila[4]))   
                            print(f"Insertando visita {fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]} en la base de datos")
                            self.conexion.commit()    
        except Exception as e:  
            print(e)


    """
    T_Factura
    - - - 
    Id o NumeroFactura 
    IdVisita 
    Precio o Factura
    """
    def anadir_facturas(self):
        self.cursor.executemany("insert into T_Factura values (?,?,?);",
            [
                (None,1,20.50),
                (None,2,200.20),
                (None,3,150.10),
                (None,4,50.70),
                (None,5,100.50),
                (None,6,15.10),
                (None,7,28.20),
                (None,1,350.20),
                (None,4,45.50),
                (None,1,30.70)
            ])
        self.conexion.commit() 
    def anadir_facturas_desde_arrchivo_csv(self,archivo_csv):
        try:
            with open(archivo_csv, encoding='utf-8') as f:    
                reader = csv.reader(f)
                next(reader)
                for linea,fila in enumerate(reader):
                        #Comprobamos que la fila tenga 3 columnas, si no, se borra
                        if len(fila) !=3:
                            input(f"Se ha detectado un problema en el csv en la fila {linea+2}: {fila} y se borrará. ")
                        else:    
                            self.cursor.execute("insert into T_Factura values (?,?,?);",(None,fila[1],fila[2]))   
                            print(f"Insertando factura {fila[0]}, {fila[1]}, {fila[2]} en la base de datos")
                            self.conexion.commit()    
        except Exception as e:  
            print(e)

    def cerrar_conexion(self):
        self.conexion.close()

