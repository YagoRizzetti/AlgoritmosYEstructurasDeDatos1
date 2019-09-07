#Un pequeño almacén de barrio necesita hacer un analisis de su libreta de cuenta corriente, 
#para ello nos solicita un programa que permita procesar n deudas. Por cada deuda se tiene el nombre
#del cliente, el monto adeudado El programa debe:

#Informar el monto adeudado promedio del almacen

#Informar los datos de la menor deuda 

#Informar el porcentaje de clientes que presentan un monto adeudado menor a un valor ingresado por 
#el usuario, respecto del total de deudas

from Registro import *
from Funciones import *

def menu():
    o = 0
    opciones = (1,2,3,4)
    while o not in opciones:
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;35m" + "\033[1;35m")
        print("                 MENU PRINCIPAL")
        print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;36m" + "\033[1;36m" + "\n")
        print("1-Monto adeudado Promedio")
        print("2-Menor Deuda")
        print("3-Porcentaje de Clientes con un monto menor deseado ")
        print("4-Salir")
        o = int(input("Elija una opcion del menu: "))
        v = True
    return o, v

def main():
    n = int(input("Ingrese la cantidad de Dudas: ")) 
    v = [None] * n
    generarDeudas(v)
    mostrarV(v)
    o = menu()
    while o[1]:
        if o[0] == 1:
            montoPromedio(v)
            o = menu()
        elif o[0] == 2:
            menorDeuda(v)
            o = menu()
        elif o[0] == 3:
            m = int(input("Ingrese un monto para saber el porcentaje de clientes que tiene una deuda menor al monto ingresado: "))
            pmmm(v,m)
            o = menu()
        elif o[0] == 4:
            print("CHAU.")
            break
main()