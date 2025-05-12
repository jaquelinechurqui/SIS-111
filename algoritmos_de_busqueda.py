precios =[400, 250, 310, 280]
menor = precios [0] #Suponer que el primer elemento es menor

for precio in precios:
    if precio < menor:
        menor = precio


#print(menor)


def precio_menor (precios):
    menor = precios [0] #Suponer que el primer elemento es menor

    for precio in precios:
        if precio < menor:
            menor = precio


    return menor

#Llamar a la funcion
precios = [400, 250, 310, 280]
print(precio_menor(precios))


#Busqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha)//2

        if lista[medio] == objetivo:
            return  medio
        
        elif  lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return - 1 #No encontrado






#--------BUSQUEDA BINARIA

datos = [12, 23, 34, 45, 67] #Importante ordenar antes!
buscado=  45

posicion = busqueda_binaria (datos, buscado)

if posicion != -1:
    print(f"Elemento encontrado en la posicion{posicion}")
else:
    print("Elementono encontrado")


#------BUSQUEDA LINEAL
def busqueda_lineal(lista, objetivo):
    for i in range (len(lista)):
        if lista[i]== objetivo:
            return i #Devuelve la posicion donde se encontro
    return -1 #Si no se enconuentra el elemento

#----------
datos = [23, 45, 12, 67,34]
buscado = 34

posicion = busqueda_lineal(datos, buscado)

if posicion != -1:
    print(f"elemento encontrado en la posicion:{posicion}")
else:
    print("elemento no encontrado")