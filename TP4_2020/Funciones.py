from Registro import *
import random
import pickle

#Funciones Auxiliares------------------------------------------------------------------------------------------------------------------------------------------------

def validar_may_que(min, mensaje):
    num = min - 1
    while num < min:
        num = int(input(mensaje))
        if num < min:
            print("Error")
    return num

def arch_csv():
    n = validar_may_que(0,"Ingrese cantidad de temas: ")
    var = ""
    archivo = open("musica.csv", "w")
    for _ in range(n):
        var += regist_arch()
    archivo.write(var)
    print("El archivo se ha creado")
    archivo.close()

def regist_arch():
    text = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
    return random.choice(text) + random.choice(text) + random.choice(text) + random.choice(text) + "," + str(random.randint(0, 5)) + "," + str(random.randint(0, 4)) + "\n"


def add_in_order(vector, registro):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].titulo == registro.titulo:
            pos = med
            break

        if registro.titulo < vector[med].titulo:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]

def mostrarVector(v):
    for i in range(len(v)):
        write(v[i])

def validMen(n,x,t1,t2):
    while n > x:
        print(t2)
        n = int(input(t1))
    return n

def validarEntre(x,i,s,t1,t2):
    while i > x or x > s:
        print(t1)
        x = int(input(t2))
    return x

#Punto1----------------------------------------------------------------------------------------------------------------------------------------------------------------

def cargar_reg():
    archivo = open("musica.csv", "r")
    mus = []
    for linea in archivo:
        lin = linea.replace("\n","")
        tuple = lin.split(",")
        musica = Tema(tuple[0],tuple[1],tuple[2])
        add_in_order(mus, musica)
    archivo.close()
    return mus

#Punto2----------------------------------------------------------------------------------------------------------------------------------------------------------------

def nuevoVector(v):
    nv = []

    t1 = "Ingerese la cantidad de temas de la lista existente a guardar en un nuevo vector: "
    n = int(input(t1))
    x = len(v)
    t2 = ("La cantidad de canciones a guardar en la nueva lista debe ser menor o igual a " + str(x))
    validMen(n,x,t1,t2)

    t3 = "Debe Ingresar Un valor Entre 0 y 5"
    t4 = ("Ingerese el numero del tipo de Genero que desea guardar en el nuevo vector: \n"
                    "0 = Balada"" \n"
                    "1 = Pop"" \n"
                    "2 = Rock"" \n"
                    "3 = Folclore"" \n"
                    "4 = Electronica"" \n"
                    "5 = Otras"" \n")
    g = int(input(t4))
    validarEntre(g,0,5,t3,t4)

    for i in range(x):
        if v[i].genero == str(g):
            nv.append(v[i])

    cant = len(nv)

    if cant < n:
        print("Se cargaron " + str(cant) + " temas debido a que no se encontraron " + str(n) + " temas del genero Elegido")
    
    return nv
    
#Punto3----------------------------------------------------------------------------------------------------------------------------------------------------------------

def genero(n):
    tupla = ("Balada","Pop","Rock","Folclore","Electorinica","Otro")
    return tupla[n]

def idioma(n):
    tupla = ("Español","Ingles","Frances","Portuges","Otros")
    return tupla[n]

def mostrarMatriz(m):
    ban = False
    for fila in range(len(m)):
        for col in range(len(m[0])):
            if m[fila][col] != 0:
                if ban == False:
                    print("Genero: ", genero(fila))
                    ban = True
                print("idioma " , idioma(col), ": ", m[fila][col] , "Temas\n" )
        ban = False

def matrizConteo(v):
    m = [[0] * 5 for i in range(6)]
    for i in range(len(v)):
        fila = int(v[i].genero)
        col = int(v[i].idioma) 
        m[fila][col] += 1

    return m
#Punto4----------------------------------------------------------------------------------------------------------------------------------------------------------------

def cantTem(m,n):
    cant = 0
    for fila in range(len(m)):
        for col in range(len(m[0])):
            if m[fila][col] != 0:
                if col == n:
                    cant += m[fila][col]
    return cant

def cantTemPorIdiom(m):
    t1 = "Debe Ingresar Un valor Entre 0 y 4"
    t2 = ("Ingerese de que idioma desea saber la cantidad de temas que hay de ese idioma: \n"
                    "0 = Español"" \n"
                    "1 = Ingles"" \n"
                    "2 = Frances"" \n"
                    "3 = Portugues"" \n"
                    "4 = Otros"" \n")
    n = int(input(t2))
    validarEntre(n,0,4,t1,t2)

    c = cantTem(m,n)

    print("Hay una cantidad de: " + str(c) + " temas con idioma " + idioma(n))

#Punto5----------------------------------------------------------------------------------------------------------------------------------------------------------------

def verfExist(v):
    ban = False
    t = input("Ingrese el titulo del tema que desea buscar en la lista: ")
    t = t.upper()
    tem = ()

    for i in range(len(v)):
        if v[i].titulo == t:
            tem = v[i]
            ban = True
            break

    return ban , tem

#Punto5----------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscarGenero(g,t1,t2):
    b = False 
    tG=["Balada","Pop","Rock","Folclore","Electronica","Otros"]
    while not b:
        for i in range(len(tG)):
            if tG[i] == g:
                b = True
                break
        if not b:
            print(t2)
            g = input(t1)
        else:
            break
    return i

def buscarTemasDelGenero(g,v):
    vn = []
    for i in range(len(v)):
        if v[i].genero == str(g):
            vn.append(v[i])
    return vn

def bGenero():
    t1 = ("Ingrese el NOMBRE del Genero de canciones que desea guardar en el archivo nuevo:  \n"
                    "1- Balada"" \n"
                    "2- Pop"" \n"
                    "3- Rock"" \n"
                    "4- Folclore"" \n"
                    "5- Electronica"" \n"
                    "6- Otros"" \n")
    t2 = "El Genero ingresado no se a Encontrado en la lista de generos Existentes. Porfavor ingrese Un genero de la lista de abajo."
    g = input(t1)
    nG = buscarGenero(g,t1,t2)
    return nG

def generarArchBin(v):
    b = True
    nG = bGenero()
    print(nG)
    vT = buscarTemasDelGenero(nG,v)
    print(len(vT))
    while len(vT) == 0:
        r = input("No se encontraron temas guardados con el genero solicitado \n"
                "Desea buscar un Nuevo Genero? s/n: ")
        if r == "s":
            nG = bGenero()
            vT = buscarTemasDelGenero(nG,v)
        elif r == "n":
            b = False
            break
        else:
            print("Respuesta no Valida, Debe Inrgesar \n " "s ---> Si \n" "n ---> No")

    if b:
        archivo = open("MusicaGenerox.dat", "wb")
        for i in range(len(vT)):
            pickle.dump(vT[i],archivo)
        archivo.close()
        return "Se genero el archivo MusicaGenerox.dat con los Temas que tenian el Genero solicitado"
    else:
        return "No se a podido generar un nuevo archivo con temas del genero solicitado."