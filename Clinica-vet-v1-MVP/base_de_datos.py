import sqlite3
def crear_conexion(path_database):
    try:
        conexion=sqlite3.connect(path_database)
        cursor=conexion.cursor()
    except:
        print("Error al conectar con la base de datos")
    return conexion, cursor

def crear_tabla_propietario(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Propietario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            dni TEXT,
            fecha_nacimiento TEXT,
            direccion TEXT,
            correo_electronico TEXT
    );   
                
    ''')
    conexion.commit()

def crear_tabla_mascota(conexion, cursor):
    cursor.execute('''
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
    conexion.commit()

def crear_tabla_visita(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Visita (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_mascota TEXT,
            fecha_visita DATETIME,
            descripcion REAL,
            tratamiento TEXT,
            foreign key (id_mascota) references T_Mascota(id)    
    );   
                
    ''')
    conexion.commit()


def crear_tabla_factura(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Factura (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_visita TEXT,
            precio REAL,
            foreign key (id_visita) references T_Visita(id) 
    );   
                
    ''')
    conexion.commit()


def anadir_propietarios(conexion, cursor):
        cursor.executemany("insert into T_Propietario values (?,?,?,?,?,?);",
            [
                (None,'Loreto','36581601D','04-05-1998','Calle Gutierrez mellado, 13','Loreto@gmail.com'),
                (None,'Carlos','56396587N','05-11-1980','Calle princesa, 6','Carlos@gmail.com'),
                (None,'Pablo','25649656X','10-09-1990','Avenida del mar, 12','Pablo@gmail.com'),
                (None,'David','65365246M','05-06-2000','Calle Fiesta, 2','David@gmail.com'),
                (None,'Sergio','25469632F','01-08-2005','Calle reina Sofía, 4','Sergio@gmail.com'),
                (None,'Angel','45635423L','14-11-1983','Calle de los apóstoles, 54','Angel@gmail.com'),

            ])
        conexion.commit()


#El propietario 4 (David) tiene 3 mascotas y el usuario 6 (Angel) tiene 2
def anadir_mascotas(conexion, cursor):
    cursor.executemany("insert into T_Mascota values (?,?,?,?,?,?,?,?,?);",
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
    conexion.commit()


def anadir_visitas(conexion, cursor):
    cursor.executemany("insert into T_Visita values (?,?,?,?,?);",
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
    conexion.commit()


def anadir_facturas(conexion, cursor):
    cursor.executemany("insert into T_Factura values (?,?,?);",
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
    conexion.commit() 


def cerrar_conexion(conexion):
    conexion.close()


