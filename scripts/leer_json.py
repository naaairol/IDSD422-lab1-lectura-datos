import json
import pandas as pd

#Abrir el json y convertirlo a una cadena
with open("data/ventas.json", encoding = "utf-8") as f:
  datos = json.load(f)

#Normalizamos
ventas = pd.json_normalize(datos)

#Resumen
print(ventas.head())

#Imprimir las dimensiones
print("\nDimensiones:", ventas.shape)

#Tipos de cada columna
print("\nTipos de columna")
print(ventas.dtypes)