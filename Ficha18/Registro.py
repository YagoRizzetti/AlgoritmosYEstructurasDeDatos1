class Empleado:
    def __init__(self, leg, nom, ape, direc, sue, ant):
        self.legajo = leg
        self.nombre = nom
        self.apellido = ape
        self.direccion = direc
        self.sueldo = sue
        self.antiguedad = ant

def write(empleado):
    print("Legajo: ", empleado.legajo, "-", end=" ")
    print("Nombre: ", empleado.nombre, "-", end=" ")
    print("Apellido: ", empleado.apellido, "-", end=" ")
    print("Direccion: ", empleado.direccion, "-", end=" ")
    print("Sueldo: ", empleado.sueldo, "-", end=" ")
    print("Antiguedad: ", empleado.antiguedad)    

e1 = Empleado(1,"juli","alvarado","depto De Gabi",1000,5)

write(e1)