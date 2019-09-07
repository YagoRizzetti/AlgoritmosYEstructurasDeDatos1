from Registro import * 
import random

def validarPositivo():
    id = random.randint(1,100)
    while id < 0:
        id = random.randint(1,100)
    return id

def validarEntre(inf,sup):
    tipo = random.randint(0,19)
    while tipo < 0 or tipo > 19:
        tipo = random.randint(0,19)
    return tipo

def mostrar(v):
    for i in range(len(v)):
        write(v[i])

def cargarDatos(v,d):
    for i in range(len(v)):
        id = validarPositivo()
        descripcion = random.choice(d)
        tipo = validarEntre(0,19)
        dias = random.randint(1,100)
        importe = random.randint(1,100000)
        v[i] = Paquete(id,descripcion,tipo,dias,importe)

def paquetesOrdenados(v):
    for i in range(len(v) - 1):
        for j in range(i+1,len(v)):
            if v[j].dias < v[i].dias:
                v[i] , v[j] = v[j] , v[i]
    mostrar(v)

def cantPaquetePorTipo(v):
    c = [0] * 20
    for i in range(len(v)):
        c[v[i].tipo] += 1
    return c 

def buscar(v):
    n = int(input("Ingrese el Numero de Identificacion: " ))
    im = int(input("Ingrese el importe minimo a buscar: "))
    b = False
    for i in range(len(v)):
        if v[i].id == n and v[i].importe >= im:
            write(v[i])
            b = True
            break
    if b == False:
        print("No Existe el Viaje que esta buscando")

def buscarD(v):
    d = int(input("Ingrese la cantidad de dias que desea buscar: "))
    n = len(v)
    inf, sup = 0 , n-1
    b = False
    while inf <= sup:
        c = (inf + sup)//2
        if v[c].dias == d:
            write(v[c])
            b = True
            break
        elif d < v[c].dias:
            sup = c - 1
        elif d > v[c].dias:
            inf = c + 1
    if b == False:
        print("No Existe el Registro que busco")

def buscarI(v):
    m = [None]
    for i in range(len(v)):
        if i == 0:
            m = v[i]
        elif v[i].importe > m.importe:
            m = v[i]
    write(m)