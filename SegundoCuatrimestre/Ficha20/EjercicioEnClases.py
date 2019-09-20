'''
DESARROLLAR UNA FUNCION QUE INFORME LA CANTIDAD DE PAQUETES VENDIDOS POR TIPO DE PAQUETE Y TIPO DE CLIENTE. SE PIDE
MOSTRAR EL RESULTADO EN FORMA DE LISTA SOLO PARA AQUELLAS CANTIDADES MAYORES A 0. SE DEBE MOSTRAR LA DESCRIPCION DEL
TIPO DE PAQUETE Y TIPO DE CLIENTE (NO LOS CODIGOS)
'''


import random

class Paquete:
    def __init__(self,numero,descripcion,paquete,cliente,importe):
        self.numero = numero
        self.descripcion = descripcion
        self.paquete = paquete
        self.cliente = cliente
        self.importe = importe


def cargarVec(vec):
    for i in range(len(vec)):
        numero = random.randint(0,100)
        descripcion = 'descripcion'+ str(i)
        paquete = random.randint(0,3)
        cliente = random.randint(1,3)
        importe = random.randint(100,3000)
        vec[i] = Paquete(numero,descripcion,paquete,cliente,importe)


def matConteo(vec):
    mat = [[0]*3 for fila in range(20)]
    for i in range(len(vec)):
        fila = vec[i].paquete
        col = vec[i].cliente -1
        mat[fila][col] +=1
    return mat


def cliente(num):
    tupla = ('Premium', 'Medium', 'New')
    return tupla[num]


def paquete(num):
    tupla = 'Europa', 'America', 'Oceania','Africa'
    return tupla[num]


def mostrarMatriz(mat):
    ban = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:    #Filtro para que no aparezcan los 0
                if ban == False:
                    print(paquete(i))
                    ban = True
                print(cliente(j),':', mat[i][j],'Paquetes')
        ban = False



def principal():
    n = int(input('Ingrese cantidad de paquetes: '))
    vec = [None] * n
    cargarVec(vec)
    mat = matConteo(vec)
    mostrarMatriz(mat)


principal()