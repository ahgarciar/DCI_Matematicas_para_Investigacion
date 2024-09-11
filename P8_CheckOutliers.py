import pandas as pd
import numpy as np

#Dado un conjunto de calificaciones
#data = {'calificacion': [10.0, 9.0, 10.0, 8.0, 15.0, 7.0]}  # 15 es outlier #OPCION 1

data = [{'calificacion': 10, 'id_unidad':1},
       {'calificacion': 9, 'id_unidad':3},
       {'calificacion': 10, 'id_unidad':4},
       {'calificacion': 8, 'id_unidad':2},
       {'calificacion': 15, 'id_unidad':5},
       {'calificacion': 7, 'id_unidad':6}
    ]  # 15 es outlier #OPCION 2

#data['calificaciones'].sort() #PARA OPCION 1
data = sorted(data, key=lambda item:item['id_unidad'])

df = pd.DataFrame(data)

##IMPRIME LA COLUMNA CON SUS DATOS ORIGINALE
print("COLUMNA ORIGINAL ORDENADA")
print(df)
print()

#QUITA LOS VALORES DE OUTLIERS AL SUSTITUIRLOS POR "NAN" = NOT A NUMBER
# Identificamos el outlier
df['calificacion'] = df['calificacion'].apply(lambda x: np.nan if x > 10 else x)

#LA COLUMNA SIN LOS VALORES QUE SON OUTLIERS
print("COLUMNA SIN OUTLIERS (DATOS CONVERTIDOS A NAN)")
print(df)
print()

# Imputación por Interporlacion (Por defecto Lineal)
df['calificacion'] = df['calificacion'].interpolate() ## se debe tener cuidado en el momento en que se ejecute

print("COLUMNA TRATADA PARA CONVERTIR OUTLIERS EN VALORES ACEPTABLES")
print(df)
print()

