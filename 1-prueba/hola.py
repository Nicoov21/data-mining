import os 
import pandas as pd
import numpy as np

csv_path = "../1-prueba/mineria_estudiantes_prob_estadistica_2025.csv"
assert os.path.exists(csv_path), f"No se encontró el archivo, verifique la ruta: {csv_path}"

df = pd.read_csv(csv_path, parse_dates=['fecha_inscripcion'])

#print("Shape: ", df.shape) #* (filas y columnas -> dimensiones)

#print(df.head()) #* Primeras 5 filas sin argumentos, si no las n filas que se argumenten -1, ya que empieza a contar desde el 0

#print("Tipos de datos: \n",df.dtypes) #* Tipos de datos en cada columna

# print("Registros faltantes de los atributos:")
# print(df.isna().sum().sort_values(ascending=False)) #* Valores faltantes por columna
#! isna() -> indica valores nulos/faltantes o valores validos
#! sum() -> suma los valores True(1) por colummna.
#! sort_values(ascending=False) -> ordena de mayor a menor según el número de nulos

#valoresFaltantes = df.isna().mean().mul(100).round(2).sort_values(ascending=False) #* Porcentaje de valores nulos por columna
#! mean() -> calcula la media o promedio por columna
#! mul(n) -> multiplica por n para convertilo a porcentaje
#! round -> redondea a 2 decimales
#print(valoresFaltantes)

nomColumns = df.select_dtypes(include=[np.number]).columns.tolist() #* Selecciona las columnas que contienen datos numéricos
#! select_dtypes(include=[np.number]) -> selecciona las columnas que incluyan datos numéricos o el que se especifique
#! columns -> Obtiene los nombres de las colummnas como un Index
#! tolist() -> Convierte ese index en una lista de Python
#print(nomColumns)

catColum = df.select_dtypes(exclude=[np.number]).columns.tolist() #* Selecciona las columnas que no contienen datos numéricos
#! exclude -> excluye las columnas que contengan datos numéricos
#print(catColum)

#descNums = df[nomColumns].describe().T #* Describe estadísticamente las columnas que contiene datos numéricos 
#! describe() -> genera estadísticas descriptivas (count, mean, std, min, 25%, 50%, 75%, max)
#! T -> Transpone la tabla cambiando filas por columnas
#print(descNums)

moda = {c: (df[c].mode(dropna=True).iloc[0] if not df[c].mode(dropna=True).empty else None) for c in catColum}
#! mode(dropna=True) -> calucla la moda (valor más frecuente) de la columna, ignorando los valores nulos
#! iloc[0] -> toma el primer valor, si es que hay moda
#! Si es que no hay moda, devuelve None 
#! c -> variable temporal que represanta cada columna en catColum
print(moda)