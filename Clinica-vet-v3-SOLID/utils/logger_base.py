import logging

class Logger:
    """
    Clase que se encarga de mostrar los mensajes en la consola
    escribe: 
    from logger_base import Logger
    Logger().info("La longitud inicial de la cadena es: "+str(len(cadena)))
    """
    log = None
    def __init__(self):
        self.log = logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.log = logging.getLogger(__name__)

    def info(self, message):
        self.log.info(message)