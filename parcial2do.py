#Analisis de datos 
nombre = input("Ingrese su nombre:")
print(f"Bienvenido {nombre}, este es un programa de analisis de datos:")

numero_ingresado = input("Ingrese un numero entero positivo:")
dig = [int(c)for c in numero_ingresado]
    
suma = 0
pares =0
mayor_numero = dig[0]
cantidad_digitos = len(dig)
for valor in dig:
    suma+= valor

    if valor % 2 == 0:
        pares += 1
   
    if valor > mayor_numero :
        mayor_numero = valor



print (f"la cantidad de sus digitos son {cantidad_digitos}")
print (f"la suma de sus digitos son {suma}")
print (f"los numeros pares son{pares}")
print(f"El numero mayor es{mayor_numero}")

 


    



