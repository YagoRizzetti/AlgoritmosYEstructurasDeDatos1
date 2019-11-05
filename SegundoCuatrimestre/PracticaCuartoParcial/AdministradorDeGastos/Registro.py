#Una empresa cuenta con 3 sucursales numeradas desde la 0 a la 2, y necesita gestionar sus gastos por mes. 
#De cada gasto se registra lo siguiente:

#Código.
#Descripción.
#Mes (1-12).
#Sucursal (0-2)
#Importe.

class Gasto:
    def __init__(self,codigo,descripcion,mes,sucursal,importe):
        self.codigo = codigo
        self.descripcion = descripcion
        self.mes = mes
        self.sucursal = sucursal
        self.importe = importe

def writeGasto(gasto):
    print("Codigo: ", gasto.codigo , "-" , end=" ")
    print("Descripcion: ", gasto.descripcion , "-" , end=" ")
    print("Mes: ", gasto.mes , "-" , end=" ")
    print("Sucursal: ", gasto.sucursal , "-" , end=" ")
    print("Importe: ", gasto.importe)
