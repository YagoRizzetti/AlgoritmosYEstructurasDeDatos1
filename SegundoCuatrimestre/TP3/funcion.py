import random
from Registro import *

def ordenar(v):
    for i in range(1, len(v)):
        for j in range(len(v) - i):
            if v[j][1] > v[j+1][1]:
                temp = v[j][0], v[j][1]
                v[j][0], v[j][1] = v[j+1][0], v[j+1][1]
                v[j+1][0], v[j+1][1] = temp
    return v

def generarArticulos(v):
    e = ("nuevo","usado")
    for i in range(len(v)):
        identificador = random.randint(1, 1000)
        precio = random.randint(1, 100000)
        ubicacion = random.randint(1, 23)
        estado = random.choice(e)
        cantidad = random.randint(0, 100)
        puntuacion = random.randint(1, 5)
        v[i] = Articulo(identificador, precio, ubicacion, estado, cantidad, puntuacion)    

def mostrarV(v):
    for i in range(len(v)):
        write(v[i])

def articulosNuevos(v):
    registros = len(v)
    atributos = len(v[0])
    an = []
    for r in range(registros):
        for a in range(atributos):
            if v[r][3] == "nuevo":
                an.append(registros[r])
    mostrarV(an)
    return an

def articulosUsados(v):
    registros = len(v)
    atributos = len(v[0])
    for r in range(registros):
        for a in range(atributos):
            print([r][a])