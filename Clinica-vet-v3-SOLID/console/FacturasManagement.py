from data.repositories.facturaRepository import FacturaRepository
from data.entities.Factura import Factura
from utils.utils import *


class FacturasManagement:
    """
    Representa las operaciones de lectora y escritora en el cmd o terminal de las facturas
    También contiene una lista para hacer operaciones con las facturas

    Args:   
        sqlite3Client (SqliteClient): Representa la base de datos
    """
    def __init__(self,sqlite3Client):
        self.facturaRepository=FacturaRepository(sqlite3Client)
        self.facturas=[]
        

    def menu_factura(self):
        while True:
            print("""
                                Menu Facturas
                ----------------------------------------------
                1. Crear 
                2. Modificar 
                3. Borrar 
                4. Mostrar todas las facturas
                5. Mostrar todas las facturas de una visita
                9 / s. Salir
                """)
            opcion2=input("Introduce una opcion: ")



            # Crear factura
            ###############################################################################
            if opcion2 == '1':
                factura=self.pedir_factura()
                if factura==None:
                    print("Factura no creada")
                else:
                       
                    self.facturaRepository.insert(id=factura.get_id(),
                                                  id_visita=factura.get_id_visita(),
                                                  precio=factura.get_precio()
                                                  )
                    print(factura," creada con éxito")








            # Modificar factura
            ###############################################################################
            elif opcion2 == '2':
                facturas_help=self.facturaRepository.get_all()
                print("Facturas disponibles para modificar:")
                print("id| id_v |precio")
                for i in range(5):
                    print(facturas_help[i])
                id_factura=input("""
                                 Introduce el id de la factura a modificar, 
                                 usa una de la de arriba 
                                 o mira las que hay en menu->Facturas->Mostrar todas las facturas: 
                                 """)
                factura=self.facturaRepository.dame_factura_por_id(id_factura)
                if factura==None:
                    print("factura no encontrada")
                else:
                    factura=self.pedir_factura_conservando_el_que_habia(factura)
                    #self.facturaRepository.modificar_factura(factura)
                    self.facturaRepository.update(
                                                    id=factura.get_id(),
                                                    id_visita=factura.get_id_visita(),
                                                    precio=factura.get_precio()
                                                  )
                    print(factura," modificado con éxito")









            # Borrar factura
            ###############################################################################
            elif opcion2 == '3':
                while True:
                    id_factura=input("Introduce el id de la factura a borrar,del 1 al 10: ")
                    if not is_integer(id_factura):
                        print("La id de la factura debe ser un entero.")
                        continue
                    try:
                        id_factura=int(id_factura)
                    except ValueError:
                        print("La id de la factura debe ser un entero.")
                        continue
                    if not is_greater_cero(id_factura):
                        print("La id de la factura debe ser mayor que 0.")
                        continue
                    break
                factura=self.facturaRepository.dame_factura_por_id(id_factura) 
                if factura==None:
                    print("factura no encontrada")
                else:
                    borrar_sin_no=input(f"¿Quieres borrar {factura}? (s para borrar): ")
                    if borrar_sin_no=='s':
                        self.facturaRepository.delete(factura.get_id())
                        print(factura," borrado con éxito")
                    else:
                        print("Operación de borrado cancelada.")








            # Mostrar todas las facturas
            ###############################################################################
            elif opcion2 == '4':
                faturas=self.facturaRepository.get_all()
                if faturas==None:
                    print("No hay faturas.")
                else:
                    self.mostrar_bonito(faturas)








            #Mostrar todas las visitas de una mascota
            ###############################################################################
            elif opcion2 == '5':
                # Mostrar las Faxturas de una visita
                print("""
                        La visita 1 tiene 3 facturas
                        La visita 4 tiene 2 facturas
                        """)
                while True:
                    id_visita=input("Introduce el id de la visita para ver sus facturas: ")
                    try:
                        id_visita=int(id_visita)
                    except ValueError:
                        print("El id de la visita debe ser un entero.")
                        continue
                    if not is_greater_cero(id_visita):
                        print("El id de la visita debe ser mayor que 0.")
                        continue
                    break
                facturas_visita=self.facturaRepository.dame_facturas_visitas_por_id_visita(id_visita)
                if len(facturas_visita)==0:
                    print("No hay facturas para esa visita.")
                else:
                    print ("id_vi|visita_fecha| id_factura")
                    for item in facturas_visita:
                        print(formatear_entero(item[0]),"|",formatear_cadena(item[1]),"|",formatear_entero(item[2]))





            
            # Salir
            elif opcion2 == '9' or opcion2 == 's' or opcion2 == 'S':
                print("Has salido de factura.")
                break
            else:
                print("Opcion no valida para menú defactura.")
            input ("Pulse una tecla para continuar... ")





















    ########################################
    # Funciones auxiliares
    ########################################
    def pedir_factura(self):
        """
        Id
        Id_visita
        precio
        """
        #Pedir id visita
        while True: 
            print("""
                  La factura tiene asociada un id de visita, 
                  si no pones uno que ya esté creado, tendrás que crear una visita nueva, 
                  esto es importane para la  relacción entre las visitas y las facturas
                  """)
            perimeros_id_visitas=self.facturaRepository.dame_10_primeros_id_de_facturas_visitas()
            if len(perimeros_id_visitas)==0:
                print("No hay visitas.")
            else:
                for item in perimeros_id_visitas:
                    print(item[0], end=" | ")
                print("...")
                print("")

            id_visita=input("Introduce el id de la visita de uno de los de arriba: ")
            if check_empty(id_visita):
                print("El id de la visita debe ser un entero.")
                continue
            try:
                id_visita=int(id_visita)
            except ValueError:
                print("El id de la visita debe ser un entero.")
                continue
            if not is_greater_cero(id_visita):
                print("El id de la visita debe ser mayor que 0.")
                continue
            if not self.facturaRepository.comprobar_existe_visita(id_visita):
                print("El id_visita no existe en la tabla visita.")
                continue
            break

        #Pedir precio   
        while True:
            precio=input("Introduce el precio: ")
            precio=precio.strip()
            if not es_moneda_euros(precio):
                print("El precio introducido no es valido, introduce 12,50  1234.56 ")
                continue
            try:
                precio=float(precio)
            except ValueError:
                print("El precio introducido no es valido, introduce 12,50  1234.56 ")
                continue
            if not is_greater_cero(precio):
                print("El precio introducido no es mayor de 0, introduce 12,50  1234.56 ")
                continue
            break      
            

        factura=Factura(None,id_visita,precio)
        return factura
    def pedir_factura_conservando_el_que_habia(self, factura:Factura):
        while True: 
            print("""
                  La factura tiene asociada un id de visita, 
                  si no pones uno que ya esté creado, tendrás que crear una visita nueva, 
                  esto es importane para la  relacción entre las visitas y las facturas
                  """)
            perimeros_id_visitas=self.facturaRepository.dame_10_primeros_id_de_facturas_visitas()
            if len(perimeros_id_visitas)==0:
                print("No hay visitas.")
            else:
                for item in perimeros_id_visitas:
                    print(item[0], end=" | ")
                print("...")
                print("")
            id_visita=input(f"En la factura el id_visita es: {factura.get_id_visita()} ?: ")
            if check_empty(id_visita):
                id_visita=factura.get_id_visita()
            try:
                id_visita=int(id_visita)
            except ValueError:
                print("El id de la visita debe ser un entero.")
                continue
            if not is_greater_cero(id_visita):
                print("El id de la visita debe ser mayor que 0.")
                continue
            if not self.facturaRepository.comprobar_existe_visita(id_visita):
                print("El id_visita no existe en la tabla visita.")
                continue
            break
        while True:
            precio=input(f"Precio: {factura.get_precio()} ? ")
            precio=precio.strip()
            if precio=="":
                precio=factura.get_precio()
                break
            if not es_moneda_euros(precio):
                print("El precio introducido no es valido, introduce 12,50  1234.56 € ")
                continue
            break   
        factura=Factura(None,id_visita,precio)
        return factura
    
    def mostrar_bonito(self,facturas):
        """
        Muestra de una forma bonita la lista que le pasas

        Args:
            fcaturas (List)
        """
        print("id  ",
            "| id_v",
            "|",formatear_cadena("Precio")
        )
        print("-"*90)
        for factura in facturas:
            print(
                formatear_entero(factura[0]),
                "|",formatear_entero(factura[1]),
                "|",float_moneda_a_str(factura[2])
                )
        print("-"*90)
