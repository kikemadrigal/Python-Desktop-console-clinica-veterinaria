import unittest
from unittest.mock import patch

class TestUtils(unittest.TestCase):
    def test_check_empty(self):
        from src.utils.utils import check_empty
        assert check_empty("")
        assert check_empty(" ")
        assert not check_empty("a")
        assert not check_empty("a ")
        assert not check_empty(" a")

    #R ecorta un string a 10 caracters y si es menor lo rellena con espacios
    def test_formatear_cadena(self):
        from src.utils.utils import formatear_cadena
        # 1 .Preparamos los datos del test
        cadena_menor="a"*8
        cadena_mayor="a"*52
        # 2. Ejecutar lo que tiene que hacer el test
        #podemos envolver la ejecucion de la funcion con un assert.raises
        #with self.assertRaises(ValueError):
        resultado_menor=formatear_cadena(cadena_menor)
        #with self.assertRaises(ValueError):
        resultado_mayor=formatear_cadena(cadena_mayor)
        # 3. Comprobar el resultado
        self.assertEqual(len(resultado_menor), 10)
        self.assertEqual(len(resultado_mayor), 10)
#Puesdes ejecutar el test en consola con: python -m unittest tests.test_utils
# o python -m unittest pero ejecutará todos los tests
if __name__ == "__main__":
    unittest.main()



   
