class CuentaCorriente:

    def __init__(self, nombre = "test", apellidos = "test", direccion = "test", telefono = "123456789", saldo = 0.0):
        self.nombre     = nombre
        self.apellidos  = apellidos
        self.direccion  = direccion
        self.telefono   = telefono
        self.saldo      = saldo

# getters y setters
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    def getDireccion(self):
        return self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono
    def getTelefono(self):
        return self.telefono
    
    def setSaldo(self, saldo):
        self.saldo = saldo
    def getSaldo(self):
        return self.saldo

# métodos

    def retirarDinero(self, cantidad):
        self.saldo = self.saldo - cantidad

    def ingresarDinero(self, cantidad):
        self.saldo = self.saldo + cantidad

    def sinSaldo(self):
        if self.saldo >= 0:
            return True
        else:
            return False

    def consultarCuenta(self):
        print ("Nombre: " + self.nombre)
        print ("Apellidos: " + self.apellidos)
        print ("Direccion: " + self.direccion)
        print ("Telefono: " + self. telefono)
        print ("Saldo: " + str(self.saldo))


if __name__ == '__main__':

    cuentaTest = CuentaCorriente("Denis", "Dilianov Filipov", "c/ Cartons", "685968324", 500)
    cuentaTest.consultarCuenta()
