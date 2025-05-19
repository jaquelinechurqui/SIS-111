 # Ejercicio 1 - Búsqueda Lineal
# Enunciado: Dada una lista desordenada, buscar si un número dado está en la lista usando búsqueda lineal.
# Si se encuentra, mostrar la posición. Si no, indicar que no está.

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

numeros = [8, 3, 5, 10, 2]
valor = 5

pos = busqueda_lineal(numeros, valor)
print("Encontrado en la posición:", pos if pos != -1 else "No está en la lista")






 # Ejercicio 2 - Búsqueda Lineal
# Enunciado: Dada una lista, contar cuántas veces aparece un número objetivo.

def contar_apariciones(lista, objetivo):
    return lista.count(objetivo)

datos = [2, 3, 4, 2, 5, 2, 6]
print("Aparece:", contar_apariciones(datos, 2), "veces")





 # Ejercicio 3 - Búsqueda Binaria
# Enunciado: Dada una lista ordenada, buscar si un número está en la lista usando búsqueda binaria.
# Si se encuentra, devolver su posición.

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

lista = [2, 4, 6, 8, 10, 12]
print("Posición:", busqueda_binaria(lista, 8))




 # Ejercicio 4 - Bubble Sort (Ordenamiento)
# Enunciado: Ordenar una lista de números de menor a mayor usando el algoritmo Bubble Sort.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 3, 8, 1, 2]
print("Ordenado:", bubble_sort(numeros.copy()))





 # Ejercicio 5 - Insertion Sort (Ordenamiento)
# Enunciado: Dada una lista de edades, ordenarlas de menor a mayor usando el algoritmo Insertion Sort.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

edades = [21, 19, 23, 20]
print("Ordenado:", insertion_sort(edades.copy()))




 # Ejercicio 6 - Selection Sort (Ordenamiento)
# Enunciado: Dada una lista de números, ordenarlos de menor a mayor usando Selection Sort.

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

valores = [30, 10, 20, 5]
print("Ordenado:", selection_sort(valores.copy()))



 # Ejercicio 7 - Comb Sort (Ordenamiento)
# Enunciado: Aplicar el algoritmo Comb Sort para ordenar una lista de números.

def comb_sort(lista):
    gap = len(lista)
    shrink = 1.3
    ordenado = False

    while not ordenado:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            ordenado = True
        i = 0
        while i + gap < len(lista):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                ordenado = False
            i += 1
    return lista

numeros = [9, 4, 1, 7, 3]
print("Ordenado:", comb_sort(numeros.copy()))



# Ejercicio 8 - Insertion Sort + Búsqueda Binaria
# Enunciado: Dada una lista desordenada, ordenarla con Insertion Sort y luego buscar un número con búsqueda binaria.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

lista = [10, 3, 5, 8, 2]
ordenada = insertion_sort(lista.copy())
print("Lista ordenada:", ordenada)
print("Posición del 8:", busqueda_binaria(ordenada, 8))