from Funciones import *

def main():
    n = int(input("ingrese la cantidad pacientes: "))
    v = [None] * n
    o = 0
    b = False
    while o != 5:
        print("1-Cargar los datos de los " + str(n) + " Pacientes")
        print("2-Ver los datos de todos los pacientes ordenados por nombre de menor a mayor")
        print("3-Ver cantidad de pacientes que se atendieron por tipo de practica") 
        print("4-Buscar paciente por numero de identificacion y cantidad de dias")
        print("5-Salir") 
        o = int(input("Ingrese una opcion: "))      
        if o == 1:
            cargarV(v)
            b = True
        elif o == 2:
            if b:
                ordenarPorNombre(v)
            else:
                print("No Hay Datos Almacenados")
        elif o == 3:
            if b:            
                pacientesPorPractica(v)
            else:
                print("No Hay Datos Almacenados")
        elif o == 4:
            if b:            
                num = int(input("Ingrese El numero de Identificacion del paciente que quiere buscar: "))
                d = int(input("Ingrese la cantidad de dias: "))
                numeroYDias(v,num,d)
            else:
                print("No Hay Datos Almacenados")


print("Gracias Vuelvan Prontos!")

main()
