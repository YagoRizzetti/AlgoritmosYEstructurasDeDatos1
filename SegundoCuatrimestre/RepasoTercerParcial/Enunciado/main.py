#Una agencia de servicios turísticos desea un programa para
#procesar los datos de los paquetes de viajes que ofrece. Por
#cada paquete se tienen los siguientes datos: el número de
#identificación del paquete, la descripción del paquete, el tipo
#de paquete (un número entero entre 0 y 19, para indicar por
#ejemplo: 0: viaje por Europa Occidental, 1: viaje por Europa
#Oriental, etc.), la cantidad de días que dura el viaje ofrecido y
#el importe a cobrar por persona.
#Se desea almacenar la información referida a los n paquetes
#en un arreglo de registros de tipo Paquete (definir el tipo
#Paquete y cargar n por teclado).

import random
from RegistroPaquete import *

def validarMayorQue(mensaje,n):
    num = int(input(mensaje + str(n) +":"))
    while num <= n:
        print("ERROR!")
        num = int(input(mensaje + str(n) +":"))
    return num

def validarEntre(i,s):
    num = int(input("ingrese valor >" + str(i) + "<" + str(s) + ":"))
    while num < i or num > s:
        print("ERROR!")
        num = int(input("Ingrese otro Valor: "))
    return num

def cargarVector(v):
    for i in range(len(v)):
        id = validarMayorQue("id mayor a: ", 0)
        des = input("Ingrese Descripcion: ")
        tip = validarEntre(0,19)
        dias = validarMayorQue("Cantidad de dias mayor a: ", 0)
        imp = float(input("Ingrese el Importe: "))
        v[i] = Paquete(id,des,tip,dias,imp)

def ordernarPorDescripcion(v):
    #SELECCION DIRECTA
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].descripción > v[j].descripcion:
                v[i], v[j] = v[j], v[i]

def mostrar(v):
    for i in range(len(v)):
        write(v[i])

def buscarPaquete(v, x, t):
    b = False
    for i in range(len(v))
        if i.id == x and i.importe >= t:
            write(v[i])
            b = True
            break
    if b == False:
        print("No se encontro el paquete con los datos que busca.")

def main():
    ban = False
    n = int(input("Ingrrese la cantidad de paquetes: ")) 
    v = [None] * n
    opciones = (1,2,3,4,5)
    o = 0
    while o not in opciones:
        print("1-Cargar Paquete")
        print("2-Ordenar Paquete")
        print("3- ")
        print("4-Buscar Paquete")
        print("5-Salir")
        o = int(input("Elija una opcion del menu: "))
        if o == 1:
            ban = True
            cargarVector(v)
        elif o == 2:
            if ban:
                ordernarPorDescripcion(v)
                mostrar(v)
            else:
                print("Vector sin datos!")
        elif o == 3:
            pass
        elif o == 4:
            x = int(input("Ingrese el numero de identificacion del vector que quiera buscar: "))
            t = int(input("Ingrese el importe minimo que deba tener el paquete: "))
            buscarPaquete(v, x, t)
        elif o == 5:
            print("ADIOS!.")
            break

main()

