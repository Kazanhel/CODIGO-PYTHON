# EJERCICIO 10 ALTERNATIVO
#Modifica el programa anterior para que en vez de mostrar un mensaje genérico en el caso
#de que alguno o los dos números sean negativos, escriba una salida diferenciada para cada una de
#las situaciones que se puedan producir, utilizando los siguientes mensajes:
#-No se calcula la suma porque el primer número es negativo.
#-No se calcula la suma porque el segundo número es negativo.
#-No se calcula la suma porque los dos números son negativos.


numeroUno = int(input("Escriba el primer numero: "))
numeroDos = int(input("Escriba el segundo numero: "))
suma = numeroUno + numeroDos
def cosas ():
    if numeroUno >= 0 and numeroDos >= 0:
        print ("La suma de ambos numeros es de: " + str(suma))
    elif numeroUno < 0 and numeroDos >= 0:
        print ("No se calcula la suma porque el primer numero es negativo")
    elif numeroUno >= 0 and numeroDos < 0:
        print ("No se calcula la suma porque el segundo numero es negativo")
    else:
        print ("No se calcula la suma porque los dos numeros son negativos")
