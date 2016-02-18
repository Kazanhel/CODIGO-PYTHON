# EJERCICIO 9
#Escribe un programa que nos pida por teclado dos números enteros y que a continuación muestre en pantalla 
#la suma de los dos números solamente si son los dos positivos. Si no se cumple que los dos números sean positivos se visualizará un mensaje indicándolo. 
#La salida ha de tener el siguiente formato: “La suma de los dos números es: XXX” 
#o “No se calcula la suma porque alguno de los números o los dos no son positivos”.


numeroUno = int(input("Escriba el primer numero: "))
numeroDos = int(input("Escriba el segundo numero: "))
suma = numeroUno + numeroDos
if numeroUno >= 0 and numeroDos >= 0:
    print ("La suma de ambos numeros es de: " + str(suma)) 
else:
    print ("No se calcula la suma porque alguno de los números o los dos no son positivos")
