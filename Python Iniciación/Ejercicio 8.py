# EJERCICIO 8
#Escribe	un programa que pida por teclado dos números y que muestre en pantalla uno de los dos mensajes siguientes en función de los números leídos: 
#a) el primer número (valor) es mayor que el segundo (valor)(introduciendo el valor de los números en el mensaje); 
#b) el primer número (valor) es menor que el segundo (valor); 
#c) los dos números son iguales (valor).


numeroUno = int(input("Escriba el primero numero: "))
numeroDos = int(input("Escriba el segundo numero: "))

if numeroUno > numeroDos:
    print ("El primero número " + str(numeroUno) + " es mayor que el segundo " + str(numeroDos))
elif numeroUno < numeroDos:
    print ("El primer valor " + str(numeroUno) + " es menor que el segundo " + str(numeroDos))
else:
    print ("Los dos numeros son iguales " + str(numeroUno))
