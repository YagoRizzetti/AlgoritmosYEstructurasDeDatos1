#Un cyber nos solicitó un programa que permita realizar un análisis del tráfico de la red, para ello debemos procesar
#n registros que contengan la dirección ip de la máquina que envía, dirección ip de la máquina que recibe la info y el
# tamaño en bytes enviados.
#En base a esto usted debe, mediante un menú de opciones, darle la oportunidad al usuario de:

#1 -Saber la cantidad total de bytes enviados por una dirección ip ingresada por el usuario

#2 -Mostrar los datos del registro que tengan la menor información enviada

#3 -Saber para una ip destino, el porcentaje de veces que recibio informacion sobre el
# total del trafico de la red

import random
from Registro import *


def verificarip(ipe,n):
    while ipe == n:
        n = random.randint(1,100)
    return n

#principal
def cargar_vector(vec):
    for i in range(len(vec)):
        ip_enviar = random.randint(1,100)
        ip_recibir = verificarip(ip_enviar,random.randint(1,100))
        tamaño = random.randint(1,256)             
        vec[i]= Trafico(ip_enviar,ip_recibir,tamaño)

def mostrarV(v):
    for i in range(len(v)):
        write(v[i])

def cantidad(v,n):#item1
    b = False
    for i in range(len(v)):
        if v[i].ipEnvia == n:
            print("El tamaño de byts que envio la IP "+ str(v[i].ipEnvia) + " Es de: " + str(v[i].tamaño))
            b = True
    if b == False:
        print("No Existe Esta IP En El Registro.")

def menor(v):#item2
    for i in range(len(v)):
        if v[i] == v[1]:
            break
        for j in range(1 ,len(v)):
            m = v[i].tamaño
            if v[j].tamaño < v[i].tamaño:
                m = v[j].tamaño
    print (m)



def principal():
    n=int(input('ingrese tamaño del vector:'))
    vec= [None] * n
    cargar_vector(vec)
    mostrarV(vec)
    op = -1
    while op != 0:
        print('menu de opciones')
        print('opcion-1-cantidad total de bytes por ip deseada')
        print('opcion-2-registro de menor informacion')
        print('opcion-3-porcentaje sobre el trafico de la red')
        print('opcion-0-salir')
        op=int(input('ingrese opcion:'))
        if op==1:
            n = int(input("Ingrese el ID que desea ver:"))
            cantidad(vec,n)
        elif op==2:
            menor(vec)
        elif op==3:
            pass
principal()

