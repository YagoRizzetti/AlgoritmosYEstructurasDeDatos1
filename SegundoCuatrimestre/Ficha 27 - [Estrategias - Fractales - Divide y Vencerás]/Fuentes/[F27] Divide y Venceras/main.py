import time
import ordenamiento

__author__ = 'Cátedra de AED'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def test():
    op = 0
    while op != 10:
        print('1. Generar el vector')
        print('2. Verificar orden')
        print('3. Ordenamiento por Selección Directa')
        print('4. Ordenamiento por Intercambio Directo (Burbuja)')
        print('5. Ordenamiento por Inserción Directa')
        print('6. Ordenamiento Heapsort')
        print('7. Ordenamiento Quicksort')
        print('8. Ordenamiento Shellsort')
        print('9. Ordenamiento Quicksort (Mediana de Tres)')
        print('10. Salir')

        op = int(input('\t\tIngrese opción: '))

        if op == 1:
            print()
            n = validate(0)
            v = n * [0]
            ordenamiento.generate_random(v)
            print('Hecho... arreglo creado...')
            print()

        elif op == 2:
            print()
            if ordenamiento.check(v):
                print('Está ordenado...')
            else:
                print('No está ordenado...')
            print()

        elif op == 3:
            print()
            print('Ordenamiento: Selección Directa.')
            t1 = time.clock()
            ordenamiento.selection_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 4:
            print()
            print('Ordenamiento: Intercambio Directo (Burbuja).')
            t1 = time.clock()
            ordenamiento.bubble_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 5:
            print()
            print('Ordenamiento: Inserción Directa.')
            t1 = time.clock()
            ordenamiento.insertion_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 6:
            print()
            print('Ordenamiento: Heap Sort.')
            t1 = time.clock()
            ordenamiento.heap_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 7:
            print()
            print('Ordenamiento: Quick Sort.')
            t1 = time.clock()
            ordenamiento.quick_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 8:
            print()
            print('Ordenamiento: Shell Sort.')
            t1 = time.clock()
            ordenamiento.shell_sort(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 9:
            print()
            print('Ordenamiento: Quick Sort (Mediana de Tres).')
            t1 = time.clock()
            ordenamiento.quick_sort_m3(v)
            t2 = time.clock()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()


# script principal...
if __name__ == '__main__':
    test()
