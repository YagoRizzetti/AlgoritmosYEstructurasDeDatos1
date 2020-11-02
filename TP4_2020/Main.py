#Se solicita un pequeño sistema para administrar listas de música personalizadas. Su primera tarea es crear, 
# mediante un módulo separado, un archivo de texto “musica.csv” con los datos de los temas musicales generados 
# en forma aleatoria. Por cada tema en el archivo de texto, debe haber una línea con los datos siguientes:


#Título o nombre.
#Género: 0-Balada, 1-Pop, 2-Rock, 3-Folclore, 4-Electrónica, 5-Otros.
#Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.

#Su segunda tarea es desarrollar un programa que incluya la definición del tipo registro Tema 
# (con un campo por cada dato contenido en el archivo de texto para un tema), y tal que el programa 
# esté controlado por menú de opciones que permita:

#1)A partir del archivo de texto musica.csv (creado con el módulo separado que se indicó), 
# generar un vector de registros, de tal manera que vaya quedando ordenado por título, con 
# todos los temas musicales. Mostrar el vector a razón de una línea por tema mostrando el género y 
# el idioma en lugar de sus códigos). (Cargar y ordenar el vector )

#2)A partir del vector generar una lista (otro vector) de n temas (n se ingresa por teclado) que sean 
# del género g (g se ingresa por teclado). Si no hubiera suficientes temas del género ingresado, 
# generar la lista con los que haya e informar con un mensaje. Mostrar la lista generada.(Generar nuevo vector y registro)

#3)A partir del vector original determinar la cantidad de temas por género y por idioma. Para eso se 
# debe utilizar una matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0. Se debe 
# mostrar el nombre del idioma y del género y no sus códigos.

#4)A partir de la matriz determinar la cantidad de temas musicales para el idioma i, siendo i un valor 
# ingresado por teclado.

#5)Buscar en el vector original un tema musical con el título x (x se ingresa por teclado). Si existe, 
# mostrar sus datos. Si no, informar con un mensaje. Si hubiera más de una cortar con el primero.

#6)Ingresar por teclado un género x. Generar un archivo binario cuyo nombre tenga la forma 
# “MusicaGenerox.dat” (reemplazando x por el número del género seleccionado) conteniendo todos los 
# temas de ese género.
#Se debe validar en toda situación posible.

from Funciones import *
from Registro import *
import random

def main():
    arch_csv()
    band = False
    band1 = False
    opcion = -1
    while opcion != 0:
        print('=' * 40,"MENU DE OPCIONES",'=' * 40)
        print('1 - Generar un vector de registros')
        print('2 - Generar una lista')
        print('3 - Determinar la cantidad de temas por género y por idioma')
        print('4 - Determinar la cantidad de temas musicales para el idioma solicitado')
        print('5 - Buscar un tema musical')
        print('6 - Generar un archivo')
        print('0 - Salir')
        opcion = int(input('Seleccione su Opcion: '))

        if opcion == 1:
            mus = cargar_reg()
            mostrarVector(mus)
            band = True
        elif opcion == 2:
            if not band:
                print("Debe cargar los datos de los participantes!")
            else:
                nV = nuevoVector(mus)
                mostrarVector(nV)
        elif opcion == 3:
            if not band:
                print("Debe cargar los datos de los participantes!")
            else:
                m = matrizConteo(mus)
                mostrarMatriz(m)
                band1 = True
        elif opcion == 4:
            if not band and not band1:
                print("Debe cargar los datos de los participantes!")
            else:
                cantTemPorIdiom(m)
        elif opcion == 5:
            if not band:
                print("Debe cargar los datos de los participantes!")
            else:
                ver = verfExist(mus)
                if ver[0]:
                    write(ver[1])
                else:
                    print("No se encontro Tema con el Titulo Ingresado")
        elif opcion == 6:
            if not band:
                print("Debe cargar los datos de los participantes!")
            else:
                r = generarArchBin(mus)
                print (r)
        else:
            print("Gracias Vuela")
            break



if __name__ == '__main__':
    main()