from RegistroLibro import *
import os.path
import pickle

def lecturaSecuancial():
    v=[]
    m = open("libros.dat","rb")
    t = os.path.getsize("libros.dat")
    while m.tell() < t:
        lib = pickle.load(m)
        if lib.isbn % 2 != 0:
            display(lib)
            v.append(lib)
    m.close()
    return v

lecturaSecuancial()