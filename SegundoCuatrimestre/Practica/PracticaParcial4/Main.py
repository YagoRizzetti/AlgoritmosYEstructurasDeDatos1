from Funciones import *

def main():
    n = int(input("Ingrese la cantidad de Paquetes: "))
    v = [None] * n
    o = 0
    b = False
    d = ("Bueno","malo","Una Verga","Tremendo","Teletubi")
    while o != 7:
        print("1-Cargar Datos")
        print("2-Ver paquetes ordenados por dias de menor a mayor")
        print("3-Ver cantidad de paquetes por tipo")
        print("4-Buscar por numero de identificacion e importe")
        print("5-Buscar por dias")
        print("6-Buscar Mayor Importe")
        print("7-Salir")
        o = int(input("Elija una opcion del Menu: "))
        if o == 1:
            cargarDatos(v,d)
            b = True
        if o == 2:
            if b:
                paquetesOrdenados(v)
            else:
                print("No Hay datos registrados")
        if o == 3:
            if b:
                c = cantPaquetePorTipo(v)
                for i in range(len(c)):
                    if c[i] != 0:
                        print ("La cantidad de paquetes del tipo " + str(i) + " es de: " + str(c[i]))
            else:
                print("No Hay datos registrados")
        if o == 4:
            if b:
                buscar(v)
            else:
                print("No Hay datos registrados")
        if o == 5:
            if b:
                buscarD(v)
            else:
                print("No Hay Datos Registrados")

        elif o == 6:
            if b:
                buscarI(v)
            else:
                print("No Hay Datos Registrados")
    print("Adios Vuelva Prontos")

main()