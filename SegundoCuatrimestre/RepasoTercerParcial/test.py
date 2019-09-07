
#Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar la información
# referida a los n alquileres de la temporada estival en un arreglo de registros
# (cargar n por teclado). Por cada alquiler, se pide guardar el nombre y dni de la persona
# que hizo la reserva, monto del alquiler y un código entre 0 y 9 que indica el tipo de cabaña
# alquilada (suponiendo que por ejemplo, el 0 indica que se alquiló una cabaña de tipo Común, el 1
# Premiun, el 2 Super Premiun, y así hasta el código 9).

#Se pide desarrollar un programa en Python controlado por un menú de opciones. Ese menú debe permitir
# gestionar las siguientes tareas a partir del arreglo pedido en el párrafo anterior, siempre usando
# funciones que acepten parámetros y/o retornen valores en cada situación en que se considere apropiado:

#1 cargar el arreglo de alquileres. Validar que el código de tipo de cabaña esté efectivamente entre
# 0 y 9. (no realizar otra validación más que la solicitada).

#2Determinar la cantidad de alquileres que registraron un monto mayor a x, siendo x
# un valor pasado por parámetro.


#4Mostrar los datos de todos los alquileres en orden de mayor a menor por el dni de las
# personas que realizaron la reserva.

#5Mostrar un informe con todos los alquileres que registraron el menor monto
# (note que podría haber más de un alquiler con el mismo monto menor).

# 6-buscar por n (por teclado) monto y si esta, permitir cambiar mo y
# si no esta, permitir agregar

#7-filtrar obras con el mayor del monto  menor a x (cargado por teclado)
# y mostar ordenado por codigo

#8- ordenar un vector aux segun el tipo

#buscar si existe un monto y si existe, incrementarlo un 15%

#8:52

import random
class Alquileres:
    def __init__(self,nom,dni,mon,cod):
        self.nombre = nom
        self.dni = dni
        self.monto = mon
        self.codigo = cod

def crear_aleatorio():
    nombre = random.choice(['mica','carlos','omar','juan','marta','vale','lito'])
    dni = random.randint(40,100)
    monto = round(random.random()*10000+10000,2)
    codigo = random.randint(0,9)
    return Alquileres(nombre, dni,monto,codigo)

def to_string(Alquileres):
    print('-Nombre' + str(Alquileres.nombre)+ ' ''-DNI:' +str(Alquileres.dni) + ' ''-Monto:' +
           str(Alquileres.monto) + ' ''-Codigo:' + str(Alquileres.codigo))

def mostrar(vec):
    n = len(vec)
    for i in range(n):
        print(to_string(vec[i]))

def vector():
    n = int(input('ingresar la cantidad de alquileres'))
    vec = n * [None]
    for i in range(n):
        vec[i] = crear_aleatorio()
    return vec

def menu():
    print('MENU DE OPCIONES')
    print('1- Cargar los datos de los alquileres y mostralos')
    print('2- determinar la cantidad de alquileres de monto mayor a x')
    print('3- mostrar los datos de los alquileres ordenados de mayor a menor segun el dni')
    print('4- mostrar un informe con los registros que tuvieron el menor monto')
    print('5- buscar un monto determinado')
    print('6- filtrar alquileres con un tipo menor a x y mostrarlo ordenado por dni de menor a mayor')
    print('7- ordenar un vector auxiliar segun el tipo de men a mayor')
    print('8- buscar si existe un monto x, en el caso de que exista, aumentarlo un 15%')
    print('9- salir')

def alquiler_may_monto(vec):
    x = int(input('ingresar un monto:'))
    n = len(vec)
    cont= 0
    for i in range(n):
        if vec[i].monto >  x:
            cont += 1
    print('la cantidad de alquileres de montos mayores al ingresado son:',cont)

def ordenar(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range (i+1,n):
            if vec[i].dni < vec[j].dni:
                vec[i], vec[j] = vec[j], vec[i]
    return vec

def validar_codigo():
    cod = int(input('ingresar un codigo entre 0 y 9'))
    while cod <0 or cod> 9:
        print('el codigo ingresado es incorrecto')
        cod = int(input('volver a ingresar el codigo'))
    return cod

def buscar_monto(vec):
    x = float(input('ingresar un monto'))
    n = len(vec)
    band_encontrado = False
    for i in range(n):
        if vec[i].monto == x:
            band_encontrado = True
            vec[i].monto = float(input('ingresar un nuevo monto'))
        else:
            if band_encontrado == False:
                vec[i].nombre = str(input('ingresar un nombre'))
                vec[i].dni = int(input('ingresar un nuevo DNI'))
                vec[i].monto = x
                vec[i].codigo = validar_codigo()
                break
    return vec

def filtro(vec):
    tip = int(input('ingresar un tipo de alquiler'))
    n = len(vec)
    vec_filtro = []
    for i in range(n):
        if vec[i].codigo < tip:
            vec_filtro.append(vec[i])
    return vec_filtro

def ordenar_dni(vec_filtro):
    n = len(vec_filtro)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec_filtro[i].dni > vec_filtro[j].dni:
                vec_filtro[i], vec_filtro[j] = vec_filtro[j], vec_filtro[i]
    return vec_filtro

def ordenar_aux(vec):
    n= len(vec)
    vector_aux = []
    for r in vec:
        vector_aux.append(r)
    for i in range(n-1):
        for j in range(i+1,n):
            if vector_aux[i].codigo > vector_aux[j].codigo:
                vector_aux[i],vector_aux[j] = vector_aux[j], vector_aux[i]
    return vector_aux

def buscar_monto_aumentar(vec):
    x  = float(input('ingresar el monto que se desea buscar'))
    n = len(vec)
    band_monto = False
    for i in range(n):
        if vec[i].monto == x:
            vec[i]. monto += (vec[i].monto)* 0.15
            band_monto = True
            mostrar(vec)
            break
    if band_monto == False:
        print('no se encontro el monto buscado')

def menor_monto(vec):
    n =len(vec)
    men = [None]
    for i in range(n):
        if i ==0:
            men = vec[i]
        elif vec[i].monto < men.monto:
            men = vec[i]
    return men

def test():
    VECTOR= None
    menu()
    opc = int(input('ingrese una opcion'))
    while opc != 9:
        if opc == 1:
            VECTOR = vector()
            mostrar(VECTOR)
        elif VECTOR!= None:
            if opc == 2:
                monto_may = alquiler_may_monto(VECTOR)
            elif opc == 3:
                orden = ordenar(VECTOR)
                mostrar(VECTOR)
            elif opc == 4:
                menor = menor_monto(VECTOR)
                to_string(menor)
            elif opc == 5:
                busq_monto= buscar_monto(VECTOR)
                mostrar(VECTOR)
            elif opc == 6:
                filtrado= filtro(VECTOR)
                ord_dni =  ordenar_dni(filtrado)
                mostrar(ord_dni)
            elif opc == 7:
                aux = ordenar_aux(VECTOR)
                mostrar(aux)
                print('='*50)
                mostrar(VECTOR)
            elif opc == 8:
                busq_monto_aum = buscar_monto_aumentar(VECTOR)
        elif VECTOR == None:
            print('la opcion ingresada es incorrecta, primero se debe ingresar la opcion N1')
        menu()
        opc = int(input('ingrese una opcion'))
    if opc == 9:
        print('Hasta luego!!')

if __name__ == '__main__':
    test()