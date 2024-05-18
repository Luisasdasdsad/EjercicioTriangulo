from triangulo import Triangulo


def main():
    try:
        # Solicitar al usuario que ingrese los lados del triángulo
        a = float(input("Ingrese el primer lado del triángulo: "))
        b = float(input("Ingrese el segundo lado del triángulo: "))
        c = float(input("Ingrese el tercer lado del triángulo: "))

        # Crear una instancia de Triangulo
        triangulo = Triangulo(a, b, c)

        # Calcular el área
        area = triangulo.calcular_area()

        # Mostrar el resultado
        print(f"El área del triángulo con lados {a}, {b} y {c} es: {area:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()