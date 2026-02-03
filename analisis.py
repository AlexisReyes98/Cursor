# Escribe un script analisis.py que lea el CSV llamado "datos.csv"

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv")

# Calcula estadísticas simples: media, mediana, desviación estándar de cada columna usando pandas
print(df.describe())

# Traza un scatter plot de Nombre_Unidad vs MIPYMES usando matplotlib
plt.scatter(df["Nombre_Unidad"], df["MIPYMES"])
plt.show()
