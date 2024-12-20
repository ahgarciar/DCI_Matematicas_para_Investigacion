import numpy as np
import pandas as pd
from scipy import stats

datos = np.array([
    [100, 100, 90],
    [20, 80, 95],
    [80, 100, 75],
    [70, 100, 15],
    [96, 91, 85],
    [90, 95, 90]
])

df = pd.DataFrame(datos, columns=["Pedro", "Javier", "Maria"])

ranking = df.apply(stats.rankdata, axis=1)
print("Columnas Rankeadas:")
print(ranking)
ranking_promedio = ranking.mean()
print("Ranking Promedio:")
print(ranking_promedio)


#Friedman Test
res = stats.friedmanchisquare(*[df[columna] for columna in df])
#Ho = hipotesis nula...
# EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#Ha = hipostesis alternativa
# NO EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#EVALUACION DE LA PRUEBA....Si pvalue < 0.05 se rechaza Ho y se acepta Ha
# SI pvalue >= 0.05 se acepta Ho y se rechaza Ha
print(res)
