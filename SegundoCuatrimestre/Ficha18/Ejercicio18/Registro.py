class apuesta:
    def __init__(self, numero, caballo, monto):
        self.numero = numero
        self.caballo = caballo
        self.monto = monto

def write(apuesta):
    print("Numero: ", apuesta.numero, end=" ")
    print("Caballo: ", apuesta.caballo, end=" ")
    print("Monto: ", apuesta.monto)