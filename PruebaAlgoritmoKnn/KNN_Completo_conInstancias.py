def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

###CARGAR INSTANCIA DE ENTRENAMIENTO
#ENTRENAMIENTO
archivo = open("../Archivos/KNN_DCI_entrenamiento.csv")
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

print("Total de datos de la Instancia",len(instancia))

print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")


##############################################################################
###CARGAR INSTANCIA DE PRUEBA
archivo = open("../Archivos/KNN_DCI_prueba.csv")
#print(archivo)
contenido = archivo.readlines()
del contenido[0] #elimina la primera fila (linea)

prueba = []
for linea in contenido:
    linea = linea.replace("\n","") # quita el salto de linea al final
    #print(linea)
    linea_tokens = linea.split(",") #separar la cadena por un caracter indicado
    #print(linea_tokens)
    # convierte a la linea en una lista con cuatro posiciones:
    # indice, nombre, vector de caracteristicas, distancia
    lista = [int(linea_tokens[0]), linea_tokens[1], list(map(float,linea_tokens[2:8])), linea_tokens[8], 0.0]
    #print(lista)
    prueba.append(lista) #agregar la lista nueva a la instancia

print("Total de datos de la Instancia",len(prueba))

print("\nInstancia de prueba:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in prueba:
    print(l)
print("\n")

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
K = 10
##############################################################################

contAciertos = 0 #contador de aciertos obtenidos en la clasificación 

for registroNC in prueba: #para recorrer a todos los registros de prueba y aplicar al algoritmo K-NN
    print("\nClasificación del registro: ")
    print(registroNC) #registor de prueba procesado para su clasificacion

    NC = registroNC[2] #vector de caracteristicas del registro actual de prueba

    estructuraDatos = {} #inicializacion de la estructura de datos

    for NoCaso, registro in enumerate(instancia):
        distancia_NC_registro = Euclidiana(NC, registro[2])
        #print(distancia_NC_i)
        estructuraDatos[NoCaso] = distancia_NC_registro

    #print(estructuraDatos)  # La distancia de los registros con el registroNC

    ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1]) #ordena los registros
    #de menor a mayor de acuerdo con la distancia con el registroNC
    #print(ordenado)

    temporalK = []
    for i in range(K):
        NoCaso = ordenado[i][0]
        #print(etiqueta)
        registro = instancia[NoCaso]
        #print(registro)
        temporalK.append(registro[3]) #obtencion de la etiqueta

    print("Clases de los vectores más cercanos al registro NC:")
    print(temporalK)  #los primeros K vectores

    from statistics import multimode  #<<<- realizado unicamente para fines academicos, no se recomienda poner la importacion aqui 
    moda = multimode(temporalK)    
    respKnn = moda[0]  # si existe más de una moda se queda con la primera de ellas  

    print("Clase asignada por el KNN: "  + str(respKnn))
    print("Clase Real: " + registroNC[3])

    if str(respKnn) == registroNC[3]:
        contAciertos += 1

print("\n\nTotal de aciertos: " + str(contAciertos))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(contAciertos/len(prueba)*100))

#Proyecto:
#Realizar la aplicación de KNN para el calculo del rendimiento de la técnica utilizando la instancia asignada
#   Consideraciones:
#           *Reportar que valor de K es el mejor y que rendimiento genera
#           *PROBAR OTRAS METRICAS DE SIMILITUD

