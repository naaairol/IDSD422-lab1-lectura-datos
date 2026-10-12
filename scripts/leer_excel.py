import pandas as pd

ventas = pd.read_excel("data/ventas.xlsx", sheet_name="ventas")
print(ventas.head())
print(ventas.shape)
print(ventas.dtypes)