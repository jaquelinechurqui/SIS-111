



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
#llMARA  AL FUNCION
lista=[3,4,5,1,3]
objetivo=5

encontrado = busqueda_binaria(lista, objetivo)
print("Elnumero buscado esta en la posicion:",encontrado)