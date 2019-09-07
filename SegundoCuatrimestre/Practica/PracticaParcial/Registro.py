class Servicio:
    def __init__(self,id,nombre,tipo,dias,medicamentos):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.dias = dias
        self.medicamentos = medicamentos

def write(servicio):
    print("Numero de Identificacion: " ,servicio.id , "-", end=" ")
    print("Nombre: " ,servicio.nombre , "-", end=" ")
    print("Tipo de Prctica: " ,servicio.tipo , "-", end=" ")
    print("Cantidad de dias: " ,servicio.dias , "-", end=" ")
    print("Cantidad de Medicamentos: " ,servicio.medicamentos )

