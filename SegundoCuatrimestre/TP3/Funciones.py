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
def agruparPorPuntuacion(v):
    app = [0] * 5
    for i in range(len(v)):
        app[v[i].puntuacion - 1] += 1 

    for i in range(len(app)):
        if app[i] != 0:
            print("La Cantidad de articulos usados con una puntuacion de " + str(i+1) + " es de: " + str(app[i]))

def articulosUsados(v):
    an = []
    for i in range(len(v)):
        if v[i].estado == "usado":
            an.append(v[i])
    a = agruparPorPuntuacion(an)
    
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
    apmpu = []
    for i in range(len(v)):
        if v[i].precio >= Promedio and v[i].estado == "usado":
            apmpu.append(v[i])
    if len(apmpu) != 0:
        print("Los articulos usados que superan el precio pormedio anterior son:")
        mostrarV(apmpu)
    else:
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
    l = 0
    b = False
    for i in range(len(v)):
        if v[i].estado == "nuevo" and v[i].puntuacion not in mc:
            mpan = v[i]
            l = i
            b = True
            break
    if b:
        for i in range(l, len(v)):
            if v[i].estado == "nuevo" and v[i].precio < mpan.precio and v[i].puntuacion not in mc:
                mpan = v[i]
                lug = i
        write(mpan)
    else:
        print("No existe un Articulo Nuevo que tenga una buena puntuacion")

#Punto 7-------------------------------------------------------------------------------------
def comprar(v):
    i = int(input("Ingrese el numero de identidicacion del producto que desea comprar: "))
    e = False
    p = []
    for a in range(len(v)):
        if v[a].identificador == i:
            p.append(v[a])
            e = True
            break
    if e:
        c = int(input("Ingrese la cantidad que desea comprar: "))
        while p[0].cantidad < c:
            c = int(input("Error! , la cantidad de productos disponibles es menor a: " + str(c) +" Porfavor ingrese una cantidad menor a " + str(p[0].cantidad)+" :"))
        p[0].cantidad -= c
        mostrarV(p)    

    else:
        print("El numero de identificacion del articulo que desea comprar no existe")
