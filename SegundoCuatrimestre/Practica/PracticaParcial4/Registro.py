class Paquete:
    def __init__(self,id,descripcion,tipo,dias,importe):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.dias = dias
        self.importe = importe

def write(paquete):
    print("Numero de Identificacion: ", paquete.id , "-", end=" ")
    print("Descripcion: ", paquete.descripcion , "-", end=" ")
    print("Tipo: ", paquete.tipo , "-", end=" ")
    print("Dias: ", paquete.dias , "-", end=" ")
    print("Importe: ", paquete.importe )
