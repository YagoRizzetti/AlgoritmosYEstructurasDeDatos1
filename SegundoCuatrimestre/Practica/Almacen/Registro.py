class Deuda:
    def __init__(self, NombreCliente, Monto):
        self.NombreCliente = NombreCliente
        self.Monto = Monto

def write(deuda):
    print("Nombre Del Cliente: ", deuda.NombreCliente , "-", end=" ")
    print("Precio: ", deuda.Monto)    