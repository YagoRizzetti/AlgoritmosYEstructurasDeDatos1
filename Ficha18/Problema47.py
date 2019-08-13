from Estudiantes import *

def cargarVector(vec):
    for i in range(len(vec)):
        print("Estudiante ", i+1)
        print("-"*30)
        leg = int(input("Ingrese el Legajo: "))
        nom = input("Ingrese el Nombre: ")
        ape = input("Ingrese Apellido: ")
        prom = int(input("Ingrese el Promedio: "))
        print("-"*30)
        vec[i] = Estudiante(leg, nom, ape, prom)

def mostrarVector(vec):
    for i in range(len(vec)):
        write(vec[i])


def main():
    n = int(input("Ingrese la cantidad de Estudiantes: "))
    v = n * [None]

    cargarVector(v)
    mostrarVector(v)

main()