import io
import os
import pickle
import os.path

class Estudiante:
    def __init__(self, leg, nom, prom):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom
        self.activo = True
def to_string(est):
    r = ''
    r += '{:<20}'.format('Legajo: ' + str(est.legajo))
    r += '{:<30}'.format('Nombre: ' + est.nombre.strip())
    r += '{:<20}'.format('Precio: ' + str(est.promedio))
    return r


def validar_legajo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup) + ' por favor: '))
        if n < inf or n > sup:
            print('Se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n


def validar_promedio():
    n = -1.0
    while n < 0.0 or n > 10.0:
        n = float(input('Valor entre 0 y 10 por favor (puede tener decimales): '))
        if n < 0 or n > 10:
            print('Error... se pidió entre 0 y 10... cargue de nuevo...')
    return n

def buscar(FD, legajo):
    if not os.path.exists(FD):
        print("Archivo Inexistente")
        return None
    m = open(FD,"rb"):
    posicion = -1
    tam = os.path.getsize(FD)
    while m.tell() < tam:
        fp = m.tell()
        registro = pickle.load(m)
        if registro.legajo == legajo:
            posicion = fp
            break
    m.close()
    return posicion

def alta(FD):
    m = open(FD,"ab")
    print("Ingrese Legajo: ")
    legajo = validar_legajo(1,100000)
    while legajo != 0:
        posicion = buscar(FD,legajo)
        if posicion == None or posicion == -1:
            nombre = input("Ingrese Nombre: ")
            nombre = nombre.ljust(30," ")
            print("Ingrese promedio: ")
            promedio = validar_promedio()
            registro = Estudiante(legajo, nombre, promedio)
            pickle.dumb(registro, m)
        else:
            print("Legajo Existente: Alta Rechazada")
        print("Ingrese otro legajo:")
        legajo = validar_legajo(1,100000)
    m.close()
    print("Fin opeacion de alta")
    input("Ingrese <ENTER> Para Continuar...")


#BAJA LOGICA----------------------------------------------------------------
def baja(FD):
    pass

def modificacion(FD):
    pass

def listado_completo(FD):
    pass

def listado_filtrado(FD):
    pass

#BAJA FISICA----------------------------------------------------------------
def depuracion(FD):
    pass


def main():

    FD = 'estudiantes.utn'

    op = 0
    while op != 7:
        print('Opciones ABM del archivo de estudiantes')
        print('   1. Alta de estudiantes')
        print('   2. Baja de estudiantes')
        print('   3. Modificación de estudiantes')
        print('   4. Listado completo de estudiantes')
        print('   5. Listado de estudiantes con promedio mayor o igual a 7')
        print('   6. Depuración del archivo de estudiantes')
        print('   7. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if op == 1:
            alta(FD)

        elif op == 2:
            baja(FD)

        elif op == 3:
            modificacion(FD)

        elif op == 4:
            listado_completo(FD)

        elif op == 5:
            listado_filtrado(FD)

        elif op == 6:
            depuracion(FD)

        elif op == 7:
            pass


# script principal...
if __name__ == '__main__':
    main()
