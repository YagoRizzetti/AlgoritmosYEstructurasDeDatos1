import random
from Registro import *

def generarDeudas(v):
    nom = ("pepe","juan","macri","gato","marito","cris","dana")
    for i in range(len(v)):
        nombre = random.choice(nom)
        monto = random.randint(1,10000)
        v[i] = Deuda(nombre,monto)

def mostrarV(v):
    for i in range(len(v)):
        write(v[i])


def montoPromedio(v):
    tm = 0
    cm = len(v)
    for i in range(cm):
        tm += v[i].Monto
    prom = tm/cm
    print(prom)


def menorDeuda(v):
    m = []
    for i in range(len(v)):
        if i == 0:
            m = v[i]
        elif v[i].Monto < m.Monto:
            m = v[i] 
    write(m)

def pmmm(v,m):
    tm = 0
    p=0
    for i in range(len(v)):
        if m > v[i].Monto:
            p+=v[i].Monto
    for i in range(len(v)):
        tm += v[i].Monto
    
    porc = p*100/tm
    
    print('el procentaje es de:' + str(porc))    





        

    