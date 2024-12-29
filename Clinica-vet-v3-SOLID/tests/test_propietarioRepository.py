import unittest
from unittest.mock import patch,Mock
import sys, os


class TestPropietarioRepository(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        myPath = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, myPath + '/../')
    #@patch('data.sqliteCliente.SqliteCliente')
    def test_comprobar_existe_propietario_dni(self):
        from data.sqliteCliente import SqliteCliente
        from data.repositories.propietarioRepository import PropietarioRepository 
        propietario_repository = PropietarioRepository(SqliteCliente())
        result_wueno = propietario_repository.comprobar_existe_propietario_dni("36581601D")
        self.assertTrue(result_wueno)
        result_malo = propietario_repository.comprobar_existe_propietario_dni("111111111")
        self.assertFalse(result_malo)
    def test_comprobar_existe_propietario_name(self):
        from data.sqliteCliente import SqliteCliente
        from data.repositories.propietarioRepository import PropietarioRepository 
        propietario_repository = PropietarioRepository(SqliteCliente())
        result_wueno = propietario_repository.comprobar_existe_propietario_name("Loreto")
        self.assertTrue(result_wueno)
        result_malo = propietario_repository.comprobar_existe_propietario_name("111111111")
        self.assertFalse(result_malo)
    def test_dame_propietarios_por_campo(self):
        from data.sqliteCliente import SqliteCliente
        from data.repositories.propietarioRepository import PropietarioRepository 
        propietario_repository = PropietarioRepository(SqliteCliente())
        result_wueno = propietario_repository.dame_propietarios_por_campo("nombre","Loreto")
        assert(len(result_wueno)>0)
        result_malo = propietario_repository.dame_propietarios_por_campo("111111111","Loreto")
        assert(result_malo==None)

#Ejecuta con python -m unittest test_propietarioRepository
if __name__ == '__main__':
    unittest.main()

        
