# Programa: Control de Temperatura Semanal

temperaturas = []

# a) Solicitar las 7 temperaturas
for dia in range(1, 8):
    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(temp)

# b) Calcular el promedio
promedio = sum(temperaturas) / len(temperaturas)

# c) Contar días con temperatura mayor al promedio
dias_mayores = 0
for temp in temperaturas:
    if temp > promedio:
        dias_mayores += 1

# d) Encontrar el día con la temperatura más baja
temp_min = min(temperaturas)
dia_min = temperaturas.index(temp_min) + 1

# Mostrar resultados
print(f"\nPromedio semanal: {promedio:.2f}°C")
print(f"Días con temperatura mayor al promedio: {dias_mayores}")
print(f"Día con la temperatura más baja: Día {dia_min}")





# Programa: Cajero Automático

PIN_CORRECTO = "1234"
saldo = 500  # saldo inicial

# a) Solicitar el PIN
pin = input("Ingrese su PIN: ")

# b) Verificar PIN
if pin == PIN_CORRECTO:
    while True:
        print("\nBienvenido. ¿Qué desea hacer?")
        print("1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Saldo actual: {saldo}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Nuevo saldo: {saldo}")
            else:
                print("Saldo insuficiente.")
        elif opcion == "3":
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f"Nuevo saldo: {saldo}")
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")
else:
    print("PIN incorrecto.")









    # Programa: Análisis de Dígitos

numero = int(input("Ingrese un número entero positivo: "))

# Convertir a cadena para recorrer dígitos
digitos = [int(d) for d in str(numero)]

# a) Cantidad de dígitos
cantidad = len(digitos)

# b) Suma de dígitos
suma = sum(digitos)

# c) Contar pares e impares
pares = sum(1 for d in digitos if d % 2 == 0)
impares = cantidad - pares

# d) Dígito mayor
mayor = max(digitos)

# Mostrar resultados
print(f"Cantidad de dígitos: {cantidad}")
print(f"Suma de dígitos: {suma}")
print(f"Dígitos pares: {pares}")
print(f"Dígitos impares: {impares}")
print(f"Dígito mayor: {mayor}")








# Programa: Ordenamiento de Notas

notas = []

# a) Ingresar las 10 notas
for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 100): "))
    notas.append(nota)

# b) Ordenar usando burbuja
for i in range(len(notas)):
    for j in range(0, len(notas) - i - 1):
        if notas[j] > notas[j + 1]:
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

# c) Mostrar lista ordenada
print("\nLista ordenada:", notas)

# d) Calcular y mostrar promedio
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")