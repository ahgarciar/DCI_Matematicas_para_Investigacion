
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
    lista = [int(linea_tokens[0]), linea_tokens[1], list(map(float,linea_tokens[2:8])), 0.0]
    #print(lista)
    instancia.append(lista) #agregar la lista nueva a la instancia


vectorReferencia = instancia[0]
print("Vector Referencia: ", vectorReferencia)
import MetricasSimilitud as metrica
for i in range(len(instancia)):
    distancia = metrica.Euclidiana(vectorReferencia[2], instancia[i][2])
    instancia[i][3] = distancia
    #print(instancia[i])

for fila in instancia:
    print(fila)

#
print("\n\nORDENADA DE MENOR A MAYOR:")
instancia.sort(key= lambda x:x[3])
for fila in instancia:
    print(fila)


