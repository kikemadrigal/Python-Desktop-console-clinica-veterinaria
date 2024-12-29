from  data.repositories.visitaRepository import VisitaRepository
from  data.entities.Visita import Visita
from utils.utils import *
class VisitasManagement:
    """
    Representa las operaciones de lectora y escritora en el cmd o terminal de las visitas

    Args:   
        sqlite3Client (SqliteClient): Representa la base de datos
    """
    def __init__(self,sqlite3Client):
        self.visitaRepository=VisitaRepository(sqlite3Client)
        self.visitas=[]
        # Rellenamos la lista de visitas
        self.visitas=self.visitaRepository.get_all()
        
    def menu_visita(self):
        while True:
            print("""
                                                Visitas
                                    -------------------------------------
                                    1 Crear
                                    2 Modificar
                                    3 Borrar
                                    4 Mostrar todas las visitas
                                    5 Mostrar las visitas de una mascota
                                    9 / s Salir
                """)
            opcion2=input ("Introduce una opcion: ")




            # 1. crear visita
            ###################################################################
            if opcion2 == '1':
                visita=self.pedir_visita()
                if(visita!=None):
                    self.visitaRepository.insert(id=visita.get_id(),
                                                 id_mascota=visita.get_id_mascota(),
                                                 fecha_visita=visita.get_fecha_visita(),
                                                 descripcion=visita.get_descripcion(),
                                                 tratamiento=visita.get_tratamiento()
                                                 )
                    # Añadimos la visita a la lista
                    self.visitas.append(visita)
                    print(visita," anadido con éxito")
                else:
                    print("Visita no creada")

            # 2. Modificar visita
            ###################################################################
            elif opcion2 == '2':
                id_visita=input("Introduce el id de la visita a modificar, si no lo sabes ve a mostrar todas las visitas, por ejemplo: del 1 al 10: ")
                visita=self.visitaRepository.dame_visita_por_id_visita(id_visita)
                if visita==None:
                    print("Visita no encontrada")
                else:
                    visita=self.pedir_visita_conservando_la_que_habia(visita)
                    self.visitaRepository.update(visita.get_id(),
                                                 id_mascota=visita.get_id_mascota(),
                                                 fecha_visita=visita.get_fecha_visita(),
                                                 descripcion=visita.get_descripcion(),
                                                 tratamiento=visita.get_tratamiento()
                                                 )
                    # La modificamos de la lista
                    for i in range(len(self.visitas)):
                        if self.visitas[i].get_id()==id_visita:
                            self.visitas[i]=visita
                    print(visita," modificado con éxito")
            # 3. Borrar visita
            ###################################################################
            elif opcion2 == '3':
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
                visita=self.visitaRepository.dame_visita_por_id_visita(id_visita) 
                if visita==None:
                    print("Visita no encontrada")
                else:
                    borrar_sin_no=input(f"¿Quieres borrar {visita}? (s para borrar): ")
                    if borrar_sin_no=='s':
                        self.visitaRepository.delete(visita.get_id())
                        #Borramos la visita d ela lista
                        for i in self.visitas:
                            if i.get_id()==visita.get_id():
                                self.visitas.remove(i)
                        print(visita," borrado con éxito")
                    else:
                        print("Operación de borrado cancelada.")




            # 4. Mostrar todas las visitas
            ###################################################################
            elif opcion2 == '4':
                visitas=self.visitaRepository.get_all()
                if len(visitas)==0:
                    print("No hay visitas.")
                else:
                    self.mostrar_bonito(visitas)



            # 5.Mostrar todas las visitas de una mascota
            ###################################################################
            elif opcion2 == '5':
                print("""
                        La mascota 1 (Coco) tiene 2 visitas
                        La mascota 2 (Pipo) tiene 2 visitas
                        La mascota 3 (Hugo) tiene 1 visita
                        la mascota 4 (Pluto) tiene 3 visitas
                        La mascota 5 (Robin) no tiene visitas 
                        La mascota 6 (Simba) tiene 1 visita
                        """)
                while True:
                    nombre_mascota=input("Introduce el nombre de la mascota para ver sus visitas: ")
                    if check_empty(nombre_mascota):
                        print("El nombre de la mascota no puede estar vacío.")
                        continue
                    nombre_mascota=nombre_mascota.capitalize().strip()
                    break
                nombre_mascota=nombre_mascota.capitalize()
                visitas_mascota=self.visitaRepository.dame_visitas_por_nombre_mascota(nombre_mascota)
                if visitas_mascota==None:
                    print("No hay visitas de la mascota",nombre_mascota)
                else:
                    self.mostrar_bonito(visitas_mascota)


            elif opcion2 == '5' or opcion2 == 's' or opcion2 == 'S':
                print("Has salido de visitas.")
                break
            else:
                print("Opcion no valida para menú de visitas.")
            input ("Pulse una tecla para continuar... ")
























    
    ########################################
    # Funciones auxiliares
    ########################################
    def pedir_visita(self):
        """
        T_Visita
        ----------
        Id o NumeroVisita 
        IdMascota 
        Fecha de la visita 
        Descripción 
        Tratamiento
        """
        print("""
                                CREANDO UNA VISITA
              -----------------------------------------------------------------
              La tabla visita tiene asociado el id de la mascota,
              por esto es necesario que introduzca el id de la mascota
              si no lo sabe, vaya al menu mascota y cree una nueva,
              las primeros id de las mascotas actuales son:
              """)
        perimeros_id_visitas=self.visitaRepository.dame_10_primeros_id_de_visitas_mascotas()
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
            if not self.visitaRepository.comprobar_existe_mascota(id_mascota):
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
    



    def pedir_visita_conservando_la_que_habia(self, visita):
        perimeros_id_visitas=self.visitaRepository.dame_10_primeros_id_de_visitas_mascotas()
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
            if not self.visitaRepository.comprobar_existe_mascota(id_mascota):
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
            
        visita=Visita(None,id_mascota,fecha_visita,dscripcion,tratamiento) 
        return visita

    def mostrar_bonito(self,visitas):
        """
        T_Visita
        ----------
        Id o NumeroVisita 
        IdMascota 
        Fecha de la visita 
        Descripción 
        Tratamiento
        """
        print("id  ",
            "| id_m",
            "|",formatear_cadena("fecha visita"),
            "|",formatear_cadena("Decripción"),
            "|",formatear_cadena("Tratamiento")
        )
        
        print("-"*70)
        for visita in visitas:
            print(
                formatear_entero(visita.get_id()),
                "|",formatear_entero(visita.get_id_mascota()),
                "|",formatear_cadena(visita.get_fecha_visita()),
                "|",formatear_cadena(visita.get_descripcion()),
                "|",formatear_cadena(visita.get_tratamiento())
                )
        print("-"*70)