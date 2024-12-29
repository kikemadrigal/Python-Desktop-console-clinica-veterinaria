"""
El centro Veterinario Avanza Plus, nos ha pedido que le hagamos una aplicación para poder 
gestionar las mascotas, los propietarios, las visitas y las facturas.  
La estructura de la base de datos nos la proporciona el mismo centro veterinario y además nos 
pide que creemos un menú con las siguientes opciones: - 
Propietario: 
    o Crear Propietario 
    o Modificar Propietario 
    o Mostrar todas las mascotas de un propietario 
Mascota: 
    o Crear Mascota 
    o Modificar Mascota 
    o Mostrar cuantas mascotas hay de un tipo especifico.  
▪ Ej. Cuantos perros hay en la base de datos. Si se quiere concretar también se puede añadir raza en la búsqueda. 
Visita: 
    o Crear Visita 
    o Modificar Visita 
    o Borrar Visita 
    o Mostrar las visitas de una mascota.
- Factura:
    o Listado de Facturas
    NOTAS:
- Se recomienda trabajar con Clases, Objetos y diferentes Módulos, try-except y
comentarios en el código.
- Se pueden añadir extras.
- A la hora de la entrega, un fichero comprimido: NombreApellido-E4
"""

import logging.config
from data.sqliteCliente import SqliteCliente
from console.PropietariosManagement import PropietariosManagement
from console.Mascotasmanagement import MascotasManagement
from console.VisitasManagement import VisitasManagement
from console.FacturasManagement import FacturasManagement
from ui.manager import Manager


def menu_principal():
    print('''
                             Menu principal
                            ----------------
                            0. Abrir interface gráfica
                            1. Propietarios
                            2. Mascotas
                            3. Visitas
                            4. Facturas
                            5 / s. Salir
    ''')

def main():
    #Creamos la base de datos
    sqlite3Client=SqliteCliente()
    #Creamos las operaciones por consola de los propietarios, mascotas, visitas y facturas
    propietariosManagement=PropietariosManagement(sqlite3Client)
    mascotasManagement= MascotasManagement(sqlite3Client)
    visitasManagement=VisitasManagement(sqlite3Client)
    facturasManagement=FacturasManagement(sqlite3Client)

    while True:
        menu_principal()
        opcion=input ("Introduce una opcion: ")
        if opcion == '0':
            app= Manager()
            app.mainloop()
        if opcion == '1':
            propietariosManagement.menu_propietario()
        elif opcion == '2':
            mascotasManagement.menu_mascota()
        elif opcion == '3':
            visitasManagement.menu_visita()
        elif opcion == '4':
            facturasManagement.menu_factura()
        elif opcion == '5' or opcion == 's' or opcion == 'S':
            print("Has salido del programa.")
            sqlite3Client.cerrar_conexion()
            break
       
        
if __name__ == "__main__":
    main()
        





