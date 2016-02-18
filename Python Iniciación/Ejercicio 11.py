# EJERCICIO 11

#Escribe un programa que pida por teclado tres valores de tipo entero, y que calcule 
#si se cumple que la suma de dos de ellos es igual al tercero. La salida del programa tiene que tener el formato:
#Números introducidos: N1	N2 N3 (tabulador)
##Y una de las cuatro líneas de salida siguientes:
###Se cumple que N1 = N2 + N3
###Se cumple que N2 = N1 + N3
###Se cumple que N3 = N1 + N2
###Los números no cumplen la condición

numeroUno = int(input("Introduce el primer valor: "))
numeroDos = int(input("Introduce el segundo valor: "))
numeroTres = int(input("Introduce el tercer valor: "))

print ("Números introducidos: " + str(numeroUno) + "    " + str(numeroDos) + "\t" + str(numeroTres))

if numeroDos + numeroTres == numeroUno:
    print ("Se cumple que: " + str(numeroUno) + "=" + str(numeroDos) + "+" + str(numeroTres))
elif numeroUno + numeroTres == numeroDos:
    print ("Se cumple que: " + str(numeroDos) + "=" + str(numeroUno) + "+" + str(numeroTres))
elif numeroUno + numeroDos == numeroTres:
    print ("Se cumple que: " + str(numeroTres) + "=" + str(numeroUno)+ "+" + str(numeroDos))
else:
    print ("Los numeros no cumplen la condición")
