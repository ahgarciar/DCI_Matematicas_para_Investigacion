def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

###CARGAR INSTANCIA
archivo = open("../Archivos/KNN_DCI.csv")
#print(archivo)
contenido = archivo.readlines()
del contenido[0] #elimina la primera fila (linea)

instancia = []
for linea in contenido:
    linea = linea.replace("\n","") # quita el salto de linea al final
    #print(linea)
    linea_tokens = linea.split(",") #separar la cadena por un caracter indicado
    #print(linea_tokens)
    # convierte a la linea en una lista con cuatro posiciones:
    # indice, nombre, vector de caracteristicas, distancia
    lista = [int(linea_tokens[0]), linea_tokens[1], list(map(float,linea_tokens[2:8])), linea_tokens[8], 0.0]
    #print(lista)
    instancia.append(lista) #agregar la lista nueva a la instancia

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print("Instancia Procesada: ")
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")
##############################################################################
##SELECCIÓN / CREACIÓN DEL VECTOR A CLASIFICAR - VECTOR DE REFERENCIA
NC = instancia[0] #NC = No Clasificado
print(NC)

del instancia[0] # quita el vector de referencia para no considerarlo en el resto del proceso

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia
K = 5  #por ejemplo, k = 5
##############################################################################

estructuraDatos = {} ##diccionario que fungira como estructura de datos para las distancias

for NoCaso, registro in enumerate(instancia):  #por cada elemento/registro de la instancia
    distancia_de_NC_a_registro = Euclidiana(NC[2], registro[2]) #El indice 2 es el vector carac   -- registro[3] = clase
    #print(distancia_NC_i)
    estructuraDatos[NoCaso] = distancia_de_NC_a_registro

#VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS)
print("TABLA DE DISTANCIAS: ")
#Impreso línea a línea
for key in estructuraDatos:
  print ("Registro ",key, " - Distancia con NC: ", estructuraDatos[key])
print("\n\n")

ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse=False) ## 0 = NoCaso   1 = Distancia  -->> #retorna una lista de tuplas

#VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS) ORDENADA
print("TABLA DE DISTANCIAS ORDENADA: ")
#Impreso línea a línea
for r in ordenado:
  print ("Registro ",r[0], " - Distancia con NC: ", r[1])
print("\n\n")


temporalK = []
for i in range(K):
    NumDeRegistro = ordenado[i][0] ##0 = NumDeCaso
    registro = instancia[NumDeRegistro] #registro correspondiente al indice (NumDeRegistro) consultado
    #print(registro)
    temporalK.append(registro[3]) ##clase/etiqueta asociada al "NumDeRegistro"

print("Clases de los K registros más parecidos(cercanos): ")
#Impreso línea a línea
for t in temporalK:
  print ("\t",t)
print("\n\n")

########################################################################
##ENCONTRAR LA MODA EN "TEMPORAL_K" PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

from statistics import mode #, multimode
claseModa = mode(temporalK)
#claseModa = multimode(temporalK)
print("Clase Asignada:", claseModa)
print("\n\n")

#
#Investigación para agregar a su documentación de LATEX en Overleaf. Tipos de Validación.
#
#   CrossValidation - Validación Cruzada
#   SplitValidation - Validación Segmentada  80%/20%  70%/30% 60%/40% => entrenamiento/prueba




