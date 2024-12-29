from data.repositories.mascotaRepository import MascotaRepository
from data.entities.Mascota import Mascota
from utils.utils import *
class MascotasManagement:
    """
    Representa las operaciones de lectora y escritora en el cmd o terminal de las mascostas
    """
    def __init__(self, sqlite3Client):
        self.sqlite3Client = sqlite3Client
        self.mascotaRepository = MascotaRepository(sqlite3Client)
        self.mascotas=[]
        # Rellenamos la lista de mascotas
        self.mascotas=self.mascotaRepository.get_all()
        
    def menu_mascota(self):
        while True:
                print("""
                                                Mascotas
                      -----------------------------------------------------------------
                                0  Buscar
                                1  Crear
                                2  Modificar
                                3  Borrar
                                4  Mostrar todas las mascotas
                                5  Mostrar cuantas mascotas hay de un tipo especifico
                                6. Otras operaciones
                                9 / s Salir
                    """)
                opcion2=input ("Introduce una opcion: ")



                # Buscar mascota
                ########################################################################################
                if opcion2 == '0':
                    while True:
                        print("""
                                                    Buscar mascota
                        -----------------------------------------------------------------
                                    1 Buscar por id
                                    2 Buscar por nombre propietario
                                    3 Buscar por nombre
                                    4 Buscar por tipo
                                    5 Buscar por raza
                                    6 Buscar por fecha de nacimiento
                                    7 Buscar por peso
                                    8 Buscar por color
                                    9 / s para salir
                        """)
                        opcion3=input ("Introduce una opcion: ")

                        #id
                        if opcion3 == '1':
                            id_mascota=self.pedir_id_mascota()
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("id",id_mascota)
                            if mascotas==None:
                                print("Mascota no encontrada")
                            else:
                                mascota=mascotas[0]
                                print(mascota)
                        #Busca por nombre propietario
                        elif opcion3 == '2':
                            while True:
                                nombre_propietario=input("Introduce el nombre del propietario de la mascota a buscar (ejemplo sergio, carlos): ")
                                if check_empty(nombre_propietario):
                                    print("El id del propietario no puede estar vacio")
                                    continue    
                                nombre_propietario=nombre_propietario.capitalize().strip()
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_nombre_propietario(nombre_propietario)
                            if mascotas==None:
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        # Buscar por nombre mascota
                        elif opcion3 == '3':
                            while True:
                                nombre_mascota=input("Introduce el nombre de la mascota a buscar: ")
                                if check_empty(nombre_mascota):
                                    print("El nombre de la mascota no puede estar vacio")
                                    continue
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("nombre",nombre_mascota)
                            
                            if mascotas==None:
                                print("Mascota no encontrada")
                            else:
                                self.mostrar_bonito(mascotas)  
                        # Buscar por tipo
                        elif opcion3 == '4':
                            tipos=self.mascotaRepository.dame_tipos()
                            tipos_mascota=[]
                            print("Los tipos son:")
                            for tipo in tipos:
                                print (tipo[0])
                                tipos_mascota.append(tipo[0])
                            while True:
                                tipo_mascota=input("Introduce el tipo de la mascota a buscar: ")
                                tipo_mascota=tipo_mascota.capitalize().strip()
                                if check_empty(tipo_mascota):
                                    print("El tipo de la mascota no puede estar vacio")
                                    continue
                                if tipo_mascota not in tipo_mascota:
                                    print("El tipo de la mascota no existe")
                                    continue
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("tipo",tipo_mascota)
                            if mascotas==None:
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        # Buscar por raza
                        elif opcion3 == '5':
                            raza_mascota=input("Introduce la raza de la mascota a buscar (pastor, angora, persa, etc): ")    
                            raza_mascota=raza_mascota.capitalize().strip()
                            while True:
                                if check_empty(raza_mascota):
                                    print("La raza de la mascota no puede estar vacio")
                                    continue
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("raza",raza_mascota)
                            if mascotas==None:    
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        # Buscar por fecha
                        elif opcion3 == '6':
                            while True:
                                fecha_nacimiento_mascota=input("Introduce la fecha de nacimiento de la mascota a buscar (dd-mm-aaaa): ") 
                                if check_empty(fecha_nacimiento_mascota):
                                    print("La fecha de nacimiento de la mascota no puede estar vacio")
                                    continue
                                if not check_fecha(fecha_nacimiento_mascota):
                                    print("La fecha de nacimiento de la mascota no es correcta")
                                    continue
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("fecha_nacimiento",fecha_nacimiento_mascota)
                            if mascotas==None:
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        # Buscar por peso
                        elif opcion3 == '7':
                            while True:
                                peso_mascota=input("Introduce el peso de la mascota a buscar (ejemplo 2.2): ")
                                if check_empty(peso_mascota):
                                    print("El peso de la mascota no puede estar vacio")
                                    continue
                                try:
                                    float(peso_mascota)
                                except ValueError:
                                    print("El peso de la mascota debe ser un float, ejemplo 2.5")
                                    continue
                                break   
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("peso",peso_mascota) 
                            if mascotas==None:    
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        # Buscar por color
                        elif opcion3 == '8':
                            while True:
                                color_mascota=input("Introduce el color de la mascota a buscar: ")
                                if check_empty(color_mascota):
                                    print("El color de la mascota no puede estar vacio")
                                    continue
                                color_mascota=color_mascota.capitalize().strip()
                                break
                            mascotas=self.mascotaRepository.dame_mascotas_por_campo("color",color_mascota)
                            if mascotas==None:
                                print("Mascotas no encontradas")
                            else:
                                self.mostrar_bonito(mascotas)
                        elif opcion3== '9' or opcion3 == 's' or opcion3 == 'S':
                            print("Has salido del menú buscar mascotas.")
                            break
                        else:
                            print("Opcion no valida")
                        input("Pulsa enter para continuar")








                # Crear mascota
                ########################################################################################
                elif opcion2 == '1':
                    mascota=self.pedir_mascota()
                    if mascota!=None:
                        self.mascotaRepository.insert(**mascota.__dict__)
                        #La metemos en la lista
                        mascota.set_id(self.mascotaRepository.get_last_id())
                        self.mascotas.append(mascota)
                        print(mascota," anadido con éxito")







                # Modificar mascota
                ########################################################################################
                elif opcion2 == '2':
                    id_mascota=self.pedir_id_mascota()
                    #Llamamos a la base de datos para que nos dé la mascota
                    mascotas=self.mascotaRepository.dame_mascotas_por_campo("id",id_mascota)  
                    if mascotas==None:
                        print("Mascota no encontrada")
                    else:
                        mascota=mascotas[0]
                        # Llamamos a la función dentro de esta clase que sigue con las preguntas
                        mascota=self.pedir_mascota_conservando_la_que_habia(mascota)
                        # Modificamos llamando a la base de datos
                        self.mascotaRepository.update(mascota.get_id(), 
                                                    id_propietario=mascota.get_id_propietario(),
                                                    nombre=mascota.get_nombre(),
                                                    tipo=mascota.get_tipo(),
                                                    raza=mascota.get_raza(),
                                                    fecha_nacimiento=mascota.get_fecha_nacimiento(),
                                                    peso=mascota.get_peso(),
                                                    color=mascota.get_color(),
                                                    notas=mascota.get_notas()
                                                )
                        # Lo modificamos en la lista
                        for i in range(len(self.mascotas)):
                            if self.mascotas[i].get_id()==mascota.get_id():
                                self.mascotas[i]=mascota
                        print(mascota," modificado con éxito")







                # Borrar mascota
                ########################################################################################
                elif opcion2 == '3':
                    id_mascota=self.pedir_id_mascota()
                    mascotas=self.mascotaRepository.dame_mascotas_por_campo("id",id_mascota) 
                    if mascotas==None:
                        print("Mascota no encontrada")
                    else:
                        mascota=mascotas[0]
                        borrar_sin_no=input(f"¿Quieres borrar {mascota}? (s para borrar): ")
                        if borrar_sin_no=='s':
                            self.mascotaRepository.delete(mascota.get_id())
                            #Lo borramos en la lista
                            for i in self.mascotas:
                                if i.get_id()==mascota.get_id():
                                    self.mascotas.remove(i)
                            print(mascota," borrado con éxito")
                        else:
                            print("Operación de borrado cancelada.")










                # Mostrar todas las mascotas
                ########################################################################################
                elif opcion2 == '4':
                    self.mostrar_bonito(self.mascotas)










                # Mostrar cuantas mascotas hay de un tipo especifico, también se puede añadir raza en la búsqueda.
                ##################################################################################################
                elif opcion2 == '5':
                    """
                    Tiene que dar algo como esto:
                                input=Perro
                                        3 de raza Terrier
                                        2 de raza Pastor
                                        1 de raza Labrador
                                        1 de raza Chihuahua
                                input= Gato
                                        2 de raza Persa
                                        1 de raza Siamés
                                        1 de raza Angora
                                input= Conejo
                                        1 de raza Salvaje
                                input= Pajaro
                                        1 de raza Canario
                    """
                    tipo_introducido=input("Introduce el tipo de mascota, por ejemplo: Perro, Gato, Pájaro, Conejo: ")
                    tipo_introducido=tipo_introducido.capitalize().strip()
                    tipos_agrupadas_por_raza=self.mascotaRepository.dame_mascotas_por_tipo_agrupadas_por_raza(tipo_introducido)
                    tipo_no_encontrado=False
                    for tipo, raza, cantidad in tipos_agrupadas_por_raza:
                        if tipo_introducido==tipo:
                            tipo_no_encontrado=True
                        print(f"Tip: {tipo}, raza {raza} tiene cantidad {cantidad}.")
                    if not tipo_no_encontrado:
                        print("No hay mascotas de ese tipo.")




                # 6. Otras operaciones  
                ####################################################################
                elif opcion2 == '6':
                    while True:
                        option3=input("""
                                        Introduce:
                                        1 ordenar por nombre
                                        2 ordenar por tipo
                                        3 ordenar por raza
                                        4 ordenar por fecha de nacimiento
                                        5 ordenar por peso
                                        6 ordenar por color
                                        9 / s para salir: 
                                        """)
                        if check_empty(option3):
                            print("El campo no puede estar vacio")
                            continue
                        if option3=='1':     
                            self.mascotas.sort(key=lambda mascota: mascota.get_nombre())
                            self.mostrar_bonito(self.mascotas)
                        elif option3=='2':
                            self.mascotas.sort(key=lambda mascota: mascota.get_tipo())
                            self.mostrar_bonito(self.mascotas)
                        elif option3=='3':
                            self.mascotas.sort(key=lambda mascota: mascota.get_raza())
                            self.mostrar_bonito(self.mascotas)
                        elif option3=='4':
                            mascotas_ordenadas_por_fecha_nacimiento=[]
                            format="%d-%m-%Y"
                            for mascota in self.mascotas:
                                copia_mascota=Mascota(mascota.get_id(),mascota.get_id_propietario(),mascota.get_nombre(),mascota.get_tipo(),mascota.get_raza(),mascota.get_fecha_nacimiento(),mascota.get_peso(),mascota.get_color(),mascota.get_notas())
                                fecha_nacimiento=mascota.get_fecha_nacimiento()
                                date_time=datetime.strptime(fecha_nacimiento, format )
                                copia_mascota.set_fecha_nacimiento(date_time)
                                mascotas_ordenadas_por_fecha_nacimiento.append(copia_mascota)
                            mascotas_ordenadas_por_fecha_nacimiento.sort(key=lambda mascota: mascota.get_fecha_nacimiento())
                            for mascota in mascotas_ordenadas_por_fecha_nacimiento:
                                print(mascota.get_id(),mascota.get_id_propietario(),mascota.get_nombre(),mascota.get_tipo(),mascota.get_raza(),mascota.get_fecha_nacimiento(),mascota.get_peso(),mascota.get_color(),mascota.get_notas())
                        elif option3=='5':
                            self.mascotas.sort(key=lambda mascota: mascota.get_peso())
                            self.mostrar_bonito(self.mascotas)
                        elif option3=='6':
                            self.mascotas.sort(key=lambda mascota: mascota.get_color())
                            self.mostrar_bonito(self.mascotas)
                        elif option3=='9' or option3=='s' or option3=='S':
                            print("Has salido de otras operaciones de mascotas.")
                            break
                        input ("Pulse una tecla para continuar... ")











                    
                # Salir
                elif opcion2 == '9' or opcion2 == 's' or opcion2 == 'S':
                    print("Has salido de mascotas.")
                    break
                else:
                    print("Opcion no valida para menú de mascotas.")
                input ("Pulse una tecla para continuar... ")
















































    def pedir_id_mascota(self):
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



    ########################################
    # Funciones auxiliares
    ########################################
    def pedir_mascota(self):
        tipos_validos=self.mascotaRepository.dame_tipos()
        while True:
            print("""
                                CREANDO UNA MASCOTA
              -----------------------------------------------------------------
              La tabla mascota tiene asociado el id del propietario,
              por esto es necesario que introduzca el id del propietario
              si no lo sabe, vaya al menu propietario y cree un propietario,
              las primeros id de los propietarios actuales son:
              """)
            mascotas_propietarios=self.mascotaRepository.dame_10_primeros_mascotas_propietarios()
            if mascotas_propietarios==None:
                print("No hay mascotas.")
            else:
                for item in mascotas_propietarios:
                    print(item[0], "(", item[1], ")", end=" | ")
                print("...")
                print("")
            id_propietario=input("Introduce el id_propietario: ")
            if check_empty(id_propietario):
                print("El id_propietario no puede estar vacio")
                continue
            try:
                id_propietario=int(id_propietario)
            except ValueError:
                print("El id_propietario debe ser un entero")
                continue
            if not is_greater_cero(id_propietario):
                print("El id_propietario debe ser mayor que 0")
                continue
            if not self.mascotaRepository.comprobar_existe_propietario("id",id_propietario):
                print("El id_propietario no existe en la tabla propietario.")
                continue
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
    





    def pedir_mascota_conservando_la_que_habia(self, mascota:Mascota)->Mascota:
        tipos_validos=self.mascotaRepository.dame_tipos()
        while True:
            print("""
                                CREANDO UNA MASCOTA
              -----------------------------------------------------------------
              La tabla mascota tiene asociado el id del propietario,
              por esto es necesario que introduzca el id del propietario
              si no lo sabe, vaya al menu propietario y cree un propietario,
              las primeros id de los propietarios actuales son:
              """)
            mascotas_propietarios=self.mascotaRepository.dame_10_primeros_mascotas_propietarios()
            if mascotas_propietarios==None:
                print("No hay mascotas.")
            else:
                for item in mascotas_propietarios:
                    id_propietario=item[0]
                    nombre_propietario=item[1]
                    print(id_propietario, "(", nombre_propietario, ")" , end=" | ")
                print("...")
                print("")
            id_propietario=input(f" id_propietario {mascota.get_id_propietario()}? Déjalo vacío para conservarlo: ")
            if id_propietario=="":
                id_propietario=mascota.get_id_propietario()
            try:
                id_propietario=int(id_propietario)
            except ValueError:
                print("El id_propietario debe ser un entero")
                continue
            if not is_greater_cero(id_propietario):
                print("El id_propietario debe ser mayor que 0")
                continue
            if not self.mascotaRepository.comprobar_existe_propietario("id",id_propietario):
                print("El id_propietario no existe")
                continue
            break

        nombre=input(f"Nombre: {mascota.get_nombre()}? Déjalo vacío para conservarlo: ")
        #Lo formatemaos para tratarlo mejor sin espacios y con la 1 mayúscula
        mascota.set_nombre(nombre.capitalize().strip())
        if nombre=="":
            nombre=mascota.get_nombre()

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
    

    def mostrar_bonito(self,mascotas):
        print("id  ",
            "| id_p",
            "|",formatear_cadena("Nombre"),
            "|",formatear_cadena("Tipo"),
            "|",formatear_cadena("Raza"),
            "|",formatear_cadena("Fecha nacimiento"),
            "| Peso",
            "|",formatear_cadena("Color"),
            "|",formatear_cadena("Notas")
        )
    
        print("-"*90)
        for mascota in mascotas:
            print(
                formatear_entero(mascota.get_id()),
                "|",formatear_entero(mascota.get_id_propietario()),
                "|",formatear_cadena(mascota.get_nombre()),
                "|", formatear_cadena(mascota.get_tipo()),
                "|",formatear_cadena(mascota.get_raza()),
                "|",formatear_cadena(mascota.get_fecha_nacimiento()),
                "|",formatear_float(mascota.get_peso()),
                "|",formatear_cadena(mascota.get_color()),
                "|",formatear_cadena(mascota.get_notas())
                )
        print("-"*90)


