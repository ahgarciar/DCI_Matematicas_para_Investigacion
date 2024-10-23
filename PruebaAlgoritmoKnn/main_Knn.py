
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
    # convierte a la linea en una lista con tres posiciones:
    # indice, nombre y vector de caracteristicas
    lista = [int(linea_tokens[0]), linea_tokens[1], list(map(float,linea_tokens[2:8]))]
    #print(lista)
    instancia.append(lista) #agregar la lista nueva a la instancia


vectorReferencia = instancia[0]
print("Vector Referencia: ", vectorReferencia)
import MetricasSimilitud as metrica
for fila in instancia:
    print(fila, end= " Distancia: ")
    distancia = metrica.Euclidiana(vectorReferencia[2], fila[2])
    print(distancia)
