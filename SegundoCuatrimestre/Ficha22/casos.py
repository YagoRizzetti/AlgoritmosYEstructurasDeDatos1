import pickle

def grabarArchivo():
    print("Procediendo a grabar numeros en el archivo...")
    m = open("prueba.num","wb")
    x, y = 2.345 , 19
    pickle.dump(x, m)
    pickle.dump(y, m)
    m.close()

def leerArchivo():
    m = open("prueba.num", "rb")
    a = pickle.load(m)
    b = pickle.load(m)
    m.close()
    print("datos recuperados desde el archivo", a, " - " , b)

def main():
    grabarArchivo()
    leerArchivo()

main()