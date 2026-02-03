# Programa para contar palabras en un archivo de texto
# 1. Pedir al usuario la ruta de un archivo de texto.
# 2. Leer el contenido del archivo.
# 3. Separar en palabras.
# 4. Contar número total de palabras.
# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

import re
from collections import Counter

archivo = input("Introduce la ruta del archivo de texto: ")

try:

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        palabras = re.findall(r'\w+', contenido.lower())
        total_palabras = len(palabras)
        print(f"El archivo contiene {total_palabras} palabras.")
        print(f"Las 10 palabras más frecuentes son:")
        for palabra, conteo in Counter(palabras).most_common(10):
            print(f"{palabra}: {conteo}")
except FileNotFoundError:

    print("El archivo especificado no existe.")

    exit(1)