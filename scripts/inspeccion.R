# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

install.packages("tidyverse")
library(tidyverse)

#1
ventas <- read_csv("data/ventas.csv")

#2
str(ventas)

#3
ventas <- ventas|>mutate(ticket = ventas/clientes)

#4
cat("Sucursal con mayor ventas:", ventas$sucursal[which.max(ventas$ventas)])
cat("Sucursal con menor ventas:", ventas$sucursal[which.min(ventas$ventas)])

ventas_per_region <- ventas |> group_by(region) |> summarize(ventas = sum(ventas))
print(ventas_per_region)

region_max <- ventas_per_region$region[which.max(ventas_per_region$ventas)]
total_max <- max(ventas_per_region$ventas)
cat("Region con mayor numero de ventas:", region_max)
cat("Con un total de:", total_max)