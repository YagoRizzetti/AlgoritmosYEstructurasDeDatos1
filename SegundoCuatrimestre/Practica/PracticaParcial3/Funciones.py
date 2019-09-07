from Registro import *
import random

def cargarV(v,d):
    for i in range(len(v)):
        id = random.randint(1,100)
        descripcion = random.choice(d)
        tipo = random.randint(0,9)
        importe = random.randint(1,1000)
        dias = random.randint(1,30)
        v[i] = Alquiler(id,descripcion,tipo,importe,dias)

def mostrarV(v):
    for i in range(len(v)):
        write(v[i])

def ordenadosImoprte(v):
    for i in range(len(v) - 1):
        for j in range(i+1 , len(v)):
            if v[i].importe > v[j].importe:
                v[i] , v[j] = v[j] , v[i]
    mostrarV(v)

def verCantPorTipo(v):
    cant = [0] * 10
    for i in range(len(v)):
        cant[v[i].tipo] += 1

    return cant

def buscar(v,desc, di):
    b = False
    for i in range(len(v)):
        if v[i].descripcion == desc and v[i].dias == di:
            write(v[i])
            b = True
            break 
    if b == False:
        print("No existe alquiler con esos datos.")
