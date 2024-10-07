# Suavizamiento Exponencial Doble - Método de Holt

import numpy as np
import matplotlib.pyplot as plt

def calc_suavizado_exponencial_doble(serie, alfa, beta):
    # El parámetro alfa controla el peso que se le da a los datos
    # valores cercanos a 1 hacen que los datos recientes tengan más influencia
    # valores cercanos a 0 dan más importancia a los datos antiguos

    # beta, por otro lado, controla el peso que se le da al cambio en el nivel (new_serie) para actualizar la tendencia.

    n = len(serie)
    new_serie = np.zeros(n)
    tendencia = np.zeros(n)

    # Inicializacion del nivel y la tendencia
    new_serie[0] = serie[0] # El primer valor suavizado es el primer valor de la serie real
    tendencia[0] = serie[1] - serie[0]  # La tendencia inicial es la diferencia entre los dos primeros puntos

    # Aplicar las fórmulas del suavizamiento exponencial doble
    for t in range(1, n):
        new_serie[t] = alfa * serie[t] + (1 - alfa) * (new_serie[t - 1] + tendencia[t - 1])
        tendencia[t] = beta * (new_serie[t] - new_serie[t - 1]) + (1 - beta) * tendencia[t - 1]

    return new_serie # Retornamos solo la serie suavizada


# Serie de tiempo a suavizar
datos = np.array([100, 132, 105, 133, 141, 137, 156, 136, 157, 124, 132, 142])  # Corresponde a los valores reales

alfa = 0.99
beta = 0.24
serie_suavizada = calc_suavizado_exponencial_doble(datos, alfa, beta)

x = [i for i in range(1, len(serie_suavizada)+1)]
plt.figure(figsize=(12, 6))
plt.plot(x, datos, label='REAL', color='blue')
plt.plot(x, serie_suavizada, label='SUAVIZADA', color='green')
plt.title('Comparación de Series')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
