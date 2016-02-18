# Construye una clase de nombre Hora que permita almacenar la hora, así como los métodos para manipularla .
class Hora():

#SetHora

    def __init__ (self, horas = 0, minutos = 0, segundos = 0):
        self.setHora(horas, minutos, segundos)
        
    def setHora(self, horas, minutos, segundos):
        try:
            if horas > 0 and horas <= 24:
                self.horas = horas
            else:
                self.horas = 0
                
            if minutos > 0 and minutos <= 59:
                self.minutos = minutos
            else:
                self.minutos = 0
                
            if segundos > 0 and segundos <= 59:
                self.segundos = segundos
            else:
                self.segundos = 0
        except TypeError:
            print("Error, introduzca otra hora")
#GetHora
            
    def getHora(self):
        horaNow = [self.horas, self.minutos, self.segundos]
        return horaNow
    
#ImprimirHora
    
    def imprimirHora(self):
        print("Ahora son las: " + str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos) + " horas")

#Set y Get
        
    def setHoras(self, horas):
        self.horas = horas
    def getHoras(self):
        return self.horas
    
    def setMinutos(self, minutos):
        self.minutos = minutos
    def getMinutos(self):
        return self.minutos
    
    def setSegundos(self, segundos):
        self.segundos = segundos
    def getSegundos(self):
        return self.segundos

    
#Casos Test
if __name__ == '__main__':

#Casos test logica
    objeto = Hora()
    print(objeto.horas, objeto.minutos, objeto.segundos)
    objeto = Hora(33, 61, 56)
    print(objeto.horas, objeto.minutos, objeto.segundos)

#Casos test para setHora
    objeto.setHora(14, 'asd', 45)
    print(objeto.horas, objeto.minutos, objeto.segundos)
    objeto.setHora(19, 35, 3)
    print(objeto.horas, objeto.minutos, objeto.segundos)

#Casos test para getHora
    horaNow = objeto.getHora()
    print(horaNow[0], horaNow[1], horaNow[2])

#Casos test para imprimirHora
    objeto.imprimirHora()


