import unittest
from models.ingrediente import Ingredientes


class TestIngrediente(unittest.TestCase):

    def test_esSano_con_calorias_menor_a_100_y_vegetariano(self):
        ingrediente = Ingredientes(nombre="Leche de almendras", calorias=50, es_vegetariano=True)
        self.assertTrue(ingrediente.esSano())

    def test_esSano_con_calorias_mayor_o_igual_a_100_y_no_vegetariano(self):
        ingrediente = Ingredientes(nombre="Chocolate", calorias=150, es_vegetariano=False)
        self.assertFalse(ingrediente.esSano())

    def test_esSano_con_calorias_mayor_o_igual_a_100_y_vegetariano(self):
        ingrediente = Ingredientes(nombre="Fresa", calorias=120, es_vegetariano=True)
        self.assertTrue(ingrediente.esSano())

    def test_esSano_con_calorias_menor_a_100_y_no_vegetariano(self):
        ingrediente = Ingredientes(nombre="Queso", calorias=80, es_vegetariano=False)
        self.assertTrue(ingrediente.esSano())
    
    def setUp(self):
        # Configuración inicial para las pruebas
        self.ingrediente = Ingredientes(nombre="Leche", inventario=10)  # Ingrediente con inventario inicial de 10
    
    def test_abastecer_aumenta_inventario(self):
        self.ingrediente.abastecer()  
        self.assertEqual(self.ingrediente.inventario, 15)  

    def test_abastecer_multiples_veces(self):
        self.ingrediente.abastecer()  
        self.assertEqual(self.ingrediente.inventario, 15)  
        self.ingrediente.abastecer()  
        self.assertEqual(self.ingrediente.inventario, 20)  

    def test_renovar_inventario(self):
        inventario_actual = self.ingrediente.renovar_inventario()  
        self.assertEqual(inventario_actual, 0)  

    def test_renovar_inventario_multiples_veces(self):
        self.ingrediente.renovar_inventario()  
        inventario_actual = self.ingrediente.renovar_inventario()  
        self.assertEqual(inventario_actual, 0)  


