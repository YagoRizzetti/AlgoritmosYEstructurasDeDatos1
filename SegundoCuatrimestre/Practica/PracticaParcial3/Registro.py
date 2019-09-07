class Alquiler:
    def __init__(self,id,descripcion,tipo,importe,dias):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.dias = dias

def write(alquiler):
    print("Numero de Identificacion: ",alquiler.id , "-", end=" ")
    print("Descripcion: ",alquiler.descripcion , "-", end=" ")
    print("Tipo: ",alquiler.tipo , "-", end=" ")
    print("Importe a Cobrar: ",alquiler.importe , "-", end=" ")
    print("Cantidad de Dias: ",alquiler.dias )

