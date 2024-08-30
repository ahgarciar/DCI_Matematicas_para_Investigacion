## Informacion adicional en: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

"""
The standard score of a sample x is calculated as:

z = (x - u) / s

where:
 u is the mean of the training samples or zero if with_mean=False,
 s is the standard deviation of the training samples or one if with_std=False.

"""


import pandas as pd
import P3_LeerInstancias as load_instance
from sklearn.preprocessing import StandardScaler

instance = "Archivos/iris_completa.csv"
contend_file = load_instance.run(instance)
print(contend_file.head(10)) # imprime en pantalla las primeras 10 filas de la instancia
#Nota. Los indices empiezan en 0

scalers = dict()

new_instance = pd.DataFrame([])
for index in range(len(contend_file.columns)-1): # no se normaliza la ultima instancia porque es nominal
    column = contend_file.columns[index]
    scaler = StandardScaler()
    new_instance[column] = pd.DataFrame(scaler.fit_transform(contend_file[[column]]), columns=[column])
    scalers.update({column: scaler})


print("Primeros datos de la instancia Estandarizada:")
print(new_instance.head(5))
print()

print("Datos de los escaladores:")
for name, scaler in scalers.items():
    #print(type(scaler))
    print("Scaler of: ", name)
    mean = scaler.mean_
    variance = scaler.var_
    print("Mean:", mean)
    print("Variance:", variance)
    print()
