import pickle
from Registro import *
import os
import io

def guardadoBinario(b, archivo):
    m = open(b, 'ab')
    pickle.dump(archivo, m)
    m.close()


def guardadoTexto(at, art, fecha, montoTotal, adicional, cantidad):
    m = open(at, "at")
    m.write("-" * 50 + "\n")
    m.write("Compra: #" + str(art.identificador) + ' - ' + str(fecha) + "\n")
    m.write("Resumen de compra: " + "\n")
    m.write("Producto: $" + str((montoTotal - adicional)) + " (" + str(cantidad) + " * $" + str(round((montoTotal - adicional) / cantidad,2)) + ")\n")
    m.write("Cargo de envio: $" + str(adicional) + "\n")
    m.write("Tu pago: $" + str(montoTotal) + "\n")
    m.close()


def mostrarIntervaloFecha(abc, fechaMin, fechaMay):
    if not os.path.exists(abc):
        print("Error!. Archivo Inexistente.")
        return
    t = os.path.getsize(abc)
    m = open(abc, "rb")
    while m.tell() < t:
        linea = pickle.load(m)
        if linea.fecha >= fechaMin and linea.fecha <= fechaMay:
            writeCompra(linea)
    m.close()


def buscarEnBinario(abf, id):
    m = open(abf, 'rb')
    t = os.path.getsize(abf)
    pos = -1
    while m.tell() < t:
        fp = m.tell()
        articulo = pickle.load(m)
        if articulo.identificador == id:
            pos = -1
            break
        elif articulo.identificador > id:
            pos = fp
            breaks
        else:
            pos = t
    return pos


def agregarBinario(abf, articulo):
    pos = buscarEnBinario(abf, articulo.identificador)
    t = os.path.getsize(abf)
    if pos != -1:
        m = open(abf, "r+b")
        aux = "Auxiliar.dat"
        m.seek(pos, io.SEEK_SET)
        while m.tell() < t:
            n = pickle.load(m)
            guardadoBinario(aux, n)
        m.seek(pos, io.SEEK_SET)
        pickle.dump(articulo, m)
        writeArticulo(articulo,)
        mA = open(aux, "rb")
        tA = os.path.getsize(aux)
        while mA.tell() < tA:
            n = pickle.load(mA)
            pickle.dump(n , m)
        mA.close()
        mA = open(aux, "wb")
        mA.close()
    elif pos == t:
        guardadoBinario(abf, articulo)

def favoritosActualizados(abf):
    print("Favoritos:")
    m = open(abf, "rb")
    t = os.path.getsize(abf)
    while m.tell() < t:
        var = pickle.load(m)
        writeArticulo(var)
    m.close()

