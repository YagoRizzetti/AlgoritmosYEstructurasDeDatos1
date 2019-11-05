class Profesional:
    def __init__(self, dni, nombre, importe, afiliacion, trabajo):
        self.dni = dni
        self.nombre = nombre
        self.importe = importe
        self.afiliacion = afiliacion
        self.trabajo = trabajo

def writeProfesional(profesional):
    print("DNI: ", profesional.dni, "-", end=" ")
    print("Nombre: ", profesional.nombre, "-", end=" ")
    print("Importe Mensual: ", profesional.importe, "-", end=" ")
    print("Afiliacion: ", profesional.afiliacion, "-", end=" ")
    print("Tipo de Trabajo: ", profesional.trabajo)
