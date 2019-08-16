from Registro import *

def contarApuestas(vector, caballo):
    contar = 0
    for apuesta in vector:
        if apuesta.caballo == caballo :
            contar += 1
    return contar

def buscar(vector, numero):
    pos = -1
    for i in range(len(vector)):
        if vector[i].numero == numero:
            pos = i
            break
    return pos

def acumularPorCaballo(vector):
    v = [0]*10
    for apuesta in vector:
        v[apuesta.caballo] += apuesta.monto
    return v


def validarEntre(mensaje, li, ls):
    valor = int(input(mensaje))
    while valor < li or valor > ls:
        print('Error ! Debe ingresar un valor en el rango que se pide [', li, ':', ls,']')
        valor = int(input(mensaje))

    return valor

def validarMayor(mensaje):
    valor = int(input(mensaje))
    while valor < 0:
        print('Error !! El valor a ingresar debe ser mayor a 0')
        valor = int(input(mensaje))
    return None

def cargarVector(vector):
    for i in range(len(vector)):
        #Cargar la info
        numero = validarMayor('Ingrese numero Ticket: ')
        caballo = validarEntre('Ingrese caballo', 0,9)
        monto = float(input('Ingrese monto: '))

        #Generar registro
        apuesta = Apuesta ()
        #Asignar
        vector[i] = apuesta


def principal ():
    n = validarMayor('Ingrese la cantidad de apuestas: ')
    vector = [None] * n
    cargarVector(vector)
    opcion = -1
    while opcion != 0:
        print('MENU DE OPCIONES')
        print('*' * 100)
        print('1- Monto total: ')
        print('2- Buscar ticket')
        print('3- Cantidad apuestas')
        print('4- Mostrar ticket')
        print('0- Salir')
        opcion = int(input('Ingrese su opcion:'))

        if opcion == 1:
            va = acumularPorCaballo (vector)
            for i in range(len(va)):
                print('Caballo', i,'total de apuesta $', va[i])
        elif opcion == 2:
            numero = validarMayor('Ingrese numero de Ticket: ')
            #BUSQUEDA SECUENCIAL
            pos = buscar(vector, numero)
            if pos == -1:
                print('No hay apuesta con ese numero')
            else:
                apuesta = vector [pos]
                apuesta.monto *= 10
                write(apuesta)
        elif opcion == 3:
            caballo = validarEntre('Ingrese caballo: ', 0,9)
            cantidad = contarApuestas(vector, caballo)
            print('La cantidad de apuestas del caballo', caballo)
principal()