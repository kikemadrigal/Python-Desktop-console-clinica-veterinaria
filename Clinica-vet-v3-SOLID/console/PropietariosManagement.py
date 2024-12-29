from data.repositories.propietarioRepository import PropietarioRepository
from data.entities.Propietario import Propietario
from utils.utils import *
# Para trabajar con fechas en el submenú 6 de otras operaciones
from datetime import datetime
class PropietariosManagement:
    """
    Representa las operaciones de lectora y escritora en el cmd o terminal de las propietarios

    Args:   
        sqlite3Client (SqliteClient): Representa la base de datos
    """

    def __init__(self, sqlite3Client) -> None:
        self.propietarioRepositorio=PropietarioRepository(sqlite3Client)
        self.propietarios=[]
        # Cargamos la lista de propietarios
        self.propietarios=self.propietarioRepositorio.get_all()

   
    def menu_propietario(self):
        while True:
            print("""
                                        Propietarios
                        -----------------------------------------------
                        0. Buscar
                        1. Crear 
                        2. Modificar
                        3. Borrar
                        4. Mostrar todos los propietarios
                        5. Mostrar todas las mascotas de un propietario
                        6. Otras operaciones
                        9  / s  Salir
                """)
            opcion2=input ("Introduce una opcion: ")




            # 0. Buscar propietario
            ##################################################################################################
            if opcion2 == '0':
                while True:
                    option3=input("""
                                  Introduce:
                                  1 para buscar por id
                                  2 para buscar por nombre
                                  3 Buscar por DNI
                                  4 / s para salir: 
                                  """)
                    if check_empty(option3):
                        print("El campo no puede estar vacio")
                        continue
                    if option3=='1':
                        id_propietario=self.pedir_id_propietario()
                        propietarios=self.propietarioRepositorio.dame_propietarios_por_campo("id",id_propietario)
                        if propietarios==None:
                            print("Propietario no encontrado")
                        else:
                            for propietario in propietarios:
                                print(propietario)
                        input("Pulse una tecla para continuar... ")
                    elif option3=='2':
                        while True:
                            nombre_propietario=input("Introduce el nombre del propietario: ")
                            nombre_propietario=nombre_propietario.capitalize().strip()
                            if check_empty(nombre_propietario):
                                print("El nombre no puede estar vacio")
                                continue
                            break
                        propietarios=self.propietarioRepositorio.dame_propietarios_por_campo("nombre",nombre_propietario)
                        if propietarios==None:
                            print("Propietario no encontrado")
                        else:
                            for propietario in propietarios:
                                print(propietario)
                        input("Pulse una tecla para continuar... ")
                    elif option3=='3':
                        while True:
                            dni_propietario=input("Introduce el DNI del propietario: ")
                            dni_propietario=dni_propietario.upper().strip()
                            if check_empty(dni_propietario):
                                print("El DNI no puede estar vacio")
                                continue
                            if is_integer(dni_propietario):
                                print("El DNI no puede ser un entero")
                                continue
                            break
                        propietarios=self.propietarioRepositorio.dame_propietarios_por_campo("dni",dni_propietario)
                        if propietarios==None:
                            print("Propietario no encontrado")
                        else:
                            for propietario in propietarios:
                                print(propietario)
                        input("Pulse una tecla para continuar... ")
                    elif option3=='4' or option3=='s' or option3=='S':
                        print("Has salido del menú de buscar un propietario.")
                        break
                    else:
                        print("Opcion no valida para menú de buscar un propietario.")








            # 1. Crear propietario
            ##################################################################
            elif opcion2 == '1':
                propietario=self.pedir_propietario()
                if(propietario!=None):
                    self.propietarioRepositorio.insert( 
                                                        id=propietario.get_id(), 
                                                        nombre=propietario.get_nombre(), 
                                                        dni=propietario.get_dni(), 
                                                        fecha_nacimiento=propietario.get_fecha_nacimiento(),
                                                        direccion=propietario.get_direccion(), 
                                                        correo_electronico=propietario.get_correo_electronico()
                                                        )
                    #La metemos en la lista
                    propietario.set_id(self.propietarioRepositorio.get_last_id())
                    self.propietarios.append(propietario)
                    print(propietario," anadido con éxito")
                else:
                    print("Propietario no creado")








            # 2. Modificar propietario: modifica el propietario Loreto o Sergio   
            # ##################################################################    
            elif opcion2 == '2':
                print("Ayuda:")
                propietarios=self.propietarioRepositorio.dame_5_primeros_id_de_propietarios()
                for propietario in propietarios:
                    print(f"{propietario.get_id()} ({propietario.get_nombre()})", end=" | ")
                print("...")
                id_propietario=self.pedir_id_propietario()
                propietarios=self.propietarioRepositorio.dame_propietarios_por_campo("id",id_propietario)
                if propietarios==None:
                    print("Propietario no encontrado")
                else:
                    propietario=propietarios[0]
                    propietario=self.pedir_propietario_conservando_el_que_habia(propietario)
                    self.propietarioRepositorio.update(propietario.get_id(), nombre=propietario.get_nombre(), dni=propietario.get_dni(), fecha_nacimiento=propietario.get_fecha_nacimiento(), direccion=propietario.get_direccion(), correo_electronico=propietario.get_correo_electronico())
                    #Lo modificamos en la lista
                    for i in range(len(self.propietarios)):
                        if self.propietarios[i].get_id()==propietario.get_id():
                            self.propietarios[i]=propietario
                    print(propietario," modificado con éxito")

                





            # 3. Borrar propietario: borra el propietario Loreto o Sergio
            ##################################################################
            elif opcion2 == '3':
                print("Ayuda:")
                propietarios=self.propietarioRepositorio.dame_5_primeros_id_de_propietarios()
                for propietario in propietarios:
                    print(f"{propietario.get_id()} ( {propietario.get_nombre()} )", end=" | ")
                print("...")
                id_propietario=self.pedir_id_propietario()
                propietarios=self.propietarioRepositorio.dame_propietarios_por_campo("id",id_propietario)
                if propietarios==None:
                    print("Propietario no encontrado")
                else:
                    propietario=propietarios[0]
                    borrar_sin_no=input(f"¿Quieres borrar al propietario con id: {propietario.get_id()} ({propietario.get_nombre()})? (s para borrar): ")
                    if borrar_sin_no=='s':
                        self.propietarioRepositorio.delete(propietario.get_id())
                        print(f"Propietario con id: {propietario.get_id()} ({propietario.get_nombre()}) borrado con éxito")
                        #Lo borramos de la lista
                        for i in self.propietarios:
                            if i.get_id()==propietario.get_id():
                                self.propietarios.remove(i)
                    else:
                        print("Propietario no borrado")
                    





                    
            # 4. Mostrar todos los propietarios
            ##################################################################            
            elif opcion2 == '4':
                self.mostrar_bonito(self.propietarios)
                
                





            # 5. Mostrar mascotas de propietario: muestra las mascotas de un propietario
            ##################################################################################################
            elif opcion2 == '5':
                mascotas_propietario=self.propietarioRepositorio.dane_las_5_primeras_mascotas_propietario()
                print("5 primeras macotas por propietario")
                for mascota_propietario in mascotas_propietario:
                    #print(f"Cantidad: {mascota_propietario[0]} Propietario: {mascota_propietario[0]}({mascota_propietario[1]}): {mascota_propietario[2]},{mascota_propietario[3]} {mascota_propietario[4]}, {mascota_propietario[5]}")
                    print(f"El propietario con id {mascota_propietario[1]} ({mascota_propietario[2]}) tiene {mascota_propietario[0]} mascotas.")
                id_propietario=self.pedir_id_propietario()
                if id_propietario==None:
                    print("Propietario no encontrado")
                else:
                    mascotas_propietario=self.propietarioRepositorio.dane_mascotas_de_un_id_propietario(id_propietario)
                if len(mascotas_propietario)==0:
                    print("El propetario no tiene mascotas.")
                else:
                    # Mostramos el 1 propietario de la lista de tuplas
                    print(f"El propietario con id {mascotas_propietario[0][0]} ({mascotas_propietario[0][1]}) tiene las siguientes mascotas:")
                    for mascota_propietario in mascotas_propietario:
                        print(f"Id: {mascota_propietario[2]}, nombre: {mascota_propietario[3]}, tipo: {mascota_propietario[4]}, raza: {mascota_propietario[5]}")
           
           
           
           
           
           
           
           
            # 6. Otras operaciones  
            ####################################################################
            elif opcion2 == '6':
                while True:
                    option3=input("""
                                    Introduce:
                                    1 ordenar por nombre
                                    2 ordenar por DNI
                                    3 ordenar por fecha de nacimiento
                                    4 / s para salir: 
                                    """)
                    if check_empty(option3):
                        print("El campo no puede estar vacio")
                        continue
                    if option3=='1':     
                        self.propietarios.sort(key=lambda propietario: propietario.get_nombre())
                        self.mostrar_bonito(self.propietarios)
                    elif option3=='2':
                        self.propietarios.sort(key=lambda propietario: propietario.get_dni())
                        self.mostrar_bonito(self.propietarios)
                    elif option3=='3':
                        propietarios_ordenados_por_fecha_nacimiento=[]
                        format="%d-%m-%Y"
                        for propietario in self.propietarios:
                            copia_propietario=Propietario(propietario.get_id(),propietario.get_nombre(),propietario.get_dni(),propietario.get_fecha_nacimiento(),propietario.get_direccion(),propietario.get_correo_electronico())
                            fecha_nacimiento=propietario.get_fecha_nacimiento()
                            date_time=datetime.strptime(fecha_nacimiento, format )
                            copia_propietario.set_fecha_nacimiento(date_time)
                            propietarios_ordenados_por_fecha_nacimiento.append(copia_propietario)
                        propietarios_ordenados_por_fecha_nacimiento.sort(key=lambda propietario: propietario.get_fecha_nacimiento())
                        for propietario in propietarios_ordenados_por_fecha_nacimiento:
                            print(propietario.get_fecha_nacimiento(),propietario.get_id(),propietario.get_nombre(), propietario.get_dni(), propietario.get_direccion(), propietario.get_correo_electronico())
                    elif option3=='4' or option3=='s' or option3=='S':
                        print("Has salido de otras operaciones de propietarios.")
                        break
                    input ("Pulse una tecla para continuar... ")










                        





                    

            # Salir
            elif opcion2 == '9' or opcion2 == 's' or opcion2 == 'S':
                print("Has salido de propietarios.")
                break
            else:
                print("Opcion no valida para menú de propietarios.")
                break
            input ("Pulse una tecla para continuar... ")









































    ########################################
    # Funciones auxiliares
    ########################################
    def pedir_id_propietario(self)->int:
        while True:
            id_propietario=input("Introduce el id del propietario, busca propietarios en el menu: ")
            if check_empty(id_propietario):
                print("El id_propietario no puede estar vacio")
                continue
            try:
                id_propietario=int(id_propietario)
            except ValueError:
                print("El id debe ser un entero")
                continue 
            if not is_greater_cero(id_propietario):
                print("El id debe ser mayor que 0")
                continue
            break
        return id_propietario
    def pedir_propietario(self):
        # Pide nombbre
        while True:
            nombre=input("Introduce el nombre (no puede estar ya creado en la base de datos): ")
            #Lo formatemaos para tratarlo mejor sin espacios y con la 1 mayúscula
            nombre=nombre.capitalize().strip()
            if check_empty(nombre):
                print("El nombre del propietario no puede estar vacio")
                continue
            if self.propietarioRepositorio.comprobar_existe_propietario_name(nombre):
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
            if self.propietarioRepositorio.comprobar_existe_propietario_dni(dni):
                print("El dni ya existe")
                continue
            break
        #Pide fecha de nacimiento
        while True:
            fecha=input("Introduce la fecha (dd-mm-aaaa): ")
            #TODO: comprobar que la fecha es correcta
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

    



    def pedir_propietario_conservando_el_que_habia(self, propietario):
        # Pide nombbre
        while True:
            nombre=input(f"Nombre: {propietario.get_nombre()}? ")
            #Lo formatemaos para tratarlo mejor sin espacios y con la 1 mayúscula
            nombre=nombre.capitalize().strip()
            if self.propietarioRepositorio.comprobar_existe_propietario_name(nombre):
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
                if self.propietarioRepositorio.comprobar_existe_propietario_dni(dni):
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
    



    def mostrar_bonito(self,propietarios:list):
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
        print("id  ",
            "|",formatear_cadena("Nombre"),
            "|",formatear_cadena("DNI"),
            "|",formatear_cadena("Fecha nacimiento"),
            "|",formatear_cadena("Dirección"),
            "|",formatear_cadena("Correo electrónico")
        )
    
        print("-"*70)
        for propietario in propietarios:
            print(
                formatear_entero(propietario.get_id()),
                "|",formatear_cadena(propietario.get_nombre()),
                "|",formatear_cadena(propietario.get_dni()),
                "|", formatear_cadena(propietario.get_fecha_nacimiento()),
                "|",formatear_cadena(propietario.get_direccion()),
                "|",formatear_cadena(propietario.get_correo_electronico())
                )
        print("-"*70)
        