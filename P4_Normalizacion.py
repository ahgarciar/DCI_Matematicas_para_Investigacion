## Informacion adicional en: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

"""
The transformation is given by:

X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_scaled = X_std * (max - min) + min

where min, max = feature_range.


feature_range -> tuple (min, max), default=(0, 1)
Desired range of transformed data.

"""


import pandas as pd
import P3_LeerInstancias as load_instance
from sklearn.preprocessing import MinMaxScaler

instance = "Archivos/iris_completa.csv"
contend_file = load_instance.run(instance)
print(contend_file.head(10)) # imprime en pantalla las primeras 10 filas de la instancia
#Nota. Los indices empiezan en 0

scalers = dict()

new_instance = pd.DataFrame([])
for index in range(len(contend_file.columns)-1): # no se normaliza la ultima instancia porque es nominal
    column = contend_file.columns[index]
    scaler = MinMaxScaler()
    new_instance[column] = pd.DataFrame(scaler.fit_transform(contend_file[[column]]), columns=[column])
    scalers.update({column: scaler})


print("Primeros datos de la instancia Normalizada:")
print(new_instance.head(5))
print()

print("Datos de los escaladores:")
for name, scaler in scalers.items():
    #print(type(scaler))
    print("Scaler of: ", name)
    min_value = scaler.data_min_
    max_value = scaler.data_max_
    print("Min Value:", min_value)
    print("Max Value:", max_value)
    print()
