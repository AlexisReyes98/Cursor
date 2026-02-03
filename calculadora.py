# Pide al usuario una operación (suma, resta, multiplicación, división) y dos números.
# Ejecute la operación y muestre el resultado.
# Debe repetirse hasta que el usuario escriba "salir" como operación.

#while True:
#    operacion = input("Introduce la operación (suma, resta, multiplicacion, division) o 'salir' para salir: ")
#    if operacion == "salir":
#        break
#    try:        
#        numero1 = float(input("Introduce el primer número: "))
#        numero2 = float(input("Introduce el segundo número: "))
#        if operacion == "suma":
#            print(numero1 + numero2)
#        elif operacion == "resta":
#            print(numero1 - numero2)
#        elif operacion == "multiplicacion":
#            print(numero1 * numero2)
#        elif operacion == "division":
#            if numero2 == 0:
#                raise ZeroDivisionError("No se puede dividir por cero.")
#            print(numero1 / numero2)
#        else:
#            print("Operación no válida.")
#    except ValueError:
#        print("Introduce un número válido.")
#    except ZeroDivisionError:
#        print("No se puede dividir por cero.")

#while True:
#    operacion = input("Introduce la operación (suma, resta, multiplicacion, division) o 'salir' para salir: ")
#    if operacion == "salir":
#        break
#    try:
#        numero1 = float(input("Introduce el primer número: "))
#        numero2 = float(input("Introduce el segundo número: "))
#        match operacion:
#            case "suma":
#                print(numero1 + numero2)
#            case "resta":
#                print(numero1 - numero2)
#            case "multiplicacion":
#                print(numero1 * numero2)
#            case "division":
#                print(numero1 / numero2)
#            case _:
#                print("Operación no válida.")
#    except ValueError:
#        print("Introduce un número válido.")
#    except ZeroDivisionError:
#        print("No se puede dividir por cero.")

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    if numero2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return numero1 / numero2

switcher = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division,
}

while True:
    operacion = input("Introduce la operación (suma, resta, multiplicacion, division) o 'salir' para salir: ")
    if operacion == "salir":
        break
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        resultado = switcher.get(operacion, lambda: "Operación no válida")(numero1, numero2)
        print(resultado)
    except ValueError:
        print("Introduce un número válido.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")