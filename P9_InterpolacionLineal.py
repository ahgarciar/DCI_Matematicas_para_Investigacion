import pandas as pd
import numpy as np

#outlier en -> índice 4
data = {'calificaciones': [10, 9, 10, 8, 15, 7]}  # 15 es outlier
df = pd.DataFrame(data)

x1 = 3  # índice antes del valor NaN
x2 = 5  # índice después del valor NaN
y1 = df.loc[x1, 'calificaciones']  # valor en el índice de x1
y2 = df.loc[x2, 'calificaciones']  # valor en el índice de x2

# Interpolacion
x = 4  # índice del outlier
y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

# Asignamos del valor interpolado
df.loc[x, 'calificaciones'] = y

print(df)

