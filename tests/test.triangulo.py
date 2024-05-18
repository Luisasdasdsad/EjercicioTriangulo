import unittest
from src.triangulo import Triangulo


class TestTriangulo(unittest.TestCase):
    def test_area(self):
        # Crear una instancia de Triangulo
        triangulo = Triangulo(5, 6, 7)

        # Calcular el área
        area = triangulo.calcular_area()

        # Verificar el área esperada
        self.assertAlmostEqual(area, 14.6969, places=4)

    def test_area_zero(self):
        triangulo = Triangulo(0, 0, 0)
        area = triangulo.calcular_area()
        self.assertEqual(area, 0)

    def test_area_imposible(self):
        triangulo = Triangulo(1, 1, 10)
        area = triangulo.calcular_area()
        self.assertEqual(area, 0)  # Un triángulo imposible debería tener área 0 o lanzar un error


if __name__ == "__main__":
    unittest.main()