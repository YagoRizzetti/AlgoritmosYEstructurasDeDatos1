from Funciones import *

def main():
    n = int(input('Ingrese cantidad de alquileres:'))
    v = [None] * n
    d = ("Choto","Bueno","Mortal","Flama","teletubi","pequeñoBandi")
    op = -1
    b = False
    while op != 5:
        print('MENU')
        print('-'*100)
        print('1-Cargar Datos')
        print('2-Ver datos ordenados por importe de menor a mayor')
        print('3-Ver cantidad de alquileres por tipo')
        print('4-Buscar por descripcion y por dias')
        print('5-SALIR')
        op = int(input('Ingrese opcion:'))
        if op == 1:
            cargarV(v,d)
            b = True
        elif op == 2:
            if b:
                ordenadosImoprte(v)
            else:
                print("No hay datos registrados")
        elif op == 3:
            if b:
                cant = verCantPorTipo(v)
                for i in range(len(cant)):
                    if cant[i] != 0:
                        print("La cantidad de alquileres que se hicieron por tipo " + str(i) + " es de: " + str(cant[i]))
            else:
                print("No hay datos registrados")
        elif op == 4:
            if b:
                desc = input("Ingrese una de las siguientes descripciones: " + str(d))
                di = int(input("Ingrese una cantidad de dias: "))
                buscar(v, desc, di)
            else:
                print("No hay datos Registrados")    

main()

