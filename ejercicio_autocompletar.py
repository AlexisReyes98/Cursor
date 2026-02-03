# Crear una lista con los cuadrados de los n primeros números naturales usando un bucle for

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)
print(cuadrados)


def primmo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(primmo(11))
