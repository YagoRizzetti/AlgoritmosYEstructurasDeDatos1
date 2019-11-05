class Articulo:
    def __init__(self, identificador, precio, ubicacion, estado, cantidad, puntuacion):
        self.identificador = identificador
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cantidad = cantidad
        self.puntuacion = puntuacion

def writeArticulo(articulo):
    print("Codigo de Identificacion: ", articulo.identificador, "-", end=" ")
    print("Precio: ", articulo.precio, "-", end=" ")
    print("Ubicacion: ", articulo.ubicacion, "-", end=" ")
    print("Estado: ", articulo.estado, "-", end=" ")
    print("Cantidad: ", articulo.cantidad, "-", end=" ")
    print("Puntuacion: ", articulo.puntuacion)


class Compra:
    def __init__(self, identificador, cantidad, precio, envio, montoTotal, fecha):
        self.identificador = identificador
        self.cantidad = cantidad
        self.precio = precio
        self.envio = envio
        self.montoTotal = montoTotal
        self.fecha = fecha

def writeCompra(compra):
    print("Codigo de Identificacion: ", compra.identificador)
    print("Cantidad: ", compra.cantidad)
    print("Envio a domicilio: ", compra.envio)
    print("Monto Total: ", compra.montoTotal)
    print("Fecha: ", compra.fecha)

    