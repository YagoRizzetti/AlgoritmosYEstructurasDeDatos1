from Registro import *
from funcion import *

def menu():
    o = 0
    opciones = (1,2,3,4,5,6,7,8)
    while o not in opciones:
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;35m" + "\033[1;35m")
        print("                 MENU PRINCIPAL")
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;36m" + "\033[1;36m" + "\n")
        print("1-Ver articulos nuevos ordenados por precio")
        print("2-ver los 5 articulos usados de mejor puntuacion")
        print("3-Distribucion Geografica ")
        print("4-Total provincial")
        print("5-Precio promedio de usados")
        print("6-Compra ideal")
        print("7-Comprar")
        print("8-Salir")
        o = int(input("Elija una opcion del menu: "))
        v = True
    return o, v

def main():
    n = int(input("Ingrese la cantidad de Articulos: ")) 
    v = [None] * n
    generarArticulos(v)
    o = menu()
    while o[1]:
        if o[0] == 1:
            n = articulosNuevos(v)
            mostrarV(n)
            o = menu()
        elif o[0] == 2:
            u = articulosUsados(v)
            mostrarV(u)
            o = menu()
        elif o[0] == 3:
            pass
        elif o[0] == 4:
            pass
        elif o[0] == 5:
            pass
        elif o[0] == 6:
            pass
        elif o[0] == 7:
            pass
        elif o[0] == 8:
            print("ADIOS!.")
            break

main() 
