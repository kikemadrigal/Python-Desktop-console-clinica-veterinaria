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
from base_de_datos import *
from operaciones_propietarios import *
from operaciones_mascotas import *
from operaciones_visitas import *
from operaciones_facturas import *
from utils import *
from propietario import Propietario
from mascota import Mascota
from visita import Visita
from factura import Factura
#El os sirve para saber si existe el archivo
import os
def menu_principal():
    print('''
                             Menu principal
                            ----------------
                            1. Propietarios
                            2. Mascotas
                            3. Visitas
                            4. Facturas
                            5 / s. Salir
    ''')

def main():
    path_database="veterinario-Avanza-Plus.db"
    inicializar_bd=False
    if not os.path.exists(path_database):
        inicializar_bd=True
    conexion, cursor=crear_conexion(path_database)
    # Se crea la tabla y los archivos si el archivo veterinario-Avanza-Plus.db no existe
    if inicializar_bd:
        crear_tabla_propietario(conexion, cursor)
        crear_tabla_mascota(conexion, cursor)
        crear_tabla_visita(conexion, cursor)
        crear_tabla_factura(conexion, cursor)
        anadir_propietarios(conexion, cursor)
        anadir_mascotas(conexion, cursor)
        anadir_visitas(conexion, cursor)
        anadir_facturas(conexion, cursor)
    
    while True:
        menu_principal()
        opcion=input ("Introduce una opcion: ")
        if opcion == '1':
            menu_propietario(conexion, cursor)
        elif opcion == '2':
            menu_mascota(conexion, cursor)
        elif opcion == '3':
            menu_visita(conexion, cursor)
        elif opcion == '4':
            menu_factura(conexion, cursor)
        elif opcion == '5' or opcion == 's' or opcion == 'S':
            print("Has salido del programa.")
            cerrar_conexion(conexion)
            break





def menu_propietario(conexion, cursor):
    while True:
        print('''
                                Menu propietario
                                ----------------
                                1. Crear 
                                2. Modificar 
                                3. Mostrar mascotas de un propietario
                                4. Mostrar todos
                                5. Eliminar
                                6. Volver al menu principal
        ''')
        opcion2=input ("Introduce una opcion: ")
        # 1. Crear propietario
        if opcion2 == '1':
            propietario=pedir_propietario(cursor)
            crear_propietario(conexion, cursor, propietario)
            print(propietario," anadido con éxito")
        #2. Modificar propietario
        elif opcion2 == '2':
            print("Ayuda:Loreto->36581601D, carlos->56396587N")
            dni_propietario=pedir_dni_propietario()
            propietarios=dame_propietarios_por_campo(cursor,"dni",dni_propietario)
            propietario=pedir_propietario_conservando_el_que_habia(cursor,propietarios[0])
            modificar_propietario(conexion, cursor, propietario)
            print(propietario," modificado con éxito")
        #3. Mostrar mascotas de un propietario
        elif opcion2 == '3':
            print("Ayuda: Loreto->36581601D, carlos->56396587N")
            dni_propietario=pedir_dni_propietario()
            propietarios=dame_propietarios_por_campo(cursor,"dni",dni_propietario)
            if propietarios==None:
                print("Propietario no encontrado")
            else:
                mascotas_propietario=dane_mascotas_de_un_id_propietario(cursor,propietarios[0].get_id())
                if len(mascotas_propietario)==0:
                    print("El propetario no tiene mascotas.")
                else:
                    # Mostramos el 1 propietario de la lista de tuplas
                    print(f"El propietario con id {mascotas_propietario[0][0]} ({mascotas_propietario[0][1]}) tiene las siguientes mascotas:")
                    for mascota_propietario in mascotas_propietario:
                        print(f"Id: {mascota_propietario[2]}, nombre: {mascota_propietario[3]}, tipo: {mascota_propietario[4]}, raza: {mascota_propietario[5]}")
        #4. Mostrar todos
        elif opcion2 == '4':
            propietarios=get_all_propietarios(cursor)
            for propietario in propietarios:
                print(f"id: {propietario.get_id()}, nombre: {propietario.get_nombre()}, dni: {propietario.get_dni()}")
        #5. Eliminar
        elif opcion2 == '5':
            print("Ayuda: Loreto->36581601D, carlos->56396587N")
            dni_propietario=pedir_dni_propietario()
            propietarios=dame_propietarios_por_campo(cursor,"dni",dni_propietario)
            if propietarios==None:
                print("Propietario no encontrado")
            else:
                propietario=propietarios[0]
                borrar_sin_no=input(f"¿Quieres borrar al propietario con id: {propietario.get_id()} ({propietario.get_nombre()})? (s para borrar): ")
                if borrar_sin_no=='s':
                    eliminar_propietario(conexion, cursor, propietario.get_dni())
                    print(propietario," eliminado con éxito")
                else:
                    print("Propietario no borrado")
        #6. Volver al menu principal      
        elif opcion2== '6' or opcion2 == 's' or opcion2 == 'S':
            print("Has salido del menú propietarios.")
            break
        else:
            print("Opcion no valida")
        input("Pulsa enter para continuar")











def menu_mascota(conexion, cursor):
    while True:
        print('''
                                Menu mascota
                                ----------------
                                1. Crear 
                                2. Modificar 
                                3. Mostrar cuantas mascotas hay de un tipo especifico
                                4. Mostrar todas
                                5. Eliminar
                                6. Volver al menu principal
        ''')
        opcion2=input ("Introduce una opcion: ")
        if opcion2 == '1':
            mascota=pedir_mascota(cursor)
            crear_mascota(conexion, cursor, mascota)
            print(mascota," anadida con éxito")
        elif opcion2 == '2':
            id_mascota=pedir_id_mascota()
            mascotas=dame_mascotas_por_campo(cursor,"id",id_mascota) 
            if mascotas==None:
                print("Mascota no encontrada")
            else:
                mascota=mascotas[0]
                # Llamamos a la función dentro de esta clase que sigue con las preguntas
                mascota=pedir_mascota_conservando_la_que_habia(cursor, mascota)
                modificar_mascota(conexion, cursor, mascota)
                print(mascota," modificado con éxito")
        elif opcion2=="3":
                tipo_introducido=input("Introduce el tipo de mascota, por ejemplo: Perro, Gato, Pájaro, Conejo: ")
                tipo_introducido=tipo_introducido.capitalize().strip()
                tipos_agrupadas_por_raza=dame_mascotas_por_tipo_agrupadas_por_raza(cursor,tipo_introducido)
                tipo_no_encontrado=False
                for tipo, raza, cantidad in tipos_agrupadas_por_raza:
                    if tipo_introducido==tipo:
                        tipo_no_encontrado=True
                    print(f"Tip: {tipo}, raza {raza} tiene cantidad {cantidad}.")
                if not tipo_no_encontrado:
                    print("No hay mascotas de ese tipo.")
        elif opcion2=="4":
            mascotas=get_all_mascotas(cursor)
            for mascota in mascotas:
                print(f"id: {mascota.get_id()}, nombre: {mascota.get_nombre()}, propietario: {mascota.get_id_propietario()}, tipo: {mascota.get_tipo()}, raza: {mascota.get_raza()}")
        elif opcion2 == '5':
            id_mascota=pedir_id_mascota()
            mascotas=dame_mascotas_por_campo(cursor,"id",id_mascota) 
            if mascotas==None:
                print("Mascota no encontrada")
            else:
                mascota=mascotas[0]
                borrar_sin_no=input(f"¿Quieres borrar la mascota con id: {mascota.get_id()} ({mascota.get_nombre()})? (s para borrar): ")
                if borrar_sin_no=='s':
                    eliminar_mascota(conexion, cursor, mascota.get_id())
                    print(mascota," eliminada con éxito")
                else:
                    print("Mascota no borrada")
        elif opcion2== '6' or opcion2 == 's' or opcion2 == 'S':
            print("Has salido del menú mascotas.")
            break
        else:
            print("Opcion no valida")
        input("Pulsa enter para continuar")












def menu_visita(conexion, cursor):
    while True:
        print('''
                                Menu visita
                                ----------------
                                1. Crear 
                                2. Modificar 
                                3. Mostrar visitas de una mascota
                                4. Mostrar todas
                                5. Eliminar
                                6. Volver al menu principal
        ''')    
        opcion2=input ("Introduce una opcion: ")
        if opcion2 == '1':
            visita=pedir_visita(cursor)
            if(visita!=None):
                crear_visita(conexion, cursor, visita)
                print(visita," anadido con éxito")
            else:
                print("Visita no creada")
        elif opcion2 == '2':
            id_visita=input("Introduce el id de la visita a modificar, si no lo sabes ve a mostrar todas las visitas, por ejemplo: del 1 al 10: ")
            visita=dame_visita_por_id_visita(cursor,id_visita)
            if visita==None:
                print("Visita no encontrada")
            else:
                visita=pedir_visita_conservando_la_que_habia(cursor,visita)
                modificar_visita(conexion, cursor, visita)
                print(visita," modificado con éxito")
        # Mostrar visitas de una mascota
        elif opcion2== '3':
            while True:
                nombre_mascota=input("Introduce el nombre de la mascota para ver sus visitas (pluto, robin): ")
                if check_empty(nombre_mascota):
                    print("El nombre de la mascota no puede estar vacío.")
                    continue
                nombre_mascota=nombre_mascota.capitalize().strip()
                break
            nombre_mascota=nombre_mascota.capitalize()
            visitas_mascota=dame_visitas_por_nombre_mascota(cursor,nombre_mascota)
            if visitas_mascota==None:
                print("No hay visitas de la mascota",nombre_mascota)
            else:
                for vista_mascota in visitas_mascota:
                    print (vista_mascota)
        # 4. Mostrar todas
        elif opcion2== '4':
            visitas=get_all_visitas(cursor)
            for visita in visitas:
                print (visita)
        elif opcion2=="5":
            print("""
                    Borra la visita 6, que Coco ya no está gordo
                    Borra la Visita 7, que Pluto no ha venido a vacunarse
                    
                    """)
            while True:
                id_visita=input("Introduce el id de la visita a borrar,del 1 al 10: ")
                if not is_integer(id_visita):
                    print("La id de la visita debe ser un entero.")
                    continue
                try:
                    id_visita=int(id_visita)
                except ValueError:
                    print("La id de la visita debe ser un entero.")
                    continue
                if not is_greater_cero(id_visita):
                    print("La id de la visita debe ser mayor que 0.")
                    continue
                break
            visita=dame_visita_por_id_visita(cursor,id_visita) 
            if visita==None:
                print("Visita no encontrada")
            else:
                borrar_sin_no=input(f"¿Quieres borrar {visita}? (s para borrar): ")
                if borrar_sin_no=='s':
                    delete_visita(conexion,cursor,visita.get_id())                   
                    print(visita," borrado con éxito")
                else:
                    print("Operación de borrado cancelada.")
        elif opcion2== '6' or opcion2 == 's' or opcion2 == 'S':
            print("Has salido del menú mascotas.")
            break
        else:
            print("Opcion no valida")
        input("Pulsa enter para continuar")







def menu_factura(conexion, cursor):
    while True:
        print('''
                                Menu factura
                                ----------------
                                1. Listado de facturas
                                2. Volver al menu principal
        ''')
        opcion2=input ("Introduce una opcion: ")
        if opcion2 == '1':
            facturas=get_all_facturas(cursor)
            for factura in facturas:
                print (factura)
        elif opcion2== '2' or opcion2 == 's' or opcion2 == 'S':
            print("Has salido del menú mascotas.")
            break
        else:
            print("Opcion no valida")
        input("Pulsa enter para continuar")





























###############################################################
# FUNCIONES AUXILIARES
###############################################################



# PROPIETARIOS
########################################################################################
def pedir_dni_propietario():
    while True:
        dni_propietario=input("Introduce el DNI del propietario: ")
        dni_propietario=dni_propietario.upper().strip()
        if check_empty(dni_propietario):
            print("El DNI no puede estar vacio")
            continue
        if not check_dni(dni_propietario):
            print("DNI no válido")
            continue
        break
    return dni_propietario
def pedir_propietario(cursor):
    # Pide nombbre
    while True:
        nombre=input("Introduce el nombre (no puede estar ya creado en la base de datos): ")
        #Lo formatemaos para tratarlo mejor sin espacios y con la 1 mayúscula
        nombre=nombre.capitalize().strip()
        if check_empty(nombre):
            print("El nombre del propietario no puede estar vacio")
            continue
        if comprobar_existe_propietario_name(cursor,nombre):
            print("El propietario ya existe")
            continue
        break
    #Pide DNI
    while True:
        dni=input("Introduce el DNI: (Si escribes el DNI sin letra, la letra se pondra automaticamente): ")
        dni=dni.upper().strip()
        #Generamos la letra si es necesario
        if len(dni)==8:
            letra=generar_letrar_dni(dni)
            dni=dni+letra
            input(f"Letra dni generada automáticamente: {dni}, pulse una tecla para cotinuar.")
        if not check_dni(dni):
            print("El DNI no es correcto")
            continue
        if comprobar_existe_propietario_dni(cursor,dni):
            print("El dni ya existe")
            continue
        break
    #Pide fecha de nacimiento
    while True:
        fecha=input("Introduce la fecha (dd-mm-aaaa): ")
        fecha=fecha.strip()
        if not check_fecha(fecha):
            print("La fecha no es correcta, tiene que ser el formato: dd-mm-aaaa")
            continue
        break
    # Pide dirección
    while True:
        direccion=input("Introduce la direccion: ")
        if check_empty(direccion):
            print("La direccion no puede estar vacia")
            continue
        break
    # Pide correo electrónico
    while True:
        correo_electronico=input("Introduce el correo electronico (ejemplo:uno@prueba.com): ")
        if not check_email(correo_electronico):
            print("El correo electronico no es correcto")
            continue
        break
    
    propietario=Propietario(None,nombre,dni,fecha,direccion,correo_electronico)
    return propietario





def pedir_propietario_conservando_el_que_habia(cursor,propietario):
    # Pide nombbre
    while True:
        nombre=input(f"Nombre: {propietario.get_nombre()}? ")
        #Lo formatemaos para tratarlo mejor sin espacios y con la 1 mayúscula
        nombre=nombre.capitalize().strip()
        if comprobar_existe_propietario_name(cursor,nombre):
            print("El propietario ya existe")
            continue
        if nombre=="":
            nombre=propietario.get_nombre()
        break
    # Pide DNI
    while True:
        dni=input(f"DNI (Sin letra para generar automáticamente la letra): {propietario.get_dni()}? ")
        dni=dni.upper().strip()
        if dni=="":
            dni=propietario.get_dni()
        else:
                #Generamos la letra si es necesario
            if len(dni)==8:
                letra=generar_letrar_dni(dni)
                dni=dni+letra
                input(f"Letra dni generada automáticamente: {dni}, pulse una tecla para cotinuar.")
            if comprobar_existe_propietario_dni(cursor,dni):
                print("El propietario ya existe")
                continue
            if not check_dni(dni):
                print("El DNI no es correcto")
                continue

        break
    # Pide fecha de nacimiento
    while True:
        fecha=input(f"Fecha (dd-mm-aaaa): {propietario.get_fecha_nacimiento()}? ")
        if fecha=="":
            fecha=propietario.get_fecha_nacimiento()
        if not check_fecha(fecha):
            print("La fecha no es correcta, tiene que ser el formato: dd-mm-aaaa")
            continue
        break
    # Pide dirección
    direccion=input(f"Direccion: {propietario.get_direccion()}? ")
    if direccion=="":
        direccion=propietario.get_direccion()
    # Pide correo electrónico
    while True:
        correo_electronico=input(f"Correo electronico: {propietario.get_correo_electronico()}? ")
        if correo_electronico=="":
            correo_electronico=propietario.get_correo_electronico()
        else:
            if not check_email(correo_electronico):
                print("El correo electronico no es correcto")
                continue
        break

    propietario=Propietario(propietario.get_id(),nombre,dni,fecha,direccion,correo_electronico)
    return propietario    























# MASCOTAS
####################################################################
def pedir_id_mascota():
    while True:
        id_mascota=input("Introduce el id de la mascota, busca mascotas en el menu: ")
        if check_empty(id_mascota):
            print("El id_mascota no puede estar vacio")
            continue
        try:
            id_mascota=int(id_mascota)
        except ValueError:
            print("El id debe ser un entero")
            continue 
        if not is_greater_cero(id_mascota):
            print("El id debe ser mayor que 0")
            continue
        break
    return id_mascota


def pedir_mascota(cursor):
    tipos_validos=dame_tipos(cursor)
    while True:
        print("""
                            CREANDO UNA MASCOTA
            -----------------------------------------------------------------
            La tabla mascota tiene asociado el id del propietario,
            por esto es necesario que introduzca el DNI del prpietario 
            para sacarle el id
            """)
        mascotas_propietarios=dame_10_primeros_mascotas_propietarios(cursor)
        if mascotas_propietarios==None:
            print("No hay mascotas.")
        else:
            for item in mascotas_propietarios:
                print(item[0], item[1] , item[2] , end=" | ")
            print("...")
            print("")

        dni_propietario=pedir_dni_propietario()
        propietarios=dame_propietarios_por_campo(cursor,"dni",dni_propietario)  
        if propietarios==None:
            print("Propietario no encontrado")
            continue
        id_propietario=propietarios[0].get_id()
        break
    while True:
        nombre=input("Introduce el nombre de la mascota: ")
        nombre=nombre.capitalize().strip()
        if check_empty(nombre):
            print("El nombre no puede estar vacio")
            continue
        break

    while True:
        print("El tipo debe ser uno de los siguientes:")
        for item in tipos_validos:
            print(item[0], end=" | ")
        print("")
        tipo=input("Introduce el tipo de uno de los de arriba: ")
        tipo=tipo.capitalize().strip()
        tipo_validado=False
        for item in tipos_validos:
            if item[0]==tipo:
                tipo_validado=True
        if not tipo_validado:
            print(f"El tipo {tipo} no es valido, selecciona uno de los de arriba.")
            continue
        break
    while True:
        raza=input("Introduce la raza: ")
        if check_empty(raza):
            print("La raza no puede estar vacia")
            continue
        break
    while True:
        fecha_nacimiento=input("Introdiuce la fecha de nacimiento (dd-mm-aaaa): ")
        if check_empty(fecha_nacimiento):
            print("La fecha de nacimiento no puede estar vacia")
            continue
        if not check_fecha(fecha_nacimiento):
            print("La fecha de nacimiento no es correcta, tiene que ser el formato: dd-mm-aaaa")
            continue
        break
    while True:
        peso=input("Introdiuce el pesoo (ejemplo 1.5 o 12.3): ")
        if check_empty(peso):
            print("El peso no puede estar vacio")
            continue
        try:
            peso=float(peso)
        except ValueError:
            print("El peso debe ser un numero")
            continue
        break
    
    color=input("Introdiuce el color: ")
    notas=input("Notas: ")
    mascota=Mascota(None,id_propietario,nombre,tipo,raza,fecha_nacimiento,peso,color,notas)
    return mascota






def pedir_mascota_conservando_la_que_habia(cursor,mascota:Mascota)->Mascota:
    tipos_validos=dame_tipos(cursor)
    while True:
        print("""
                            ACTUALIANDO UNA MASCOTA
            -----------------------------------------------------------------
            La tabla mascota tiene asociado el id del propietario,
            por esto es necesario que introduzca el DNI del propietario
            para sacarle el id
            """)
        mascotas_propietarios=dame_10_primeros_mascotas_propietarios(cursor)
        if mascotas_propietarios==None:
            print("No hay mascotas.")
        else:
            for item in mascotas_propietarios:
                id_propietario=item[0]
                dni_propietario=item[1]
                nombre_propietario=item[2]
                print(id_propietario, dni_propietario, nombre_propietario , end=" | ")
            print("...")
            print("")
     
        propietario=dame_propietarios_por_campo(cursor,"id",mascota.get_id_propietario())[0]
        dni_propietario=input(f"El dni propietario es: {propietario.get_dni()} de {propietario.get_nombre()}? Déjalo vacío para conservarlo: ")
        if dni_propietario=="":
            id_propietario=propietario.get_id()
        else:
            propietarios=dame_propietarios_por_campo(cursor,"dni",dni_propietario)  
            if propietarios==None:
                print("Propietario no encontrado")
                continue
            id_propietario=propietarios[0].get_id()
        break
    while True:
        nombre=input(f"Nombre: {mascota.get_nombre()}? Déjalo vacío para conservarlo: ")
        if nombre=="":
            nombre=mascota.get_nombre()
        if check_empty(nombre):
            print("El nombre no puede estar vacio")
            continue
        mascota.set_nombre(nombre.capitalize().strip())
        break

    while True: 
        print("El tipo debe ser uno de los siguientes:")
        for item in tipos_validos:
            print(item[0], end=" | ")
        print("")   
        tipo=input(f"tipo: {mascota.get_tipo()}? Déjalo vacío para conservarlo: ")
        if tipo=="":
            tipo=mascota.get_tipo()
        tipo=tipo.capitalize().strip()
        tipo_validado=False
        for item in tipos_validos:
            if item[0]==tipo:
                tipo_validado=True
        if not tipo_validado:
            print(f"El tipo {tipo} no es valido, selecciona uno de los de arriba.")
            continue
        

        break

    raza=input(f"Raza: {mascota.get_raza()}? Déjalo vacío para conservarlo: ")
    if raza=="":
        raza=mascota.get_raza()

    while True:
        fecha_nacimiento=input(f"fecha nacimiento: {mascota.get_fecha_nacimiento()}? Déjalo vacío para conservarlo: ")
        if fecha_nacimiento=="":
            fecha_nacimiento=mascota.get_fecha_nacimiento()
        if not check_fecha(fecha_nacimiento):
            print("La fecha de nacimiento no es correcta, tiene que ser el formato: dd-mm-aaaa")
            continue
        break

    while True:
        peso=input(f"Peso: {mascota.get_peso()}? Déjalo vacío para conservarlo: ")
        if peso=="":
            peso=mascota.get_peso()
        try:
            peso=float(peso)
        except ValueError:
            print("El peso debe ser un numero")
            continue
        break

    color=input(f"Color: {mascota.get_color()}? Déjalo vacío para conservarlo: ")
    if color=="":
        color=mascota.get_color()

    notas=input(f"Notas: {mascota.get_notas()}? Déjalo vacío para conservarlo: ")
    if notas=="":
        notas=mascota.get_notas()

    mascota=Mascota(mascota.get_id(),id_propietario,nombre,tipo,raza,fecha_nacimiento,peso,color,notas)
    return mascota















# VISITA
##################################################################
def pedir_visita(cursor):
    print("""
                            CREANDO UNA VISITA
            -----------------------------------------------------------------
            La tabla visita tiene asociado el id de la mascota,
            por esto es necesario que introduzca el id de la mascota
            si no lo sabe, vaya al menu mascota y cree una nueva,
            las primeros id de las mascotas actuales son:
            """)
    perimeros_id_visitas=dame_10_primeros_id_de_visitas_mascotas(cursor)
    if len(perimeros_id_visitas)==0:
        print("No hay visitas.")
    else:
        for item in perimeros_id_visitas:
            print(item[0],"("+item[1]+")", end=" | ")
        print("")
    while True:
        id_mascota=input("Introduce el id de la mascota de uno de los de arriba: ")
        if check_empty(id_mascota):
            print("El id de la mascota no puede estar vacío.")
            continue
        try:
            id_mascota=int(id_mascota)
        except ValueError:
            print("El id_mascota debe ser un entero")
            continue
        if not is_greater_cero(id_mascota):
            print("El id_mascota debe ser mayor que 0")
            continue
        if not comprobar_existe_mascota(cursor,id_mascota):
            print("El id_mascota no existe en la tabla mascota.")
            continue
        break
    while True:
        fecha_visita=input("Introduce la fecha de la visita (dd-mm-aaaa): ")
        if check_empty(fecha_visita):
            print("La fecha de la visita no puede estar vacía.")
            continue
        if not check_fecha(fecha_visita):
            print("La fecha de la visita no es correcta.")
            continue
        break
    while True:
        descripcion=input("Introduce la descripción de la visita: ")
        if check_empty(descripcion):
            print("La descripción de la visita no puede estar vacía.")
            continue
        break
    while True:
        tratamiento=input("Introduce el tratamiento de la visita: ")
        if check_empty(tratamiento):
            print("El tratamiento de la visita no puede estar vacío.")
            continue
        break

    visita=Visita(None,id_mascota,fecha_visita,descripcion,tratamiento) 
    return visita
    



def pedir_visita_conservando_la_que_habia(cursor, visita):
    perimeros_id_visitas=dame_10_primeros_id_de_visitas_mascotas(cursor)
    if len(perimeros_id_visitas)==0:
        print("No hay visitas.")
    else:
        for item in perimeros_id_visitas:
            print(item[0], "("+item[1]+")", end=" | ")
        print("")
    #pedir id_visita
    while True:
        id_mascota=input(f"id mascota: {visita.get_id_mascota()} ? (vacío para dejar el que hay): ")
        if id_mascota=="":
            id_mascota=visita.get_id_mascota()
        try:
            id_mascota=int(id_mascota)
        except ValueError:
            print("El id_mascota debe ser un entero")
            continue
        if not is_greater_cero(id_mascota):
            print("El id_mascota debe ser mayor que 0")
            continue
        if not comprobar_existe_mascota(cursor,id_mascota):
            print("El id_mascota no existe en la tabla mascota.")
            continue
        break
    #pedir fecha
    while True:   
        fecha_visita=input(f"fecha visita (dd-mm-aaaa): {visita.get_fecha_visita()} ? (vacío para dejar el que hay): ")
        if fecha_visita=="":
            fecha_visita=visita.get_fecha_visita()
        if not check_fecha(fecha_visita):
            print("La fecha de la visita no es correcta.")
            continue
        break

    dscripcion=input(f"descripcion: {visita.get_descripcion()} ? (vacío para dejar el que hay): ")
    if dscripcion=="":
        dscripcion=visita.get_descripcion()

    tratamiento=input(f"tratamiento: {visita.get_tratamiento()} ? (vacío para dejar el que hay): ")
    if tratamiento=="":
        tratamiento=visita.get_tratamiento()
        
    visita=Visita(visita.get_id(),id_mascota,fecha_visita,dscripcion,tratamiento) 
    return visita















        
if __name__ == "__main__":
    main()
        





