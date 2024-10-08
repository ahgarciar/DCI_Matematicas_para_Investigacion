
import pandas as pd
import P3_LeerInstancias as load_instance

instance = "Archivos/iris_completa.csv"
contend_file = load_instance.run(instance)
print(contend_file.head(10)) # imprime en pantalla las primeras 10 filas de la instancia
#Nota. Los indices empiezan en 0

nombre_columnas = contend_file.columns[1]  # INDICE DE LA COLUMNA A GRAFICAR
column = contend_file[nombre_columnas]

from matplotlib import pyplot as plt
# Graficar la columna
plt.figure(figsize=(10, 6))
plt.plot(column, marker='o')
plt.yticks(column)
plt.title(nombre_columnas)
plt.xlabel('Índice')
plt.ylabel('Valores de la Columna')
plt.grid(True)
plt.show()

