__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from generador import *
from invitado import *
import pickle
import os.path


def leer_archivo(fd):
    v = list()
    if os.path.exists(fd):
        m = open(fd,'rb')
        while m.tell() < os.path.getsize(fd):
            reg = pickle.load(m)
            v.append(reg)
        m.close()
    else:
        print('El archivo no existe')
    return v


def mostrar_vector(v):
    for invitado in v:
        print(to_string(invitado))


def contar_invitados(v):
    m = [[0] * 13 for i in range(10)]
    for invitado in v:
        m[invitado.ong][invitado.mesa]+= 1
    return m


def mostrar_conteo(m):
    for i in range(len(m)):
        print(describir_ong(i))
        for j in range (len(m[i])):
            if m[i][j] > 0:
                print('Mesa',j,':',m[i][j])


def validar_entre(desde, hasta, mensaje):
    n = int(input(mensaje))
    while n < desde or n > hasta:
        print('Inválido! Debe estar entre',desde,'y',hasta)
        n = int(input(mensaje))
    return n


def buscar_mayor_donacion(v,ong):
    may = None
    for invitado in v:
        if invitado.ong == ong:
            if may == None or invitado.monto > may.monto:
                may = invitado

    return may



def mostrar_vector(v):
    print('Nombre\tMesa\tOrganización\tMonto')
    for invitado in v:
        print(to_string(invitado))


def generar_archivo_ong(v,ong):
    fd = 'Donaciones' + str(ong)+ '.dat'
    m = open(fd,'wb')
    for invitado in v:
        if invitado.ong == ong:
            pickle.dump(invitado,m)
    m.close()


def sumar_recaudacion(ong):
    va = [0] * 13
    fd = 'Donaciones' + str(ong)+ '.dat'
    if os.path.exists(fd):
        m = open(fd,'rb')
        tot = os.path.getsize(fd)
        while m.tell() < tot:
            reg = pickle.load(m)
            va[reg.mesa] += reg.monto
    else:
        print('El archivo',fd,'no existe')
    return va


def main():
    v = leer_archivo('invitados.dat')
    opcion = -1
    while opcion!=0:
        print ('*' * 80)
        print('MENÚ GALA DE BENEFICENCIA')
        print('1. Listado completo de invitados')
        print('2. Invitados por ONG y por mesa')
        print('3. Invitado que realizó la mayor donación, para una cierta ONG')
        print('4. Generar archivo de ONG')
        print('5. Buscar archivo de ONG')
        print('0. Salir')
        opcion = int(input('Ingrese opción: '))
        if opcion == 1:
            mostrar_vector(v)
        elif opcion == 2:
            m = contar_invitados(v)
            mostrar_conteo(m)
        elif opcion == 3:
            ong = validar_entre(0,9,'Ingrese ONG: ')
            reg = buscar_mayor_donacion(v,ong)
        elif opcion == 4:
            ong = int(input('Ingrese ong:'))
            generar_archivo_ong(v,ong)
        elif opcion == 5:
            ong = int(input('Ingrese ong:'))
            va = sumar_recaudacion(ong)
            for i in range(len(va)):
                print('Mesa {:>3} $ {:>12.2f}'.format(i,va[i]))
        print ('*' * 80)

generar_archivo()

main()