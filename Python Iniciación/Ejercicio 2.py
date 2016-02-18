# EJERCICIO 2
#Escribe un programa que pida por teclado el radio de una circunferencia,
#y que a continuación calcule y escriba en pantalla la longitud de la circunferencia y del área del círculo.


import math

radioC = int(input("Introduce el radio de la circunferencia: "))
print ("La longitud de la circunferencia es:", math.pi * radioC *2)
print ("El area de la circunferencia es:", math.pi * radioC**2)


