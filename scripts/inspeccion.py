# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"]/ventas["clientes"]

print(ventas.head())

#print(ventas["ventas"].max())
print("Sucursal con mayor ventas:", ventas.loc[ventas["ventas"].idxmax(), "sucursal"])

print("Sucursal con menor ventas:", ventas.loc[ventas["ventas"].idxmin(), "sucursal"])

#Están agrupadas todas las ventas por región y la suma de todas las ventas
ventas_per_region = ventas.groupby("region").sum("ventas")

print(ventas_per_region)

#Quiero obtener la región con la mayor cantidad de ventas
print("Region con mayor numero de ventas:", ventas_per_region["ventas"].idxmax())
print("Con un total de:", ventas_per_region.loc[ventas_per_region["ventas"].idxmax(), "ventas"])