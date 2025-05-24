#CONTROL DE TEMPERATURA
def control_temperatura():
    #pedir al usuario 7 temperaturas
    temperaturas = []
    for i in range(1,8):
        temp= float(input(f"Ingrese la temperatura del dia{i}:"))
        temperaturas.append(temp)

    promedio = sum(temperaturas)/ len(temperaturas)
    print("El promedio total de sus temperaturas es:", promedio)

    dias_mayores = 0
    for temp in temperaturas:
        if temp > promedio:
            dias_mayores += 1
    print ("El numero de dias con temperatura mayor al poremdio son:",dias_mayores)

    temp_min = min(temperaturas)
    dia_min = temperaturas.index(temp_min) + 1
    print(f"El dia con la temperatura mas baja fue{dia_min}:")

#llamar a la funcion
control_temperatura()


#PROMEDIO DE NOTAS
def prom_notas():
    promedios = []
    for i in range (1,8):
        prom = int(input(f"Ingrese su promedio{i}:"))   
        promedios.append(prom)

    #Calculo promedio general
    promedio_total = sum(promedios)//len(promedios)
    print("Su promedio final es:", promedio_total)

    #Calculo de proemdio
    estudiantes = 0
    for aprob in promedios:
        if aprob >= 60:
            estudiantes +=1
    print (f"Los estudinates aprobados son {estudiantes}")


    #PROMEDIO MAS BAJO
    nota_baja = min(promedios)
    nota_menor = promedios.index(nota_baja) + 1 
    print(f"El estudiante que obtuvo la menor nota se encuentra en el numero: {nota_menor}")

#Llamar a la funcion
prom_notas()

#CAJERO AUTOMATICO
pin_correcto = 1234
saldo =5000  # saldo disponible

#Inicio del programa
pin = int(input("Ingrese su pin:"))

if pin == pin_correcto:
    print("Bienvenido, que desea hacer:")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("3. Salir")

    opcion = input("Seleccione una opcion:")

    if opcion == "1":
        print ( " Su saldo actual es", saldo)

    elif opcion == "2":
        retiro = int(input("ingrese el monto a retirar:"))
        if retiro <= saldo:
            saldo_disponible = saldo - retiro
            print("Retiro exitoso, su saldo actual es:", saldo_disponible)
        else:
            print("saldo insuficiente")

    elif opcion == "3":
            depositar = int(input("Ingrese su el monto a depositar"))
            saldo_actual = depositar + saldo
            print(f"Su saldo actual es{saldo_actual}")
    elif opcion == "4":
        print ("Querido cliente gracias por usar el cajero, hasta pronto")
    else :
         print("opcion invalida")
else:
    print("Pin incorrecto")


#Analisis de Digitos de un Numero
can_digit = 0
suma = 0 
mayor = 0
pares = 0
digito = input("Ingrese un numero entero positivo:")
for digitos in digito:
    digit = int(digitos)
    can_digit +=1
    suma += digit

    if digit % 2 == 0:
        pares +=1

    if digit > mayor:
        mayor = digit
print (f"la cantidad de digitos  son: {can_digit}")
print (f"La suma de sus digitos son: { suma}")
print (f"los digitos pares son:{pares}")
print(f"el digito mayor es: {mayor}")

#Contador de Vocales y Consonantes
vocales = 0
consonantes = 0 
palabra = input ("Ingrese una frase:")
for frase in palabra :
    frase = frase.lower()
    if frase.isalpha():
        if frase in "aeiou":
            vocales +=1
        else:
            consonantes += 1
print(f"La frase tiene: {vocales}vocales")
print(f"La frase tiene: {consonantes}consonantes")

#Ordenamiento de Notas
notas = []
for i in range (1,6):
    nota = float(input(f"Ingrese la nota del estudiante{i}:"))
    notas.append(nota)

notas.sort()
print("Notas ordenadas de menor a mayor:")
for nota in notas:
    print(nota)

prom = sum(notas)/ len(notas)
print(f"El promedio de sus calificaciones es: {prom}")


#Numero  ́Magico por Mitades
numero = input("Ingrese un numero de al menos dos cifras:")

largo = len(numero)
mitad = largo //2

if largo % 2 == 0 :
    izquierda = numero[:mitad]
    derecha = numero[mitad:]
else:
    izquierda = numero [:mitad]
    derecha = numero [mitad + 1:]

suma_derecha = 0
suma_izquierda = 0

for deren in derecha:
    suma_derecha += int(deren)

for izqui in izquierda:
    suma_izquierda += int(izqui)

print(f"La suma del lado derecho es: {suma_derecha}")
print(f"La suma del lado izquierdo es: {suma_izquierda}")
if suma_derecha == suma_izquierda:
    print("Si es un numero magico")
else:
    print("No es un numero magico")

