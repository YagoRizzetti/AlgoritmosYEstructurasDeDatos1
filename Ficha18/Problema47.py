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

def ordenarPorLegajo(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n)
            if vec[i].legajo > vec[j].legajo:
                vec[i], vec[j] = vec[j], vec[i]

def listado(vec,x):
    for in in range(len(vec)):
        if vec[i].promedio >= x:
            write(vec(i))

def cambiarPromedio(vec, x):
        ban = False
        for i in range(len(vec)):
            if vec[i].promedio == x:
				vec[i].promedio = 7
				write(vec[i])
		if ban == False:
			print("No hay alumnos con ese nombre")

def buscarPromedio(vec, x):
	band = False
	for i in range(len(vec)):
		if vec[i].promedio == x:
			write(vec[i])
			band = True
			break
	if band == False:
		print("No hay alumnos con ese promedio")

def main():
    n = int(input("Ingrese la cantidad de Estudiantes: "))
    v = n * [None]

    cargarVector(v)
    mostrarVector(v)
    ordenarPorLegajo(v)
    x = int(input("Ingrese el promedio necesario para hacer el curso: "))
    listado(v,x)
	cambiarPromedio(v,x)
	buscarPromedio(v,x)

main()