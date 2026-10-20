# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Recibí tres archivos, cada uno en un formato diferente; ERP de sucursales, plataforma de fidelización y finanzas. Comprobé que, efectivamente, la información, independientemente del sistema, es la misma. Lo ideal sería tratar de utilizar un solo formato, preferiblemente CSV gracias a su robustez y facilidad para trabajar.

## 1. ¿Los tres formatos contienen la misma información?

Independientemente del tipo de archivo en el que están almacenados los datos no existe ninguna alteración de su contenido.

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | ventas = pd.read_csv("data/ventas.csv") |
| JSON | API de fidelización | 5 | 4| with open("data/ventas.json", encoding = "utf-8") as f: datos = json.load(f) |
| Excel | Consolidado de finanzas | 5 | 4 | ventas = pd.read_excel("data/ventas.xlsx", sheet_name="ventas") |


## 2. Tipos de datos y calidad

Observando detenidamente los datos, cada variable llegó con el tipo esperado que nos permite trabajar sobre dicha columna sin ningún problema.

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | int(64) | numeric | Número entero; cantidad de ventas |
| `clientes` | int(64) | numeric | Número entero; cantidad de clientes |
| `sucursal` | 	object | character | Texto: nombre de la sucursal |
| `region` | 	object | character | Texo: región de la sucursal |

En el dado caso de, por ejemplo, si la variable "ventas" hubiera llegado como texto, representaría un problema enorme. Esto podría indicar inconsistencias representadas por caracteres no numéricos.

## 3. Particularidades técnicas encontradas

Al formato JSON no lo pude trabajar simplemente como llegó. Es importante recordar que este formato tiene múltiples niveles, por lo que es necesario "aplanarlo" para trabajarlo sin ningún problema como dataframe. Por otro lado, XLSX es bastante más simple, únicamente tuve que indicarle que hoja es la que se va a transformar a dataframe mediante el parámetro "sheet_name". Y, finalmente, CSV es el predilecto. No es necesario aplicarle ninguna correción o consideración.

Hablando un poco sobre las variables, python toma a las variables de tipo categóricas como objetc. En este caso, sucursal y región pertenecen a este tipo. En R, por otro lado, dejan de llamarse object para ser conocidas como character.


## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | Quito Norte: 12450; Quito Sur: 9870; Guayaquil Centro: 15200; Guayaquil Norte: 13980; Cuenca: 8540 |
| Ticket promedio (ventas ÷ clientes) | 38.07 |
| Sucursal con mayor venta | Guayaquil Centro: 15200 |
| Sucursal con menor venta | Cuenca: 8540 |
| Región con mayor venta total | Sierra: 30860 |

## 5. Conclusiones y recomendación

1. Para terminar, es apropiado decir que los tres sistemas de la empresa proveen los mismos datos. Independientemente del formato en el que estos se encuentran, de forma que, únicamente el formato es distinto, no el contenido.
2. Por último, es posible indicar que, antes de realizar un análisis a profundidad, primero es necesario identificar el tipo de dato de cada columna. Esto para comprobar que no existe ninguna discrepancia en los datos que impida continuar con el análisis.
3. Finalmente, las métricas resultantes de la empresa son: Sierra como región con mayor número de ventas totales con 30.860, seguido de Guayaquil Centro con 15.200 y Cuenca como la sucursal con el menor número de ventas siendo este 8540.

Dado que el formato más cómodo y menos complejo de cargar para empezar a realizar el análisis es el CSV. Se recomienda que este sea el predilecto para realizar próximos análisis de datos.