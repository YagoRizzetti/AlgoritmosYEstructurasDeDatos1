from Funciones import *

def main(ab,li):
    n = int(input("Ingrese una cantidad Positiva de Miembros a registrar: \n-->"))
    n = validarMayorQue("Ingrese una cantidad de Posotiva Miembros a registrar: \n-->",n,0)
    v = [None] * n
    nombresRegistrados = [None] * len(v)
    registrosIngresados = False    
    proxliminf = 0
    if os.path.exists(li):
        ultLimInf = leerUltLimInf(li)
    else:
        ultLimInf = proxliminf
    o = 0
    while o != 7:
        print("-"*50)
        print("                MENU PRINCIPAL")
        print("-"*50)
        print("\n1-Registrar Miembros \n2-Ver Miembros Registrados",
            "\n3-Guardar datos en un archivo de los miembro segun su tipo de trabajo y si importe mensual",
            " \n4-Ver Los miembros guardados en el archivo \n5-Buscar Miembro Registrado por nombre particular",
            "\n6-Ver la cantidad de miembros por afiliacion y por trabajo \n7-Salir")
        o = int(input("Ingrese una opcion del Menu: \n-->"))
        if o == 1:
            reg = int(input("Ingrese una forma de carga de datos de los Miembros \n1-Manual \n2-Automatica \n-->"))
            formaDeCarga = validarEntre("Ingrese una forma de carga de datos de los Miembros \n1-Manual \n2-Automatica \n-->",reg,1,2)
            if formaDeCarga == 1:
                proxliminf = cargaManual(v,nombresRegistrados,ultLimInf,proxliminf)
            else:
                cargaAutomatica(v,nombresRegistrados,ultLimInf)
                proxliminf = int(ultLimInf) + len(v)  
            registrosIngresados = True
        if o == 2:
            if registrosIngresados:
                mostrarVector(v)
            else:
                print("\nNo Se Encontraron Registros Cargados.\n")
        if o == 3:
            if registrosIngresados:
                m = float(input("Ingrese El importe mensual minimo que deben tener los miembros que desea guardar en el archivo: "))
                m = validarMayorQue("Ingrese El importe mensual minimo que deben tener los miembros que desea guardar en el archivo: ", m, 0)
                crearArchivo(v,m,ab)
            else:
                print("\nNo Se Encontraron Registros Cargados.\n")
        if o == 4:
            if registrosIngresados:
                verRegistrosDelArchivo(ab)
            else:
                print("\nNo Se Encontraron Registros Cargados.\n")
        if o == 5:
            buscarPorNombre(v,nombresRegistrados)
        if o == 6:
            if registrosIngresados:
                matrizConteo(v)
            else:
                print("\nNo Se Encontraron Registros Cargados.\n")                
    guardarLimInf(li,proxliminf)
    print("Gracias Vuelva Pronto.")

ab = "Archivo.dat"
li = "limiteInferior.dat"

if os.path.exists(ab) or os.path.exists(li):
    res = int(input("Hay Archivos Existente de Ejecuciones anteriores con datos Registrados anteriormente desea borrarlo o agregarle nuevos registros\n1-Borrar Archivo \n2-Utilizar Archivo Existente \n-->"))
    res = validarEntre("Hay un Archivo Existente de Ejecuciones anteriores con datos Registrados anteriormente desea borrarlo o agregarle nuevos registros\n1-Borrar Archivo \n2-Utilizar Archivo Existente \n-->",res,1,2)
    if res == 1:
        if os.path.exists(ab):
            os.remove(ab)
        if os.path.exists(li):
            os.remove(li)
        if __name__ == "__main__":
            main(ab,li)
    else:
        if __name__ == "__main__":
            main(ab,li)

else:
    if __name__ == "__main__":
        main(ab,li)

