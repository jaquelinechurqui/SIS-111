#Suma Alternada de Dıgitos
numero = input("Ingrese un numero")

suma = 0
expresion = ""

for i in range(len(numero)):
    digito = int(numero[i])
    if i == 0:
        suma +=digito
        expresion += str(digito)
    elif i % 2 == 0:
        suma += digito
        expresion +=  "+" + str(digito)
    else:
        suma -= digito
        expresion +=  "-" + str(digito)

print(expresion + "=" + str(suma))

#Suma de Dıgitos en Posiciones Pares e Impares
numero = input("Ingrese un numero entero positivo: ")

suma_pares = 0
suma_impares = 0
expresiones_pares = " "
expresiones_impares = " "
for i in range(len(numero)) :
    digito = int(numero[i])

    if i == 0:
        suma_impares += digito
        expresiones_impares += str(digito)

    elif i == 1:
        suma_pares += digito
        expresiones_pares += str(digito)

    elif i % 2 == 0:
        suma_impares += digito
        expresiones_impares += "+"  + str(digito)
    else:
        suma_pares += digito
        expresiones_pares += "+" + str(digito)

print( expresiones_impares + "=" +  str(suma_impares))
print( expresiones_pares + "=" + str( suma_pares))

if suma_pares > suma_impares:
    print(  "La suma de los pares es mayor: " , suma_pares)

elif suma_impares > suma_pares:
    print(  "La suma de los impares es mayor: " , suma_impares)
else:
    print( " Tanto la suma de los pares, como de los impares son iguales")



#Ultimo ejercicio:

numero = input("Bienvenido, ingrese un numero entero positivo:")
#Cantidad de digitos
cant_total = len(numero)
print("La cantidad total de digitos son:", cant_total)

#suma de digitos
suma = 0 
for sumi in numero:
    digit = int(sumi)
    suma += digit
print("La suma de sus digitos es", suma)

#Suma alternada de digitos
suma_total = 0
expresion = " "
for i in range(len(numero)):
    dig = int(numero[i])
    if i == 0:
        suma += dig
        expresion += str(dig) 
    elif i % 2 == 0:
        suma += dig
        expresion += " + " +str(dig) 
    else:
        suma -= dig
        expresion += " - " +str(dig)  

print( expresion + " = "  + str(suma))
#suma impares y pares

suma_pares = 0
suma_impares = 0
expresiones_pares = " "
expresiones_impares = " "
for i in range(len(numero)) :
    digito = int(numero[i])

    if i == 0:
        suma_impares += digito
        expresiones_impares += str(digito)

    elif i == 1:
        suma_pares += digito
        expresiones_pares += str(digito)

    elif i % 2 == 0:
        suma_impares += digito
        expresiones_impares += "+"  + str(digito)
    else:
        suma_pares += digito
        expresiones_pares += "+" + str(digito)

print( "La suma de los impares es:", expresiones_impares + "=" +  str(suma_impares))
print( "La suma de los pares es:", expresiones_pares + "=" + str( suma_pares))

if suma_pares > suma_impares:
    print(  "La suma de los pares es mayor: " , suma_pares)
        
elif suma_impares > suma_pares:
    print(  "La suma de los impares es mayor: " , suma_impares)
else:
    print( " Tanto la suma de los pares, como de los impares son iguales")
