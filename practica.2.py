nombre = input ( " Ingresa tu nombre:")
print(f"Bienvenido {nombre} este es un porgrama d esuma de numeros pares:")
def cont_vocal(word):
    suma = 0
    vocales = "aeiou"
    for letra in word:
        if letra == vocales:
            suma = suma + 1
    return(suma)

# Llamar a la funcion
word = input("Ingrese una palabra:")
total = cont_vocal(word)
print("La suma de sus vocales es:", total)
