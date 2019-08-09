from funciones import *

def main():
    print('\033[1;35m' + 'SISTEMA PARA EL CONTROL DE PEAJE' + '\033[1;36m' + '\n')
    opcion = 0
    op = 0
    while opcion == 0:
        print('1- Definir forma de carga')
        print('2- Procesar las pasadas')
        print('3- Ver resultados')
        print('4- Salir' + "\n")
        opcion = int(input("Elija una opción: "))

        while (opcion < 1 and opcion > 4) or ((opcion == 2 or opcion == 3) and op == 0):    
            opcion = int(input('\033[1;31m' + "ERROR! debe Ingresar una de las opciones del MENU:" + '\033[1;37m'))

        if opcion == 1:
            print('\033[1;35m' + 'SELECCIONE TIPO DE CARGA' + '\033[1;36m' + '\n')
            print('1- Carga manual')
            print('2- Carga automatica')
            op = int(input("Ingrese una opcion: "))
            while op != 1 and op != 2:
                op = int(input('\033[1;31m' +"ERROR!. Ingrese una opcion de carga: " + '\033[1;37m'))
            if op == 1 or op == 2:
                r = procesar(op)
                print('\033[1;35m' + 'RESULTADOS: ' + '\033[1;37m')
                print('-' * 40)
                print('SE REGISTRARON UN TOTAL DE ' + str(r[0]) + ' MOTOS.')
                print('SE REGISTRARON UN TOTAL DE ' + str(r[1]) + ' AUTOS.')
                print('SE REGISTRARON UN TOTAL DE ' + str(r[2]) + ' CAMIONES')
                print('-' * 40)
                print('RECAUDACION POR TIPOS: ')
                print('TELEPEAJE: ' + str(r[4]))
                print('EFECTIVO: ' + str(r[3]))
                print('RECAUDACION TOTAL: ' + str(r[4] + r[3]))
                print('-' * 40)
                print('CANTIDAD TOTAL DE PASES: ' + str(r[5] + r[6]))
                print('PROMEDIO DE PASES POR HORA: ', ((r[5] + r[6]) / 4))
                if r[5] < r[6]:
                    print('FORMA DE PASES CON MAYOR CANTIDAD DE PASES: PASES TELEPEAJE CON ' + str(r[6]) + ' PASADAS')
                else:
                    print('FORMA DE PASES CON MAYOR CANTIDAD DE PASES: PASES EFECTIVO CON ' + str(r[5]) + ' PASADAS')
                if str(r[7]) > r[8]:
                    print('PATENTE MAS NUEVA REGISTRADA ES: ', r[7] + '\033[0;37m')
                else:
                    print('PATENTE MAS NUEVA REGISTRADA ES: ', r[8] + '\033[0;37m')

main()
