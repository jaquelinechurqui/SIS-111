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
    for i in range (1,7):
        prom = int(input("Ingrese su promedio{i}"))   
        promedios.append(prom)

    #Calculo promedio general
    promedio_total = sum(promedios)//len(promedios)
    print("Su promedio final es:", promedio_total)

    #Calculo de proemdio
    estudiantes = 0
    for aprob in promedios:
        if aprob >= 60
            estudiantes +=1
    print (f"Los estudinates aprobados son {estudiantes}")


    #PROMEDIO MAS BAJO
    nota_baja = min(promedios)
    
