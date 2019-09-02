class Articulo:
    def __init__(self, identificador, precio, ubicacion, estado, cantidad, puntuacion):
        self.identificador = identificador
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cantidad = cantidad
        self.puntuacion = puntuacion


def write(articulo):
    print("Codigo de Identificacion: ", articulo.identificador, "-", end=" ")
    print("Precio: ", articulo.precio, "-", end=" ")
    print("Ubicacion: ", articulo.ubicacion, "-", end=" ")
    print("Estado: ", articulo.estado, "-", end=" ")
    print("Cantidad: ", articulo.cantidad, "-", end=" ")
    print("Puntuacion: ", articulo.puntuacion)
