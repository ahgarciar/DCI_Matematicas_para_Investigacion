resultados_pedro = [100, 20, 80, 70, 96, 90]
resultados_javier = [100, 80, 100, 100, 91, 95]
resultado_maria = [90, 95, 75, 15, 85, 90]

##
#LAS PRUEBAS POSTHOC TIENEN UTILIDAD SOLO CUANDO EXISTE UNA DIFERENCIA
#ESTADISTICA ENTRE LOS GRUPOS Y SE DESEA CONCOER AL GRUPO O GRUPOS
#QUE SON DIFERENTES
############################################################
import numpy as np
data = np.array([resultados_pedro, resultados_javier, resultado_maria])
############################################################

from scikit_posthocs import posthoc_conover_friedman
res = posthoc_conover_friedman(data.T)
print(res)
