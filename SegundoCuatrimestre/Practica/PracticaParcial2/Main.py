from Funciones import *

def main():
    n = int(input("Ingrese la cantidad de servicios a registrar: "))
    v = [None] * n
    o = -1
    b = False
    nom = ("Monji","Tita","Loren","Lucho","Mati","Rodri")
    while o != 5:
        print("1-Cargar datos:")
        print("2-Mostrar todos los datos ordenados de mayor a menor por numero de identificacion")
        print("3-Ver la cantidad de servicios por tipo")
        print("4-Buscar un servicio por descripcion y cantidad de personas")
        print("5-Salir")
        o = int(input("Elija una opcion del menu: "))
        if o == 1:
            cargarV(v,nom)
            b = True
        if o == 2:
            if b:
                ordenadoMAM(v)
            else:
                print("No hay datos registrados")
        if o == 3:
            if b:
                verCantPorTipo(v)
            else:
                print("No hay datos registrados")
        if o == 4:
            buscar(v,nom)
    
    print("Adios Vuelvan Prontos!")

main()