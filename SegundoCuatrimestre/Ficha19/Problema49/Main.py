from Registro import *
from Funciones import *

def menu():
    o = 0
    opciones = (1,2,3,4,5,6,7,8)
    while o not in opciones:
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;35m" + "\033[1;35m")
        print("                 MENU PRINCIPAL")
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;36m" + "\033[1;36m" + "\n")
        print("1-Cargar Datos")
        print("2-Ver datos de los socios que pagen un arancel mayor a un precio deseado")
        print("3-Ver el mayor arancel que se abona en el club")
        print("4-Ver todos los socios ordenados por numero de identificacion")
        print("5-Ingresar 100 aranceles a un usuario deseado")
        print("6-Buscar un socio por numero de identificacion")
        print("7-Ver cantidad de socios por deporte")
        print("8-Salir")
        o = int(input("Elija una opcion del menu: "))
        v = True
    return o, v

def main():
    n = int(input("Ingrese la cantidad de Socios: ")) 
    v = [None] * n
    o = menu()
    b = False
    while o[1]:
        if o[0] == 1:
            generarDatos(v)
            b = True
            o = menu()
        elif o[0] == 2:
            if b :
                a = input("Ingrese la cantidad de arancel: ")
                mapd(v,a)
                mostrarV(v)
            else:
                print("Sin datos")
            o = menu()
        elif o[0] == 3:
            d = distribucionGeografica(v)
            o = menu()
        elif o[0] == 4:
            t = totalProvincial(v)
            o = menu()
        elif o[0] == 5:
            promedioUsados(v)
            o = menu()
        elif o[0] == 6:
            compraIdeal(v)
            o = menu()
        elif o[0] == 7:
            comprar(v)
            o = menu()
        elif o[0] == 8:
            print("ADIOS!.")
            break

main() 