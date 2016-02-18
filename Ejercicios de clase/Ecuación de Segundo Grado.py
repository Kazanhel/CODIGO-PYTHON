def resultadoEcuacion(a, b, c):
	import math
	if a != 0:
    raizUno = (-b + math.sqrt((b**2) - (4 * a * c)) /2 * a
    raizDos = (-b - math.sqrt((b**2) - (4 * a * c)) /2 * a
  
		return raizDos, raizUno
	else:
		return None

	
#CASOS TEST

print (resultadoEcuacion(3, 4, 5))

#PRIMER caso: if b=0 AND -c/a<0 --> NO HAY SOLUCION
if b == 0 and -c/a < 0:
	print ("No existe solucion")
else:
	print ("FAIL b = 0 and -c/a < 0")

#SEGUNDO caso:  if b=0 AND c=0 --> raizUno=raizDos=0
raizUno, raizDos = resultadoEcuacion(a, 0, 0)
if raizUno == 0, raizDos == 0:
	print ("PASS b = 0 and c = 0")
else:
	print ("FAIL b = 0 and c = 0")

#TERCER caso: if c=0 --> raizUno=0 AND raizDos=-b/a
if raizUno, raizDos == resultadoEcuacion(a, b, 0):
	print (raizUno == 0 and raizDos == -b/a)
else: 
	print ("FAIL c = 0")
	
#CUARTO caso: if a=0 --> NO HAY SOLUCION
if None == resultadoEcuacion(0, b, c):
	print ("PASS a = 0")
else:
	print ("FAIL a = 0")






























