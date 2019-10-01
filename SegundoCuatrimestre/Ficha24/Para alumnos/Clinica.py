__author__ = 'Karina'

import pickle
import os.path
import os


class Paciente:
    def __init__(self,historiaClinica, nombre, codigoEnfermedad,fechaVisita):
        self.hc = historiaClinica
        self.nombre=nombre
        self.codigoEnfermedad = codigoEnfermedad
        self.fechaVisita = fechaVisita

# Punto 1
# Los datos deben cargarse y almacenarse inicialmente en un arreglo de registros,
# a razón de un registro por paciente, el cual debe mantenerse en todo momento
# ordenado de menor a mayor de acuerdo al valor del número de historia clínica de los pacientes.

def cargarVectorOrdenado(n):

    p=[]
    for i in range(n):
        historiaClinica = validarMayorQue(0,'Ingrese HC: ')
        nombre = input('Ingrese nombre: ')
        nombre = nombre.ljust(20,' ')
        codigoEnfermedad = validarIntervalo(0,9,'Ingrese codigo enfermedad: ')
        fechaVisita = validarMayorQue(0,'Ingrese fecha: ')

        paciente = Paciente(historiaClinica,nombre,codigoEnfermedad,fechaVisita)
        insertarOrdenado(p,paciente)

    return p

def validarMayorQue(limite,mensaje):

    valor = int(input(mensaje))
    while valor<=limite:
        print('ERROR...')
        valor = int(input(mensaje))
    return valor

# intervalo con limite inferior y superior incluidos
def validarIntervalo(inferior,superior,mensaje):

    valor = int(input(mensaje))
    while valor<inferior or valor>superior:
        print('ERROR...')
        valor = int(input(mensaje))
    return valor

def insertarOrdenado(p,paciente):
    n=len(p)
    pos=n
    for i in range(n):
        if paciente.hc < p[i].hc:
            pos = i
            break
    p[pos:pos] = [paciente]

def to_string(paciente):
    print('Historia clinica: ', paciente.hc)
    print('Nombre: ',paciente.nombre)
    print('Fecha ultima visita: ', paciente.fechaVisita)
    print('Codigo enfermedad o problema: ', paciente.codigoEnfermedad)
    print()
    
def mostrarVector(p):
    n=len(p)
    for i in range(n):
        to_string(p[i])

# Punto 2
# Crear un archivo con todos los pacientes del vector cuyo nro de historia clinica sea mayor a x, donde x
# es un valor pasado por parametro

def crearArchivoPacientes(arch,vec, x):
        m = open(arch,'wb')
        n=len(vec)
        for i in range(n):
            if vec[i].hc> x:
                pickle.dump(vec[i],m)
        m.close()

# Punto 3
# Mostrar el archivo generado en el punto anterior.

def mostrarArchivo(arch):

    if not os.path.exists(arch):
        print('ERROR: Archivo inexistente!!')
        return

    t = os.path.getsize(arch)
    m = open(arch,'rb')
    while m.tell()<t:
        paciente = pickle.load(m)
        to_string(paciente)
    m.close()

# Punto 4
# Usando el archivo creado en el punto 2, crear en memoria
# otro arreglo que contenga los registros
# de los pacientes cuyo código de enfermedad sea 8 o 9.
# Recuerde: debe crear otro arreglo de registros,
# y no eliminar ni modificar el original que se creó en el punto 1.

def generarVectorDesdeArchivo(arch):
    aux=[]
    if not os.path.exists(arch):
        print('ERROR: Archivo inexistente!!')
        return
    t = os.path.getsize(arch)
    m = open(arch,'rb')
    while m.tell()<t:
        paciente = pickle.load(m)

        if paciente.codigoEnfermedad ==8 or paciente.codigoEnfermedad==9:
            aux.append(paciente)

    m.close()
    return aux


# Punto 5
# A partir del archivo creado en el punto 2, determinar la
# cantidad de pacientes que visitaron la clínica por cada
# tipo de enfermedad o problema.

def generarVectorDeConteo(arch):

    if not os.path.exists(arch):
        print('ERROR: Archivo inexistente!!')
        return
    vec = [0]*10
    t = os.path.getsize(arch)
    m = open(arch,'rb')
    while m.tell()<t:
        paciente = pickle.load(m)
        indice = paciente.codigoEnfermedad
        vec[indice]+=1
    m.close()
    return vec

def mostrarVectorConteo(vec):
    n=len(vec)
    for i in range(n):
        print('Cantidad pacientes codigo enfermedad o problema ',i,' : ',vec[i])

def main():
    FD = 'pacientes.med'
    p, p2 = [], []
    op = 0
    while op != 6:
        print('Consultorio Dr. Matasanos')
        print(' 1. Registrar pacientes en forma ordenada')
        print(' 2. Creación de un archivo con hc mayor a x')
        print(' 3. Mostrar el archivo')
        print(' 4. Creación de arreglo a partir del archivo (pacientes con código 8 o 9)')
        print(' 5. Cantidad de pacientes por código de enfermedad o problema')
        print(' 6. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            n= validarMayorQue(0,'Ingrese cantidad de pacientes: ')
            p = cargarVectorOrdenado(n)
            mostrarVector(p)
        elif op == 2:
            x = validarMayorQue(0,'Ingrese hc para comparar: ')
            crearArchivoPacientes(FD,p,x)
        elif op == 3:
            mostrarArchivo(FD)
        elif op == 4:
            p2=generarVectorDesdeArchivo(FD)
            mostrarVector(p2)
        elif op == 5:
            vec=generarVectorDeConteo(FD)
            mostrarVectorConteo(vec)
        elif op == 6:
            pass

# script principal...
if __name__ == '__main__':
    main()