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

alfas = np.linspace(0.01, 0.99, 100)
betas = np.linspace(0.01, 0.99, 100)

results = {}

for alfa in alfas:
    for beta in betas:
        smoothed_series = serie_suavizada = calc_suavizado_exponencial_doble(datos, alfa, beta)
        results[(alfa, beta)] = smoothed_series

errors = {}

from SuavizamientoExponencial import MetricasDeError as metricas

for (alpha, beta), smoothed_series in results.items():
    mse = metricas.calcMSE(datos, smoothed_series)
    errors[(alpha, beta)] = mse

# Ordenamos los errores de menor a mayor
sorted_errors = sorted(errors.items(), key=lambda x: x[1])

# Mostramos las mejores combinaciones de alpha y beta
for (alpha, beta), error in sorted_errors[:5]:
    print(f"alpha: {alpha}, beta: {beta}, MSE: {error}")