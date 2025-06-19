#---------------------
# ESTRUCTURAS DE CONTROL
#---------------------

#Bloque de control que permite controlar el flujo de ejecución de un programa

#---------------------
# CONDICIONALES 
#---------------------

# if - si pasa tal cosa
# elif - si pasa tal otra
# else - si no pasa ni lo primero ni lo segundo pasará lo que dice else

x=10
if x >0:
    print("x es menor igual a 5")
elif x <0:
    print("x es un número negativo") 
else:
    print("x es igual a 0")

#---------------------
# CONDICIONALES TERNARIAS
#---------------------

# Forma concisa de expresar una estructura condicional en una sola línea 
# valor_si_condicion_verdadera if condicion (formula) else falsa

x=10
resultado = "positivo" if x>0 else "negativo"



#---------------------
# BUCLES  Permiten ejecutar repetidamente un bloque de código mientras se cumpla una condicion o se vuelva falsa
#---------------------

# Bucle While
# while condicion:  codigo a ejecutar si la condicion es verdadera

contador = 0
while contador < 5:
    print("contador es:", contador)
    contador += 1 # hace que el contador sume 1 hasta cumplir la condicion (tener cuidado donde se agrega el contador si por debajo o encima del print)

print(contador)

#Bucle FOR
# for indice in range(cantidad): codigo a ejecutar en cada interacion

for i in range(1,11,2): # el tercer numero despues de la coma pide contar de dos en dos y va a ser par o impar dependiendo de si empieza en 0 o 1
    print(i)


#---------------------
# Manejo de Excepciones o errores
#---------------------

# try - excepciones que puede generar una excepción
# except TipoDeExcepción as nombre_variable - codigo para manejar la excepción
# finally - codigo que siempre se ejecuta, OPCIONAL

#Manejo de la división por cero
a=10
b=5
try: #Intenta hacer algo
    resultado=a/b
    print(resultado)

except ZeroDivisionError: #si tiene un error se puede manejar desde aqui
    print("No se puede dividir por cero")

finally: #Intenta hacer algo siempre
    resultado=0
    print(resultado)


#---------------------
# PABLABRAS CLAVE - Estructuras de Control
#---------------------

#BREAK
for i in range(5):
    if i == 3:
        break
    print(i) # Se espera 1,2, (no muestra el 3)

#CONTINUE
for i in range(5):
    if i == 3:
        continue
    print(i) # Se espera 1,2,4 (no muestra el 3)

#PASS
edad = 19
if edad > 18:
    print("puedes ingresar a esta institucion")
elif edad == 18:
    pass
else:
    print("no tienes edad suficiente para entrar aquí")





