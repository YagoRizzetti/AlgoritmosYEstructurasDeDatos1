class Estudiante:
    def __init__(self, leg, nom, ape, prom):
        self.legajo = leg
        self.nombre = nom
        self.apellido = ape
        self.promedio = prom
    
def write(estudiante):
    print("Legajo: ", estudiante.legajo,"-" , end=" ")
    print("Nombre: ", estudiante.nombre,"-" , end=" ")
    print("Apellido: ", estudiante.apellido,"-" , end=" ")
    print("Promedio: ", estudiante.promedio)

