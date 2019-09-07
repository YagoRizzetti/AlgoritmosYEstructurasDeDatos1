from Registro import *
import random 


def mostrarV(v):
    for i in range(len(v)):
        write(v[i])

def cargarV(v):
    nom = ("Mariano","Gabi","Negro","Nico","Facu","Nacho")
    for i in range(len(v)):
        id = random.randint(1,10000)
        nombre = random.choice(nom)
        tipo = random.randint(0,29)
        dias = random.randint(1,100)
        medicamentos = random.randint(1,50)
        v[i] = Servicio(id,nombre,tipo,dias,medicamentos)

def ordenarPorNombre(v):
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i].nombre > v[j].nombre:
                v[i] , v[j] = v[j] , v[i]
    mostrarV(v)

def pacientesPorPractica(v):
    cppp = [0] * 30
    for i in range(len(v)):
        cppp[v[i].tipo] +=1 
    
    for i in range(len(cppp)):
        if cppp[i] != 0:
            print("La cantidad de pacientes que se atendieron en la practica " + str(i) + " es de: " + str(cppp[i]))

def numeroYDias(v,n,d):
    b = False
    for i in range(len(v)):
        if v[i].id == n and v[i].dias >= d:
            write(v[i])
            b = True
            break
    if b == False:
        print("No Existe ningun paciente con los datos ingresados")



