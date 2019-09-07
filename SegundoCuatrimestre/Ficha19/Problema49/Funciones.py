from Registro import *

def generarDatos(v):
    for i in range(v):
        id = int(input("Ingrese el numero de identificacion: "))
        nombre =input("Ingrese el nombre del socio: ")
        arancel = float(input("Ingrese el arancel: "))
        deporte = validarEntre(0,9)
        v[i] = socio(id, nombre, arancel, deporte)

def mapd(v,p):
    pass
