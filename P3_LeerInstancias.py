
import pandas as pd


def run(instance_name):
    file = pd.read_csv(instance_name)  # dataframe
    return file


instance = "Archivos/iris_completa.csv"
contend_file = run(instance)
print(contend_file.head(10)) # imprime en pantalla las primeras 10 filas de la instancia
#Nota. Los indices empiezan en 0


