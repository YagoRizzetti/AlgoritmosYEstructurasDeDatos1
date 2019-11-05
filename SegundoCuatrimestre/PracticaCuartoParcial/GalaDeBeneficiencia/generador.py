__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from invitado import *
import pickle
import random


def generar_archivo():
    nombres = ['Marcelo Tinelli', 'Susana Gimenez', 'Mirtha Legrand','Juana Viale', 'Mariana Fabbiani',
               'Mauricio Macri', 'Juliana Awada', 'Jorge Rial', 'Guillermo Andino', 'Alejandro Fantino',
               'Sebastian Yatra', 'Tini Stoessel', 'Lali Espósito', 'Jimena Baron', 'Paulo Londra' 
               'Carolina Ardohain','Nicole Neuman', 'Paula Chaves', 'Valeria Mazza',
               'Abel Pintos', 'Luciano Pereyra', 'Soledad Pastorutti','Dartez']
    m = open('invitados.dat', 'wb')
    for nombre in nombres:
        mesa = random.randrange(13)
        ong = random.randrange(10)
        monto = random.randrange(1000, 100000, 100)
        pickle._dump(Invitado(nombre, mesa, ong, monto), m)
    m.close()


if __name__ == '__main__':
    generar_archivo()