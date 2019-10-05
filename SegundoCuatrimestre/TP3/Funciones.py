import random
from Registro import *

#Generando Datos Aleatoriamente
def generarArticulos(v):
    e = ("nuevo","usado")
    iden = 0
    for i in range(len(v)):
        iden += 1
        identificador = iden
        precio = random.randint(1, 100000)
        ubicacion = random.randint(0, 22)
        estado = random.choice(e)
        cantidad = random.randint(0, 100)
        puntuacion = random.randint(1, 5)
        v[i] = Articulo(identificador, precio, ubicacion, estado, cantidad, puntuacion)    

#Mostrando Todos los Datos de los articulos encontrados en el Vector v
def mostrarV(v):
    for i in range(len(v)):
        write(v[i])

#Punto 1-------------------------------------------------------------------------------------
def orderPorPrecio(v):
    for i in range(len(v) - 1):
        for j in range(i+1 , len(v)):
            if v[j].precio > v[i].precio:
                v[i] , v[j] = v[j] , v[i]
    mostrarV(v)

def articulosNuevos(v):
    an = []
    for i in range(len(v)):
        if v[i].estado == "nuevo":
            an.append(v[i])
    orderPorPrecio(an)

#Punto 2-------------------------------------------------------------------------------------
def articulosUsados(v):
    an = [0,0,0,0,0]
    for i in range(len(v)):
        if v[i].estado == "usado":
            an[v[i].puntuacion - 1] += 1
    for i in range(len(an)):
        if an[i] != 0:
            print("La Cantidad de articulos usados con una puntuacion de " + str(i+1) + " es de: " + str(an[i]))
    
#Punto 3-------------------------------------------------------------------------------------
def puntuacion(num):
    tupla = ('Muy Mala', 'Mala', 'Bueno', 'Muy Bueno', 'Exelente')
    return tupla[num]

def ubicacion(num):
    tupla = ("Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán")
    return tupla[num]

def mostrarMatriz(mat):
    ban = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:    #Filtro para que no aparezcan los 0
                if ban == False:
                    print(ubicacion(i))
                    ban = True
                print("Puntuacion", puntuacion(j),':', mat[i][j],'Articulos\n')
        ban = False

def distribucionGeografica(vec):
    mat = [[0]*5 for fila in range(23)]
    for i in range(len(vec)):
        fila = vec[i].ubicacion
        col = vec[i].puntuacion -1
        mat[fila][col] += vec[i].cantidad
    return mat

#Punto 4-------------------------------------------------------------------------------------
def tp(m,p):
    a = 0
    for i in range(len(m[0])):
        a += m[p][i]
    return a


def totalProvincial(v):
    ban = False
    tupla = ("Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán")
    
    for i in range(len(tupla)):
        print(str(i) + "-" + tupla[i])
    
    p = int(input("Ingrese una Provincia: "))
    
    for i in range(len(v)):
        if v[i].ubicacion == p:
            ban = True
    
    if ban:
        m = distribucionGeografica(v)
        t = tp(m,p)
        print("La Provincia " + tupla[p] + " Tiene un total de " + str(t) + " Articulos")
    else:
        print("No existe ningun articulo registrado en esa provincia")     

#Punto 5-------------------------------------------------------------------------------------
def usadosPrcioMayorPromedio(v,Promedio):
    b = False
    for i in range(len(v)):
        if v[i].precio >= Promedio and v[i].estado == "usado":
            if b == False:
                print("Los articulos usados que superan el precio pormedio anterior son:")
                b = True
            write(v[i])
    if b == False:
        print("No existen articulos usados que superen El precio promedio de todos los articulos registrados")

def promedioUsados(v):
    countcpu = 0
    tpu = 0
    for i in range(len(v)):
        if v[i].estado == "usado":
            countcpu +=1
            tpu += v[i].precio
    if countcpu != 0:
        ppu = tpu/countcpu
        print("Promedio de precios de los articulos usados: " + str(ppu))
        usadosPrcioMayorPromedio(v,ppu) 
    else:
        print("No hay articulos usados")

#Punto 6-------------------------------------------------------------------------------------
def compraIdeal(v):
    mc = (1,2)
    mpan = []
    b = False
    for i in range(len(v)):
        if v[i].estado == "nuevo" and v[i].puntuacion not in mc:
            mpan = v[i]
            b = True
            if v[i].precio < mpan.precio:
                mpan = v[i]
    if b:
        write(mpan)
    else:
        print("No existe un Articulo Nuevo que tenga una buena puntuacion")

#Punto 7-------------------------------------------------------------------------------------
def comprar(v):
    i = int(input("Ingrese el numero de identificacion del producto que desea comprar: "))
    e = False
    n = len(v)-1
    iz , d = 0 , n
    p = []
    while iz <= d:
        c = (iz + d)//2
        if i == v[c].identificador :
            p.append(v[c])
            e = True
            break
        elif i < v[c].identificador:
            d = c-1
        else:
            iz = c+1

    if e:
        cant = int(input("Ingrese la cantidad que desea comprar: "))
        while p[0].cantidad < cant:
            cant = int(input("Error! , la cantidad de productos disponibles es menor a: " + str(cant) +" Porfavor ingrese una cantidad menor a " + str(p[0].cantidad)+" :"))
        p[0].cantidad -= cant
        mostrarV(p)    

    else:
        print("El numero de identificacion del articulo que desea comprar no existe")
