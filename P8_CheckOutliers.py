import pandas as pd
import numpy as np

#Dado un conjunto de calificaciones
data = {'calificaciones': [10, 9, 10, 8, 15, 7]}  # 15 es outlier
#data = {'calificaciones': [10.0, 9.0, 10.0, 8.0, 15.0, 7.0]}  # 15 es outlier
df = pd.DataFrame(data)

# Identificamos el outlier
df['calificaciones'] = df['calificaciones'].apply(lambda x: np.nan if x > 10 else x)

# Imputación por Interporlacion (Por defecto Lineal)
df['calificaciones'] = df['calificaciones'].interpolate() ## se debe tener cuidado en el momento en que se ejecute

print(df)