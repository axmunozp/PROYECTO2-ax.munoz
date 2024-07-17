import unittest
from models.producto import Productos
from models.ingrediente import Ingredientes

class TestProductos(unittest.TestCase):

    def setUp(self):
        self.producto_con_ingredientes = Productos(
            ingrediente1=Ingredientes(nombre="Ingrediente 1", precio=10, calorias=50),
            ingrediente2=Ingredientes(nombre="Ingrediente 2", precio=15, calorias=70),
            ingrediente3=Ingredientes(nombre="Ingrediente 3", precio=20, calorias=90)
        )
        self.producto_con_ingredientes_2 = Productos(
            nombre="Producto 1",
            precio_publico=100,
            ingrediente1=Ingredientes(nombre="Ingrediente 1", precio=10),
            ingrediente2=Ingredientes(nombre="Ingrediente 2", precio=15),
            ingrediente3=Ingredientes(nombre="Ingrediente 3", precio=20)
        )
        


    def test_calcular_costo(self):
        resultado = self.producto_con_ingredientes.calcular_costo()
        costo_esperado = 10 + 15 + 20
        self.assertEqual(resultado, f"Costo del producto: ${costo_esperado}")

    def test_calcular_calorias(self):
        resultado = self.producto_con_ingredientes.calcular_calorias()
        calorias_esperadas = round((50 + 70 + 90) * 0.95, 2)
        self.assertEqual(resultado, f"Calorias totales: {calorias_esperadas}")

    def test_calcular_rentabilidad(self):
        # Prueba para calcular_rentabilidad
        resultado = self.producto_con_ingredientes_2.calcular_rentabilidad()
        # Calculamos la rentabilidad esperada
        precios_ingredientes = 10 + 15 + 20  # Suma de los precios de los ingredientes
        rentabilidad_esperada = 100 - precios_ingredientes
        self.assertEqual(resultado, f"Rentabilidad: ${rentabilidad_esperada}")

