a = 4
b = 4
c = ( a + b )
print (c)

nombre = "Lucas"
nombre = "Dalto"
nombre = "Pedrito"
print (nombre)
#Las variables primero se declaran luego se definen las podemos reutilizar como en el ejemplo tambien podemos hacerlo con los numeros.
numero = 10
numero += 15
numero +=34
print (numero)

#CONCATENACION
#esto funciona cuando solo ocupas texto
nombre = 'Jaqueline'
bienvenida = 'Hola ' + nombre + ' como estas?'
print (bienvenida)


#Cuando ocupas numero se hace lo sgte: se ocupa LLAVES ejm:
edad = 35
EDAD = f'Tu  edad es:{edad} welcome'
print  (EDAD)


#DEL se ocupa para borrar datos EJM :
edad = 35
EDAD = f'Tu  edad es:{edad} welcome'
del edad #OJO ES DESPUES DE QUE HAYAS DECLARADO LAVARIABLE
print  (EDAD)

edad = 35
del edad #OJO ES DESPUES DE QUE HAYAS DECLARADO LAVARIABLE
EDAD = f'Tu  edad es:{edad} welcome'
print  (EDAD)