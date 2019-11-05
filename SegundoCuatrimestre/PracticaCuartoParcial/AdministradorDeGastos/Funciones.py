from Registro import *
import random, os, pickle

def validarEntre(m,n,inf,sup):
    while n < inf or n > sup:
        print("ERROR. Numero Invalido! \n intente Ingresando un numero entre: " + str(inf) + " y " + str(sup))
        n = int(input(m))
    return n

def validarMayorQue(m,n,inf):
    while n < inf:
        print("ERROR. Numero Invalido! \n Intente Ingresando un numero Mayor a: " + str(inf))
        n = int(input(m))
    return n

#Punto 1 --------------------------------------------------------------------------------------------------

def generarRegistros(v):
    desc =  ("hola", "chau", "gabi", "nico", "facu", "damian", "tumi")
    for i in range(len(v)):
        codigo = i + 1
        descripcion = random.choice(desc)
        mes = random.randint(1,12)
        sucursal = random.randint(0,2)
        importe = round(random.uniform(1000,10000),2)
        v[i] = Gasto(codigo,descripcion,mes,sucursal,importe)

#Punto 2 --------------------------------------------------------------------------------------------------

def mostrarRegistros(v):
    for i in range(len(v)):
        writeGasto(v[i])

#Punto 3 --------------------------------------------------------------------------------------------------

def generarArchivo(v,imp,arc):
    b = False
    res = ("s","n")
    if os.path.exists(arc):
        r = input("Hay un archivo ya generado con gastos desea sobreescribirlo? S/N: \n -->").lower()
        while r not in res:
            r = input("Hay un archivo ya generado con gastos desea sobreescribirlo? S/N: \n -->").lower()
        if r == "n":
            b = True

    if b == False:
        m = open(arc,"wb")
        for i in range(len(v)):
            if v[i].importe > imp:
                pickle.dump(v[i],m)
        m.close()

    else:
        print("El Archivo No se a modificado")

#Punto 4 --------------------------------------------------------------------------------------------------

def verRegistrosArchivo(arc):
    if os.path.exists(arc):
        m = open(arc,"rb")
        t = os.path.getsize(arc)
        while m.tell() < t:
            line = pickle.load(m)
            writeGasto(line)
        m.close()

    else:
        print("No Hay Ningun Archivo Creado")

#Punto 5 --------------------------------------------------------------------------------------------------

def sucursal(pos):
    tupla = ("Sucursal 1", "Sucursal 2", "Sucursal 3")
    return tupla[pos]

def mes(pos):
    tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    return tupla[pos]

def mostrarMatriz(mat):
    ban = False
    for fila in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[fila][col] != 0:
                if ban == False:
                    print(mes(col),"\n")
                    ban = True
                print("La Sucursal: " , sucursal(fila) , "\n Gasto un total de: " , mat[fila][col])

        ban = False

def matrizAcu(arc,mat):
    if os.path.exists(arc):
        m = open(arc,"rb")
        t = os.path.getsize(arc)
        while m.tell() < t:
            reg = pickle.load(m)
            fila = reg.sucursal
            col = reg.mes - 1
            mat[fila][col] += reg.importe
        m.close()
        mostrarMatriz(mat)

    else:
        print("No Hay Ningun Archivo Creado")

#Punto 6 --------------------------------------------------------------------------------------------------

def totalizarGastosDeUnMes(mat):
    total = 0
    m = "Elija el mes que quiere ver el total de gastos: \n1-Enero \n2-Febrero \n3-Marzo \n4-Abril \n5-Mayo \n6-Junio \n7-Julio \n8-Agosto \n9-Septiembre \n10-Octubre \n11-Noviembre \n12-Diciembre \n-->"
    me = int(input(m))
    validarEntre(m,me,1,12)
    for fila in range(len(mat)):
        for col in range(len(mat[0])):
            if col + 1 == me:
                total += mat[fila][col]
                break
    me = str(mes(me-1))
    print("En El mes "+ me + "El Gasto Total fue de: " + str(total)) 