import random
from Registro import *

def mostrar(v):
    for i in range(len(v)):
        write(v[i])

def cargarV(v,nom):
    for i in range(len(v)):
        id = random.randint(1,100)
        nombre = random.choice(nom)
        tipo = random.randint(0,14)
        importe = random.randint(1,10000)
        personal = random.randint(1,30)
        v[i] = Servicio(id,nombre,tipo,importe,personal)
        
def ordenadoMAM(v):
    n = len(v)
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i].id < v[j].id:
                v[i], v[j] = v[j], v[i]
    mostrar(v)

def verCantPorTipo(v):
    acu = [0] * 15
    for i in range(len(v)):
        acu[v[i].tipo] += 1
    
    for i in range(len(acu)):
        if acu[i] != 0:
            print("La cantidad de servicios por tipo " + str(i) + " es de: " + str(acu[i]))

def buscar(v,n):
    d = input("Ingrese descripcion que se encuentre dentro de las siguientes: " + str(n))
    c = int(input("Ingrese la cantidad de personas: "))
    for i in range(len(v)):
        if v[i].nombre == d and v[i].personal >= c:
            write(v[i])
            break