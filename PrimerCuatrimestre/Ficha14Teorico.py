#Cargar por teclado un conjunto de valores tales que todos ellos esten comprendidos entre cero y 99 
#(Incluidos ambos).Se indica el fin de carga de datos con el -1. Determinar cuantas veces aparecio 
#cada numero


def mostrarResultados(v):
    for i in range(len(v)):
        if v[i] != 0:
            print("El numero ", i , " Ingreso ", v[i], " Veces.")


def procesarDatos(v):
    num = int(input("Ingrese Un Numero: "))
    while num != -1:
        if num >= 0 and num <= 99:
            v[num] += 1
        else:
            print("Error!") 
        num = int(input("Ingrese Un Numero: "))

def test():
    v = 100 * [0]
    procesarDatos(v)
    mostrarResultados(v)

test()