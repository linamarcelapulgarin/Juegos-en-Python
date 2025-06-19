from operator import truediv


print("Hola mundo")
#Esto es un texto que será ignorado en la ejecución del programa Python
print("Hola mundo al final")

#---------------------------------
#SINTAXIS DE PYTHON
#---------------------------------

#Reglas que de deben seguir para escribir el código para que sea vbálido y pueda ser interpretado correctamente

#INDENTACION
#Espacio en blanco llamado tabulación al comienzo de una línea de código
#El scope no se delimitará por llaves si no a través de la indentación

#-----Esta es una estructura-----------------------
s=5
for i in range(s):
    print(i)
#----------------------------


#---------------------------------
#VARIABLES
#---------------------------------
#Contenedores que almacenan datos que pueden variar durante la ejecución de un programa
#Cada variable tiene un nombre único y un valor asociado
#Para asignarle el valor se utiliza "="

x=5
nombre = "Juan"

print(x)
print(nombre)
y = str(x) #casteo (cambiar de tipo de formato)

#VALIDO: Si comienza con una letra y sin caracteres especiales
mivariable = "texto"

#VALIDO:Si comienza con una letra y guiones bajos
mi_variable ="texto"

#VALIDO:
_mi_variable = "texto"

#VALIDO: camelCase, mayusculas en el nombre de la variable
miVariable ="texto"

#VALIDO: Puede ser todo mayúsucla
MIVARIABLE = "Texto"

#VALIDO: Utilizar números pero no al comienzo
mivariable2 = "texto"

#NO VALIDO: Comenzar con número
#NO VALIDO: Usar guion medio
#NO VALIDO: Usar espacios
#NO VALIDO: Símbolo $ pesos

#---------------------------------
#TIPOS DE DATOS
#---------------------------------

#TEXTO
# -str String (Cadena de caracteres)
Texto = " cadena de caracteres"

#NUMÉRICOS

# - int (entero)
numero_entero=10 

# - float (flotante)
numero_flotante=3.14

#- complex [Número complejo 
numero_complejo = 2 + 3j

#SECUENCIA
# List(lista) (colección ordenada y mutable)
lista = [1,2,3,4]

#- tuple (tupla) [colección ordenada y inmutable]
tuple = (1,2,3)

#- range (rango) [secuencia inmutable de números]
rango = range (0,10)

#MAPPING TIME (MAPEO)

# - dict (diccionario) [coleccion no ordenada de pares clave-valor, clave- valor]
diccionario = {"nombre":"Sergio", 
               "Edad": 34
}

#SET TYPES (Tipos de conjuntos)

#- set (conjunto) [colección no ordenada y mutable de elementos UNICOS (No se pueden repetir)
conjunto = {1,2,3}

# - frozenset (conjunto inmutable)
conjunto_inmutable = frozenset({1,2,3})

#BOOLEAN TYPES

#- boolean  (puede ser verdadero o falso)
booleano = True
booleano2 = False

#BOLEANOS BINARIOS
# - Bytes [representa una secuencia inmutable de bytes]
bytes_data = b"datos"

#- bytearray (array de bytes) [una secuencia mutable de bytes]
bytearray_data = bytearray(b"datos")

#- memoryview (vista de memoria) [permite acceder a la memoria de objetos de bytes sin hacer copia]
memoria = memoryview(b"datos")

#NONE / NULL (NULE)

#NoneType (nulo) [Representa la ausencia de valor o la no definición]
nulo= None

#-----------------------------------
# CASTEO
#-----------------------------------

# Texto str
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

#Numéricas (int, float, complex)
variable4 = 10
variable5 = 2.5
variable6 = 3j

#Casteo de str a int
variable_casteada = int (variable2)

#casteo de int a str
variable_casteada2 = str(variable4)

print(type(variable1)) #<class 'str'>
print(type(variable2)) #<class 'str'>
print(type(variable3)) #<class 'str'>
print(type(variable4)) #<class 'int'>
print(type(variable5)) #<class 'float'>
print(type(variable6)) #<class 'complex'>

print(type(variable_casteada)) #<class 'str'>
print(type(variable_casteada2)) #<class 'str'>


#OTRO EJEMPLO

lista = ["manzana", "pera", "naranja"]

print(type(lista))
x=list(("manzana", "pera", "naranja"))

print(type(x))

#-----------------------------

tupla = ["manzana", "pera", "naranja"]
list= list(tupla)
print(type(list))

#Se castea (cambia de tipo de dato) tipoDeDato("Dato original")
#Con la palabra type podremos saber que tipo de datos estamos trabajando

#-----------------------------
#TIPOS DE DATOS NUMÉRICOS
#-----------------------------
X=1
Y=2.4
Z= 2j

print(type(X))
print(type(Y))
print(type(Z))

x=5
y=float(x)

print(y)
print(type(y))

#-----------------------------------
#RANDOM -- Tiene muchos más datos pero estos son ejemplos que se pueden importar 
#-----------------------------------
import random

x=random.randrange(1,10) # incluye los valore de 0 a 9
print(x)

x=random.random() # dato de clase flotante
print(x)
print(type(x))

x=random.randint(1,10) # dato de clase aleatoria entera tiene en cuenta el 10
print(x)
print(type(x))

#-----------------------------------
#CADENA DE CARACTERES
#-----------------------------------
#Las comillas triples permiten hacer saltos de línea

txt = """
Hola Mundo
"""
print(txt)

#para llamar el caracter se hace con el indice que indica la posición donde se encuentra el elemento en la estructura ejemplo 0=H o cero es la posición donde se encuentra H
# Para invocar el índice se debe hacer con corchete, no parentesis
txt= "Hola Mundo"
print(txt[0])
print(txt[1])
print(txt[2])
print(txt[3])

txt= "Hola Mundo" 
int=len(txt)
print(int) # devuelve la cantidad de caracteres, total 10

txt= """Hola Mundo
"""
int=len(txt)
print(int) # también cuenta los saltos de linea

#las búsquedas y la mayoría de los métodos son case sensitive y también a las acentuaciones

txt= "En este texto les explicaré acerca de las cadenas de los caracteres en inglés llamadas STRING"
print("inglés" in txt) #se fija en los acentos

#también se pueden buscar palabras que no están en el texto

txt= "En este texto les explicaré acerca de las cadenas de los caracteres en inglés llamadas STRING"
print("inglés" not in txt) #se fija en los acentos

#En slicing ponemos desde un caracter hasta un caracter no incluido
txt= "seguimos trabajando con STRINGS"
print (txt[8:19])
print (txt[23:])
print (txt[-7:-1])

txt= "CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO"
minuscula = txt.lower()
print (minuscula)

txt= "CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO"
mayuscula = txt.upper()
print (mayuscula)


#El siguiente metodo hace que se elimien los espacios

txt= "         Uyh! Me dejé algunos espacios antes y después de este texto    "
texto_importante= "clave  "
texto_corregido =txt.strip()
texto_corregido2 =texto_importante.strip()

print(texto_corregido)
print(texto_corregido2)

#CONCATENACIÓN
a= "Hola"
b= "Mundo"
c =a +" "+ b

txt= "El contenido de este curso va a durar"
horas = 10

concatenado= txt + str(horas) + " horas"
print(concatenado) # no va a funcionar porque son tipos de datos distintos, al menos que pase horas a formato string

txt= "El contenido de este curso va a durar {} horas"
horas = 10
print(txt.format(horas)) #format permite agregarlo como un objeto independientemente de si no es un formato string

txt= "El contenido de este curso va a durar {0}horas y tendrá {1}clases"# se le puede dar orden a los formatos
horas = 10
clases= 60
print(txt.format(horas, clases)) 

#con la barra invertida podemos escapar de los caracteres especiales \n salto de línea \t para tabulaciones y \ para un backspace o borrar
txt= "la mejor serie que vi en mi vida es\"game of thrones\""
print(txt)




