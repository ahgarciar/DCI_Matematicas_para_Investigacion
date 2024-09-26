#Datos obtenidos desde arduino sin procesamiento adicional..
resultados_pedro = [100, 20, 80, 70, 96, 90]
resultados_pedro = [100, 80, 100, 100, 91, 95]
resultado_maria = [90, 95, 75, 15, 85, 90]

print(resultados_pedro)
print(resultados_pedro)
print(resultado_maria)

#Friedman Test
from scipy import stats
res = stats.friedmanchisquare(resultados_pedro, resultados_pedro, resultado_maria)
#Ho = hipotesis nula...
# NO EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#Ha = hipostesis alternativa
# EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)

#EVALUACION DE LA PRUEBA....Si pvalue < 0.05 se rechaza Ho y se acepta Ha

#ES DECIR SI pvalue >= 0.05 se acepta Ho y se rechaza Ha

print(res)