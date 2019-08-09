import time
import random

def nuevaPatente(patente_nueva,x):
    #VERIFICAR PATENTE MAS NUEVA
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


def ultimaPatente(patente,l):
    #INGRESAR PATENTE
    n_patente = input('\n' + '\033[1;35m' +  'INGRESE PATENTE: ' + '\033[1;37m' + '\n')
    n_patente = n_patente.upper()
    c_patente = 1
    numeros = '0123456789'
    #VALIDAR PATENTE
    while len(n_patente) != 6 and len(n_patente) != 7:
        n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\037[0;m'))
        c_patente = 0

    if len(n_patente) == 6:
        for letra in n_patente:
            if n_patente[0] not in l or n_patente[1] not in l or n_patente[2] not in l:
                n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\033[1;37m'))
                c_patente = 0
            if n_patente[3] not in numeros or n_patente[4] not in numeros or n_patente[5] not in numeros:
                n_patente = str(input('\033[1;31m' + 'ERROR...INGRESE PATENTE:' + '\033[1;37m'))
                c_patente = 0
            c_patente += 1
            f_patente = 1

    elif len(n_patente) == 7:
        for letra in n_patente:
            if n_patente[0] not in l or n_patente[1] not in l or n_patente[5] not in l or n_patente[6] not in l:
                n_patente = str(input('\033[1;31m' + 'ERROR..INGRESE PATENTE:' + '\033[1;37m'))
                c_patente = 0
            if n_patente[2] not in numeros or n_patente[3] not in numeros or n_patente[4] not in numeros:
                n_patente = str(input('\033[1;31m' + 'ERROR...INGRESE PATENTE:' + '\033[1;37m'))
                c_patente = 0

            c_patente += 1
            f_patente = 1

    return patente


def procesar(carga):
    pE = pT = m = a = c = pases_t = pasE = pasT = hora_1 = hora_2 = hora_3 = hora_4 = patente = 0
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    patente_nueva = ''
    
    # CARGA MANUAL
    if carga == 1:
        # CONTROLAR TIEMPO 
        inicio = fin = time.time()
        while (fin - inicio) < 240:
            tiempo = (fin - inicio)
            # MOSTRAR TIEMPO RESTANTE
            print('\033[1;32m' , 'TIEMPO RESTANTE: ', 240 - round(tiempo) , '\033[1;32m' + '\n')
            # CONTROLAR EN QUE HORA SE ESTA TRANSCURRIENDO
            if tiempo > 60:
                hora_1 += 1
            elif tiempo > 120:
                hora_2 += 1
            elif tiempo > 180:
                hora_3 += 1
            elif tiempo < 180:
                hora_4 += 1

            #INGRESAR VEHICULO
            print('\033[1;35m' + 'CARGA MANUAL' + '\n')
            print('\033[1;35m' +  'SELEECIONE TIPO DE VEHICULO' + '\033[1;37m' + '\n')
            print('1- Moto')
            print('2- Auto')
            print('3- Camion')
            tipo = int(input())
            #VALIDAR VEHICULO INGRESADO
            while tipo < 1 and tipo > 3:
                tipo = int(input('\033[1;35m' + "ERROR!. EL VALOR INGRESADO ES INVALIDO ELIJA UN VALOR DE LOS MENCIONADOS ANTES: " + '\033[1;37m'))
            #INGRESAR FORMA DE PAGO
            print('\n' + '\033[1;35m' +  'SELECCIONE FORMA DE PAGO' + '\033[1;37m' + '\n')
            print('1- Efectivo')
            print('2- Telepeaje')
            forma_pago = int(input())
            #VALIDAR FORMA DE  PAGO
            while forma_pago != 1 and forma_pago != 2:
                forma_pago = int(input('\033[1;35m' + "ERROR!. EL VALOR INGRESADO ES INVALIDO ELIJA UN VALOR DE LOS MENCIONADOS ANTES: " + '\033[1;37m'))
            if forma_pago == 1:
                pasE += 1
                if tipo == 1:
                    pE += 20
                    a += 1

                elif tipo == 2:
                    pE += 40
                    m += 1
                else:
                    pE += 80
                    c += 1
            else:
                pasT += 1
                patente = ultimaPatente(patente,l)
                if tipo == 1:
                    pT += 20
                    m += 1

                elif tipo == 2:
                    pT += 40
                    a += 1
                else:
                    pT += 80
                    c += 1

            print('-' * 60)
            pases_t += 1
            fin = time.time()
        print('\033[1;31m' + 'FIN DEL TIEMPO' + '\033[1;35m')

    # CARGA AUTOMATICO
    if carga == 2:
        #CONTROLAR TIEMPO TRANSCURRIDO
        inicio = fin = time.time()
        while (fin - inicio) < 240:
            tiempo = (fin - inicio)
            #MOSTRAR TIEMPO RESTANTE
            print('\033[1;32m' , 'TIEMPO RESTANTE: ', 240 - round(tiempo) ,'\n')
            print('\033[1;35m' , 'CARGA AUTOMATICA', '\n')            
            #CARGA DE VAHICULO
            tipo = random.randint(1, 3)
            #CARGA DE FORMA DE PAGO
            forma_pago = random.randint(1, 2)

            if forma_pago == 2:
                pasT += 1
                if tipo == 1:
                    pT += 20
                    m += 1
                elif tipo == 2:
                    pT += 40
                    a += 1
                else:
                    pT += 80
                    c += 1
                n = random.randint(6, 7)
                pat_ale = ''
                if n == 6:
                    for i in range(6):
                        if i == 0 or i == 1 or i == 2:
                            pat_ale += str(random.choice(l))
                        else:
                            pat_ale += str(random.randint(0, 9))
                elif n == 7:
                    for i in range(7):
                        if i == 0 or i == 1 or i == 5 or i == 6:
                            pat_ale += str(random.choice(l))
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
                pasE += 1
                if tipo == 1:
                    pE += 20
                    m += 1

                elif tipo == 2:
                    pE += 40
                    a += 1
                else:
                    pE += 80
                    c += 1
                print('Tipo de vehiculo: ', tipo)
                print('Forma de pago: ', forma_pago)
            time.sleep(random.randint(1, 3))
            fin = time.time()
        print('\033[1;31m' + 'FIN DEL TIEMPO' + '\033[1;35m' +'\n')


    return m, a, c, pE, pT, pasT, pasE, patente, patente_nueva 
