# EJERCICIO 12
#Escribe	un programa que pida por teclado dos números y que calcule y muestre su suma solamente si:
#los dos son pares 
#el primero es menor que cincuenta 
#y el segundo está dentro del intervalo cerrado 100-500. 
#En el caso de que no se cumplan las condiciones, en vez de la suma ha de visualizarse un mensaje de error.

numeroUno = int(input("Introduce el primer valor: "))
numeroDos = int(input("Introduce el segundo valor: "))
sumaNumeros = numeroUno + numeroDos
if (numeroUno%2== 0) and (numeroDos%2==0) and numeroUno < 50 and numeroDos > 100 and numeroDos < 500:
    print (sumaNumeros)
else:
    print ("No se cumplen las condiciones de la suma. Vuelva a intentarlo!")
