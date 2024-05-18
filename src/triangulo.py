import math


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_area(self):
        # Calcular el semiperímetro
        s = (self.a + self.b + self.c) / 2

        # Aplicar la fórmula de Herón
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return area