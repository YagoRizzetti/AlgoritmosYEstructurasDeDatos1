import pickle
from RegistroLibro import *

def grabarArchivo():
    print("Prueba de grabacion de varios Registros...")
    lib1 = Libro(2131, "Fundacion", "pepe")
    lib2 = Libro(2231, "hola", "juan")
    lib3 = Libro(2324, "chau", "nico")

    fd = "libros.dat"
    m = open(fd,"wb")
    pickle.dump(lib1,m)
    pickle.dump(lib2,m)
    pickle.dump(lib3,m)
    m.close()
    print("Se grabaron varios registros en el archivo: ", fd)

def leerArchivo():
    fd = "libros.dat"
    m = open(fd , "rb")
    lib1 = pickle.load(m)
    lib2 = pickle.load(m)
    lib3 = pickle.load(m)
    m.close()
    print("datos recuperados desde el archivo: ", fd)
    display(lib1)
    display(lib2)
    display(lib3)


def main():
    grabarArchivo()
    leerArchivo()

main()
