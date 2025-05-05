#Palindromo
def es_palindromo_con_return (num):
    #Validar que un plaindromo solo acepta numeros positivos
    if num < 0 : return False

    num_original = num
    num_invertido = 0

    #Recorrer todos los digitos del numero
    while num > 0:
        dig = num % 10
        num_invertido =  num_invertido * 10 + dig
        num = num // 10
    

    return num_original == num_invertido

#Llamar a la funcion es_palindromo(num):
#var_num = int(input("Ingrese un numero:"))
#var_palindromo = es_palindromo_con_return(var_num)
#if var_palindromo:
    print("Es palindromo")
#else:
    print("No es palindromo")




#Palindromo
def es_palindromo_sin_return (num):
    #Validar que un plaindromo solo acepta numeros positivos
    if num < 0 : print("No se aceptan numeros negativos")

    num_original = num
    num_invertido = 0

    #Recorrer todos los digitos del numero
    while num > 0:
        dig = num % 10
        num_invertido =  num_invertido * 10 + dig
        num = num // 10
    

    if num_original== num_invertido:
        print("Es palindromo")
    else:
        print("no es palindromo")

#Llamar a la funcion es_palindromo(num):
#var_num = int(input("Ingrese un numero:"))
#var_palindromo = es_palindromo_sin_return(var_num)
#es_palindromo_sin_return(var_num)



#EXERCISE 7
#Largest Product Betwwen Two Numbers
#Input: 2, 3, 5, 7
def LargestProductBetwweenTwoNumbers(num1, num2, num3, num4):
    res1 = num1 *num2
    res2 = num1 *num3
    res3 = num1 *num4

    res4 = num2 *num1
    res5= num2 *num3
    res6 = num2 *num4

    res7 = num3 *num1
    res8 = num3 *num2
    res9 = num3 *num4

    res10 = num4 *num1
    res11= num4 *num2
    res12= num4 *num3





    producto_mayor = 0
    if(res1 > res2):
        producto_mayor = res1
    else:
         producto_mayor = res2
    #----
    if res3 > producto_mayor : producto_mayor = res3
    #----
    if res4 > producto_mayor : producto_mayor = res4
    #----
    if res5 > producto_mayor : producto_mayor = res5
    #----
    if res6 > producto_mayor : producto_mayor = res6
    #----
    if res7 > producto_mayor : producto_mayor = res7
    #----
    if res8 > producto_mayor : producto_mayor = res8
    #----
    if res9 > producto_mayor : producto_mayor = res9
    #----
    if res10 > producto_mayor : producto_mayor = res10
    #----
    if res11 > producto_mayor : producto_mayor = res11
    #----
    if res12 > producto_mayor : producto_mayor = res12

    print("Largest product:", producto_mayor)

#Llamar a la funcion LargestProductBewtweenTwoNUmbers
#LargestProductBetwweenTwoNumbers(2, 3, 5, 7)


def LargestProductBetwweenTwoNumbers_UsingFor(num1, num2, num3, num4):
    # Pedir los 4 numeros al usuario
    numeros = []
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    numeros.append(num4)

    #Inicializar el producto maximo
    producto_max = numewros[0] * nujmeros[1]

    #Comparar todos los pares posibles manualmente
    for i in range(4):
        for j in range (i + 1, 4):
            producto = numeros [i] * numeros [j]
            if producto > producto_max:
                producto_max = producto

    print(f"El producto mas grande ntre dos de los numeros es: {producto_max}")

LargestProductBetwweenTwoNumbers_UsingFor(2, 3, 5, 7)