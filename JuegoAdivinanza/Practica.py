#JUEGO DE ADIVINANZA
#Practica de estructuras de control

import random


numero_secreto =random.randint(1,101)
adivinado = False

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
   entrada = (input ("Indroduce un número del 1 al 100: ")) 
   numero =int(entrada)
   if numero == numero_secreto:
            print("¡Felicidades, has adivinado el número secreto!")
            adivinado = True
   elif numero < numero_secreto:
         print("el número es mayor al ingresado")
   else:
        print("el número es menor del ingresado")












