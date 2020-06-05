from functions import *

def main():
    user = ""
    valid = False
    cant = 0
    print("         ¡Bienvenido a Estadisticas COVID-19!         ")
    while cant < 3:
        user = input("Ingrese el usuario que realizara el reporte:\n--->")
        cant += 1
        user.lower
        valU = validarUser(user, valid)
        if valU[1] == True:
            valid = True
            break

    if valid == True:
        print("Bienvenido!")
        o = 0
        n = int(input("Ingrese la cantidad de pacientes a registrar: ")) 
        cargados = False
        while o != 12:
            print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;35m" + "\033[1;35m")
            print("                 MENU PRINCIPAL")
            print("\033[1;35m" + "\033[4;35m" + "_"*50 + "\033[0;36m" + "\033[1;36m" + "\n")
            print("1-cargar datos de los " + str(n) + " Pacientes")
            print("2-Cantidad de Casos Positivos y porcentaje")
            print("3-Edad Promedio de los pacientes en grupo de riesgo")
            print("4-cantidad y porcentaje del personal de salud")
            print("5-Edad Promedio de los casos Confirmados")
            print("6-Menor edad de los casos autoctonos")
            print("7-cantidad y porcentaje de casos por region")
            print("8-cantidad de casos confirmados por viaje al exterior")
            print("9-Cantidad de casos sospechosos en contacto con casos confirmados")
            print("10-Regiones sin casos Confirmados")
            print("11-Porcentaje de casos positivos autoctonos con respecto al total de positivos")
            print("12-Salir")

            o = int(input("Elija una opcion del menu: "))
            if o == 1:
                if cargados == False:
                    res = cargarDatos(n)
                    cargados = True
                else:
                    print("Los pacientes ya fueron cargados")
            if o == 2:
                print("La cantidad de casos Positivos registrados son: " + str(res[0]))
                print("El porcentaje de casos positivos es de: " + str(res[1]) + "%")
            if o == 3:
                print("La edad promedio de los pacientes en grupo de riesgo es de: " + str(res[2]))
            if o == 4:
                print("La cantidad de pacientes que son personal de salud son: " + str(res[3]))
                print("El porcentaje de pacientes que son personal de salud es de: " + str(res[4]) + "%")                
            if o == 5:
                print("La edad promedio de los pacientes en grupo de riesgo es de: " + str(res[5]))
            if o == 6:
                print("La menor edad de casos autoctonos es de: " + str(res[6]))
            if o == 7:
                print("la cantidad de casos en la capital es de: " + str(res[7]) + " y su porcentaje sobre el total de casos es de: " + str(res[11]))
                print("la cantidad de casos en Cordoba es de: " + str(res[8]) + " y su porcentaje sobre el total de casos es de: " + str(res[12]))
                print("la cantidad de casos en El Norte es de: " + str(res[9]) + " y su porcentaje sobre el total de casos es de: " + str(res[13]))
                print("la cantidad de casos en El Sur es de: " + str(res[10]) + " y su porcentaje sobre el total de casos es de: " + str(res[14]))
            if o == 8:
                print("La cantidad de casos positivos por viaje al exterior es de: " + str(res[15]))
            if o == 9:
                print("La cantidad de casos sospechosos que tuvieron contacto con casos confirmados es de: " + str(res[16]))
            if o == 10:
                regSinCasos(res[17], res[18])
            if o == 11:
                print("El porcentaje de casos autoctonos positivos con respecto al total de positivos es de: " + str(res[19]) + "%")
            if o == 12:
                break




    else:
        print("Lo sentimos no se pudo validar el usuario")
    
    
     


main()