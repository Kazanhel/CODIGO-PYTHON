# EJERCICIO 13

#Diseña	un programa que calcule el importe final de una venta considerando que sobre el valor bruto se hace un descuento según la siguiente tabla:
#Valores <=20 implican un descuento del 0%
#Valores >20 y <=100 implican un descuento descuento del 5%
#Valores >100 implican un descuento 10%


precioVenta = int(input("Introduzca el precio de la venta para que se le aplique el descuento: "))
cincoPorCiento = precioVenta * 0.95
diezPorCiento = precioVenta * 0.9
if precioVenta <= 20:
    print ("No se le aplicará ningun descuento. Precio final: " + str(precioVenta) + " euros")
elif precioVenta > 20 and precioVenta <= 100:
    print ("Se le aplica un descuento del 5%. Precio final: " + str(float(cincoPorCiento)) + " euros.")
else:
    print ("Se le aplica un descuento del 10%. Precio final: " + str(float(diezPorCiento)) + " euros.")
