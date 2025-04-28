def nombre_funcion2():
    print("salida de funcion 1")

def nombre_funcion2():
    print("salida de funcion 2")

def funcion_retorno():
    variable = 456
    return 123


#Salida consola
var_salida= funcion_retorno()
print(var_salida)


def obtener_edad ():
    edad = int(input)("Indique su edad")
    if(edad > 0):
        return edad
    else:
        return 0
    
def habilitado_brevet(hedad):
    if(hedad == 0): return "SOLOS POSITIVOS"

    if(hedad >=18):
        return "Verdadero :)"
    else:
        return "Falso :("

def  calcular_descuento_producto():
    precio_original = 100
    descuento = 20
    precio_descuento = (precio_original * descuento) / 100
    precio_final = precio_original - precio_descuento
    return precio_final

def  calcular_descuento_producto_mejorado(precio_original, descuento):
    precio_descuento = (precio_original * descuento) / 100
    precio_final = precio_original - precio_descuento
    return precio_final

def  calcular_descuento_producto_mejorado_x2(precio_original, descuento):
    return precio_original - (precio_original * descuento)/100

def  calcular_descuento_producto_mejorado_x3(precio_original, descuento):
    return precio_original * (1-descuento/100)

#Salida de la consola 
#var_precio_f = calcular_descuento_producto()
#print(var_precio_f)

precio_original = int(input("INGRESE EL PRECIO DEL PRODUCTO:"))
descuento = int(input("INGRESE EL % DE DESCUENTO DEL PRODUCTO:"))
var_precio_ff = calcular_descuento_producto_mejorado_x3(precio_original,descuento)
print(var_precio_ff)

#1. Edad minima para votar
def minima_votar():
    print("La edad minima es 18 años")

#2. Numero mayor entre dos numeros
def mayor_dos_num(numA, numB):
    if(numA == numB): return "IGUALES"

    if(numA > numB):
        return numA
    else:
        return numB
    
def mayor_dos_num_mejorado(numA, numB):
    if(numA == numB): return "IGUALES"

    return numA if ( numA > numB) else numB

#Algortimo base
def recorrer_digitos(num):
    while(num > 0 ):
        dig = num % 10
        print (dig)
        num = num // 10

#Par / Impar de los digitos de un num
def par_impar_dig(num):
    while(num > 0):
         dig = num % 10
         print (dig)

         var_temp = "PAR" if(dig % 2 == 0 ) else "IMPAR"
         print(var_temp)

         num = num // 10
         return suma

#Salida de la consola




#Salida consola
#var_numA = int(input("INGRESE EL NUM A: "))
#var_numB = int(input("INGRESE EL NUM B: "))