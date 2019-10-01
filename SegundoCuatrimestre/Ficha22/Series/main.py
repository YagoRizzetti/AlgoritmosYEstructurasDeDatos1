import random
import pickle
import os.path
from Registros import *



def crearArchivo():
    titulos = ("El Negro Ilusionado de Nuevo", 
    "El Corazon Roto del Negro", "Nico Encarando", "TECNO no Trates De Entenderlo", "Vamo A La Barra",
    "La Perra de la UTN", "Tengo Gastroenteritis")

    m = open("series.dat","wb")
    for i in range(len(titulos)):
        genero = random.ranrange(6)
        idioma = random.ranrange(5)
        temporadas = random.ranrange(30)
        duracion = random.ranrange(300)
        serie = Serie(titulos[i],genero,idioma,temporadas,duracion)
        pickle.dumb(serie,)    