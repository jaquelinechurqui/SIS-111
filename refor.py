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