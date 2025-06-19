#------------------------
#OPERADORES ARITMÉTICOS
#------------------------

# + Suma
# - Resta
# * Multiplicación
# / Division
#// Para dividir entero (devuelve el valor entero del resultado)
# % Resto o módulo de una división 
# ** Exponenciación
a=2
b=3
c=a+b
d=a//b # con dos barras da división me da el valor entero 
e=a%b
f=a**b


print(c)
print(d)
print(e)
print(f)
print(type(d))
print(type(c))
print(type(e))
print(type(f))

#------------------------
#OPERADORES DE ASIGNACIÓN
#------------------------

# = Asignación (toma un valor de texto, numérico, etc y le asigna un valor)

x=10
sumatorio = 3

#10
x += sumatorio #13
x += sumatorio #16
x += sumatorio #19
x += sumatorio #22

print(x) # Imprimirá el último valor asignado a esa variable

x=10
arestar = 3

#10
x -= arestar #7
x -= arestar #4
x -= arestar #1


print(x) # Imprimirá el último valor asignado a esa variable

#------------------------
#OPERADORES DE COMPARACION - Devuelve boleanos
#------------------------

#No es lo mismo un solo igual = a dos iguales ==
# == dos iguales nos ayuda a revisar si hay igualdad no para asignar

x=5
y=x

print(x==y)

# ! Signo de admiración es negación (se ampliará)
# != Sirve para comparar diferencias ¿son diferentes? 
# < > menor y mayor

 
x=5
y=40

print(x!= y)

#------------------------
#OPERADORES LOGICOS
#------------------------

# and - va a devolver TRUE si y solo si ambas afirmaciones son verdaderas
# or - Devuelve TRUE si algunas de las situaciones son verdaderas
# not - Devuelve lo opuesto al valor que siga negación de lo que sigue

x=0
#booleano = x >= 3 or x != 10

booleano = not x == 0 # x no es igual a cero

print(booleano)

#------------------------
#OPERADORES DE IDENTIDAD
#------------------------ 

# is / ==
# is not/ !=

#------------------------
#OPERADORES DE PERTENENCIA
#------------------------ 

# in -  busca un valor dentro de un string, arroja un boleano
# not in - arroja un boleano