def operaciones():

    # Pedir al usuario que ingrese dos números
    x = input("Ingrese el primer número: ")
    y = input("Ingrese el segundo número: ")

    # Convertir las entradas a enteros
    x1 = int(x)
    y1 = int(y)

    # Pedir al usuario que elija la operación
    operacion = input("Ingrese la operación que desea realizar (suma/resta): ").strip().lower()

    # Realizar la operación correspondiente
    if operacion == "suma":
        resultado = x1 + y1
        operacion_texto = "suma"
    elif operacion == "resta":
        resultado = x1 - y1
        operacion_texto = "resta"
    else:
        return "Operación no válida. Por favor, ingrese 'suma' o 'resta'."

    return f"El resultado de la {operacion_texto} es: {resultado}"
print(operaciones())
