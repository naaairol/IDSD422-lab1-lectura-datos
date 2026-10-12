import pandas as pd

#CSV a dataframe
ventas = pd.read_csv("data/ventas.csv")

#Resumen del dataframe
print(ventas.head())

#Imprimir las dimensiones
print("\nDimensiones:", ventas.shape)

#Tipos de cada columna
print("\nTipos de columna")
print(ventas.dtypes)