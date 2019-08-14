import random
import time

def nuevaPatente(patente_nueva,x):
    if len(patente_nueva) < len(x):
        patente_nueva = x
        return x
    elif len(patente_nueva) == len(x):
        if patente_nueva < x:
            patente_nueva = x
            return x
        else:
            return patente_nueva
    else:
        return patente_nueva


def contadores(tipo, forma_pago, pases_efec, precio_efec, vehi_1, vehi_2, vehi_3, precio_tele, pases_tele):
    if forma_pago == 1:
        pases_efec += 1
        if tipo == 1:
            precio_efec += 20
            vehi_1 += 1

        elif tipo == 2:
            precio_efec += 40
            vehi_2 += 1
        else:
            precio_efec += 80
            vehi_3 += 1
    else:
        pases_tele += 1
        if tipo == 1:
            precio_tele += 20
            vehi_1 += 1

        elif tipo == 2:
            precio_tele += 40
            vehi_2 += 1
        else:
            precio_tele += 80
            vehi_3 += 1


def verificar(x):
    opc = int(input('INGRESE OPCION:'))
    print(opc)
    while opc not in x:
        opc = int(input('\033[1;31m' + 'OPCION INCORRECTA...INGRESE UNA OPCION VALIDA: ' + '\033[0;m'))
    return opc


def patente(new_patente, letraslista):
    n_patente = input('INGRESE PATENTE: ')
    c_patente = 1
    f_patente = -1
    numeros = '0123456789'
    letraslista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while f_patente != 1:
        if len(n_patente) == 6:
            for letra in n_patente:
                if n_patente[0] not in letraslista or n_patente[1] not in letraslista or n_patente[2] not in letraslista:
                    n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\033[0;m'))
                    c_patente = 0
                if n_patente[3] not in numeros or n_patente[4] not in numeros or n_patente[5] not in numeros:
                    n_patente = str(input('\033[1;31m' + 'ERROR...INGRESE PATENTE:' + '\033[0;m'))
                    c_patente = 0
                c_patente += 1
                f_patente = 1

        elif len(n_patente) == 7:
            for letra in n_patente:
                if n_patente[0] not in letraslista or n_patente[1] not in letraslista or n_patente[5] not in letraslista or n_patente[6] not in letraslista:
                    n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\033[0;m'))
                    c_patente = 0
                if n_patente[2] not in numeros or n_patente[3] not in numeros or n_patente[4] not in numeros:
                    n_patente = str(input('\033[1;31m' + 'ERROR...INGRESE PATENTE:' + '\033[0;m'))
                    c_patente = 0

                c_patente += 1
                f_patente = 1
        else:
            n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\033[0;m'))
            c_patente = 0

    return new_patente


def principal():
    precio_efec = precio_tele = vehi_1 = vehi_2 = vehi_3 = pases_t = pases_efec = pases_tele = minuto_1 = minuto_2 \
    = minuto_3 = minuto_4 = new_patente = 0
    letraslista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    patente_nueva = ''

    print('\033[1;35m' + 'SISTEMA PARA EL CONTROL DE PEAJE' + '\033[0;36m' + '\n')
    opcion = -1
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print('1) Definir forma de carga')
        print('2) Procesar las pasadas')
        print('3) Ver resultados')
        print('4) Salir' + "\n")
        tipos_menu = (1, 2, 3, 4)
        opcion = verificar(tipos_menu)

    if opcion == 1:
        opcion = -1
        print('SELECCIONE TIPO DE CARGA')
        while opcion != 1 and opcion != 2:
            print('1) Carga manual')
            print('2) Carga automatica')
            c_tipos_cargas = (1, 2, 3)
            opcion = verificar(c_tipos_cargas)

        # CARGA MANUAL
        if opcion == 1:
            inicio = fin = time.time()
            while (fin - inicio) < 30:
                tiempo = (fin - inicio)
                print('TIEMPO RESTANTE:', str(30 - round(tiempo)))
                if tiempo > 60:
                    minuto_1 += 1
                elif tiempo > 120:
                    minuto_2 += 1
                elif tiempo > 180:
                    minuto_3 += 1
                elif tiempo < 180:
                    minuto_4 += 1
                print('\033[1;35m' + 'CARGA MANUAL' + '\033[0;36m' + '\n')
                print('\n', 'SELEECIONE TIPO DE VEHICULO')
                c_tipos_vehiculos = (1, 2, 3)
                print('1. Moto')
                print('2. Auto')
                print('3. Camion')
                tipo = verificar(c_tipos_vehiculos)

                print('\n', 'SELECCIONE FORMA DE PAGO')
                c_tipos_pago = (1, 2)
                print('1. Efectivo')
                print('2. Telepeaje')
                forma_pago = verificar(c_tipos_pago)
                if forma_pago == 1:
                    pases_efec += 1
                    if tipo == 1:
                        precio_efec += 20
                        vehi_1 += 1

                    elif tipo == 2:
                        precio_efec += 40
                        vehi_2 += 1
                    else:
                        precio_efec += 80
                        vehi_3 += 1
                else:
                    pases_tele += 1
                    new_patente = patente(new_patente, letraslista)
                    if tipo == 1:
                        precio_tele += 20
                        vehi_1 += 1

                    elif tipo == 2:
                        precio_tele += 40
                        vehi_2 += 1
                    else:
                        precio_tele += 80
                        vehi_3 += 1

                print('-' * 60)
                pases_t += 1
                fin = time.time()
            print('\033[1;31m' + 'FIN DEL TIEMPO' + '\033[0;m')

        # AUTOMATICO
        if opcion == 2:
            inicio = fin = time.time()
            while (fin - inicio) < 10:
                tiempo = (fin - inicio)
                print('TIEMPO RESTANTE: ', 10 - round(tiempo))
                tipo = random.randint(1, 3)
                forma_pago = random.randint(1, 2)
                if forma_pago == 2:
                    pases_tele += 1
                    if tipo == 1:
                        precio_tele += 20
                        vehi_1 += 1
                    elif tipo == 2:
                        precio_tele += 40
                        vehi_2 += 1
                    else:
                        precio_tele += 80
                        vehi_3 += 1
                    n = random.randint(6, 7)
                    pat_ale = ''
                    if n == 6:
                        for i in range(6):
                            if i == 0 or i == 1 or i == 2:
                                pat_ale += str(random.choice(letraslista))
                            else:
                                pat_ale += str(random.randint(0, 9))
                    elif n == 7:
                        for i in range(7):
                            if i == 0 or i == 1 or i == 5 or i == 6:
                                pat_ale += str(random.choice(letraslista))
                            else:
                                pat_ale += str(random.randint(0, 9))
                    print('Tipo de vehiculo: ', tipo)
                    print('Forma de pago: ', forma_pago)
                    print('Patente: ', pat_ale)
                    y = nuevaPatente(patente_nueva, pat_ale)
                    patente_nueva = y
                    print('PATENTE MAS NUEVA', patente_nueva)
                    print('-' * 20)
                else:
                    pases_efec += 1
                    if tipo == 1:
                        precio_efec += 20
                        vehi_1 += 1

                    elif tipo == 2:
                        precio_efec += 40
                        vehi_2 += 1
                    else:
                        precio_efec += 80
                        vehi_3 += 1
                    print('Tipo de vehiculo: ', tipo)
                    print('Forma de pago: ', forma_pago)
                time.sleep(random.randint(1, 3))
                fin = time.time()

    if opcion == 3 or pases_efec > 0 or pases_tele > 0:
        pases_t = pases_efec + pases_tele
        print('CANTIDAD DE VEHICULOS: ')
        print('MOTO: ' + str(vehi_1))
        print('AUTO: ' + str(vehi_2))
        print('CAMION: ' + str(vehi_3))
        print('-' * 20)
        print('RECAUDACION POR TIPOS: ')
        print('EFECTIVO: ' + str(precio_efec))
        print('TELEPEAJE: ' + str(precio_tele))
        print('RECAUDACION TOTAL: ' + str((precio_tele + precio_efec)))
        print('-' * 20)
        print('CANTIDAD TOTAL DE PASES: ' + str(pases_t))
        if pases_tele > pases_efec:
            print('METODO CON MAYOR CANTIDAD DE PASES: PASES TELEPEAJE CON ' + str(pases_tele) + ' PASADAS')
        else:
            print('METODO CON MAYOR CANTIDAD DE PASES: PASES EFECTIVO CON ' + str(pases_efec) + ' PASADAS')
        print('PROMEDIO DE PASES POR HORA: ', (pases_t / 4))
        if str(new_patente) > patente_nueva:
            print('PATENTE MAS NUEVA: ', new_patente, ' HORA:')
        else:
            print('PATENTE MAS NUEVA: ', patente_nueva, ' HORA:')

principal()
