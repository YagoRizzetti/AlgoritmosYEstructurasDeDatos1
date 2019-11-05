from Registro import *
import random
import os
import pickle

def validarMayorQue(mensaje,n,lim):
    while n <= lim:
        print("ERROR. Numero Invalido!")
        n = int(input(mensaje))
    return n

def validarEntre(mensaje,num,liminf,limsup):
    while num < liminf or num > limsup:
        print("ERROR. Numero Invalido!")
        num = int(input(mensaje))
    return num

def guardarLimInf(li,proxliminf):
    m = open(li,"w")
    m.write(str(proxliminf))
    m.close()

def leerUltLimInf(li):
    m = open(li,"r")
    lim = m.read()
    m.close()
    return lim

#Punto 1---------------------------------------------------------------------------------------------------


def cargaAutomatica(v,nombresRegistrados,ultLimInf):
    nombres = ("Juan","Maria","Pedro","Julia","Micaela","Giuliana","Gabriel","Nicolas","Mariano","Lucia","Diegote") 
    for i in range(len(v)):
        dni = int(ultLimInf) + i + 1
        nombre = random.choice(nombres).lower()
        nombresRegistrados[i] = nombre
        importe = round(random.uniform(100, 5000), 2)
        afiliacion = random.randint(0,4)
        trabajo = random.randint(0,14)
        v[i] = Profesional(dni,nombre,importe,afiliacion,trabajo)


def cargaManual(v,nombresRegistrados,ultLimInf,proxliminf):
    liminf = ultLimInf
    for i in range(len(v)):
        n = int(input("Ingrese El Numero de DNI del Miembro " + str(i+1) + " debe ser mayor a " + str(ultLimInf) + ": \n-->"))
        dni = validarMayorQue("Ingrese El Numero de DNI del Miembro" + str(i+1) + " debe ser mayor a " + str(ultLimInf) + ": \n-->",n,int(ultLimInf))
        liminf = dni
        
        nombre = input("Ingrese Un Nombre: \n-->").lower()
        nombresRegistrados[i] = nombre

        imp = float(input("Ingrese los Ingresos Mensuales: \n-->"))
        importe = validarMayorQue("Ingrese los Ingresos Mensuales: \n-->",imp, 0)
        
        afi = int(input("Ingrese el tipo de afiliacion: \n0-hola \n1-chau \n2-je \n3-ji \n-->"))
        afiliacion = validarEntre("Ingrese el tipo de afiliacion: \n0-hola \n1-chau \n2-je \n3-ji \n-->",afi,0,3)
        
        trab = int(input("El tipo de Trabajo: \n0-a \n1-b \n2-c \n3-d \n4-e \n5-f \n6-g \n-->"))
        trabajo = validarEntre("El tipo de Trabajo: \n0-a \n1-b \n2-c \n3-d \n4-e \n5-f \n6-g \n-->",trab,0,6)
        v[i] = Profesional(dni,nombre,importe,afiliacion,trabajo)
    proxliminf = liminf
    return proxliminf

#Punto 2---------------------------------------------------------------------------------------------------

def mostrarVector(v):
    for i in range(len(v)):
        writeProfesional(v[i])

#Punto 3---------------------------------------------------------------------------------------------------

def crearArchivo(v,impmin,ab):
    if os.path.exists(ab):
        m = open(ab,"ab")
        for i in range(len(v)):
            if v[i].trabajo == 3 or v[i].trabajo == 4 or v[i].trabajo == 5 and v[i].importe > impmin:
                pickle.dump(v[i],m)

    else:
        m = open(ab,"wb")
        for i in range(len(v)):
            if v[i].trabajo == 3 or v[i].trabajo == 4 or v[i].trabajo == 5 and v[i].importe > impmin:
                pickle.dump(v[i],m)
    print("Datos cargados al archivo: ", ab)
    m.close()


#Punto 4---------------------------------------------------------------------------------------------------

def verRegistrosDelArchivo(ab):
    if os.path.exists(ab):
        m = open(ab,"rb")
        t = os.path.getsize(ab)
        while m.tell() < t:
            line = pickle.load(m)
            writeProfesional(line)
        m.close()
    else:
        print("No Hay Ningun Archivo Generado")    

#Punto 5---------------------------------------------------------------------------------------------------

def buscarPorNombre(v,nombresRegistrados):
    print("Ingrese Un Nombre que se encuentre Dentro de los Siguientes Nombres Registrados :" )
    for i in range(len(nombresRegistrados)):
            if i != (len(nombresRegistrados)-1):
                print(nombresRegistrados[i] , end=" - ")
            else:
                print(nombresRegistrados[i])
    nom = input("\n-->").lower()
    while nom not in nombresRegistrados:
        print("ERROR. El Nombre Ingresado No Esta Registrado \nPruebe Ingresando uno de los siguientes nombres:")
        for i in range(len(nombresRegistrados)):
            if i != (len(nombresRegistrados)-1):
                print(nombresRegistrados[i] , end=" - ")
            else:
                print(nombresRegistrados[i])
        nom = input("\n-->").lower()
    print("Se Mostrara El primer Registro que se encuentre con el nombre: ", nom)
    for i in range(len(v)):
        if nom == v[i].nombre:
            writeProfesional(v[i])
            break
#Punto 6---------------------------------------------------------------------------------------------------

def afiliacion(n):
    tupla = ("a","b","c","d","e")
    return tupla[n]

def trabajo(n):
    tupla = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ")
    return tupla[n]

def mostrarMatriz(m):
    ban = False
    for fila in range(len(m)):
        for col in range(len(m[0])):
            if m[fila][col] != 0:
                if ban == False:
                    print("Afiliacion: ", afiliacion(fila))
                    ban = True
                print("Trabajo " , trabajo(col), ": ", m[fila][col] , "Profesionales\n" )
        ban = False

def matrizConteo(v):
    m = [[0] * 15 for i in range(5)]
    for i in range(len(v)):
        fila = v[i].afiliacion
        col = v[i].trabajo 
        m[fila][col] += 1
    
    mostrarMatriz(m)