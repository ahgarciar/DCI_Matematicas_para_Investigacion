import numpy as np
import matplotlib.pyplot as plt
from SuavizamientoExponencial import MetricasDeError as metricas


def calc_suavizado_exponencial(serie, alfa):
    # El parámetro alfa controla el peso que se le da a los datos
    # valores cercanos a 1 hacen que los datos recientes tengan más influencia
    # valores cercanos a 0 dan más importancia a los datos antiguos

    new_serie = np.zeros_like(serie) # reserva memoria y rellena con ceros
    new_serie[0] = serie[0]  # El primer valor suavizado es el primer valor de la serie real
    for t in range(1, len(serie)): #calcula los nuevos valores para la serie suavizada
        new_serie[t] = alfa * serie[t] + (1 - alfa) * new_serie[t-1]
    return new_serie


# Serie de tiempo a suavizar
datos = np.array([100, 132, 105, 133, 141, 137, 156, 136, 157, 124, 132, 142])  # Corresponde a los valores reales

# Auxiliares para almacenar los resultados del analisis de sensibilidad
mae_list = []
mse_list = []
rmse_list = []
mape_list = []

########### ANALISIS DE SENSIBILIDAD DEL PARAMETRO ALFA
alfas = np.linspace(0.01, 0.99, 100)

for alfa_actual in alfas:
    serie_suavizada = calc_suavizado_exponencial(datos, alfa_actual)
    mae_list.append(metricas.calcMAE(datos, serie_suavizada))
    mse_list.append(metricas.calcMSE(datos, serie_suavizada))
    rmse_list.append(metricas.calcRMSE(datos, serie_suavizada))
    mape_list.append(metricas.calcMAPE(datos, serie_suavizada))

############ RESULTADOS DEL ANALISIS DE SENSIBILIDAD
plt.figure(figsize=(12, 6))
plt.plot(alfas, mae_list, label='MAE', color='blue')
#plt.plot(alphas, mse_list, label='MSE', color='brown')
plt.plot(alfas, rmse_list, label='RMSE', color='green')
plt.plot(alfas, mape_list, label='MAPE', color='red')
plt.title('Análisis de sesibilidad del parametro "ALFA"')
plt.xlabel('Alfa')
plt.ylabel('Error')
plt.legend()
plt.grid(True)
plt.show()
