import random , pickle , os
from Registro import *
from Archivos import *
from datetime import *

#Generando Datos Aleatoriamente
def generarArticulos(v):
    e = ("nuevo","usado")
    iden = 0
    for i in range(len(v)):
        iden += 1
        identificador = iden
        precio = round(random.uniform(1, 100000),2)
        ubicacion = random.randint(0, 22)
        estado = random.choice(e)
        cantidad = random.randint(1, 100)
        puntuacion = random.randint(1, 5)
        v[i] = Articulo(identificador, precio, ubicacion, estado, cantidad, puntuacion)

#Mostrando Todos los Datos de los articulos encontrados en el Vector v
def mostrarV(v):
    for i in range(len(v)):
        writeArticulo(v[i])

#Validando valores dentro de un intervalo
def validarEntre(men, mini, may):
    num = int(input(men))
    while num <= mini or num > may:
        print("ERROR!. numero invalido.")
        num = int(input(men))
    return num

#Buscando un Articulo por ID
def buscarPorIdentificador(v, id):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if id == v[c].identificador:
            return c
        elif id < v[c].identificador:
            der = c - 1
        else:
            izq = c + 1
    return -1

#Punto 1-------------------------------------------------------------------------------------

def comprar(art):
    fecha = str(date.today())
    envio = False
    adicional = 0
    cant = validarEntre("Ingrese la cantidad que desea comprar: ", 0 , art.cantidad)
    art.cantidad -= cant
    montoTotal = round(art.precio * cant, 2)
    print("Articulo Actualizado")
    writeArticulo(art)
    print("Elija una opcion:\n","1-Envio a Domicilio(10% de recargo)\n","2-Retiro por sucursal")
    env = int(input())
    while env < 1 or env > 2:
        print("La opcion ingresada no es valida")
        env = int(input())
    if env == 1:
        envio = True
        adicional = round(art.precio // 100 * 10 , 2)
        montoTotal += adicional
    return cant, envio, montoTotal, fecha, adicional

def validarStock(v, art, abc, atc, a):
    if v[art].cantidad == 0:
        print("Articulo Encontrado: ")
        writeArticulo(v[art])
        print("El Articulo No dispone de stock en este momento.")
    else:
        print("Articulo Encontrado")
        writeArticulo(v[art])
        cantidad, envio, montoTotal, fecha, adicional = comprar(v[art])
        compra = Compra(v[art].identificador, cantidad, v[art].precio, envio, montoTotal, fecha)
        guardadoBinario(abc, compra)
        guardadoTexto(atc, v[art], fecha, montoTotal, adicional, cantidad)
        a = True
        print("\nEl Monto Total a pagar es de: $", montoTotal)
        if adicional != 0:
            print("Costo adicional por envio: $", adicional)
    return a        

#Punto 2-------------------------------------------------------------------------------------

def intervaloFechas(abc):
    mensaje = "Ingrese el Rango de fechas de las compras que a realizado en el formato: '(AAAA-MM-DD)'." 
    print(mensaje)
    fechaMin = input('Desde: ')
    fechaMay = input('Hasta: ')
    while len(fechaMin) != 10 or len(fechaMay) != 10 or fechaMin > fechaMay:
        if fechaMin > fechaMay:
            print("ERROR!. La Fecha Minima es mayor que la Fecha Mayor")
            print(mensaje)
            fechaMin = input('Desde: ')
            fechaMay = input('Hasta: ')
        else:
            print("ERROR!. El formato Ingresado es invalido")
            print(mensaje)
            fechaMin = input('Desde: ')
            fechaMay = input('Hasta: ')
    mostrarIntervaloFecha(abc, fechaMin, fechaMay)    

#Punto 3-------------------------------------------------------------------------------------

def mostrarVR(v,men,may):
    for i in range(len(v)):
        if v[i].precio > men and v[i].precio < may:
            writeArticulo(v[i])


def rangoPrecio(men,may):
    pMin = float(input("Ingrese un precio minimo para establecer un nuevo rango entre:" + str(men) + " y " + str(may) + ": "))
    while pMin < men or pMin > may:
        print("ERROR!. 'El precio ingresado debe estar entre:' " + str(men) + " y " + str(may))
        pMin = float(input("Ingrese un precio minimo para establecer un nuevo rango entre:" + str(men) + " y " + str(may)+ ": "))

    pMay = float(input("Ingrese un precio maximo para establecer un nuevo rango entre:" + str(pMin) + " y " + str(may)+ ": "))
    while pMay < pMin or pMay > may:
        print("ERROR!. 'El precio ingresado debe estar entre:' " + str(pMin) + " y " + str(may))
        pMay = float(input("Ingrese un precio maximo para establecer un nuevo rango entre:" + str(pMin) + " y " + str(may)+ ": "))

    return pMin , pMay


def menYMay(v):
    n = len(v)
    men = v[0].precio
    may = v[0].precio
    for i in range(n):
        if v[i].precio < men:
            men = round(v[i].precio,2)
        if v[i].precio > may:
            may = round(v[i].precio,2)
    rango = rangoPrecio(men,may)
    mostrarVR(v,rango[0],rango[1])


#Punto 4-------------------------------------------------------------------------------------

def agregarFavorito(articulo, v):
    n = len(v)
    id = articulo.identificador
    num = buscarPorIdentificador(v, id)
    if n == 0:
        v.append(articulo)
    elif num == -1:
        p = n
        izq, der = 0, n - 1
        while izq <= der:
            c = (izq + der) // 2
            if v[c].identificador == id:
                p = c
                break
            if id < v[c].identificador:
                der = c - 1
            else:
                izq = c + 1
            if izq > der:
                p = izq
        v[p:p] = [articulo]
    else:
        print("\nEl articulo ya esta entre tus favoritos.")

#Punto 5-------------------------------------------------------------------------------------

def actualizarFavoritos(abf,fav):
    if os.path.exists(abf):
        for i in range(len(fav)):
            agregarBinario(abf, fav[i])
    else:
        for i in range(len(fav)):
            guardadoBinario(abf, fav[i])

