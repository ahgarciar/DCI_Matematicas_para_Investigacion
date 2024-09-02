
import pandas as pd
import P3_LeerInstancias as load_instance

instance = "Archivos/iris_completa.csv"
contend_file = load_instance.run(instance)
print(contend_file.head(10)) # imprime en pantalla las primeras 10 filas de la instancia
#Nota. Los indices empiezan en 0

nombre_columnas = contend_file.columns[1]  # INDICE DE LA COLUMNA A GRAFICAR
column = contend_file[nombre_columnas]

from matplotlib import pyplot as plt
plt.boxplot(column)
plt.title(nombre_columnas)
plt.show()
