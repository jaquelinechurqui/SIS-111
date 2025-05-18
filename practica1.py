#Suma d enumeros pares


nombre = input ( " Ingresa tu nombre:")
print(f"Bienvenido {nombre} este es un porgrama d esuma de numeros pares:")
def sum_num(num):
    suma=0
    for i in  range(1, num + 1):
        if i % 2 == 0:
            suma += i
    return suma
        
#Llamar a la funcion

num = int(input("Ingrese un numero entero:"))

sum_pares = sum_num(num)
print (" La suma de los numeros pares son :", sum_pares)


