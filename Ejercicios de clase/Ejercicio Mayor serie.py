#el usuario mete números hasta que introduce un PUNTO.
#El programa muestra el MAYOR de la serie, el MENOR de la serie y la MEDIA
#de todos los números

###### RUTINAS ######



def cargarSerieNumeros(serieNumerosPositivos):
    ''' Es necesario programar las precondiciones'''
    contador = 0
    while contador:
	    entrada = int( input('Introduce un numero: ') )
	    if entrada >= 0:
	    	contador += 1
	    elif type(entrada) != int:
                break
	    else:
	    	print("Se descarta el numero negativo")
    return



def calcularMayorSerie(serieNumeros):
	# a modo de precondicion:
	if not serieNumeros:
		return None
	numeroMayor = 0
	for numero in serieNumeros:
		if numero > numeroMayor:
			numeroMayor = numero
		else:
			pass
	return numeroMayor


###### MAIN ######

print("Introduce una serie de números enteros POSITIVOS. El programa te devolverá el MAYOR, el MENOR y la MEDIA de la serie de números. Cuando quieras detener la serie de números introduce un PUNTO '.'")

serieNumeros = []

longitudSerie =  int( input('Introduce la longitud de la serie de numeros positivos: ') )

cargarSerieNumerosPositivos(serieNumeros, longitudSerie)

numeroMayor = calcularMayorSerie(serieNumeros)

if numeroMayor or numeroMayor == 0:
	print("El mayor numero es: ", numeroMayor)
else:
	print("No existe serie de numeros")


###### CASOS TEST ######

# Casos test calcularMayorSerie(serieNumeros):

print("###### Casos Test calcularMayorSerie ######")

testListaVacia = ([], None)

casosTest = [([0], 0),
			 ([1, 2, 3, 4], 4),
			 ([-1, -2, 3], 3),
			 ([1, 2, 3, 4, 5], 5),
			 ([5, 2, 5, 4, 0], 5),
			 ([5, 5, 5], 5)]

### caso Test lista vacia

if calcularMayorSerie(testListaVacia[0]) == testListaVacia[1]:
	# Consultar libro pag. 216 string formatting expressions
	print("caso %s => %s OK" % (testListaVacia[0], testListaVacia[1]) )
else:
	print("caso %s => %s Fallo" % (testListaVacia[0], testListaVacia[1]) )

### resto de casos Test

for casoTest in casosTest:
	numeroMayor = calcularMayorSerie(casoTest[0])
	if numeroMayor == casoTest[1]:
		# Consultar libro pag. 216 string formatting expressions
		print("caso %s => %d OK" % (casoTest[0], numeroMayor ) )
	else:
		print("caso %s => %d Fallo" % (casoTest[0], numeroMayor ) )

### casos test con colores

print("###### Casos Test calcularMayorSerie con colores ######")

if calcularMayorSerie(testListaVacia[0]) == testListaVacia[1]:
	# Consultar libro pag. 216 string formatting expressions
	print("caso %s => %s" % (testListaVacia[0], testListaVacia[1]), bcolors.OKGREEN + "OK" + bcolors.ENDC)
else:
	print("caso %s => %s" % (testListaVacia[0], testListaVacia[1]), bcolors.FAIL + "FAIL" + bcolors.ENDC)

for casoTest in casosTest:
	numeroMayor = calcularMayorSerie(casoTest[0])
	if numeroMayor == casoTest[1]:
		# Consultar libro pag. 216 string formatting expressions
		print("caso %s => %d" % (casoTest[0], numeroMayor), bcolors.OKGREEN + "OK" + bcolors.ENDC) 
	else:
		print("caso %s => %d" % (casoTest[0], numeroMayor), bcolors.FAIL + "FAIL" + bcolors.ENDC) 
