import math as m


def Euclidiana(X, Y): # tanto X como Y tienen la misma cantidad de elementos
    distancia = 0
    for i in range(len(X)): #sumatoria
        distancia += m.pow(X[i] - Y[i], 2)  # eleva la diferencia al cuadrado
    distancia = m.sqrt(distancia)
    return distancia

def Manhattan(X, Y):
    distancia = 0
    ####.....>>>><<<<<
    return  distancia
