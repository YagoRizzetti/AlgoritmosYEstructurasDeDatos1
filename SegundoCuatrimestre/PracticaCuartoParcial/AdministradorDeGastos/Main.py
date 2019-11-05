#Se necesita hacer lo siguiente, trabajando desde un menu de opciones:

#Cargar los n registros de gastos en un vector.
#Mostrar el vector de gastos.
#Generar un archivo con aquellos gastos cuyo importe supere cierto valor.
#Mostrar el archivo.
#Generar una matriz de acumulación a partir del archivo generado en el punto 3,que represente el gasto total por mes y sucursal.
#A partir de la matriz, totalizar los gastos de un determinado mes.

from Funciones import *
import os

def main():
    m1 = "Ingrese la cantidad de registros que desee generar: \n-->"
    m2 = "Elija una opcion del menu \n-->"
    m3 = "Ingrese el importe minimo que debe tener el registro que desea guardar en el Archivo \n-->"
    arc = "Gastos.dat"
    mat = [[0]* 12 for i in range(3)]
    n = int(input(m1))
    validarMayorQue(m1,n,0)
    v = [None] * n
    b = False
    matriz = False
    o = 0
    while o != 7:
        print("1-Cargar Datos \n2-Ver Registros Generados \n3-Generar Un archivo con registros predeterminados",
        "\n4-Ver los Registros Guardados en el Archivo", 
        "\n5-Ver el gasto total por mes y sucursal de los registros guardados en el archivo",
        "\n6-Ver los gastos totales por un mes determinado de los registros guardados en el archivo \n7-Salir")
        o = int(input(m2))
        validarEntre(m2,o,1,7)
        if o == 1:
            if b == False:
                generarRegistros(v)
                b = True
            else:
                print("Los Registros Ya Fueron Generados!")
        elif o == 2:
            if b:
                mostrarRegistros(v)
            else:
                print("No se Encontraron Registros Generados")
        elif o == 3:
            im = float(input(m3))
            validarEntre(m3,im,1000,10000)
            generarArchivo(v,im,arc)
        elif o == 4:
            mat = verRegistrosArchivo(arc)
        elif o == 5:
            matrizAcu(arc,mat)
            matriz = True
        elif o == 6:
            if matriz:
                totalizarGastosDeUnMes(mat)
            else:
                print("No se genero el Archivo Con los registros Especificos")


if __name__ == "__main__":
    main()