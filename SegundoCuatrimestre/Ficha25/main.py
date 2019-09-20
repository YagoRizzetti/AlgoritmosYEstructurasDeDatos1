import utf-8

def cargar_nombre(x):


def main():
    # nombre físico por default del archivo...
    fd = 'default.txt'
    op = 0
    while op != 8:
        print('Opciones para gestión del archivo de texto:', fd)
        print(' 1. Cargar nombre físico del archivo')
        print(' 2. Crear archivo nuevo y grabar texto')
        print(' 3. Abrir archivo y agregar texto al final')
        print(' 4. Mostrar contenido completo del archivo')
        print(' 5. Buscar y contar una palabra o cadena en el archivo')
        print(' 6. Duplicar contenido del archivo (en el mismo archivo)')
        print(' 7. Truncar contenido del archivo a dos líneas')
        print(' 8. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            fd = cargar_nombre()
        elif op == 2:
            

#Busqueda binaria
# x igual el valor que se busca
    #n = len(vec)
    #izq , der = 0 , n-1
    #ban = False
    #while izq <= der:
    #    c = (izq + der)//2
    #    if vec[c].numero == x:
    #       write(vec[c])
    #       ban = True
    #       break
    #    elif x < vec[c].numero:
    #        der = c-1
    #    else:
    #        izq = c+1
    #return None