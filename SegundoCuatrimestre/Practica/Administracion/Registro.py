class Examen:
    def __init__(self, dni, nombre, cargo, puntaje):
        self.dni = dni
        self.nombre = nombre
        self.cargo = cargo
        self.puntaje = puntaje

def write(examen):
    print("DNI: ", examen.dni , "-", end=" ")
    print("Nombre: " ,examen.nombre , "-", end=" ")
    print("Cargo: " ,examen.cargo , "-", end=" ")
    print("Puntaje: " ,examen.puntaje , "-", end=" ")