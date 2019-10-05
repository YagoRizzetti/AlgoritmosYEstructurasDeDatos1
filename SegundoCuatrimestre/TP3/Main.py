#1)    Nuevos por precio: generar un nuevo arreglo conteniendo sólo las publicaciones 
#      de artículos nuevos. Mostrar el listado ordenado por precio (de menor a mayor).

#2)    Usados por calificación: determinar cantidad de publicaciones en estado usado
#      por cada puntuación de vendedor (5 totales).

#3)    Distribución geográfica: informar la cantidad de artículos disponibles por ubicación 
#      geográfica y puntuación del vendedor, pero mostrando el resultado en forma de matriz. 
#      Se debe mostrar el nombre de cada provincia (no el código) y la descripción de la 
#      puntuación del vendedor (no el código), y solo para las cantidades mayores a cero.

#4)    Total provincial: a partir de la matriz, informar el total de artículos para una provincia
#      que se ingresa por teclado (validar que se encuentre cargada).

#5)    Precio promedio de usados: mostrar las publicaciones con estado usado, cuyo precio supera el 
#      precio promedio de usados del listado.

#6)    Compra ideal: informar cual es el menor precio para un artículo nuevo, omitiendo los vendedores 
#      con calificación Mala.

#7)    Comprar: buscar una publicación cuyo código se ingresa por teclado. Si no existe, informar 
#      con un mensaje. Si existe, preguntar al usuario qué cantidad de artículos desea comprar, 
#      validar que la cantidad disponible sea suficiente, y confirmar/rechazar la compra según corresponda.

from Registro import *
from Funciones import *

def main():
    n = int(input("Ingrese la cantidad de Articulos: ")) 
    v = [None] * n
    generarArticulos(v)
    mostrarV(v)
    o = 0
    ban = False
    while o != 8:
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;35m" + "\033[1;35m")
        print("                 MENU PRINCIPAL")
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;36m" + "\033[1;36m" + "\n")
        print("1-Ver articulos nuevos ordenados por precio")
        print("2-ver Cantidad de articulos usados por Puntuacion")
        print("3-Distribucion Geografica ")
        print("4-Total provincial")
        print("5-Precio promedio de usados")
        print("6-Compra ideal")
        print("7-Comprar")
        print("8-Salir")
        o = int(input("Elija una opcion del menu: "))
        if o == 1:
            articulosNuevos(v)
        elif o == 2:
            articulosUsados(v)
        elif o == 3:
            if ban == False:
                d = distribucionGeografica(v)
                ban = True
            mostrarMatriz(d)
        elif o == 4:
            totalProvincial(v)                
        elif o == 5:
            promedioUsados(v)
        elif o == 6:
            compraIdeal(v)
        elif o == 7:
            comprar(v)

    print("ADIOS VUELVAN PRONTOS!.")

main() 
