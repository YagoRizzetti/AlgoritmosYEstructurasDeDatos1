class Servicio:
    def __init__(self,id,nombre,tipo,importe,personal):
        self.id =id
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
        self.personal = personal

def write(servicio):
    print("Numero de Identificacion: ",servicio.id , "-" , end=" ")
    print("Nombre del servicio: ",servicio.nombre , "-" , end=" ")
    print("tipo de servicio: ",servicio.tipo , "-" , end=" ")
    print("importe: ",servicio.importe , "-" , end=" ")
    print("Cantidad de personal: ",servicio.personal , "-" , end=" ")
