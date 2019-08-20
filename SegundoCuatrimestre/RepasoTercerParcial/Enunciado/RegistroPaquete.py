class Paquete: 
    def __init__(self, id, desc, tipo, dias, imp):
        self.id = id
        self.descripcion = desc
        self.tipo = tipo
        self.dias = dias
        self.importe = imp


def write(paquete):
    print("numero: ", paquete.id, "-", end=" ")
    print("descripcion: ", paquete.descripcion, "-", end=" ")
    print("tipo: ", paquete.tipo, "-", end=" ")
    print("dias: ", paquete.dias, "-", end=" ")
    print("importe: ", paquete.importe)
