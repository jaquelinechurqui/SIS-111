#Devolcuion de listas
def num_pares(lista):
    pares = []
    for numero in lista :
        if numero % 2 == 0:
            pares.append(numero)
    return ( pares )
numeros = [ 2, 3, 4, 5, 6, 7]
resultado = num_pares(numeros)
#print(f"los numeros pares son {resultado}")


#Operadores aritmeticos
#nombre= input("ingresa tu nombre:")
#print(f"Bienvenido/a {nombre} este es un programa de operadores aritmeticos:")
def devol_num (num_1, num_2):
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 // num_2
    return suma, resta, multiplicacion, division

#llamar a la fiuncion
#num_1 = int(input("Ingrese un numero entero:"))
#num_2 = int(input("Ingrese un numero entero:"))

#s, r, m, d = devol_num(num_1, num_2) 

#print("el resultado se la suma es:", s)
#print("el resultado se la resta es:", r)
#print("el resultado se la multipicacion es:", m)
#print("el resultado se la division es:", d)



#Calculos
nombre = input("Ingrese su nombre:")
print(f"Bienvenido {nombre}, este es un programa de calculos:")


def calcular(num_1, num_2):
    suma = 2*(num_1 + num_2)
    resta = num_1 - num_2
    potencia = num_1 ** num_2
    return suma, resta, potencia

#llamar a la funcion
num_1 = int(input("Ingrese un numero entero:"))
num_2 = int(input("Ingrese un numero entero:"))

sumi, rest, pot = calcular(num_1, num_2)

print("El resultado se la suma es:", sumi)
print("El resultado se la suma es:", rest)
print("El resultado se la suma es:", pot)