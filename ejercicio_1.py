def operacion(opcion, num1, num2):
    if opcion == 1:
        return num1 + num2
    elif opcion == 2:
        return num1 * num2
    else:
        return "Opción no válida"


while True:
    print("Ingrese un número ")
    print("1. Suma")
    print("2. Multiplicacion")
    opcion = int(input())

    print("Ingrese un número:")
    num1 = int(input())

    print("Ingrese otro número:")
    num2 = int(input())

    resultado = operacion(opcion, num1, num2)
    print("El resultado es:", resultado)